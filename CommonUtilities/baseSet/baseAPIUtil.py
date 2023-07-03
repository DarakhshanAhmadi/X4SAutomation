import time

from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from pages.cbconnect.api_settings.apiHeaderParam import cbConnectAuthorization


class BaseAPIUtility:
    logger = LogGenerator.logGen()

    """
        This is an internal function is to replace API QUERY URL "?" with the desired parameter 
            param1 = api_method_name
            param2 = valueToReplace
    """

    def do_update_api_query_url(self, api_method_name, value_to_replace):
        api_method_name = api_method_name.replace("?", value_to_replace)
        self.logger.info("CB Connect API method is getting as : %s", api_method_name)
        return api_method_name

    def get_header_for_connect_api(self, service_name, marketplace="default"):
        parse_config_json = ParseConfigFile()
        connect_api_url = parse_config_json.get_data_from_config_json(marketplace, "cbConnectApi_url",
                                                                      "CredConfig.json")
        connect_api_key = "cbConnectApi_key_" + service_name.lower()
        connect_api_key = parse_config_json.get_data_from_config_json(marketplace, connect_api_key,
                                                                      "CredConfig.json")
        connect_api_key = {cbConnectAuthorization: connect_api_key}
        self.logger.info("Setting up the API header for CB Connect with API KEY as : %s", connect_api_key)
        return connect_api_key

    def do_sleep(self, sleep_value):
        parse_config_json = ParseConfigFile()
        min_sleep_time = parse_config_json.get_data_from_config_json("sleepTime", "min_sleep")
        above_min_sleep_time = parse_config_json.get_data_from_config_json("sleepTime", "above_min_sleep")
        above_min_2_sleep_time = parse_config_json.get_data_from_config_json("sleepTime", "above_min_2_sleep")
        average_sleep_time = parse_config_json.get_data_from_config_json("sleepTime", "average_sleep")
        above_average_sleep_time = parse_config_json.get_data_from_config_json("sleepTime", "above_average_sleep")
        max_sleep_time = parse_config_json.get_data_from_config_json("sleepTime", "max_sleep")

        if sleep_value == "min":
            sleep_time = int(min_sleep_time)
        elif sleep_value == "above_min":
            sleep_time = int(above_min_sleep_time)
        elif sleep_value == "above_min_2":
            sleep_time = int(above_min_2_sleep_time)
        elif sleep_value == "average":
            sleep_time = int(average_sleep_time)
        elif sleep_value == "above_average":
            sleep_time = int(above_average_sleep_time)
        elif sleep_value == "max":
            sleep_time = int(max_sleep_time)
        else:
            sleep_time = 1  # Default value

        self.logger.info("Sleeping for %s seconds.." % sleep_time)
        time.sleep(sleep_time)
