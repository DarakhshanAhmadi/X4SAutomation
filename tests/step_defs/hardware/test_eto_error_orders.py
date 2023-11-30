from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from RestApi.Operations.data_creation_via_api import DataCreationViaApi
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateEmailToOrderData import ValidateEmailToOrderData
from pages.X4A.TestSteps.validateOrderExceptionData import ValidateOrderExceptionData
from pages.X4A.TestSteps.validateSalesOrdersData import ValidateSalesOrdersData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
order_management_srv_obj = X4AInputOrderDbManagementService()


@scenario("features/hardware/eto_error_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/eto_error_orders.feature", "Validate ETO error order details")
def test_validate_eto_error_order_details():
    pass


@scenario("features/hardware/eto_error_orders.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('Launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    create_order_steps = ValidateOrderExceptionData(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "order_exception_orders"
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


@then(parsers.parse('Provide user ID and Password to login'))
def login(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        validate_order_exception_data.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('The user traverse to Order Exception menu'))
def click_on_order_exception_menu(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.click_on_order_exception(feature_file_name, screen_shot):
            raise Exception("Failed to click on Order Exception menu")
    except Exception as e:
        logger.error("Error while clicking on Order Exception menu %s", e)
        raise e


@then(parsers.parse('Click on Email to order tab'))
def click_eto_tab(init_driver):
    feature_file_name = "eto_error_orders"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        email_to_order_steps.verify_eto_tab_click(feature_file_name)
        logger.info("Clicked on email to order tab successfully.")
    except Exception as e:
        logger.error("Not able to click on email to order tab %s" + str(e))
        raise e


@then(parsers.parse('Click on eto error order'))
def click_on_eto_error_order(init_driver):
    feature_file_name = "eto_error_orders"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        email_to_order_steps.verify_eto_error_order_click(feature_file_name)
        logger.info("Clicked on eto error order successfully.")
    except Exception as e:
        logger.error("Not able to click on error order %s" + str(e))
        raise e


@then(parsers.parse('Verify the eto error order details'))
def verify_eto_error_order_details(init_driver):
    feature_file_name = "eto_error_orders"
    email_to_order_steps = ValidateEmailToOrderData(init_driver)
    try:
        email_to_order_steps.eto_error_order_details_validate(feature_file_name)
        logger.info("Verified eto error order details successfully.")
    except Exception as e:
        logger.error("Not able to verify eto error order details %s" + str(e))
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "eto_error_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        validate_sales_orders.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e