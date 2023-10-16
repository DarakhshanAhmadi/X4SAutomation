import datetime
import requests

from CommonUtilities.APIUtilities import APIUtilities
from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_json_common import common_json_ops
from RestApi.ApiSettings import ApiBaseURLs, apiHeaderParam


class EDIDataValidation:
    logger = LogGenerator.logGen()
    common_json = common_json_ops()
    api_utilities = APIUtilities()

    def set_api_endpoint_headers(self):
        global edi_api_url, headers
        edi_api_url = ApiBaseURLs.edi_order_url
        headers = apiHeaderParam.headers_edi_data_validation

    def hit_api_post_request(self, path):
        global data
        data = self.common_json.read_json_file(path)
        response = requests.post(edi_api_url, json=data, headers=headers)
        self.logger.info("Triggered API Endpoint")
        json_data = response.json()
        assert response.status_code == 200
        self.logger.info("API response status code is 200")
        return json_data

    def currency_code_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\CA-DEV-23090829247966422325.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "currencyCode"):
            assert json_response["currencyCode"] is None, "Currency code is mismatched not available in input jSON"

    def currency_code_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithCurrencyCode.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "currencyCode"):
            assert json_response["currencyCode"] == data["header02Record"][
                "currencyCode"], "Currency code is mismatched available in input jSON"

    def terms9_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\CA-DEV-23090829247966422325.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "terms-9"):
            assert json_response["terms9"] is None, "Terms9 is mismatched not available in input jSON"

    def terms9_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "terms-9"):
            assert json_response["terms9"] == data["header02Record"][
                "terms-9"], "Terms9 is mismatched available in input jSON"

    def po_date_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithoutPODate.json"
        json_response = self.hit_api_post_request(path)
        curr_date = datetime.date.today()
        formatted_curr_date = curr_date.strftime("%Y%m%d")
        if self.api_utilities.keys_exists(data, "header02Record", "poDate"):
            assert json_response["poDate"] == formatted_curr_date, "PODate is mismatched for empty value in input jSON"

    def po_date_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithCurrencyCode.json"
        json_response = self.hit_api_post_request(path)
        curr_date = datetime.date.today()
        formatted_curr_date = curr_date.strftime("%Y%m%d")
        if self.api_utilities.keys_exists(data, "header02Record", "poDate"):
            if int(data["header02Record"]["poDate"]) > int(formatted_curr_date):
                assert json_response["poDate"] == data["header02Record"][
                    "poDate"], "PODate is mismatched available in input jSON"
            elif int(data["header02Record"]["poDate"]) == int(formatted_curr_date):
                assert json_response["poDate"] == data["header02Record"][
                    "poDate"], "PODate is mismatched available in input jSON"
            else:
                assert json_response["poDate"] == data["header02Record"][
                    "poDate"], "PODate is mismatched available in input jSON"

    def eta_date_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\CA-DEV-23090829247966422325.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "etaDate"):
            assert json_response["etaDate"] == "", "ETA date is mismatched not available in input jSON"

    def eta_date_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithETADate.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "etaDate"):
            assert json_response["etaDate"] == data["header02Record"][
                "etaDate"], "ETA date is mismatched available in input jSON"

    def cancel_date_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\CA-DEV-23090829247966422325.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "cancelDate"):
            assert json_response["cancelDate"] == "", "Cancel date is mismatched not available in input jSON"

    def cancel_date_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "cancelDate"):
            assert json_response["cancelDate"] == data["header02Record"][
                "cancelDate"], "Cancel date is mismatched available in input jSON"

    def required_ship_date_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithETADate.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "requiredShipDate"):
            assert json_response[
                       "requiredShipDate"] == "", "Required ship date is mismatched not available in input jSON"

    def required_ship_date_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\CA-DEV-23090829247966422325.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "requiredShipDate"):
            assert json_response["requiredShipDate"] == data["header02Record"][
                "requiredShipDate"], "Required ship date is mismatched available in input jSON"

    def department_no_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithETADate.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "departmentNumber"):
            assert json_response[
                       "departmentNumber"] == "", "Department number is mismatched not available in input jSON"

    def department_no_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "departmentNumber"):
            assert json_response["departmentNumber"] == data["header02Record"][
                "departmentNumber"].upper(), "Department number is mismatched available in input jSON"

    def seller_sales_no_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithETADate.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "sellerSalesNumber"):
            assert json_response[
                       "sellerSalesNumber"] == "", "Seller sales number is mismatched not available in input jSON"

    def seller_sales_no_available_validate(self):
        """This test case is kept on hold as test data is not available"""
        pass

    def enduser_po_no_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "endUserPoNumber"):
            assert json_response["endUserPoNumber"] == "", "End User PO is mismatched not available in input jSON"

    def enduser_po_no_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithETADate.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "endUserPoNumber"):
            assert json_response["endUserPoNumber"] == data["header02Record"][
                "endUserPoNumber"].upper(), "EndUser PO is mismatched available in input jSON"

    def customer_order_no_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "customerOrderNumber"):
            assert json_response[
                       "customerOrderNumber"] == "", "Customer order number is mismatched not available in input jSON"

    def customer_order_no_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithCustomerOrderNo.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "customerOrderNumber"):
            assert json_response["customerOrderNumber"] == data["header02Record"][
                "customerOrderNumber"].upper(), "Customer order number is mismatched available in input jSON"
            assert json_response["header02DepOrderNumber"] == data["header02Record"][
                "customerOrderNumber"], "Header02DepOrderNumber is mismatched"

    def customer_vendor_no_not_available_validate(self):
        """This test case is kept on hold as test data is not available"""
        pass

    def customer_vendor_no_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "customerVendorNumber"):
            assert json_response["customerVendorNumber"] == data["header02Record"][
                "customerVendorNumber"].upper(), "Customer vendor number is mismatched available in input jSON"

    def contract_no_for_order_type_rl_kd_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithOrderTypeRL.json"
        json_response = self.hit_api_post_request(path)
        if data["header02Record"]["orderType"] == "RL" or data["header02Record"]["orderType"] == "KD":
            if self.api_utilities.keys_exists(data, "header02Record", "contractNumber"):
                assert json_response["contractNumber"] == data["header02Record"][
                    "contractNumber"].upper(), "Contract number is mismatched"

    def premium_service_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "premiumService"):
            assert json_response["premiumService"] == "", "Premium service is mismatched not available in input jSON"

    def premium_service_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithPremiumService.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "premiumService"):
            assert json_response["premiumService"] == "", "Premium service is mismatched available in input jSON"

    def fixed_delivery_date_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "fixedDeliveryDate"):
            assert json_response[
                       "fixedDeliveryDate"] == "", "Fixed delivery date is mismatched not available in input jSON"

    def fixed_delivery_date_available_validate(self):
        """This test case is kept on hold as test data is not available"""
        pass

    def warehouse_action_code_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "warehouseActionCode"):
            assert json_response[
                       "warehouseActionCode"] == "", "Warehouse action code is mismatched not available in input jSON"

    def warehouse_action_code_available_validate(self):
        """This test case is kept on hold as test data is not available"""
        pass

    def back_order_flag_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "backOrderFlag"):
            assert json_response["backOrderFlag"] == "", "Back order flag is mismatched not available in input jSON"

    def back_order_flag_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithCustomerOrderNo.json"
        json_response = self.hit_api_post_request(path)
        backorderflag = data["header02Record"]["backOrderFlag"]
        json_response_back_order_flag = json_response["backOrderFlag"]
        if self.api_utilities.keys_exists(data, "header02Record", "backOrderFlag"):
            if backorderflag == "K":
                assert json_response_back_order_flag == "K", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "P":
                assert json_response_back_order_flag == "P", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "N":
                assert json_response_back_order_flag == "N", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "E":
                assert json_response_back_order_flag == "E", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "B":
                assert json_response_back_order_flag == "B", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "SC":
                assert json_response_back_order_flag == "C", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "SV":
                assert json_response_back_order_flag == "V", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "SK":
                assert json_response_back_order_flag == "S", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "Y":
                assert json_response_back_order_flag == "Y", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "BK":
                assert json_response_back_order_flag == "Y", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "SP":
                assert json_response_back_order_flag == "Y", "Back order flag is mismatched available in input jSON"
            elif backorderflag == "PR":
                assert json_response_back_order_flag == "Y", "Back order flag is mismatched available in input jSON"
            else:
                self.logger.info("Invalid back order flag")

    def buyer_information_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header08Record"):
            buyer_data_dict = json_response["buyerData"]
            for key in buyer_data_dict.keys():
                if isinstance(buyer_data_dict[key], dict):
                    new_dict = buyer_data_dict[key]
                    for k in new_dict.keys():
                        assert new_dict[k] is None, "Buyer information is mismatched not available in input jSON"
                else:
                    assert buyer_data_dict[key] is None, "Buyer information is mismatched not available in input jSON"

    def buyer_information_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithHeader08Record.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header08Record"):
            buyer_data_dict = json_response["buyerData"]
            input_dict = data["header08Record"]
            for key in buyer_data_dict.keys():
                if isinstance(buyer_data_dict[key], dict):
                    new_dict = buyer_data_dict[key]
                    for k in new_dict.keys():
                        if k in input_dict:
                            assert new_dict[k] == input_dict[
                                k], "Buyer information is mismatched available in input jSON"
                        else:
                            assert new_dict[k] is None, "Buyer information is mismatched available in input jSON"
                else:
                    if key in input_dict:
                        assert buyer_data_dict[key] == input_dict[
                            key], "Buyer information is mismatched available in input jSON"
                    else:
                        assert buyer_data_dict[key] is None, "Buyer information is mismatched available in input jSON"

    def frieght_code_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "frieghtCode"):
            assert json_response["carrierData"][
                       "frieghtCode"] is None, "Frieght code is mismatched not available in input jSON"

    def frieght_code_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithFrieghtCode.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "frieghtCode"):
            assert json_response["carrierData"]["frieghtCode"] == data["header02Record"][
                "frieghtCode"], "Frieght code is mismatched available in input jSON"

    def third_party_frieght_account_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "thirdPartyFrieghtAccount"):
            assert json_response["carrierData"][
                       "thirdPartyFrieghtAccount"] == "", "Third party frieght account is mismatched not available in input jSON"

    def third_party_frieght_account_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithFrieghtCode.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "thirdPartyFrieghtAccount"):
            assert json_response["carrierData"]["thirdPartyFrieghtAccount"] == data["header02Record"][
                "thirdPartyFrieghtAccount"], "Third party frieght account is mismatched available in input jSON"

    def im_carrier_field_and_imi_ship_via_field_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithOrderTypeSO.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "orderType"):
            if data["header02Record"]["orderType"] == "SO":
                assert json_response["carrierData"]["imCarrierCode"] == "OT", "IMCarrierCode is mismatched"
                assert json_response["carrierData"]["imiShipVia"] == "DO NOT SHIP", "IMIShipVia is mismatched"

    def carrier_code_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithTerms.json"
        json_response = self.hit_api_post_request(path)
        if not self.api_utilities.keys_exists(data, "header02Record", "carrier"):
            assert json_response["carrierData"][
                       "customerCarrierCode"] == "Carrier", "Carrier code is mismatched not available in input jSON"

    def carrier_code_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithOrderTypeRL.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header02Record", "carrier"):
            assert json_response["carrierData"]["customerCarrierCode"] == data["header02Record"]["carrier"]
            assert json_response["carrierData"]["imiShipVia"] == data["header02Record"][
                "carrier"], "Carrier code is mismatched available in input jSON"

    def header16_form_code_not_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithoutHeader16FormCode.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header16Record"):
            header16_form_code_op = json_response["header16Record"][0]
            assert header16_form_code_op[
                       "header16FormCode"] == "END", "Header16FormCode is mismatched not available in input jSON"

    def header16_form_code_available_validate(self):
        path = ".\\RestApi\\Resources\\EDI\\IPJSONWithCurrencyCode.json"
        json_response = self.hit_api_post_request(path)
        if self.api_utilities.keys_exists(data, "header16Record"):
            # Header16FormCode Output
            header16_record_output_list = json_response["header16Record"]
            header16_form_code_output_list = []
            for item in header16_record_output_list:
                header16_form_code_output_list.append(item["header16FormCode"])

            # Header16FormCode Input
            header16_record_input_list = data["header16Record"]
            header16_form_code_input_list = []
            for item in header16_record_input_list:
                header16_form_code_input_list.append(item["header16FormCode"])
            header16_form_code_input_list = list(set(header16_form_code_input_list))

            # Compare header16FormCode input and output list
            assert set(header16_form_code_output_list) == set(
                header16_form_code_input_list), "Header16FormCode is mismatched available in input jSON"
