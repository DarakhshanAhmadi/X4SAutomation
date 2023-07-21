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


@scenario("features/hardware/cancel_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/cancel_orders.feature", "Verify Cancel order button for more than one record")
def test_error_list():
    pass


@scenario("features/hardware/cancel_orders.feature", "Verify Cancel order button for one record")
def test_single_record_error_list():
    pass


@scenario("features/hardware/cancel_orders.feature", "Verify on click Yes, Cancel order button")
def test_cancel_order_popup():
    pass


@scenario("features/hardware/cancel_orders.feature", "Verify on click cancel order button without giving reason")
def test_cancel_order_without_reason():
    pass


@scenario("features/hardware/cancel_orders.feature", "Verify on click cancel order button with proper reason")
def test_cancel_order_with_reason():
    pass


@scenario("features/hardware/cancel_orders.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    create_order_steps = CreateOrder(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "cancel_orders"
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
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        # breakpoint()
        create_order_steps.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('the user traverse to Error Order menu'))
def click_on_error_orders_menu(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.click_on_error_orders(feature_file_name, screen_shot):
            raise Exception("Failed to click on error Orders menu")
    except Exception as e:
        logger.error("Error while clicking on Error Orders menu %s", e)
        raise e


@when(parsers.parse('Selected more than one record from System Error list'))
def multiple_record_system_error_list(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.select_multiple_record(feature_file_name, screen_shot):
            raise Exception("Failed to select multiple record")
    except Exception as e:
        logger.error("Error while selecting multiple record %s", e)
        raise e


@then(parsers.parse('Cancel button should remain disable'))
def status_of_disabled_cancel_button(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    status = 'disabled'
    try:
        if not create_order_steps.do_verify_cancel_button(feature_file_name, screen_shot, status):
            raise Exception("Failed to verify that cancel button is disabled")
    except Exception as e:
        logger.error("Error while verifying that cancel button is disabled %s", e)
        raise e


@when(parsers.parse('Selected only one record from System Error list'))
def single_record_system_error_list(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.single_record_list(feature_file_name, screen_shot):
            raise Exception("Failed to select single record")
    except Exception as e:
        logger.error("Error while selecting single record %s", e)
        raise e


@then(parsers.parse('Cancel button should get enable'))
def status_of_enabled_cancel_button(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    status = 'enabled'
    try:
        if not create_order_steps.do_verify_cancel_button(feature_file_name, screen_shot, status):
            raise Exception("Failed to verify that cancel button is enabled")
    except Exception as e:
        logger.error("Error while verifying that cancel button is enabled %s", e)
        raise e


@when(parsers.parse('Cancel button clicked'))
def do_click_cancel_button(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_click_cancel_button(feature_file_name, screen_shot):
            raise Exception("Failed to click cancel button")
    except Exception as e:
        logger.error("Error while clicking the cancel button %s", e)
        raise e


@then(parsers.parse('verify the cancel order popup'))
def verify_cancel_order_popup(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_verify_cancel_order_popup(feature_file_name, screen_shot):
            raise Exception("Failed to verify that cancel order popup")
    except Exception as e:
        logger.error("Error while verifying the cancel order popup %s", e)
        raise e


@when(parsers.parse('click to No keep order button'))
def do_click_no_cancel_button(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_click_no_cancel_button(feature_file_name, screen_shot):
            raise Exception("Failed to click No button of cancel order popup")
    except Exception as e:
        logger.error("Error while clicking No button of cancel order popup %s", e)
        raise e


@then(parsers.parse('verify error detail page opened'))
def verify_error_details_page(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_verify_error_details_page(feature_file_name, screen_shot):
            raise Exception("Failed to verify error details page opened")
    except Exception as e:
        logger.error("Error while verifying error details page %s", e)
        raise e


@when(parsers.parse('Click on the YES button'))
def do_click_yes_cancel_button(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_click_yes_cancel_button(feature_file_name, screen_shot):
            raise Exception("failed to click yes Cancel button")

    except Exception as e:
        logger.error("Error while clicking yes cancel button %s", e)
        raise e


@then(parsers.parse('verify the cancel order popup after yes button'))
def verify_cancel_order_popup_after_yes(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.verify_cancel_order_popup_after_yes(feature_file_name, screen_shot):
            raise Exception("Failed to verify cancel order popup after clicking yes button")
    except Exception as e:
        logger.error("Error while verifying cancel order popup after clicking yes button %s", e)
        raise e


@when(parsers.parse('Click on the BACK button'))
def do_click_back_cancel_button(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_click_back_cancel_button(feature_file_name, screen_shot):
            raise Exception("failed to click back Cancel button")

    except Exception as e:
        logger.error("Error while clicking back cancel button %s", e)
        raise e


@then(parsers.parse('verify redirect back to "Cancel Order" popup'))
def verify_redirect_cancel_order_popup(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_verify_cancel_order_popup(feature_file_name, screen_shot):
            raise Exception("Failed to verify that cancel order popup")
    except Exception as e:
        logger.error("Error while verifying the cancel order popup %s", e)
        raise e


@when(parsers.parse('Click Cancel Order button without giving reason'))
def do_cancel_order_without_reason(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_cancel_order_without_reason(feature_file_name, screen_shot):
            raise Exception("failed to cancel order without reason")

    except Exception as e:
        logger.error("Error while cancelling order without reason %s", e)
        raise e


@then(parsers.parse('verify cancel order message'))
def verify_cancel_order_message(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_verify_cancel_order_message(feature_file_name, screen_shot):
            raise Exception("Failed to verify that cancel order message")
    except Exception as e:
        logger.error("Error while verifying the cancel order message %s", e)
        raise e


@when(parsers.parse('Order cancel with proper reason'))
def do_cancel_order_with_reason(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_cancel_order_with_reason(feature_file_name, screen_shot):
            raise Exception("failed to cancel order with reason")

    except Exception as e:
        logger.error("Error while cancelling order with reason %s", e)
        raise e


@then(parsers.parse('verify successfully cancel order message'))
def do_cancel_order_success_message(init_driver):
    feature_file_name = "cancel_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_cancel_order_success_message(feature_file_name, screen_shot):
            raise Exception("failed to verify cancel order success message")

    except Exception as e:
        logger.error("Error while verifying cancel order success message %s", e)
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        create_order_steps.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e
