from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateInventoryInquiryData import ValidateInventoryInquiryData
from tests.test_base_x4a import BaseTest

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
order_management_srv_obj = X4AInputOrderDbManagementService()



@scenario("features/hardware/inventory_inquiry.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/inventory_inquiry.feature", "Verify table columns and quick search options")
def test_verify_columns_and_search_options():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "inventory_inquiry"
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = validate_inventory_inquiry.filtered_orders_by_feature_file(test_data_order, feature_file_name)
        logger.info(filtered_order_data)
        for order_index, test_data_order in filtered_order_data.iterrows():
            x4a_input_order_list.clear()
            logger.info(test_data_order)
            x4a_input_order_data = prepare_obj.prepare_x4a_inp_ord_data_obj(test_data_order)
            x4a_input_order_list.append(x4a_input_order_data)
            order_management_srv_obj.save_x4a_input_order(db_file_path, x4a_input_order_list)
        environment = parse_config_json.get_data_from_config_json("environment", "environment_type", "config.json")
        logger.info(environment)
        if environment == 'Stage':
            url = parse_config_json.get_data_from_config_json("x4aStageCredentials", "x4aBaseUrl", "config.json")
        else:
            url = parse_config_json.get_data_from_config_json("x4aBetaCredentials", "x4aBaseUrl", "config.json")
        init_driver.get(url)
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('provide user ID and Password to login'))
def login(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        validate_inventory_inquiry.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@then(parsers.parse('the user traverse to Inventory Inquiry menu'))
def click_on_inventory_inquiry_menu(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.click_on_inventory_inquiry(feature_file_name, screen_shot):
            raise Exception("Failed to click on Inventory Inquiry menu")
    except Exception as e:
        logger.error("Error while clicking on Inventory Inquiry menu %s", e)
        raise e


@then(parsers.parse('verify the columns in the table are correct'))
def check_table_columns(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.verify_inventory_inquiry_table_columns(feature_file_name, screen_shot):
            raise Exception("Failed to verify Inventory Inquiry table columns")
    except Exception as e:
        logger.error("Error while verifying Inventory Inquiry table columns %s", e)
        raise e
