import re

import requests

from CommonUtilities.parse_config import ParseConfigFile
from RestApi.ApiSettings import ApiBaseURLs
from RestApi.ApiSettings import apiHeaderParam
from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_json_common import common_json_ops
from db.model.X4ASalesOrderDetails import X4ASalesOrderDetails
from db.model.X4ASalesOrderLines import X4ASalesOrderLine
from db.service.X4ASalesOrderDetailsDbManagementService import X4ASalesOrderDetailsDbManagementService
from db.service.X4ASalesOrderLinesDbManagementService import X4ASalesOrderLinesDbManagementService


class FetchOrderViaApi:
    logger = LogGenerator.logGen()
    common_json = common_json_ops()
    db_file_path = ParseConfigFile().get_data_from_config_json("dbLocation", "db_file_path")
    order_details = ["entrymethoddescription", "ordernumber", "ordertype", "customerordernumber", "enduserponumber", "orderstatus",
                      "ordertotalvalue",
                     "currencycode", "shiptoaddress", "billtoaddress", "enduserinfo", "extendedspecs"]
    address_fields = ["addressline1", "addressline2", "addressline3", "addressline4", "city", "state", "postalcode",
                       "countrycode"]
    bill_to_address = ["suffix", "name", "addressline1", "addressline2", "addressline3", "city", "state", "postalcode",
                       "countrycode"]
    end_user_info = ["enduserid", "addressid", "contactid"]
    lines = ["erpordernumber", "linenumber", "linestatus", "partnumber", "manufacturerpartnumber", "partdescription1",
             "partdescription2", "isacopapplied",
             "unitweight", "unitprice", "extendedprice", "adjustedcost", "requestedquantity", "confirmedquantity",
             "backorderquantity",
             "specialbidnumber"] #"serialnumberdetails"

    def post_request_for_sales_order_detail_fetch(self, im_order_number, order_date):
        try:
            sales_order_base_url = ApiBaseURLs.order_details_base_url
            path = ".\\RestApi\\Resources\\sales_order_details_payload.json"
            self.logger.info("post url: " + sales_order_base_url)
            headers = apiHeaderParam.headers_sales_order_details
            authentication = apiHeaderParam.headers_sales_order_auth
            json_data = self.common_json.read_json_file(path)
            # update date
            json_data = self.common_json.update_json_object(json_data, "servicerequest", "orderdetailrequest", "orderdate", order_date)
            # update order number
            json_data = self.common_json.update_json_object(json_data, "servicerequest", "orderdetailrequest", "ordernumber", im_order_number)
            self.logger.info("Json Body: " + str(json_data))
            response = requests.post(sales_order_base_url, auth=authentication, json=json_data, headers=headers)

            order_details_json_data = response.json()
            self.logger.info(response.status_code)
            assert response.status_code == 200
            status_code = self.common_json.read_json_data(order_details_json_data, "serviceresponse", "responsepreamble",
                                                         "statuscode")
            assert status_code == '200', "status code is not 200 in response json"
            return order_details_json_data
        except Exception as e:
            self.logger.info("Error while fetching order details from API : " + str(e))
            raise e

    def extract_order_details_data_and_save_in_db(self, json_data, feature_file_name):
        sales_order_details_list = []
        order_entry_channel = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "entrymethoddescription")
        im_order_number = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "ordernumber")
        order_type = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "ordertype")
        reseller_po = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "customerordernumber")
        end_user_po = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "enduserponumber")
        order_status = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "orderstatus")
        order_value = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "ordertotalvalue")
        currency_code = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "currencycode")
        terms_code = self.extract_terms_code(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "extendedspecs"))
        ship_from_warehouse_id = self.extract_ship_from_details(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "lines"), "shipfromwarehouseid")
        warehouse_name = self.extract_ship_from_details(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "lines"), "warehousename")
        carrier_code = self.extract_ship_from_details(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "lines"), "carriercode")
        ship_to_suffix = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "shiptoaddress"), "suffix")
        ship_to_name = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "shiptoaddress"), "name")
        ship_to_address = self.format_address(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "shiptoaddress"))
        ship_to_phone = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "shiptoaddress"), "phonenumber")
        ship_to_contact = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "shiptoaddress"), "attention")
        ship_to_email = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "shiptoaddress"), "email")
        bill_to_suffix = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "billtoaddress"), "suffix")
        bill_to_name = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "billtoaddress"), "name")
        bill_to_address = self.format_address(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "billtoaddress"))
        bill_to_phone = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "billtoaddress"), "phonenumber")
        bill_to_contact = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "billtoaddress"), "mobilenumber")
        bill_to_email = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "billtoaddress"), "email")
        end_user_id = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "enduserinfo"), "enduserid")
        end_user_address = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "enduserinfo"), "addressid")
        end_user_contact = self.common_json.read_json_data1(self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "enduserinfo"), "contactid")
        sales_order_details_obj = X4ASalesOrderDetails(feature_file_name,order_entry_channel, im_order_number, order_type, reseller_po, end_user_po,
                                                       order_status, order_value, currency_code, terms_code, ship_from_warehouse_id, warehouse_name, carrier_code,
                                                       ship_to_suffix, ship_to_name, ship_to_address, ship_to_phone, ship_to_contact, ship_to_email, bill_to_suffix, bill_to_name, bill_to_address, bill_to_phone, bill_to_contact,
                                                       bill_to_email, end_user_id, end_user_address, end_user_contact)
        sales_order_details_list.append(sales_order_details_obj)
        X4ASalesOrderDetailsDbManagementService().save_sales_order_details_data(self.db_file_path, sales_order_details_list)

    def extract_order_lines_and_save_to_db(self, json_data):
        sales_order_lines_list = []
        order_lines = self.common_json.read_json_data(json_data, "serviceresponse", "orderdetailresponse", "lines")
        self.logger.info(order_lines)
        for obj in order_lines:
            if obj["partnumber"]:
                self.logger.info(obj["partnumber"])
                im_order_number = obj["erpordernumber"]
                line_number = obj["linenumber"]
                line_status = obj["linestatus"]
                im_part_number = obj["partnumber"]
                vpn = obj["manufacturerpartnumber"]
                description = obj["partdescription1"] + " " + obj["partdescription2"]
                is_acop_applied = obj["isacopapplied"]
                unit_weight = obj["unitweight"]
                unit_price = obj["unitprice"]
                extended_price = obj["extendedprice"]
                cost = obj["adjustedcost"]
                quantity = obj["requestedquantity"]
                quantity_confirmed = obj["confirmedquantity"]
                quantity_backordered = obj["backorderquantity"]
                serial_numbers = self.extract_serial_numbers(obj["serialnumberdetails"])
                special_bid_number = obj["specialbidnumber"]
                order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
                sales_order_details_tbl_id = X4ASalesOrderDetailsDbManagementService().get_id_by_im_order_number(self.db_file_path, order_number)
                sales_order_lines_obj = X4ASalesOrderLine(im_order_number, line_number, line_status, im_part_number, vpn, description, is_acop_applied, unit_weight,
                                                          unit_price, extended_price, cost, quantity, quantity_confirmed, quantity_backordered, serial_numbers,
                                                          special_bid_number, sales_order_details_tbl_id)
                sales_order_lines_list.append(sales_order_lines_obj)
        X4ASalesOrderLinesDbManagementService().save_sales_order_lines_data(self.db_file_path, sales_order_lines_list)

    def extract_terms_code(self, list_data):
        terms_code = ""
        for obj in list_data:
            if obj["attributename"] == "termscode":
                terms_code = obj["attributevalue"]
                break
        return terms_code

    def extract_ship_from_details(self, list_data, variable_name):
        variable_data = ""
        self.logger.info(list_data)
        for obj in list_data:
            if obj["partnumber"]:
                intermediate_data = obj["shipmentdetails"]
                for data in intermediate_data:
                    variable_data = data[variable_name]
                break
        return variable_data

    def format_address(self, data_obj):
        address = ""
        for field in self.address_fields:
            if data_obj[field]:
                address = address + data_obj[field] + ","
        self.logger.info(address)
        return address[:-1]

    def extract_serial_numbers(self, list_data):
        data = ""
        for i in list_data:
            data += i + ","
        return data[:-1]
