from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from RestApi.Operations.data_creation_via_api import DataCreationViaApi
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateOrderExceptionData import ValidateOrderExceptionData
from pages.X4A.TestSteps.validateSalesOrdersData import ValidateSalesOrdersData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
order_management_srv_obj = X4AInputOrderDbManagementService()


@scenario("features/hardware/order_exception_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify resubmit order popup")
def test_resubmit_order_popup():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify Order not present in list after successfully resubmitted")
def test_verify_order_in_list_after_successful_resubmitted():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify Reference Details Edit popup content")
def test_verify_reference_details_edit_popup_contents():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify the PO number and End customer order invalid message")
def test_verify_po_and_end_customer_order_number_invalid_message():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify the PO number and End customer order for the max length")
def test_verify_po_and_end_customer_max_length():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify resubmitted successful message")
def test_verify_resubmitted_successful_message():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify Shipping Notes Edit popup content")
def test_verify_shipping_notes_edit_popup_contents():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Updated data should get displayed under shipping notes")
def test_updated_data_display_under_shipping_notes():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify filter panel options")
def test_filter_panel_options():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify Order entry method and Country options list")
def test_order_entry_method_country_options_list():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Selected values get cleared from filter header")
def test_selected_values_get_cleared_from_filter_header():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify Data in grid should get updated as per selected filter")
def test_data_in_grid_should_get_updated_as_per_selected_filter():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Last order attempt on section should display inside filter panel")
def test_last_order_attempt_on_section_should_display_inside_filter_panel():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Created on section should display inside filter panel")
def test_created_on_on_section_should_display_inside_filter_panel():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify VMF Details Edit popup content")
def test_vmf_details_edit_popup_content():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Updated VMF data should get display on Order Details page")
def test_updated_vmf_data_should_get_display_on_order_details_page():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify End User Details Edit popup content")
def test_end_user_details_edit_popup_content():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Searching End User")
def test_searching_end_user():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify Add New End User Edit popup content")
def test_add_new_end_user_edit_popup_content():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify Billing Address Edit popup content")
def test_billing_address_edit_popup_content():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify billing address search with suffix")
def test_verify_billing_address_search_with_suffix():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify that order resubmitted successfully after click on Mark for Cancel option")
def test_verify_that_order_resubmitted_successfully_after_click_on_mark_for_cancel_option():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify that At least one order line is required to resubmit the order message")
def test_verify_that_at_least_one_order_line_is_required_to_resubmit_the_order_message():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Modify existing Order line")
def test_modify_existing_order_line():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Update Quantity, Reseller price and End User PO value and resubmit the order")
def test_update_quantity_reseller_price_and_end_user_po_value_and_resubmit_the_order():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Operator Id on Order Details Page")
def test_operator_id_on_order_details_page():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Order Channel on Order Details Page")
def test_operator_channel_on_order_details_page():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Shipping Details on Order Details Page")
def test_shipping_details_on_order_details_page():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify Shipping Address Edit popup contents")
def test_verify_shipping_address_edit_popup_contents():
    pass


@scenario("features/hardware/order_exception_orders.feature", "Verify Shipping address search")
def test_verify_shipping_address_search():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify Resubmitting Data error order with duplicate PO# for US marketplace")
def test_verify_resubmiting_data_error_order_with_duplicate_po_for_us():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify Resubmitting Data error order with duplicate PO# for CA marketplace")
def test_verify_resubmiting_data_error_order_with_duplicate_po_for_ca():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Verify Resubmitting Data error order with duplicate case sensitive PO# for CA marketplace")
def test_verify_resubmiting_data_error_order_with_duplicate_case_sensitive_po_for_ca():
    pass


@scenario("features/hardware/order_exception_orders.feature",
          "Order Exception Search")
def test_order_exception_search():
    pass


