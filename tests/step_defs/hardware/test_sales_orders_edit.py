from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateSalesOrdersData import ValidateSalesOrdersData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
order_management_srv_obj = X4AInputOrderDbManagementService()


@scenario("features/hardware/sales_orders_edit.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/sales_orders_edit.feature", "Validate Updated Order Details")
def test_validate_updated_order_details():
    pass


@scenario("features/hardware/sales_orders_edit.feature", "Validate unmark cancel order line")
def test_unmark_order_lines():
    pass


@scenario("features/hardware/sales_orders_edit.feature", "Verify customer hold cancel order")
def test_cancel_order():
    pass


@scenario("features/hardware/sales_orders_edit.feature", "Validate Mark a single line item for cancel")
def test_mark_for_cancel_single_line_item():
    pass


@scenario("features/hardware/sales_orders_edit.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "sales_orders_edit"
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = validate_sales_orers.filtered_orders_by_feature_file(test_data_order, feature_file_name)
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
    feature_file_name = "sales_orders_edit"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        validate_sales_orers.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@then(parsers.parse('the user traverse to Sales Order menu'))
def click_on_sales_orders_menu(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_sales_orders(feature_file_name, screen_shot):
            raise Exception("Failed to click on Sales Orders menu")
    except Exception as e:
        logger.error("Error while clicking on Sales Orders menu %s", e)
        raise e


@when(parsers.parse('search a order with specific IM Order number {order_no}'))
def search_im_order_number(init_driver, order_no):
    init_driver.refresh()
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        im_order_number = order_no
        if not validate_sales_orders.do_search_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to search IM Order Number")
    except Exception as e:
        logger.error("Error while searching IM Order Number %s", e)
        raise e


@then(parsers.parse('Validate the IM Order number {order_no} is listed'))
def validate_im_order_number(init_driver, order_no):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        im_order_number = order_no
        if not validate_sales_orders.do_validate_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to Validate IM Order Number")
    except Exception as e:
        logger.error("Not able to Validate IM Order Number %s", e)
        raise e


@when(parsers.parse('Click on searched IM order number'))
def click_on_im_order_number(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        logger.info("click")
        if not validate_sales_orers.click_on_im_order_num(feature_file_name):
            raise Exception("Failed to click on searched IM order number")
    except Exception as e:
        logger.error("Error while click on searched IM order number %s", e)
        raise e


@when(parsers.parse('Click on Billing tab on Order Details page'))
def click_on_billing_tab(init_driver):
    #init_driver.refresh()
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_billing_tab(feature_file_name):
            raise Exception("Failed to click on Billing tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Billing tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order Details tab on Order Details page'))
def click_on_order_detail_tab(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders_edit"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_order_details_tab(feature_file_name):
            raise Exception("Failed to click on Order Details tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Details tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order lines tab on Order Details page'))
def click_on_order_lines_tab(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_order_lines_tab(feature_file_name):
            raise Exception("Failed to click on Order Lines tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Lines tab on Order Details page %s", e)
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        validate_sales_orers.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e


@then(parsers.parse('Update end user po and reseller po'))
def update_end_user_po_and_reseller_po(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_po = input_order_data.get("end_user_po")
        reseller_po = input_order_data.get("reseller_po")
        if not validate_sales_orders.update_end_user_po_and_reseller_po(end_user_po, reseller_po, feature_file_name,
                                                                        screen_shot):
            raise Exception("Failed to update for end user po and reseller po")
    except Exception as e:
        logger.error("Not able to update for end user po and reseller po %s", e)
        raise e


@then(parsers.parse('Validate end user po and reseller po updated'))
def validate_end_user_po_and_reseller_po_updated(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_po = input_order_data.get("end_user_po")
        reseller_po = input_order_data.get("reseller_po")
        if not validate_sales_orders.verify_end_user_po_and_reseller_po_updated(end_user_po, reseller_po,
                                                                                feature_file_name, screen_shot):
            raise Exception("Failed to verify end user po and reseller po updated")
    except Exception as e:
        logger.error("Not able to verify end user po and reseller po updated %s", e)
        raise e


@then(parsers.parse('Validate Cancel update of end user po and reseller po'))
def validate_cancel_update_of_end_user_po_and_reseller_po(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_po = input_order_data.get("end_user_po")
        reseller_po = input_order_data.get("reseller_po")
        if not validate_sales_orders.do_validate_cancel_update_of_end_user_po_and_reseller_po(end_user_po, reseller_po,
                                                                                              feature_file_name,
                                                                                              screen_shot):
            raise Exception("Failed to Validate Cancel update for end user po and reseller po")
    except Exception as e:
        logger.error("Not able to Validate Cancel update for end user po and reseller po %s", e)
        raise e


@then(parsers.parse('Validate ACOP field is present and has valid value'))
def validate_acop_field(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.do_validate_acop_field(feature_file_name, screen_shot):
            raise Exception("Failed to Validate ACOP field")
    except Exception as e:
        logger.error("Not able to Validate ACOP field %s", e)
        raise e


@when(parsers.parse('Check if the order is editable'))
def check_if_order_is_editable(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_order_status_to_edit(feature_file_name, screen_shot):
            raise Exception("Failed to check if order is editable")
    except Exception as e:
        logger.error("Not able to check if order is editable %s", e)
        raise e


@then(parsers.parse('Update order line special bid unit price and quantity'))
def update_order_line(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        special_bid = input_order_data.get('edit_order_lines').split(",")[0]
        unit_price = input_order_data.get('edit_order_lines').split(",")[1]
        quantity = input_order_data.get('edit_order_lines').split(",")[2]

        if not validate_sales_orders.update_order_line_data(special_bid, unit_price, quantity, feature_file_name,
                                                            screen_shot):
            raise Exception("Failed to update order line")
    except Exception as e:
        logger.error("Not able to update order line %s", e)
        raise e


@then(parsers.parse('Cancel order line changes and validate it'))
def update_order_line_and_validate(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        special_bid = input_order_data.get('edit_order_lines').split(",")[0]
        unit_price = input_order_data.get('edit_order_lines').split(",")[1]
        quantity = input_order_data.get('edit_order_lines').split(",")[2]
        if not validate_sales_orders.cancel_order_line_changes_and_validate_data(special_bid, unit_price, quantity,
                                                                                 feature_file_name, screen_shot):
            raise Exception("Failed to cancel order line changes")
    except Exception as e:
        logger.error("Not able to update order line %s", e)
        raise e


@then(parsers.parse('Validate order line changes are updated'))
def order_line_changed_updated(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        special_bid = input_order_data.get('edit_order_lines').split(",")[0]
        unit_price = input_order_data.get('edit_order_lines').split(",")[1]
        quantity = input_order_data.get('edit_order_lines').split(",")[2]
        if not validate_sales_orders.validate_order_line_changed_updated(special_bid, unit_price, quantity,
                                                                         feature_file_name, screen_shot):
            raise Exception("Failed to validate order line changes")
    except Exception as e:
        logger.error("Not able to validate updated order line changes %s", e)
        raise e


@then(parsers.parse('Cancel ship to and end user info details and validate'))
def validate_cancel_ship_to_end_user_info_details(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        shipto_id = input_order_data.get('ship_to_info').split(",")[0]
        enduser_companyname = input_order_data.get('end_user_info').split(",")[2]
        if not validate_sales_orders.cancel_shipto_enduser_info_and_validate_data(shipto_id, enduser_companyname, feature_file_name, screen_shot):
            raise Exception("Failed to cancel ship to and end user info details")
    except Exception as e:
        logger.error("Not able to cancel ship to and end user info details %s", e)
        raise e


@then(parsers.parse('Update ship to and end user info'))
def update_ship_to_end_user_info(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        shipto_id = input_order_data.get('ship_to_info').split(",")[0]
        enduser_companyname = input_order_data.get('end_user_info').split(",")[2]
        if not validate_sales_orders.update_shipto_enduser_info(shipto_id, enduser_companyname, feature_file_name, screen_shot):
            raise Exception("Failed to update ship to and end user info details")
    except Exception as e:
        logger.error("Not able to update ship to and end user info details %s", e)
        raise e


@then(parsers.parse('Validate ship to and end user info updated'))
def validate_ship_to_end_user_info_updated(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        shipto_id = input_order_data.get('ship_to_info').split(",")[0]
        shipto_companyname = input_order_data.get('ship_to_info').split(",")[1]
        shipto_address = input_order_data.get('ship_to_info').split(",")[2]
        enduser_id = input_order_data.get('end_user_info').split(",")[0]
        enduser_contact = input_order_data.get('end_user_info').split(",")[1]
        enduser_companyname = input_order_data.get('end_user_info').split(",")[2]
        enduser_phonenumber = input_order_data.get('end_user_info').split(",")[3]
        enduser_address = input_order_data.get('end_user_info').split(",")[4]
        enduser_email = input_order_data.get('end_user_info').split(",")[5]
        if not validate_sales_orders.updated_shipto_enduser_info_validate(shipto_id, shipto_companyname, shipto_address,
                                                                enduser_id, enduser_contact, enduser_companyname,
                                                                enduser_phonenumber, enduser_address, enduser_email,
                                                                feature_file_name, screen_shot):
            raise Exception("Failed to update ship to and end user info details")
    except Exception as e:
        logger.error("Not able to update ship to and end user info details %s", e)
        raise e


@when(parsers.parse('Click on three dots and check that the options are correct'))
def validate_order_lines_option(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_options_on_order_lines(feature_file_name, screen_shot):
            raise Exception("Failed to cancel order line changes")
    except Exception as e:
        logger.error("Not able to update order line %s", e)
        raise e


@then(parsers.parse('Click on mark for cancel for order lines'))
def click_mark_for_cancel(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_mark_for_cancel(feature_file_name, screen_shot):
            raise Exception("Failed to click on mark for cancel")
    except Exception as e:
        logger.error("Not able to click on mark for cancel %s", e)
        raise e


@then(parsers.parse('Click on Unmark for cancel order line'))
def click_unmark_for_cancel(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_unmark_for_cancel(feature_file_name, screen_shot):
            raise Exception("Failed to click on unmark for cancel")
    except Exception as e:
        logger.error("Not able to click on unmark for cancel %s", e)
        raise e


@when(parsers.parse('Verify order status is "{status}"'))
def verify_order_status(init_driver, status):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_order_status(feature_file_name, status):
            raise Exception("Failed to validate order status")
    except Exception as e:
        logger.error("Error while validating order status %s", e)
        raise e


@when(parsers.parse('Verify order status {status} falls under edit category'))
def order_status_verification(init_driver, status):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_order_status_category(status, feature_file_name):
            raise Exception("Failed to validate order status")
    except Exception as e:
        logger.error("Error while validating order status %s", e)
        raise e


@then(parsers.parse('Click on order management link'))
def order_management_link_click(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_order_mgmt_click(feature_file_name):
            raise Exception("Failed to click on order management link")
    except Exception as e:
        logger.error("Error while clicking on order management link %s", e)
        raise e


@then(parsers.parse('Validate cancel order button is displayed'))
def is_cancel_order_button_displayed(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_cancel_order_button_displayed(feature_file_name):
            raise Exception("Failed to verify cancel order button")
    except Exception as e:
        logger.error("Error while validating cancel order button %s", e)
        raise e


@then(parsers.parse('Click on cancel order button'))
def cancel_order_btn_click(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_cancel_order_btn(feature_file_name):
            raise Exception("Failed to click on cancel order button")
    except Exception as e:
        logger.error("Error while clicking cancel order button %s", e)
        raise e


@then(parsers.parse('Verify the elements displayed on cancel order alert'))
def verify_cancel_order_alert_elements(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.cancel_order_alert_elements(feature_file_name):
            raise Exception("Failed to verify cancel order alert elements")
    except Exception as e:
        logger.error("Error while verifying cancel order alert elements %s", e)
        raise e


@then(parsers.parse('Cancel the order'))
def cancel_order(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_cancel_order(feature_file_name):
            raise Exception("Failed to click on cancel order button")
    except Exception as e:
        logger.error("Error while clicking on cancel order button %s", e)
        raise e


@then(parsers.parse('Verify success toast notification is displayed'))
def verify_success_notification(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.success_message_verify(feature_file_name):
            raise Exception("Failed to verify success toast notification")
    except Exception as e:
        logger.error("Error while verifying success toast notification %s", e)
        raise e


@then(parsers.parse("Click on mark for cancel for single line item"))
def cancel_single_line_item(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_cancel_single_line_item(feature_file_name):
            raise Exception("Failed to click on mark for cancel for single line item")
    except Exception as e:
        logger.error("Error while clicking on mark for cancel for single line item %s", e)
        raise e


@then(parsers.parse("Verify order line and edit button will not be active"))
def verify_order_line_edit_button_not_active(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_order_line_edit_button_not_active(feature_file_name):
            raise Exception("Failed to verify order line and edit button")
    except Exception as e:
        logger.error("Error while verifying order line and edit button %s", e)
        raise e


@then(parsers.parse("Click on resubmit order"))
def click_resubmit_order(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_resubmit_order_click(feature_file_name):
            raise Exception("Failed to click on resubmit order button")
    except Exception as e:
        logger.error("Error while clicking on resubmit order button %s", e)
        raise e


@then(parsers.parse("Verify cancelled order line is not visible"))
def verify_cancelled_order_line_not_visible(init_driver):
    feature_file_name = "sales_orders_edit"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_cancelled_order_not_visible(feature_file_name):
            raise Exception("Failed to verify cancelled order line")
    except Exception as e:
        logger.error("Error while verifying cancelled order line %s", e)
        raise e
