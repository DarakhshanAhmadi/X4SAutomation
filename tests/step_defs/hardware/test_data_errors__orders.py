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


@scenario("features/hardware/data_errors_orders.feature", "Verify Reference Details Edit popup content")
def test_verify_reference_details_edit_popup_contents():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Verify the PO number and End customer order invalid message")
def test_verify_po_and_end_customer_order_number_invalid_message():
    pass


@scenario("features/hardware/data_errors_orders.feature",
          "Verify the PO number and End customer order for the max length")
def test_verify_po_and_end_customer_max_length():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Verify resubmitted successful message")
def test_verify_resubmitted_successful_message():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Verify Shipping Notes Edit popup content")
def test_verify_shipping_notes_edit_popup_contents():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Updated data should get displayed under shipping notes")
def test_updated_data_display_under_shipping_notes():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Verify filter panel options")
def test_filter_panel_options():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Verify Order entry method and Country options list")
def test_order_entry_method_country_options_list():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Selected values get cleared from filter header")
def test_selected_values_get_cleared_from_filter_header():
    pass


@scenario("features/hardware/data_errors_orders.feature",
          "Verify Data in grid should get updated as per selected filter")
def test_data_in_grid_shoul_get_updated_as_per_selected_filter():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Verify VMF Details Edit popup content")
def test_vmf_details_edit_popup_content():
    pass


@scenario("features/hardware/data_errors_orders.feature", "Updated VMF data should get display on Order Details page")
def test_updated_vmf_data_should_get_display_on_order_details_page():
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


