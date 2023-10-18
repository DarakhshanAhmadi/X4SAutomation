# import datetime
import os

from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AEmailToOrderDataDbManagementService import X4AEmailToOrderDataDbManagementService
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateEmailToOrderData import ValidateEmailToOrderData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_email_to_order_list = []
db_file_path = ReadConfig.get_db_file_path()
email_to_order_management_srv_obj = X4AEmailToOrderDataDbManagementService()
latest_downloaded_file = ""
latest_downloaded_files = ""


@scenario("features/hardware/email_to_order.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/email_to_order.feature", "ETO order management")
def test_ETO_order_management():
    pass


@scenario("features/hardware/email_to_order.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    email_to_order_management_srv_obj = X4AEmailToOrderDataDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "email_to_order"
    try:
        #
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = email_to_order_steps.filtered_orders_by_feature_file(test_data_order,
                                                                                      feature_file_name)
        logger.info("the value of filtered data", filtered_order_data)
        for order_index, test_data_order in filtered_order_data.iterrows():
            x4a_email_to_order_list.clear()
            logger.info("the value of test data", test_data_order)
            x4a_email_to_order_data = prepare_obj.prepare_x4a_email_to_order_data_obj(test_data_order)
            x4a_email_to_order_list.append(x4a_email_to_order_data)
            email_to_order_management_srv_obj.save_scenario_details(db_file_path, x4a_email_to_order_list)
        environment = parse_config_json.get_data_from_config_json("environment", "environment_type", "config.json")
        logger.info(environment)
        if environment == 'Stage':
            url = parse_config_json.get_data_from_config_json("x4aStageCredentials", "x4aBaseUrl", "config.json")
        else:
            url = parse_config_json.get_data_from_config_json("x4aBetaCredentials", "x4aBaseUrl", "config.json")
        init_driver.get(url)
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s" + str(e))
        raise e


@then(parsers.parse('provide user ID and Password to login'))
def login(init_driver):
    feature_file_name = "email_to_order"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        email_to_order_steps.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s" + str(e))
        raise e


@when(parsers.parse('the user traverse to Email to order menu'))
def click_on_email_to_order_menu(init_driver):
    feature_file_name = "email_to_order"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        if not email_to_order_steps.click_on_email_to_order_menu(feature_file_name, screen_shot):
            raise Exception("Failed to click on Email to order menu")
    except Exception as e:
        logger.error("Error while clicking on Email to order menu %s" + str(e))
        raise e


@then(parsers.parse('verify Email to order page'))
def verify_email_to_order_page(init_driver):
    feature_file_name = "email_to_order"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        if not email_to_order_steps.verify_email_to_order_page(feature_file_name, screen_shot):
            raise Exception("Failed to verify Email Orders page")
    except Exception as e:
        logger.error("Error while verifying Email Orders page %s" + str(e))
        raise e


@when(parsers.parse('ETO order selected'))
def do_eto_select_order(init_driver):
    feature_file_name = "email_to_order"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        if not email_to_order_steps.do_eto_select_order(feature_file_name, screen_shot):
            raise Exception("Failed to select ETO order")
    except Exception as e:
        logger.error("Error while selecting ETO order %s" + str(e))
        raise e


#
@then(parsers.parse('verify ETO order page headers'))
def verify_ETO_order_page_haeder(init_driver):
    feature_file_name = "email_to_order"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        if not email_to_order_steps.verify_ETO_order_page_haeder(feature_file_name, screen_shot):
            raise Exception("Failed to verify ETO order page headers")
    except Exception as e:
        logger.error("Error while verifying ETO order page headers %s" + str(e))
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "email_to_order"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        email_to_order_steps.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s" + str(e))
        raise e