@scenario("features/hardware/order_exception_orders.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('The order exception is created via api'))
def create_order_exception(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_in_db(db_file_path, feature_file_name, confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data Error order %s", e)
        raise e


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


@when(parsers.parse('Search and Select the Data Errors Order'))
def search_select_data_errors_order_record(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("data_errors_resubmit_order_confirmation_id")
        if not validate_order_exception_data.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that Resubmit Order button should display'))
def resubmit_order_button_visible(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.is_resubmit_order_button_visible(feature_file_name):
            raise Exception("Failed to verify that Data Error Resubmit Order Button")
    except Exception as e:
        logger.error("Error while verify that Data Error Resubmit Order Button %s", e)
        raise e


@then(parsers.parse('Update the correct Reseller PO'))
def update_the_correct_reseller_po(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.update_reseller_po_data_error_order(feature_file_name):
            raise Exception("Failed to update correct reseller po for data error order")
    except Exception as e:
        logger.error("Error while updating correct reseller po for data error order %s", e)
        raise e


@then(parsers.parse('Update the correct End customer order'))
def update_the_correct_end_customer_order(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.update_end_customer_order_data_error_order(feature_file_name):
            raise Exception("Failed to update correct End customer order for data error order")
    except Exception as e:
        logger.error("Error while updating correct End customer order for data error order %s", e)
        raise e


@when(parsers.parse('Resubmit Order Button clicked'))
def do_click_resubmit_order_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_resubmit_order_button(feature_file_name):
            raise Exception("Failed to click Resubmit Order button")
    except Exception as e:
        logger.error("Error while clicking the Resubmit Order button %s", e)
        raise e


@then(parsers.parse('Verify contents of Resubmit Order Confirmation popup'))
def verify_resubmit_order_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_content_of_resubmit_order_popup(feature_file_name):
            raise Exception("Failed to verify contents of Resubmit Order popup")
    except Exception as e:
        logger.error("Error while verifying contents of Resubmit Order popup %s", e)


@when(parsers.parse('Click on Review button'))
def click_on_review_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_resubmit_order_review_button(feature_file_name):
            raise Exception("Failed to click on Review Button")
    except Exception as e:
        logger.error("Error while clicking on Review Button %s", e)
        raise e


@then(parsers.parse('Verify Order Details page opened'))
def verify_order_details_page(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_details_page(feature_file_name):
            raise Exception("Failed to verify Order Details page opened")
    except Exception as e:
        logger.error("Error while verifying Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Resubmit Order Yes button'))
def click_on_reprocess_order_yes_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_reprocess_order_yes_button(feature_file_name):
            raise Exception("Failed to click on Yes, "
                            " Order Button")
    except Exception as e:
        logger.error("Error while clicking on Yes, Resubmit Order Button %s", e)
        raise e


@then(parsers.parse('Verify that Order has been successfully resubmitted message should display'))
def verify_resubmitted_order_success_message(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_resubmitted_order_success_message(feature_file_name):
            raise Exception("failed to verify Order has been successfully resubmitted success message")
    except Exception as e:
        logger.error("Error while verifying Order has been successfully resubmitted success message %s", e)
        raise e


@then(parsers.parse('Verify that Data Error Order should not be there in list'))
def verify_data_error_order_not_in_list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("data_errors_resubmit_order_confirmation_id")
        if not validate_order_exception_data.do_verify_data_error_order_in_list(feature_file_name, confirmation_id):
            raise Exception("failed to Verify that Data Error resubmitted Order should not be there in list")
    except Exception as e:
        logger.error("Error while Verifying that Data Error resubmitted Order should not be there in list %s", e)
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        validate_order_exception_data.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e


@given(parsers.parse('The order exception is created via api for Reference Details'))
def create_order_for_reference_details(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_reference_details_in_db(db_file_path, feature_file_name,
                                                                                      confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for Reference Details'))
def search_select_data_errors_order_record_for_reference_details(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("modify_reference_details_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that Edit icon should display beside Reference Details title'))
def reference_details_edit_icon_visible(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.is_reference_details_edit_icon_visible(feature_file_name):
            raise Exception("Failed to verify that Edit icon display beside Reference Details title")
    except Exception as e:
        logger.error("Error while verify that Edit icon display beside Reference Details title %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit Reference Details popup'))
def verify_contents_of_edit_reference_details_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_edit_reference_details(feature_file_name):
            raise Exception("Failed to verify contents of Edit Reference Details popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit Reference Details popup %s", e)


@then(parsers.parse('Verify PO textbox should not allow entering more than 18 characters'))
def verify_po_textbox_should_not_allow_more_that_18_characters(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_more_than_eighteen_char_in_po_field(feature_file_name):
            raise Exception("Failed to Verify PO # textbox should not allow entering more than 18 characters")
    except Exception as e:
        logger.error("Error while Verify PO # textbox should not allow entering more than 18 characters %s", e)


@then(parsers.parse('Verify that PO number is invalid once add this ^ special character'))
def verify_po_textbox_should_not_allow_more_caret_special_char(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_po_number_invalid_message(feature_file_name):
            raise Exception("Failed to PO number is invalid once add this ^ special character")
    except Exception as e:
        logger.error("Error while Verify PO number is invalid once add this ^ special character %s", e)


@then(parsers.parse('Verify End customer order textbox should not allow entering more than 18 characters'))
def verify_end_customer_order_textbox_should_not_allow_more_that_18_characters(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_more_than_eighteen_char_in_end_customer_order_field(
                feature_file_name):
            raise Exception(
                "Failed to Verify End customer order # textbox should not allow entering more than 18 characters")
    except Exception as e:
        logger.error(
            "Error while Verify End customer order # textbox should not allow entering more than 18 characters %s", e)


@then(parsers.parse('Verify that End customer order number is invalid once add this ^ special character'))
def verify_end_customer_order_textbox_should_not_allow_caret_special_char(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_end_customer_order_number_invalid_message(feature_file_name):
            raise Exception("Failed to End customer order number is invalid once add this ^ special character")
    except Exception as e:
        logger.error("Error while Verify End customer order number is invalid once add this ^ special character %s", e)


@when(parsers.parse('Click on X icon then verify that modified data should not get updated on order details page'))
def verify_modified_data_not_update_after_click_on_x_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_modified_data_after_click_on_x_icon(feature_file_name):
            raise Exception(
                "Failed to Click on X icon then verify that modified data should not get updated on order details page")
    except Exception as e:
        logger.error(
            "Error while Click on X icon then verify that modified data should not get updated on order details page %s",
            e)


@when(
    parsers.parse('Click on Cancel button then verify that modified data should not get updated on order details page'))
def verify_modified_data_not_update_after_click_on_cancel_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_modified_data_after_click_on_cancel_button(feature_file_name):
            raise Exception(
                "Failed to Click on Cancel button then verify that modified data should not get updated on order details page")
    except Exception as e:
        logger.error(
            "Error while Click on Cancel button then verify that modified data should not get updated on order details page %s",
            e)


@when(
    parsers.parse(
        'Update PO and End customer order number with valid data then validate updated data on order details page'))
def update_po_and_end_customer_with_valid_data_then_validate(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_updated_po_and_end_customer_order_data(feature_file_name):
            raise Exception(
                "Failed to Update PO and End customer order number with valid data then validate updated data on order details page")
    except Exception as e:
        logger.error(
            "Error while updating PO and End customer order number with valid data then validate updated data on order details page %s",
            e)


@given(parsers.parse('The order exception is created via api for Shipping notes'))
def create_order_for_shipping_notes(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_shipping_notes_in_db(db_file_path, feature_file_name,
                                                                                   confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for Shipping Notes'))
def search_select_data_errors_order_record_for_shipping_notes(init_driver):
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("modify_shipping_notes_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that Edit icon should display beside Shipping Notes'))
def shipping_notes_edit_icon_visible(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.is_shipping_notes_edit_icon_visible(feature_file_name):
            raise Exception("Failed to verify that Edit icon display beside Shipping Notes")
    except Exception as e:
        logger.error("Error while verify that Edit icon display beside Shipping Notes %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit Shipping Notes popup'))
def verify_contents_of_edit_shipping_notes_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_edit_shipping_notes(feature_file_name):
            raise Exception("Failed to verify contents of Edit Shipping Notes popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit Shipping Notes popup %s", e)


@when(parsers.parse('Click on X icon on popup'))
def click_on_x_icon(init_driver):
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        if not create_order_steps.click_on_x_icon(feature_file_name):
            raise Exception("Failed to click on X icon on popup")
    except Exception as e:
        logger.error("Error while clicking on X icon on popup %s", e)
        raise e


@when(parsers.parse('Click on Cancel button on popup'))
def click_on_cancel_button(init_driver):
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        if not create_order_steps.click_on_cancel_button(feature_file_name):
            raise Exception("Failed to click on Cancel button on popup")
    except Exception as e:
        logger.error("Error while clicking on Cancel button on popup %s", e)
        raise e


@when(parsers.parse('Add the more 100 characters then validate message for maximum limit'))
def validate_maximum_limit_message(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_validate_maximum_limit_message(feature_file_name):
            raise Exception("Failed to Add the more 100 characters and validate message for maximum limit")
    except Exception as e:
        logger.error("Error while adding the more 100 characters and validate message for maximum limit %s", e)


@then(parsers.parse(
    'Update shipping notes with special characters and validate updated data should get display under shipping notes'))
def validate_maximum_limit_message(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_validate_updated_shipping_notes_data(feature_file_name):
            raise Exception(
                "Failed to Update shipping notes with special characters and validate updated data should get display under shipping notes")
    except Exception as e:
        logger.error(
            "Error while updateing shipping notes with special characters and validate updated data should get display under shipping notes %s",
            e)


@when(parsers.parse('Click on Filter icon'))
def click_on_filter_icon(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_filter_icon(feature_file_name):
            raise Exception("Failed to click Filter Icon")
    except Exception as e:
        logger.error("Error while clicking Filter icon %s", e)
        raise e


@then(parsers.parse('Verify filter panel options'))
def verify_filter_panel_options(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_filter_options(feature_file_name):
            raise Exception("Failed to verify filter options")
    except Exception as e:
        logger.error("Error while verifing filter options %s", e)
        raise e


@when(parsers.parse('Verify Order entry method options list'))
def verify_order_entry_method_options_list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_entry_method_options_list(feature_file_name):
            raise Exception("Failed to verify Order entry method options list")
    except Exception as e:
        logger.error("Error while verifing Order entry method options list %s", e)
        raise e


@then(parsers.parse('Verify Country options list'))
def verify_country_options_list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_country_options_list(feature_file_name):
            raise Exception("Failed to verify Country options list")
    except Exception as e:
        logger.error("Error while verifing Country options list %s", e)
        raise e


@then(parsers.parse('After selected any option clear all button should display'))
def verify_clear_all_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_clear_all_button(feature_file_name):
            raise Exception("Failed to verify after selected any option clear all button should display")
    except Exception as e:
        logger.error("Error while after selecting any option clear all button should display %s", e)
        raise e


@then(parsers.parse('Selected multiple order entry method options should get display in header'))
def verify_selected_multiple_option_display_on_header(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_selected_options_ord_entry_mtd_on_header(feature_file_name):
            raise Exception(
                "Failed to verify Selected multiple order entry method options should get display in header")
    except Exception as e:
        logger.error("Error while selecting multiple order entry method options should get display in header %s", e)
        raise e


@when(parsers.parse('Select any option from Order Entry Method dropdown list'))
def verify_select_any_option_from_order_entry_method_dropdown_list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        order_entry_method = "G360"
        if not validate_order_exception_data.do_select_order_entry_method(feature_file_name, order_entry_method):
            raise Exception(
                "Failed to Select any option from Order Entry Method dropdown list")
    except Exception as e:
        logger.error("Error while selecting any option from Order Entry Method dropdown list %s", e)
        raise e


@then(parsers.parse(
    'Data in grid should get updated as per selected Order Entry Method filter if no data found for selected value No orders found message should display'))
def data_in_grid_should_get_updated_as_per_order_entry_method_filter(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        order_entry_method = "G360"
        if not validate_order_exception_data.do_verify_update_data_grid_as_per_order_entry_method_filter(
                feature_file_name,
                order_entry_method):
            raise Exception(
                "Failed to verify Data in grid should get updated as per selected Order Entry Method filter if no data found for selected value No orders found message should display")
    except Exception as e:
        logger.error(
            "Error while verifing Data in grid should get updated as per selected Order Entry Method filter if no data found for selected value No orders found message should display %s",
            e)
        raise e


@when(parsers.parse('Select any option from Country dropdown list'))
def verify_select_any_option_from_country_dropdown_list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        country = "United States"
        if not validate_order_exception_data.do_select_country(feature_file_name, country):
            raise Exception(
                "Failed to Select any option from Country dropdown list")
    except Exception as e:
        logger.error("Error while selecting any option from Country dropdown list %s", e)
        raise e


@then(parsers.parse(
    'Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display'))
def data_in_grid_should_get_updated_as_per_filter(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        country = "US"
        if not validate_order_exception_data.do_verify_update_data_grid_as_per_country_filter(feature_file_name,
                                                                                              country):
            raise Exception(
                "Failed to verify Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display")
    except Exception as e:
        logger.error(
            "Error while verifing Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display %s",
            e)
        raise e


@when(parsers.parse('Select any option from Order Entry Method and Country dropdown list'))
def do_select_any_option_from_order_entry_and_country_dropdown_list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        order_entry_method = "ACTO"
        country = "Canada"
        if not validate_order_exception_data.do_select_option_from_ord_entry_method_and_country(feature_file_name,
                                                                                                order_entry_method,
                                                                                                country):
            raise Exception("Failed to Select any option from Order Entry Method and Country dropdown list")
    except Exception as e:
        logger.error("Error while Selecting any option from Order Entry Method and Country dropdown list %s", e)
        raise e


@when(parsers.parse('Click on Clear all button'))
def do_click_clear_all_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_clear_all_button(feature_file_name):
            raise Exception("Failed to click Clear all button")
    except Exception as e:
        logger.error("Error while clicking Clear all button %s", e)
        raise e


@then(parsers.parse('Selected values should get cleared from filter header and all data should get loaded in grid'))
def selected_value_get_cleared_from_filter_header_and_all_data_should_get_loaded_in_grid(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_selected_values_cleared_from_filter_header(feature_file_name):
            raise Exception(
                "Failed to Selected values should get cleared from filter header and all data should get loaded in grid")
    except Exception as e:
        logger.error(
            "Error while Selecting values should get cleared from filter header and all data should get loaded in grid %s",
            e)
        raise e


@given(parsers.parse('The order exception is created via api for VMF Details'))
def create_order_for_vmf_details(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_vmf_details_in_db(db_file_path, feature_file_name,
                                                                                confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for VMF Details'))
def search_select_data_errors_order_record_for_vmf_details(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("modify_vmf_details_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that Edit icon should display beside VMF Details'))
def vmf_details_edit_icon_visible(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.is_vmf_details_edit_icon_visible(feature_file_name):
            raise Exception("Failed to verify that Edit icon display beside VMF Details")
    except Exception as e:
        logger.error("Error while verify that Edit icon display beside VMF Details %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit VMF Details popup'))
def verify_contents_of_edit_vmf_details_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_edit_vmf_details(feature_file_name):
            raise Exception("Failed to verify contents of Edit VMF Details popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit VMF Details popup %s", e)


@when(parsers.parse('Verify that Attribute value should allow special characters'))
def verify_attribute_value_allow_special_charcter(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_attribute_value_allow_special_character(feature_file_name):
            raise Exception("Failed to Verify that Attribute value should allow special characters")
    except Exception as e:
        logger.error("Error while verifying Attribute value should allow special characters %s", e)


@then(parsers.parse(
    'Enter valid data for Attribute value fields save it then Verify Saved data should get display in order details page'))
def verify_saved_data_in_order_details_page(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_validate_vmf_saved_data(feature_file_name):
            raise Exception(
                "Failed to Enter valid data for Attribute value fields save it then Verify Saved data should get display in order details page")
    except Exception as e:
        logger.error(
            "Error while Entering valid data for Attribute value fields save it then Verify Saved data should get display in order details page %s",
            e)


@then(parsers.parse(
    'Verify that VMF entered data should not get saved after click on X icon'))
def verify_entered_data_not_save_after_click_on_close_data(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_validate_vmf_data_not_saved(feature_file_name):
            raise Exception(
                "Failed to Verify that VMF entered data should not get saved after click on X icon")
    except Exception as e:
        logger.error(
            "Error while Verifying VMF entered data should not get saved after click on X icon %s",
            e)


@then(parsers.parse(
    'Verify that modified VMF data should not get updated on order details page after click on Cancel button'))
def verify_modified_vmf_data_not_updated_after_click_on_cancel_data(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_validate_modified_vmf_data_not_updated(feature_file_name):
            raise Exception(
                "Failed to Verify that modified VMF data should not get updated on order details page after click on Cancel button")
    except Exception as e:
        logger.error(
            "Error while Verifying modified VMF data should not get updated on order details page after click on Cancel button %s",
            e)


@given(parsers.parse('The order exception is created via api for End User Details'))
def create_order_for_end_user_details(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_end_user_details_in_db(db_file_path, feature_file_name,
                                                                                     confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for End User Details'))
def search_select_data_errors_order_record_for_end_user_details(init_driver):
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("modify_end_user_details_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that Edit icon should display beside End User Details'))
def end_user_details_edit_icon_visible(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.is_end_user_details_edit_icon_visible(feature_file_name):
            raise Exception("Failed to verify that Edit icon display beside End User Details")
    except Exception as e:
        logger.error("Error while verify that Edit icon display beside End User Details %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit End User Details popup'))
def verify_contents_of_edit_end_user_details_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_edit_end_user_details(feature_file_name):
            raise Exception("Failed to verify contents of Edit End User Details popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit End User Details popup %s", e)


@then(parsers.parse('Verify that all address matching with entered text should get displayed'))
def verify_that_all_address_matching_with_entered_text_displayed(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_all_addr_matching_with_entered_text(feature_file_name):
            raise Exception("Failed to Verify all address matching with entered text should get displayed")
    except Exception as e:
        logger.error("Error while Verifing all address matching with entered text should get displayed %s", e)


@then(parsers.parse(
    'Select the end user with suffix and verify that Edit icon should display for user and Save button should get enabled'))
def select_the_any_end_user_with_suffix_verify_edit_button_display_and_save_button_should_get_enabled(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        end_user_with_suffix = 'EVREST_DS010'
        if not validate_order_exception_data.do_verify_edit_button_and_save_button_enable(feature_file_name,
                                                                                          end_user_with_suffix):
            raise Exception(
                "Failed to Select the end user with suffix and verify that Edit icon should display for user and Save button should get enabled")
    except Exception as e:
        logger.error(
            "Error while Select the end user with suffix and verify that Edit icon should display for user and Save button should get enabled %s",
            e)


@then(parsers.parse(
    'Click on Save Button and Verify that selected end user information should get displayed on order details page'))
def verify_selected_end_user_information_should_get_displayed_on_order_details_page(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_selected_end_user_info_on_order_details_page(feature_file_name):
            raise Exception(
                "Failed to Click on Save Button and Verify that selected end user information should get displayed on order details page")
    except Exception as e:
        logger.error(
            "Error while Click on Save Button and Verify that selected end user information should get displayed on order details page %s",
            e)


@then(parsers.parse('Verify contents of selected end user with suffix edit popup'))
def verify_contents_of_selected_end_user_with_suffix_edit_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_selected_end_user_with_suffix_edit_popup(
                feature_file_name):
            raise Exception("Failed to verify contents of selected end user with suffix edit popup")
    except Exception as e:
        logger.error("Error while verifying contents of selected end user with suffix edit popup %s", e)


@then(parsers.parse(
    'Modify Name, Phone Number, Email and Click on Add button then Verify that updated end user information should display on order details page'))
def modify_name_phone_number_email_verify_that_updated_end_user_information_should_display_on_order_details_page(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        end_user = 'EVREST_DS010'
        if not validate_order_exception_data.do_verify_modified_end_user_info_on_order_details_page(feature_file_name,
                                                                                                    end_user):
            raise Exception(
                "Failed to modify Name, Phone Number, Email and Click on Add button then Verify that updated end user information should display on order details page")
    except Exception as e:
        logger.error(
            "Error while modifying Name Phone Number Email and Click on Add button then Verify that updated end user information should display on order details page %s",
            e)


@when(parsers.parse(
    'Remove the data from Name, Phone Number, Email and Click on Add button then Validation required message should display'))
def remove_the_data_from_name_phone_number_email_and_click_on_add_button_then_validate_required_message_should_display(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_validate_message_for_mandatory_fields(feature_file_name):
            raise Exception(
                "Failed to Remove the data from Name, Phone Number, Email and Click on Add button then Validate required message should display")
    except Exception as e:
        logger.error(
            "Error while Clicking on Add button without giving any values and validating message should display for all mandatory fields %s",
            e)


@then(parsers.parse('Verify contents of Edit Add New End User popup'))
def verify_contents_of_edit_add_new_end_user_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_edit_add_new_end_user(feature_file_name):
            raise Exception("Failed to Verify contents of Edit Add New End User popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit Add New End User popup %s", e)


@then(parsers.parse('Verify that Customer type options list'))
def verify_that_customer_type_option_list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_customer_type_option_list(feature_file_name):
            raise Exception("Failed to Verify that Customer type options list")
    except Exception as e:
        logger.error("Error while verifying Customer type options list %s", e)


@then(parsers.parse(
    'Verify that added new end user should display and user should able to select it and checkbox is disable'))
def verify_that_added_new_user_should_display_and_user_should_able_to_select_it(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_add_new_user_with_valid_data(feature_file_name):
            raise Exception("Failed to Verify that added new user should display and user should able to select it")
    except Exception as e:
        logger.error("Error while verifying that added new user should display and user should able to select it %s", e)


@given(parsers.parse('The order exception is created via api for Billing Address'))
def create_order_for_billing_address_details(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_billing_address_details_in_db(db_file_path,
                                                                                            feature_file_name,
                                                                                            confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for Billing Address'))
def search_select_data_errors_order_record_for_billing_address(init_driver):
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("modify_billing_address_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit Billing Address popup'))
def verify_contents_of_edit_billing_address_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_edit_billing_address(feature_file_name):
            raise Exception("Failed to verify contents of Edit Billing Address popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit Billing Address popup %s", e)


@when(parsers.parse('Click on X icon on popup and Verify that Order Details page should display'))
def click_on_x_icon_on_pop_and_verify_that_order_details_page_should_display(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_details_page_after_click_on_x_icon(feature_file_name):
            raise Exception("Failed to Click on X icon on popup and Verify that Order Details page should display")
    except Exception as e:
        logger.error("Error while Clicking on X icon on popup and Verify that Order Details page should display %s", e)


@when(parsers.parse('Click on Cancel button on popup and Verify that Order Details page should display'))
def click_on_cancel_button_on_pop_and_verify_that_order_details_page_should_display(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_details_page_after_click_on_cancel_button(
                feature_file_name):
            raise Exception(
                "Failed to Click on Cancel button on popup and Verify that Order Details page should display")
    except Exception as e:
        logger.error(
            "Error while Clicking on Cancel button on popup and Verify that Order Details page should display %s", e)


@when(
    parsers.parse('Search with special characters then No records found matching your search criteria should display'))
def search_with_special_characters_then_no_records_found_matching_your_search_criteria_should_display(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_search_with_special_character(feature_file_name):
            raise Exception(
                "Failed to search with special characters then No records found matching your search criteria should display")
    except Exception as e:
        logger.error(
            "Error while Searching with special characters then No records found matching your search criteria should display %s",
            e)


@when(parsers.parse('Search with valid Suffix and then Billing address details should get loaded in popup'))
def search_with_valid_suffix_and_then_billing_address_details_should_get_loaded_in_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_search_with_valid_suffix(feature_file_name):
            raise Exception(
                "Failed to Search with valid Suffix and then Billing address details should get loaded in popup")
    except Exception as e:
        logger.error(
            "Error while Searching with valid Suffix and then Billing address details should get loaded in popup %s",
            e)


@when(parsers.parse('Select the searched address and then Save button should get enabled on selecting address'))
def select_the_searched_address_and_then_save_button_should_get_enabled_on_selecting_address(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_select_searched_addr_and_save_button_enabled(feature_file_name):
            raise Exception(
                "Failed to Select the searched address and then Save button should get enabled on selecting address")
    except Exception as e:
        logger.error(
            "Error while Selecting the searched address and then Save button should get enabled on selecting address %s",
            e)


@then(parsers.parse('Verify that selected billing address should get displayed on Order details page'))
def verify_that_selected_billing_address_should_get_displayed_on_order_details_page(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_selected_billing_addr_on_order_details_page(feature_file_name):
            raise Exception(
                "Failed to Verify that selected billing address should get displayed on Order details page")
    except Exception as e:
        logger.error(
            "Error while Verifying that selected billing address should get displayed on Order details page %s",
            e)


@given(parsers.parse('The order exception is created via api for Order Line'))
def create_order_for_order_line(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_order_line_in_db(db_file_path,
                                                                               feature_file_name,
                                                                               confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for Order Line'))
def search_select_data_errors_order_record_for_order_line(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("order_line_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that remove icon should display for order line'))
def verify_that_remove_icon_should_display_for_order_line(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_line_remove_icon(feature_file_name):
            raise Exception(
                "Failed to Verify that remove icon should display for order line")
    except Exception as e:
        logger.error(
            "Error while Verifying that remove icon should display for order line %s",
            e)


@when(parsers.parse(
    'Click on Mark for Cancel option and Verify line should grey out and should not allow further edit operations'))
def click_on_mark_for_cancel_option_and_verify_line_should_grey_out_and_should_not_allow_further_edit_operations(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_on_mark_for_cancel_and_line_not_editable(feature_file_name):
            raise Exception(
                "Failed to Click on Mark for Cancel option and Verify line should grey out and should not allow further edit operations")
    except Exception as e:
        logger.error(
            "Error while Clicking on Mark for Cancel option and Verify line should grey out and should not allow further edit operations %s",
            e)


@when(parsers.parse(
    'Click on Unmark for Cancel option and Verify line should become enable and it should allow edit operations'))
def click_on_mark_for_cancel_option_and_verify_line_should_grey_out_and_should_not_allow_further_edit_operations(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_on_unmark_for_cancel_and_line_is_editable(feature_file_name):
            raise Exception(
                "Failed to Click on Unmark for Cancel option and Verify line should become enable and it should allow edit operations")
    except Exception as e:
        logger.error(
            "Error while Clicking on Unmark for Cancel option and Verify line should become enable and it should allow edit operations %s",
            e)


@then(parsers.parse('Verify that Order should get resubmitted succesfully after cancel the Order line'))
def verify_that_order_should_get_resubmitted_succesfully_after_cancel_the_order_line(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_resubmitted_successfully(feature_file_name):
            raise Exception(
                "Failed to Verify that Order should get resubmitted succesfully after cancel the Order line")
    except Exception as e:
        logger.error(
            "Error while Verifying that Order should get resubmitted succesfully after cancel the Order line %s",
            e)


@when(parsers.parse(
    'Click on Mark for Cancel option from dropdown and Verify line should grey out'))
def click_on_mark_for_cancel_option_from_dropdown_and_verify_line_should_grey_out(
        init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_on_mark_for_cancel_from_dropdown_and_line_grey_out(
                feature_file_name):
            raise Exception(
                "Failed to Click on Mark for Cancel option from dropdown and Verify line should grey out")
    except Exception as e:
        logger.error(
            "Error while Clicking on Mark for Cancel option from dropdown and Verify line should grey out %s",
            e)


@when(parsers.parse(
    'Click on Unmark for Cancel option from dropdown and Verify line should get enable'))
def click_on_unmark_for_cancel_option_from_dropdown_and_verify_line_should_get_unable(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_on_unmark_for_cancel_from_dropdown_and_line_get_unable(
                feature_file_name):
            raise Exception(
                "Failed to Click on Unmark for Cancel option from dropdown and Verify line should get enable")
    except Exception as e:
        logger.error(
            "Error while Clicking on Unmark for Cancel option from dropdown and Verify line should get enable %s",
            e)


@then(parsers.parse('Verify that At least one order line is required to resubmit the order message'))
def verify_that_at_least_one_order_line_is_required_to_resubmit_the_order_message(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_atleast_one_order_line_required_message(feature_file_name):
            raise Exception(
                "Failed to Verify that At least one order line is required to resubmit the order message")
    except Exception as e:
        logger.error(
            "Error while Verifying At least one order line is required to resubmit the order message %s",
            e)


@then(parsers.parse('Verify that Last order attempt on section should display inside filter panel'))
def verify_that_last_order_attempt_on_section_should_display_inside_filter_panel(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_last_order_attempt_on_section(feature_file_name):
            raise Exception(
                "Failed to Verify that Last order attempt on section should display inside filter panel")
    except Exception as e:
        logger.error(
            "Error while Verifying that Last order attempt on section should display inside filter panel %s",
            e)


@then(parsers.parse('Verify that Created on section should display inside filter panel'))
def verify_that_created_on_section_should_display_inside_filter_panel(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_created_on_section(feature_file_name):
            raise Exception(
                "Failed to Verify that Created on section should display inside filter panel")
    except Exception as e:
        logger.error(
            "Error while Verifying that Created on section should display inside filter panel %s",
            e)


@then(parsers.parse('Verify that contents of Last order attempt on section'))
def verify_that_contents_of_last_order_attempt_on_section(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_last_order_attempt_on_section(feature_file_name):
            raise Exception(
                "Failed to Verify that contents of Last order attempt on section")
    except Exception as e:
        logger.error(
            "Error while Verify that contents of Last order attempt on section %s",
            e)


@then(parsers.parse('Verify that contents of Created On section'))
def verify_that_contents_of_created_on_section(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_created_on_section(feature_file_name):
            raise Exception(
                "Failed to Verify that contents of Created On section")
    except Exception as e:
        logger.error(
            "Error while Verify that contents of Created On section %s",
            e)


@then(
    parsers.parse('Verify that Last order attempt on section Calendar should open and it should allow date selection'))
def verify_that_last_order_attempt_on_section_calendar_should_open_and_it_should_allow_date_selection(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_last_ord_attempt_on_sec_calender_open_and_able_to_select_date(
                feature_file_name):
            raise Exception(
                "Failed to Verify that Last order attempt on section Calendar should open and it should allow date selection")
    except Exception as e:
        logger.error(
            "Error while Verify that Last order attempt on section Calendar should open and it should allow date selection %s",
            e)


@then(
    parsers.parse('Verify that Created On section Calendar should open and it should allow date selection'))
def verify_that_created_on_section_calendar_should_open_and_it_should_allow_date_selection(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_created_on_sec_calender_open_and_able_to_select_date(
                feature_file_name):
            raise Exception(
                "Failed to Verify that Created On section Calendar should open and it should allow date selection")
    except Exception as e:
        logger.error(
            "Error while Verify that Created On section Calendar should open and it should allow date selection %s",
            e)


@then(
    parsers.parse(
        'Select the Last order attempt on section From and To date and Verify that Data should get filtered on selected date ranges'))
def select_the_last_order_attempts_on_from_and_to_date_and_verify_that_data_should_get_filtered_on_selected_date_ranges(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_last_ord_attempt_on_data_get_filter_as_per_selected_date_range(
                feature_file_name):
            raise Exception(
                "Failed to Selecting the Last order attempt on section From and To date and Verifying  Data should get filtered on selected date ranges")
    except Exception as e:
        logger.error(
            "Error while Selecting the Last order attempt on section From and To date and Verifying  Data should get filtered on selected date ranges %s",
            e)


@then(
    parsers.parse(
        'Select the Created On section From and To date and Verify that Data should get filtered on selected date ranges'))
def select_the_created_on_from_and_to_date_and_verify_that_data_should_get_filtered_on_selected_date_ranges(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_created_on_data_get_filter_as_per_selected_date_range(
                feature_file_name):
            raise Exception(
                "Failed to Selecting the Created on section From and To date and Verifying  Data should get filtered on selected date ranges")
    except Exception as e:
        logger.error(
            "Error while Selecting the Created on section From and To date and Verifying  Data should get filtered on selected date ranges %s",
            e)


@then(
    parsers.parse(
        'Select last 30 days checkbox from Last order attempt on section and Verify that data should get filtered on selected date ranges'))
def select_last_30_days_checkbox_from_last_order_attempts_on_section_and_verify_that_data_should_get_filtered_on_selected_date_ranges(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.verify_filter_by_last_ord_attempt_on_data_by_selecting_30_days_in_pages(
                feature_file_name):
            raise Exception(
                "Failed to Selecting last 30 days checkbox from Last order attempt on section and Verifying  Data should get filtered on selected date ranges")
    except Exception as e:
        logger.error(
            "Error while Selecting last 30 days checkbox from Last order attempt on section and Verifying  Data should get filtered on selected date ranges %s",
            e)


@then(
    parsers.parse(
        'Select last 30 days checkbox from Created on section and Verify that data should get filtered on selected date ranges'))
def select_last_30_days_checkbox_from_created_on_section_and_verify_that_data_should_get_filtered_on_selected_date_ranges(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.verify_filter_by_created_on_data_by_selecting_30_days_in_pages(
                feature_file_name):
            raise Exception(
                "Failed to Selecting last 30 days checkbox from Created on section and Verifying  Data should get filtered on selected date ranges")
    except Exception as e:
        logger.error(
            "Error while Selecting last 30 days checkbox from Created on section and Verifying  Data should get filtered on selected date ranges %s",
            e)


@given(parsers.parse('The order exception is created via api for modify Order Line'))
def create_order_for_modify_order_line(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_modify_order_line_in_db(db_file_path,
                                                                                      feature_file_name,
                                                                                      confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for modify Order Line'))
def search_select_data_errors_order_record_for_modify_order_line(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("modify_order_line_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify that Edit Icon should display for each lines'))
def verify_that_edit_icon_should_display_for_order_line(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_line_edit_icon(feature_file_name):
            raise Exception(
                "Failed to Verify that Edit Icon should display for each lines")
    except Exception as e:
        logger.error(
            "Error while Verifying that Edit Icon should display for each lines %s",
            e)


@when(parsers.parse('Click on edit icon and Verify that Update and Cancel Icon should display'))
def click_on_edit_icon_and_verify_that_update_and_cancel_icon_should_display(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_update_and_cancel_icon(feature_file_name):
            raise Exception(
                "Failed to Click on edit icon and Verify that Update and Cancel Icon should display")
    except Exception as e:
        logger.error(
            "Error while Clicking on edit icon and Verifying that Update and Cancel Icon should display %s",
            e)


@then(parsers.parse('Verify that Quantity, Reseller price, End user price and End user po# fields become editable'))
def verify_that_quantity_reseller_price_end_user_price_and_end_user_po_fields_become_editable(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_editable_order_line_fields(feature_file_name):
            raise Exception(
                "Failed to Verify that Quantity, Reseller price, End user price and End user po# fields become editable")
    except Exception as e:
        logger.error(
            "Error while Verifying Quantity, Reseller price, End user price and End user po# fields become editable %s",
            e)


@when(parsers.parse('Click on X icon and Verify that updated data should get discarded'))
def click_on_x_icon_and_verify_that_updated_data_should_get_discarded(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_line_updated_data_discarded(feature_file_name):
            raise Exception(
                "Failed to Click on X icon and Verify that Updated data should get discarded")
    except Exception as e:
        logger.error(
            "Error while Clicking on X icon and Verify that Updated data should get discarded %s",
            e)


@then(parsers.parse(
    'Verify that Quantity, Reseller price, End user price and End user po# fields not allow non numeric content'))
def verify_that_quantity_reseller_price_end_user_price_and_end_user_po_fields_not_allow_non_numeric_content(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_line_fields_not_allow_non_numberic_content(
                feature_file_name):
            raise Exception(
                "Failed to Verify that Quantity, Reseller price, End user price and End user po# fields not allow non numeric content")
    except Exception as e:
        logger.error(
            "Error while Verifying  Quantity, Reseller price, End user price and End user po# fields not allow non numeric content %s",
            e)


@when(parsers.parse('Update the Order line Quantity, Reseller price and End User PO value'))
def update_the_order_line_quantity_reseller_price_and_end_user_po_value(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_update_order_line_field_value(feature_file_name):
            raise Exception(
                "Failed to Update the Order line Quantity, Reseller price and End User PO value")
    except Exception as e:
        logger.error(
            "Error while Updating the Order line Quantity, Reseller price and End User PO value %s",
            e)


@then(parsers.parse('Verify that Operator ID should be display on the Order details page'))
def verify_that_operator_id_should_be_display_on_the_order_details_page(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_operator_id(feature_file_name):
            raise Exception(
                "Failed to Verify that Operator ID should be display on the Order details page")
    except Exception as e:
        logger.error(
            "Error while Verifying that Operator ID should be display on the Order details page %s",
            e)


@then(parsers.parse('Verify that Channel label should get displayed on Order details page'))
def verify_that_channel_label_should_be_display_on_the_order_details_page(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_operator_id(feature_file_name):
            raise Exception(
                "Failed to Verify that Operator ID should be display on the Order details page")
    except Exception as e:
        logger.error(
            "Error while Verifying that Operator ID should be display on the Order details page %s",
            e)


@given(parsers.parse('The order exception is created via api using IM360 payload'))
def create_order_using_im360_payload(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_im360_order_exception_create()
        logger.info(f'IM360 Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_im360_confirmation_id_in_db(db_file_path, feature_file_name, confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@then(parsers.parse('Verify that Order channel should match with the channel showing on list page'))
def Verify_that_order_channel_should_match_with_the_channel_showing_on_list_page(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("im360_data_errors_order_confirmation_id")
        if not validate_order_exception_data.do_verify_order_channel_matched(feature_file_name, confirmation_id):
            raise Exception(
                "Failed to Verify that Order channel should match with the channel showing on list page")
    except Exception as e:
        logger.error(
            "Error while Verify that Order channel should match with the channel showing on list page %s",
            e)


@given(parsers.parse('Create order exception Using X4D payload without {shipingdetails} via api'))
def create_order_using_x4d_payload(init_driver, shipingdetails):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_x4d_order_exception_create(shipingdetails)
        logger.info(f'X4D Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_x4d_confirmation_id_in_db(db_file_path, feature_file_name, confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Order Exception order %s", e)
        raise e


@then(parsers.parse('Verify that Shipping Details option section should display'))
def Verify_that_shipping_details_optional_section_should_display(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("x4d_data_errors_order_confirmation_id")
        if not validate_order_exception_data.do_verify_shipping_details(feature_file_name, confirmation_id):
            raise Exception(
                "Failed to Verify that Shipping Details should display")
    except Exception as e:
        logger.error(
            "Error while Verify that Shipping Details should display %s",
            e)


@given(parsers.parse('The order exception is created via api for Shipping Address'))
def create_order_for_shipping_address_details(init_driver):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_order_exception_create()
        logger.info(f'Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_confirmation_id_for_shipping_address_details_in_db(db_file_path,
                                                                                             feature_file_name,
                                                                                             confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Data error order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for Shipping Address'))
def search_select_data_errors_order_record_for_shipping_address(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("modify_shipping_address_data_errors_order_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit Shipping Address popup'))
def verify_contents_of_edit_shipping_address_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_edit_shipping_address(feature_file_name):
            raise Exception("Failed to verify contents of Edit Shipping Address popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit Shipping Address popup %s", e)


@when(parsers.parse('Click on X icon on shipping address popup and Verify that Order Details page should display'))
def click_on_x_icon_on_shipping_address_popup_and_verify_that_order_details_page_should_display(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_details_page_after_click_on_x_icon_shipping_addr_popup(
                feature_file_name):
            raise Exception(
                "Failed to Click on X icon on shipping address popup and Verify that Order Details page should display")
    except Exception as e:
        logger.error(
            "Error while Clicking on X icon on shipping address popup and Verify that Order Details page should display %s",
            e)


@when(
    parsers.parse('Click on Cancel button on shipping address popup and Verify that Order Details page should display'))
def click_on_cancel_button_on_shipping_address_popup_and_verify_that_order_details_page_should_display(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_order_details_page_after_click_on_cancel_button_shipping_addr_popup(
                feature_file_name):
            raise Exception(
                "Failed to Click on Cancel button on shipping address popup and Verify that Order Details page should display")
    except Exception as e:
        logger.error(
            "Error while Clicking on Cancel button on shipping address popup and Verify that Order Details page should display %s",
            e)


@when(parsers.parse('Verify that all shipping address matching with search entered text should get displayed'))
def verify_that_all_shipping_address_matching_with_search_entered_text_should_get_displayed(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_all_shipping_addr_matching_with_entered_text(
                feature_file_name):
            raise Exception(
                "Failed to Verify that all shipping address matching with search entered text should get displayed")
    except Exception as e:
        logger.error(
            "Error while Verifying that all shipping address matching with search entered text should get displayed %s",
            e)


@then(parsers.parse('Verify that Add New Shipping Address pop up contents'))
def verify_contents_of_add_new_shipping_address_popup(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_contents_of_add_new_shipping_address_popup(feature_file_name):
            raise Exception("Failed to Verify that Add New Shipping Address pop up contents")
    except Exception as e:
        logger.error("Error while verifying contents of  Add New Shipping Address pop up %s", e)


@then(parsers.parse('Add the new shipping address and verify that Added data should display'))
def add_the_new_shipping_address_and_verify_that_added_data_should_display(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_added_new_shipping_addr_data(feature_file_name):
            raise Exception("Failed to Add the new shipping address and verify that Added data should display")
    except Exception as e:
        logger.error("Error while Adding the new shipping address and verify that Added data should display %s", e)


@when(parsers.parse(
    'Click on X icon on Add new shipping address popup and Verify that entered data should not get saved'))
def click_on_x_icon_on_add_new_shipping_address_popup_and_verify_that_entered_data_should_not_get_saved(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_data_not_save_after_click_on_x_icon_on_popup(
                feature_file_name):
            raise Exception(
                "Failed to Click on X icon on Add new shipping address popup and Verify that entered data should not get saved")
    except Exception as e:
        logger.error(
            "Error while Clicking on X icon on Add new shipping address popup and Verify that entered data should not get saved %s",
            e)


@when(
    parsers.parse(
        'Click on Cancel button on Add new shipping address popup and Verify that entered data should not get saved'))
def click_on_cancel_icon_on_add_new_shipping_address_popup_and_verify_that_entered_data_should_not_get_saved(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_verify_data_not_save_after_click_on_cancel_icon_on_popup(
                feature_file_name):
            raise Exception(
                "Failed to Click on Cancel button on Add new shipping address popup and Verify that entered data should not get saved")
    except Exception as e:
        logger.error(
            "Error while Clicking on Cancel button on Add new shipping address popup and Verify that entered data should not get saved %s",
            e)


@given(parsers.parse('Create Data Error Order for duplicate {po_number} PO via api for {country} markeplace'))
def create_data_error_order_for_duplicate_po_via_api(init_driver, po_number, country):
    feature_file_name = "order_exception_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_x4c_order_exception_create(po_number, country)
        logger.info(f'X4C Confirmation ID: {confirmation_id}')
        if not len(confirmation_id) == 0:
            order_management_srv_obj.save_x4c_confirmation_id_in_db(db_file_path, feature_file_name, confirmation_id)
        else:
            raise Exception('Confirmation Id is empty')
    except Exception as e:
        logger.error("Not able create the Order Exception order %s", e)
        raise e


@when(parsers.parse('Search and Select the Data Errors Order for Duplicate PO'))
def search_select_data_errors_order_record_for_duplicate_po(init_driver):
    init_driver.refresh()
    feature_file_name = "order_exception_orders"
    create_order_steps = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("x4c_duplicate_po_data_errors_order_confirmation_id")
        if not create_order_steps.search_and_select_data_errors_order(feature_file_name, confirmation_id):
            raise Exception("Failed to select Data error order")
    except Exception as e:
        logger.error("Error while selecting Data error order first record %s", e)
        raise e


@when(parsers.parse('Correct the PO# and resubmit the order'))
def correct_the_po_and_resubmit_the_order(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_correct_PO_and_resubmit_order(feature_file_name):
            raise Exception(
                "Failed to correcting the PO# and resubmiting the order")
    except Exception as e:
        logger.error(
            "Error while correcting the PO# and resubmiting the order %s",
            e)


@then(parsers.parse('Verify that Data Error should get removed form data error list'))
def verify_data_error_order_get_remove_from__list(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("x4c_duplicate_po_data_errors_order_confirmation_id")
        if not validate_order_exception_data.do_verify_data_error_order_in_list(feature_file_name, confirmation_id):
            raise Exception("failed to Verify that Data Error resubmitted Order should not be there in list")
    except Exception as e:
        logger.error("Error while Verifying that Data Error resubmitted Order should not be there in list %s", e)
        raise e


@when(
    parsers.parse('Correct the PO# and Add new line then Verify Resubmit Order message and Cancel and Proceed button'))
def correct_the_po_and_add_new_line_verify_resubmit_order_message_and_cancel_and_proceed_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_correct_PO_add_new_line_and_resubmit_order_cancel_proceed_button(
                feature_file_name):
            raise Exception(
                "Failed to correcting the PO# and Add new line then Verify Resubmit Order message and Cancel and Proceed button")
    except Exception as e:
        logger.error(
            "Error while correcting the PO# and Add new line then Verify Resubmit Order message and Cancel and Proceed button %s",
            e)


@when(parsers.parse('Click on Cancel Order button then popup should open to enter reject reason'))
def click_on_cancel_order_button_then_popup_should_open_to_enter_reject_reason(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_cancel_button_and_verify_reject_reason_open(feature_file_name):
            raise Exception(
                "Failed to Clicking on Cancel Order button then popup should open to enter reject reason")
    except Exception as e:
        logger.error(
            "Error while Clicking on Cancel Order button then popup should open to enter reject reason %s",
            e)


@when(parsers.parse('Click on Proceed button and resubmit the order'))
def click_on_proceed_button_and_resubmit_the_order(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_click_proceed_button_and_resubmit_the_order(feature_file_name):
            raise Exception(
                "Failed to Clicking on Proceed button and resubmitting the order")
    except Exception as e:
        logger.error(
            "Error while Clicking on Proceed button and resubmitting the order %s",
            e)


@when(parsers.parse('Correct the PO# and resubmit the order'))
def correct_the_po_and_resubmit_the_order(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_correct_PO_and_resubmit_order(feature_file_name):
            raise Exception(
                "Failed to correcting the PO# and resubmiting the order")
    except Exception as e:
        logger.error(
            "Error while correcting the PO# and resubmiting the order %s",
            e)


@when(
    parsers.parse('Correct the End Customer order# then Verify Resubmit Order message and Cancel and Proceed button'))
def correct_the_po_and_add_new_line_verify_resubmit_order_message_and_cancel_and_proceed_button(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.do_correct_end_customer_po_and_resubmit_order_cancel_proceed_button(
                feature_file_name):
            raise Exception(
                "Failed to correcting the End Customer order# then Verify Resubmit Order message and Cancel and Proceed button")
    except Exception as e:
        logger.error(
            "Error while correcting the End Customer order# then Verify Resubmit Order message and Cancel and Proceed button %s",
            e)


@when(parsers.parse(
    'Search with confirmation id and Verify that data should get displayed in the list as per searched Confirmation ID'))
def search_with_confirmation_id_and_verify_that_data_should_get_displayed_in_the_list_as_per_searched_confirmation_id(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        confirmation_id = input_order_data.get("data_errors_resubmit_order_confirmation_id")
        if not validate_order_exception_data.search_with_confirmation_id_verify_search_result(
                feature_file_name, confirmation_id):
            raise Exception(
                "Failed to Search with confirmation id and Verify that data should get displayed in the list as per searched Confirmation ID")
    except Exception as e:
        logger.error(
            "Error while searching with confirmation id and Verify that data should get displayed in the list as per searched Confirmation ID %s",
            e)
        raise e


@when(parsers.parse(
    'Search with Reject reason and Verify that data should get displayed in the list as per searched Reject reason'))
def search_with_reject_reason_and_verify_that_data_should_get_displayed_in_the_list_as_per_searched_reject_reason(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        reject_reason = "There is an invalid Character in the field"
        if not validate_order_exception_data.search_with_reject_reason_verify_search_result(
                feature_file_name, reject_reason):
            raise Exception(
                "Failed to Search with Reject reason and Verify that data should get displayed in the list as per searched Reject reason")
    except Exception as e:
        logger.error(
            "Error while searching with Reject reason and Verify that data should get displayed in the list as per searched Reject reason %s",
            e)
        raise e


@when(parsers.parse(
    'Search with Customer name and Verify that data should get displayed in the list as per searched Customer name'))
def search_with_customer_name_and_verify_that_data_should_get_displayed_in_the_list_as_per_searched_customer_name(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        customer_name = "INGRAM MICRO CAP TEST ACCOUNT"
        if not validate_order_exception_data.search_with_customer_name_verify_search_result(
                feature_file_name, customer_name):
            raise Exception(
                "Failed to Search with Customer name and Verify that data should get displayed in the list as per searched Customer name")
    except Exception as e:
        logger.error(
            "Error while searching with Customer name and Verify that data should get displayed in the list as per searched Customer name %s",
            e)
        raise e


@when(
    parsers.parse('Search with some invalid text and Verify that No failed orders found message should get displayed'))
def search_with_some_invalid_text_and_verify_that_no_failed_orders_found_message_should_get_displayed(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.search_with_invalid_text_verify_no_failed_order_found_message(
                feature_file_name):
            raise Exception(
                "Failed to search with some invalid text and Verify that No failed orders found message should get displayed")
    except Exception as e:
        logger.error(
            "Error while searching with some invalid text and Verify that No failed orders found message should get displayed %s",
            e)
        raise e


@when(parsers.parse(
    'Search with 2 characters and Verify that Minimum 3 charcters are required message should get displayed'))
def search_with_2_character_and_verify_that_minimum_3_chacters_are_required_message_should_get_displayed(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        if not validate_order_exception_data.search_with_two_char_verify_message(
                feature_file_name):
            raise Exception(
                "Failed to Search with 2 characters and Verify that Minimum 3 charcters are required message should get displayed")
    except Exception as e:
        logger.error(
            "Error while Search with 2 characters and Verify that Minimum 3 charcters are required message should get displayed %s",
            e)
        raise e


@when(parsers.parse(
    'Search with BCN and Verify that data should get displayed in the list as per searched BCN'))
def search_with_bcn_and_verify_that_data_should_get_displayed_in_the_list_as_per_searched_bcn(init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        bcn = "20222222"
        if not validate_order_exception_data.do_validate_reseller_bcn(bcn, feature_file_name, screen_shot):
            raise Exception(
                "Failed to Search with BCN and Verify that data should get displayed in the list as per searched BCN")
    except Exception as e:
        logger.error(
            "Error while Search with BCN and Verify that data should get displayed in the list as per searched BCN %s",
            e)
        raise e


@when(parsers.parse(
    'Searched with Reseller PO and Verify that data should get displayed in the list as per Reseller PO'))
def search_with_reseller_po_and_verify_that_data_should_get_displayed_in_the_list_as_per_searched_reseller_po(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        reseller_po = "TESTPO^"
        if not validate_order_exception_data.search_with_reseller_po_verify_result(reseller_po, feature_file_name,
                                                                                   screen_shot):
            raise Exception(
                "Failed to Search with BCN and Verify that data should get displayed in the list as per searched BCN")
    except Exception as e:
        logger.error(
            "Error while Search with BCN and Verify that data should get displayed in the list as per searched BCN %s",
            e)
        raise e


@when(parsers.parse(
    'Searched with substring of reseller po and Verify that data should get displayed in the list as per Reseller PO'))
def search_with_reseller_po_and_verify_that_data_should_get_displayed_in_the_list_as_per_searched_reseller_po(
        init_driver):
    feature_file_name = "order_exception_orders"
    validate_order_exception_data = ValidateOrderExceptionData(init_driver)
    try:
        substring_of_reseller_po = "TEST"
        if not validate_order_exception_data.search_with_substring_of_reseller_po_verify_result(
                substring_of_reseller_po, feature_file_name, screen_shot):
            raise Exception(
                "Failed to Searched with substring of reseller po and Verify that data should get displayed in the list as per Reseller PO")
    except Exception as e:
        logger.error(
            "Error while Searched with substring of reseller po and Verify that data should get displayed in the list as per Reseller PO %s",
            e)
        raise e