@given(parsers.parse('the error order is created via api for Reference Details'))
def create_order_for_reference_details(init_driver):
    feature_file_name = "data_errors_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_error_order_create()
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
    feature_file_name = "data_errors_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    breakpoint()
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
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.is_reference_details_edit_icon_visible(feature_file_name):
            raise Exception("Failed to verify that Edit icon display beside Reference Details title")
    except Exception as e:
        logger.error("Error while verify that Edit icon display beside Reference Details title %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit Reference Details popup'))
def verify_contents_of_edit_reference_details_popup(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_contents_of_edit_reference_details(feature_file_name):
            raise Exception("Failed to verify contents of Edit Reference Details popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit Reference Details popup %s", e)


@then(parsers.parse('Verify PO textbox should not allow entering more than 18 characters'))
def verify_po_textbox_should_not_allow_more_that_18_characters(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_more_than_eighteen_char_in_po_field(feature_file_name):
            raise Exception("Failed to Verify PO # textbox should not allow entering more than 18 characters")
    except Exception as e:
        logger.error("Error while Verify PO # textbox should not allow entering more than 18 characters %s", e)


@then(parsers.parse('Verify that PO number is invalid once add this ^ special character'))
def verify_po_textbox_should_not_allow_more_caret_special_char(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_po_number_invalid_message(feature_file_name):
            raise Exception("Failed to PO number is invalid once add this ^ special character")
    except Exception as e:
        logger.error("Error while Verify PO number is invalid once add this ^ special character %s", e)


@then(parsers.parse('Verify End customer order textbox should not allow entering more than 18 characters'))
def verify_end_customer_order_textbox_should_not_allow_more_that_18_characters(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_more_than_eighteen_char_in_end_customer_order_field(
                feature_file_name):
            raise Exception(
                "Failed to Verify End customer order # textbox should not allow entering more than 18 characters")
    except Exception as e:
        logger.error(
            "Error while Verify End customer order # textbox should not allow entering more than 18 characters %s", e)


@then(parsers.parse('Verify that End customer order number is invalid once add this ^ special character'))
def verify_end_customer_order_textbox_should_not_allow_caret_special_char(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_end_customer_order_number_invalid_message(feature_file_name):
            raise Exception("Failed to End customer order number is invalid once add this ^ special character")
    except Exception as e:
        logger.error("Error while Verify End customer order number is invalid once add this ^ special character %s", e)


@when(parsers.parse('Click on X icon then verify that modified data should not get updated on order details page'))
def verify_modified_data_not_update_after_click_on_x_button(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_modified_data_after_click_on_x_icon(feature_file_name):
            raise Exception(
                "Failed to Click on X icon then verify that modified data should not get updated on order details page")
    except Exception as e:
        logger.error(
            "Error while Click on X icon then verify that modified data should not get updated on order details page %s",
            e)


@when(
    parsers.parse('Click on Cancel button then verify that modified data should not get updated on order details page'))
def verify_modified_data_not_update_after_click_on_cancel_button(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_modified_data_after_click_on_cancel_button(feature_file_name):
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
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_updated_po_and_end_customer_order_data(feature_file_name):
            raise Exception(
                "Failed to Update PO and End customer order number with valid data then validate updated data on order details page")
    except Exception as e:
        logger.error(
            "Error while updating PO and End customer order number with valid data then validate updated data on order details page %s",
            e)


@given(parsers.parse('the error order is created via api for Shipping notes'))
def create_order_for_ship(init_driver):
    feature_file_name = "data_errors_orders"
    data_create_obj = DataCreationViaApi(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        confirmation_id = data_create_obj.post_request_for_error_order_create()
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
    feature_file_name = "data_errors_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    breakpoint()
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
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.is_shipping_notes_edit_icon_visible(feature_file_name):
            raise Exception("Failed to verify that Edit icon display beside Shipping Notes")
    except Exception as e:
        logger.error("Error while verify that Edit icon display beside Shipping Notes %s", e)
        raise e


@then(parsers.parse('Verify contents of Edit Shipping Notes popup'))
def verify_contents_of_edit_shipping_notes_popup(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_contents_of_edit_shipping_notes(feature_file_name):
            raise Exception("Failed to verify contents of Edit Shipping Notes popup")
    except Exception as e:
        logger.error("Error while verifying contents of Edit Shipping Notes popup %s", e)


@when(parsers.parse('Click on X icon on popup'))
def click_on_x_icon(init_driver):
    feature_file_name = "data_errors_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.click_on_x_icon(feature_file_name):
            raise Exception("Failed to click on X icon on popup")
    except Exception as e:
        logger.error("Error while clicking on X icon on popup %s", e)
        raise e


@when(parsers.parse('Click on Cancel button on popup'))
def click_on_cancel_button(init_driver):
    feature_file_name = "data_errors_orders"
    create_order_steps = ValidateErrorOrdersData(init_driver)
    try:
        if not create_order_steps.click_on_cancel_button(feature_file_name):
            raise Exception("Failed to click on Cancel button on popup")
    except Exception as e:
        logger.error("Error while clicking on Cancel button on popup %s", e)
        raise e


@when(parsers.parse('Add the more 100 characters then validate message for maximum limit'))
def validate_maximum_limit_message(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_validate_maximum_limit_message(feature_file_name):
            raise Exception("Failed to Add the more 100 characters and validate message for maximum limit")
    except Exception as e:
        logger.error("Error while adding the more 100 characters and validate message for maximum limit %s", e)


@then(parsers.parse(
    'Update shipping notes with special characters and validate updated data should get display under shipping notes'))
def validate_maximum_limit_message(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_validate_updated_shipping_notes_data(feature_file_name):
            raise Exception(
                "Failed to Update shipping notes with special characters and validate updated data should get display under shipping notes")
    except Exception as e:
        logger.error(
            "Error while updateing shipping notes with special characters and validate updated data should get display under shipping notes %s",
            e)


@when(parsers.parse('Click on Filter icon'))
def click_on_filter_icon(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_filter_icon(feature_file_name):
            raise Exception("Failed to click Filter Icon")
    except Exception as e:
        logger.error("Error while clicking Filter icon %s", e)
        raise e


@then(parsers.parse('Verify filter panel options'))
def verify_filter_panel_options(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_filter_options(feature_file_name):
            raise Exception("Failed to verify filter options")
    except Exception as e:
        logger.error("Error while verifing filter options %s", e)
        raise e


@when(parsers.parse('Verify Order entry method options list'))
def verify_order_entry_method_options_list(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_order_entry_method_options_list(feature_file_name):
            raise Exception("Failed to verify Order entry method options list")
    except Exception as e:
        logger.error("Error while verifing Order entry method options list %s", e)
        raise e


@then(parsers.parse('Verify Country options list'))
def verify_country_options_list(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_country_options_list(feature_file_name):
            raise Exception("Failed to verify Country options list")
    except Exception as e:
        logger.error("Error while verifing Country options list %s", e)
        raise e


@then(parsers.parse('After selected any option clear all button should display'))
def verify_clear_all_button(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_clear_all_button(feature_file_name):
            raise Exception("Failed to verify after selected any option clear all button should display")
    except Exception as e:
        logger.error("Error while after selecting any option clear all button should display %s", e)
        raise e


@then(parsers.parse('Selected multiple order entry method options should get display in header'))
def verify_selected_multiple_option_display_on_header(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_selected_options_ord_entry_mtd_on_header(feature_file_name):
            raise Exception(
                "Failed to verify Selected multiple order entry method options should get display in header")
    except Exception as e:
        logger.error("Error while selecting multiple order entry method options should get display in header %s", e)
        raise e


@when(parsers.parse('Select any option from Order Entry Method dropdown list'))
def verify_select_any_option_from_order_entry_method_dropdown_list(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        order_entry_method = "G360"
        if not validate_error_orders_data.do_select_order_entry_method(feature_file_name, order_entry_method):
            raise Exception(
                "Failed to Select any option from Order Entry Method dropdown list")
    except Exception as e:
        logger.error("Error while selecting any option from Order Entry Method dropdown list %s", e)
        raise e


@then(parsers.parse(
    'Data in grid should get updated as per selected Order Entry Method filter if no data found for selected value No orders found message should display'))
def data_in_grid_should_get_updated_as_per_order_entry_method_filter(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        order_entry_method = "G360"
        if not validate_error_orders_data.do_verify_update_data_grid_as_per_order_entry_method_filter(feature_file_name,
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
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        country = "United States"
        if not validate_error_orders_data.do_select_country(feature_file_name, country):
            raise Exception(
                "Failed to Select any option from Country dropdown list")
    except Exception as e:
        logger.error("Error while selecting any option from Country dropdown list %s", e)
        raise e


@then(parsers.parse(
    'Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display'))
def data_in_grid_should_get_updated_as_per_filter(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        country = "US"
        if not validate_error_orders_data.do_verify_update_data_grid_as_per_country_filter(feature_file_name, country):
            raise Exception(
                "Failed to verify Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display")
    except Exception as e:
        logger.error(
            "Error while verifing Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display %s",
            e)
        raise e


@when(parsers.parse('Select any option from Order Entry Method and Country dropdown list'))
def do_select_any_option_from_order_entry_and_country_dropdown_list(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        order_entry_method = "ACTO"
        country = "Canada"
        if not validate_error_orders_data.do_select_option_from_ord_entry_method_and_country(feature_file_name,
                                                                                             order_entry_method,
                                                                                             country):
            raise Exception("Failed to Select any option from Order Entry Method and Country dropdown list")
    except Exception as e:
        logger.error("Error while Selecting any option from Order Entry Method and Country dropdown list %s", e)
        raise e


@when(parsers.parse('Click on Clear all button'))
def do_click_clear_all_button(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_click_clear_all_button(feature_file_name):
            raise Exception("Failed to click Clear all button")
    except Exception as e:
        logger.error("Error while clicking Clear all button %s", e)
        raise e


@then(parsers.parse('Selected values should get cleared from filter header and all data should get loaded in grid'))
def selected_value_get_cleared_from_filter_header_and_all_data_should_get_loaded_in_grid(init_driver):
    feature_file_name = "data_errors_orders"
    validate_error_orders_data = ValidateErrorOrdersData(init_driver)
    try:
        if not validate_error_orders_data.do_verify_selected_values_cleared_from_filter_header(feature_file_name):
            raise Exception(
                "Failed to Selected values should get cleared from filter header and all data should get loaded in grid")
    except Exception as e:
        logger.error(
            "Error while Selecting values should get cleared from filter header and all data should get loaded in grid %s",
            e)
        raise e

