from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from RestApi.Operations.data_creation_via_api import DataCreationViaApi
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateErrorOrdersData import ValidateErrorOrdersData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
order_management_srv_obj = X4AInputOrderDbManagementService()


@scenario("features/hardware/data_errors_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Verify resubmit order popup")
def test_resubmit_order_popup():
    pass


@scenario("features/hardware/data_errors_orders.feature",
          "Verify Order not present in list after successfully resubmitted")
def test_verify_order_in_list_after_successful_resubmitted():
    pass


@scenario("features/hardware/data_errors_orders.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('the error order is created via api'))
def create_order(init_driver):
    feature_file_name = "data_errors_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_error_order_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_in_db(db_file_path, feature_file_name, confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    create_order_steps = ValidateErrorOrdersData(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "data_errors_orders"
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
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        validate_error_orders_data.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('the user traverse to Error Order menu'))
def click_on_error_orders_menu(init_driver):
    feature_file_name = "data_errors_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.click_on_error_orders(feature_file_name, screen_shot):
            raise Exception("Failed to click on error Orders menu")
    except Exception as e:
        logger.error("Error while clicking on Error Orders menu %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order'))
def search_select_data_errors_order_record(init_driver):
    feature_file_name = "data_errors_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("data_errors_resubmit_order_confirmation_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that Resubmit Order button should display'))
def resubmit_order_button_visible(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.is_resubmit_order_button_visible(feature_file_name):
            raise Exception("Failed to verify that Data Error Resubmit Order Button")
    except Exception as e:
        logger.error("Error while verify that Data Error Resubmit Order Button %s", e)
        raise e


@then(parsers.parse('Update the correct Reseller PO'))
def update_the_correct_reseller_po(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.update_reseller_po_data_error_order(feature_file_name):
            raise Exception("Failed to update correct reseller po for data error order")
    except Exception as e:
        logger.error("Error while updating correct reseller po for data error order %s", e)
        raise e


@then(parsers.parse('Update the correct End customer order'))
def update_the_correct_end_customer_order(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.update_end_customer_order_data_error_order(feature_file_name):
            raise Exception("Failed to update correct End customer order for data error order")
    except Exception as e:
        logger.error("Error while updating correct End customer order for data error order %s", e)
        raise e


@when(parsers.parse('Resubmit Order Button clicked'))
def do_click_resubmit_order_button(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_resubmit_order_button(feature_file_name):
            raise Exception("Failed to click Resubmit Order button")
    except Exception as e:
        logger.error("Error while clicking the Resubmit Order button %s", e)
        raise e


@then(parsers.parse('Verify contents of Resubmit Order Confirmation popup'))
def verify_resubmit_order_popup(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_content_of_resubmit_order_popup(feature_file_name):
            raise Exception("Failed to verify contents of Resubmit Order popup")
    except Exception as e:
        logger.error("Error while verifying contents of Resubmit Order popup %s", e)


@when(parsers.parse('Click on Review button'))
def click_on_review_button(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_resubmit_order_review_button(feature_file_name):
            raise Exception("Failed to click on Review Button")
    except Exception as e:
        logger.error("Error while clicking on Review Button %s", e)
        raise e


@then(parsers.parse('Verify Order Details page opened'))
def verify_order_details_page(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_order_details_page(feature_file_name):
            raise Exception("Failed to verify Order Details page opened")
    except Exception as e:
        logger.error("Error while verifying Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Resubmit Order Yes button'))
def click_on_reprocess_order_yes_button(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_reprocess_order_yes_button(feature_file_name):
            raise Exception("Failed to click on Yes, "
                            " Order Button")
    except Exception as e:
        logger.error("Error while clicking on Yes, Resubmit Order Button %s", e)
        raise e


@then(parsers.parse('Verify that Order has been successfully resubmitted message should display'))
def verify_resubmitted_order_success_message(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_resubmitted_order_success_message(feature_file_name):
            raise Exception("failed to verify Order has been successfully resubmitted success message")
    except Exception as e:
        logger.error("Error while verifying Order has been successfully resubmitted success message %s", e)
        raise e


@then(parsers.parse('Verify that Data Error Order should not be there in list'))
def verify_data_error_order_not_in_list(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("data_errors_resubmit_order_confirmation_id")
        if not validate_error_orders_data.do_verify_data_error_order_in_list(feature_file_name, confirmation_id):
            raise Exception("failed to Verify that Data Error resubmitted Order should not be there in list")
    except Exception as e:
        logger.error("Error while Verifying that Data Error resubmitted Order should not be there in list %s", e)
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        validate_error_orders_data.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e
