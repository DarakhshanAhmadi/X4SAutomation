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

    def post_request_for_error_order_create(self):
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

    def post_request_for_im360_error_order_create(self):
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
