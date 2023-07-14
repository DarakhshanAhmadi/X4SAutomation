import os
from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateData import CreateOrder

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()


@scenario("features/hardware/aged_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass

@scenario("features/hardware/aged_orders.feature", "Search order by BCN from Aged Order")
def test_aged_orders():
    pass

@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    create_order_steps = CreateOrder(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "aged_orders"
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = create_order_steps.filtered_orders_by_feature_file(test_data_order, feature_file_name)
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


@then(parsers.parse('provide user ID and Password to login'))
def login(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        create_order_steps.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('the user traverse to Aged Order Tab'))
def click_on_aged_orders(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.click_on_aged_order(feature_file_name, screen_shot):
            raise Exception("Failed to click on aged orders")
    except Exception as e:
        logger.error("Error while clicking on aged orders %s", e)
        raise e
