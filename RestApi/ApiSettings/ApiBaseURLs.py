from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger

parse_config_json = ParseConfigFile()


api_address = parse_config_json.get_data_from_config_json("restApi", "data_error_order_creation_api", "config.json")
logger.info(api_address)

error_order_base_url = api_address+"/system.webapi.asyncorder/v1/orders"
order_details_base_url = "https://imservices-qa1-usch01.corporate.ingrammicro.com:9043/ea-api/v1/orderdetails"