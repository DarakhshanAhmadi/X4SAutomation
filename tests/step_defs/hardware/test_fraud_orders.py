from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateErrorOrdersData import ValidateErrorOrdersData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
order_management_srv_obj = X4AInputOrderDbManagementService()


@scenario("features/hardware/fraud_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/fraud_orders.feature", "Verify Fraud Orders tab")
def test_fraud_order_tab():
    pass


@scenario("features/hardware/fraud_orders.feature", "Verify Reprocess Order Button")
def test_reprocess_order_button():
    pass


@scenario("features/hardware/fraud_orders.feature", "Verify Order in list after successful reprocess")
def test_verify_order_in_list_after_successful_reprocess():
    pass


@scenario("features/hardware/fraud_orders.feature", "Verify fraud Cancel Order Button")
def test_verify_fraud_cancel_order_button():
    pass


@scenario("features/hardware/fraud_orders.feature", "Verify Cancel order popup after click on Yes, Cancel order button")
def test_verify_cancel_order_popup_after_click_on_yes_cancel_order_button():
    pass


@scenario("features/hardware/fraud_orders.feature", "Verify to click on Cancel order button without giving reason")
def test_cancel_order_without_reason():
    pass


@scenario("features/hardware/fraud_orders.feature", "Verify on click Cancel order button with proper reason")
def test_cancel_order_with_reason():
    pass


