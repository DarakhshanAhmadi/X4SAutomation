import requests
from RestApi.ApiSettings import ApiBaseURLs
from RestApi.ApiSettings import apiHeaderParam
from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_json_common import common_json_ops


class DataCreationViaApi:
    logger = LogGenerator.logGen()
    common_json = common_json_ops()

    def __init__(self, driver):
        self.driver = driver

    def post_request_for_order_exception_create(self):
        error_order_base_url = ApiBaseURLs.error_order_base_url
        path = ".\\RestApi\\Resources\\data_error_order_payload.json"
        self.logger.info("post url: " + error_order_base_url)
        headers = apiHeaderParam.headers
        data = self.common_json.read_json_file(path)
        self.logger.info(data)
        response = requests.post(error_order_base_url, json=data, headers=headers)
        json_data = response.json()
        self.logger.info(response.status_code)
        assert response.status_code == 200
        self.logger.info("json POST response body: ", json_data)
        confirmation_id = json_data["id"]
        return confirmation_id

    def post_request_for_im360_order_exception_create(self):
        error_order_base_url = ApiBaseURLs.error_order_base_url
        path = ".\\RestApi\\Resources\\im360_data_error_order_payload.json"
        self.logger.info("post url: " + error_order_base_url)
        headers = apiHeaderParam.headers
        data = self.common_json.read_json_file(path)
        self.logger.info(data)
        response = requests.post(error_order_base_url, json=data, headers=headers)
        json_data = response.json()
        self.logger.info(response.status_code)
        assert response.status_code == 200
        self.logger.info("json POST response body: ", json_data)
        confirmation_id = json_data["id"]
        return confirmation_id

    def post_request_for_x4d_order_exception_create(self, shipingdetails):
        error_order_base_url = ApiBaseURLs.error_order_base_url
        path = ".\\RestApi\\Resources\\x4d_data_error_order_" + shipingdetails + "_shiping_details_payload.json"
        self.logger.info("post url: " + error_order_base_url)
        headers = apiHeaderParam.headers
        data = self.common_json.read_json_file(path)
        self.logger.info(data)
        response = requests.post(error_order_base_url, json=data, headers=headers)
        json_data = response.json()
        self.logger.info(response.status_code)
        assert response.status_code == 200
        self.logger.info("json POST response body: ", json_data)
        confirmation_id = json_data["id"]
        return confirmation_id

    def post_request_for_x4c_order_exception_create(self, po_number, country):
        data_error_order_base_url = ApiBaseURLs.data_error_order_url
        path = ".\\RestApi\\Resources\\x4c_data_error_order_duplicate_po_" + country + "_payload.json"
        self.logger.info("post url: " + data_error_order_base_url)
        headers = apiHeaderParam.headers
        headers['IM-SiteCode'] = country
        authentication = apiHeaderParam.headers_sales_order_auth
        data = self.common_json.read_json_file(path)
        data['customerOrderNumber'] = po_number
        special_symbols = '^'
        if special_symbols not in po_number:
            data['endCustomerOrderNumber'] = "ENDTESTPO^"
        self.logger.info(data)
        response = requests.post(data_error_order_base_url, auth=authentication, json=data, headers=headers)
        json_data = response.json()
        self.logger.info(response.status_code)
        assert response.status_code == 200
        self.logger.info("json POST response body: ", json_data)
        confirmation_id = json_data["id"]
        return confirmation_id