@scenario("features/hardware/fraud_orders.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    breakpoint()
    create_order_steps = ValidateErrorOrdersData(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "fraud_orders"
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
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        validate_error_orders_data.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('the user traverse to Error Order menu'))
def click_on_error_orders_menu(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.click_on_error_orders(feature_file_name, screen_shot):
            raise Exception("Failed to click on error Orders menu")
    except Exception as e:
        logger.error("Error while clicking on Error Orders menu %s", e)
        raise e


@then(parsers.parse('Verify that Fraud Orders tab shown on Error orders page'))
def fraud_orders_tab_visible(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.is_fraud_orders_tab_visible(feature_file_name):
            raise Exception("Failed to verify that Fraud Orders tab shown on Error orders page")
    except Exception as e:
        logger.error("Error while verify that Order value header data on Order Details page %s", e)
        raise e


@when(parsers.parse('Search and Select the Order'))
def search_select_order_record(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("fraud_reprocess_order_confirmation_id")
        if not create_order_steps.search_and_select_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select fraud first record")
    except Exception as e:
        logger.error("Error while selecting fraud first record %s", e)
        raise e


@then(parsers.parse('Verify that Reprocess Order button should display'))
def reprocess_order_button_visible(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.is_reprocess_order_button_visible(feature_file_name):
            raise Exception("Failed to verify that Reprocess Order Button")
    except Exception as e:
        logger.error("Error while verify that Reprocess Order Button %s", e)
        raise e


@when(parsers.parse('Reprocess Order Button button clicked'))
def do_click_reprocess_order_button(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_reprocess_order_button(feature_file_name):
            raise Exception("Failed to click Reprocess Order button")
    except Exception as e:
        logger.error("Error while clicking the Reprocess Order button %s", e)
        raise e


@then(parsers.parse('Verify the Reprocess Order popup'))
def verify_reprocess_order_popup(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_reprocess_order_popup(feature_file_name):
            raise Exception("Failed to verify that Reprocess Order popup")
    except Exception as e:
        logger.error("Error while verifying the Reprocess Order popup %s", e)


@when(parsers.parse('Click to Review button'))
def click_on_review_button(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_reprocess_order_review_button(feature_file_name):
            raise Exception("Failed to click on Review Button")
    except Exception as e:
        logger.error("Error while clicking on Review Button %s", e)
        raise e


@then(parsers.parse('Verify Order Details page opened'))
def verify_order_details_page(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_order_details_page(feature_file_name):
            raise Exception("Failed to verify Order Details page opened")
    except Exception as e:
        logger.error("Error while verifying Order Details page %s", e)
        raise e


@when(parsers.parse('Search and Select the Order for Cancel'))
def search_select_order_record(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        fraud_cancel_order_confirmation_id = input_order_data.get("fraud_cancel_order_confirmation_id")
        if not create_order_steps.search_and_select_order(feature_file_name, fraud_cancel_order_confirmation_id):
            raise Exception("Failed to select fraud first record")
    except Exception as e:
        logger.error("Error while selecting fraud first record %s", e)
        raise e


@when(parsers.parse('Click on Reprocess Order Yes button'))
def click_on_reprocess_order_yes_button(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_reprocess_order_yes_button(feature_file_name):
            raise Exception("Failed to click on Yes, Reprocess Order Button")
    except Exception as e:
        logger.error("Error while clicking on Yes, Reprocess Order Button %s", e)
        raise e


@then(parsers.parse('Verify that Reprocessed! Order was successfully resubmitted message should display'))
def verify_reprocess_order_success_message(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_reprocess_order_success_message(feature_file_name):
            raise Exception("failed to verify Reprocessed! Order was successfully resubmitted success message")
    except Exception as e:
        logger.error("Error while verifying Reprocessed! Order was successfully resubmitted success message %s", e)
        raise e


@then(parsers.parse('Verify that Order should not be there in list'))
def verify_order_not_in_list(init_driver):
    breakpoint()
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("fraud_reprocess_order_confirmation_id")
        if not validate_error_orders_data.do_verify_order_in_list(feature_file_name, confirmation_id):
            raise Exception("failed to Verify that Reprocess Order should not be there in list")
    except Exception as e:
        logger.error("Error while Verifying that Reprocess Order should not be there in list %s", e)
        raise e


@then(parsers.parse('Verify that Cancel Order button should display'))
def fraud_cancel_order_button_visible(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.is_fraud_cancel_order_button_visible(feature_file_name):
            raise Exception("Failed to verify that Fraud Cancel Order Button")
    except Exception as e:
        logger.error("Error while verify that Fraud Cancel Order Button %s", e)
        raise e


@when(parsers.parse('Cancel Order Button button clicked'))
def do_click_cancel_order_button(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_cancel_order_button(feature_file_name):
            raise Exception("Failed to click Cancel Order button")
    except Exception as e:
        logger.error("Error while clicking the Cancel Order button %s", e)
        raise e


@then(parsers.parse('Verify the Fraud Cancel Order popup'))
def verify_cancel_order_popup(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_fraud_cancel_order_popup(feature_file_name):
            raise Exception("Failed to verify that Cancel Order popup")
    except Exception as e:
        logger.error("Error while verifying the Cancel Order popup %s", e)


@when(parsers.parse('click to No keep order button'))
def do_click_no_cancel_button(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_click_no_cancel_button(feature_file_name, screen_shot):
            raise Exception("Failed to click No button of cancel order popup")
    except Exception as e:
        logger.error("Error while clicking No button of cancel order popup %s", e)
        raise e


@when(parsers.parse('Click on the Yes Cancel Order button'))
def do_click_yes_cancel_button(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_click_fraud_yes_cancel_button(feature_file_name, screen_shot):
            raise Exception("failed to click YES, Cancel Order button")

    except Exception as e:
        logger.error("Error while clicking YES, Cancel Order button %s", e)
        raise e


@then(parsers.parse('Verify the cancel order popup after yes button'))
def verify_cancel_order_popup_after_yes(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.verify_cancel_order_popup_after_yes(feature_file_name, screen_shot):
            raise Exception("Failed to verify cancel order popup after clicking yes button")
    except Exception as e:
        logger.error("Error while verifying cancel order popup after clicking yes button %s", e)
        raise e


@when(parsers.parse('Click on the BACK button'))
def do_click_back_cancel_button(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_click_back_cancel_button(feature_file_name, screen_shot):
            raise Exception("failed to Click BACK Cancel button")
    except Exception as e:
        logger.error("Error while clicking BACK Cancel button %s", e)
        raise e


@then(parsers.parse('Verify redirect back to Cancel Order popup'))
def verify_redirect_cancel_order_popup(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_verify_fraud_cancel_order_popup(feature_file_name):
            raise Exception("Failed to verify that Cancel order popup")
    except Exception as e:
        logger.error("Error while verifying the Cancel order popup %s", e)
        raise e


@when(parsers.parse('Click on Cancel Order button without giving reason'))
def do_cancel_order_without_reason(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_cancel_order_without_reason(feature_file_name, screen_shot):
            raise Exception("Failed to Click on Cancel Order button without giving reason")
    except Exception as e:
        logger.error("Error while Clicking on Cancel Order button without giving reason %s", e)
        raise e


@then(parsers.parse('Verify Cancel order message'))
def verify_cancel_order_message(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_verify_cancel_order_message(feature_file_name, screen_shot):
            raise Exception("Failed to verify that Cancel order message")
    except Exception as e:
        logger.error("Error while verifying the Cancel order message %s", e)
        raise e


@when(parsers.parse('Order cancel with proper reason'))
def do_cancel_order_with_reason(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_cancel_order_with_reason(feature_file_name, screen_shot):
            raise Exception("failed to Cancel order with reason")

    except Exception as e:
        logger.error("Error while cancelling order with reason %s", e)
        raise e


@then(parsers.parse('Verify successfully cancel order message'))
def do_cancel_order_success_message(init_driver):
    feature_file_name = "fraud_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.do_cancel_order_success_message(feature_file_name, screen_shot):
            raise Exception("failed to verify Cancel order success message")

    except Exception as e:
        logger.error("Error while verifying cancel order success message %s", e)
        raise e


@then(parsers.parse('Verify that Cancel Order should not be there in list'))
def verify_cancel_order_not_in_list(init_driver):
    breakpoint()
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("fraud_cancel_order_confirmation_id")
        if not validate_error_orders_data.do_verify_order_in_list(feature_file_name, confirmation_id):
            raise Exception("failed to Verify that Cancel Order should not be there in list")
    except Exception as e:
        logger.error("Error while Verifying that Cancel Order should not be there in list %s", e)
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "fraud_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        validate_error_orders_data.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e
