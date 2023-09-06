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


@scenario("features/hardware/sales_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/sales_orders.feature", "All columns visible on Sales Orders Page")
def test_column_visible_on_sales_orders_listing_page():
    pass


@scenario("features/hardware/sales_orders.feature", "Search order by IM Order from Sales Order")
def test_search_im_order_number():
    pass


@scenario("features/hardware/sales_orders.feature", "validation of created on date ascending")
def test_validate_created_on_ascending():
    pass


@scenario("features/hardware/sales_orders.feature", "validation of created on date descending")
def test_validate_created_on_descending():
    pass


# @scenario("features/hardware/sales_orders.feature", "All tabs visible on Order Details page")
# def test_all_tabs_on_order_details_tab():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Same header display for all tab")
# def test_same_header_display_for_all_tab():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Ingram order number and Order Status title on Order details page")
# def test_ingram_order_number_and_order_status_title_order_details_tab():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Header data on Order details page")
# def test_header_data_on_order_details_tab():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Reference Number fields data validation")
# def test_reference_number_fields_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Bill to info fields data validation")
# def test_bill_to_fields_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Ship to info fields data validation")
# def test_ship_to_fields_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "End user info fields data validation")
# def test_end_user_fields_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Order lines tab fields data validation")
# def test_order_lines_fields_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Serial number header data validation")
# def test_serial_number_header_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Additional Attributes header data validation")
# def test_additional_attributes_header_data_validation():
#     pass


@scenario("features/hardware/sales_orders.feature", "Verify filter with IM order")
def test_filter_by_im_order():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by Order type")
def test_filter_by_order_type():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by BCN")
def test_filter_by_bcn():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by Reseller PO")
def test_filter_by_reseller_po():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by Reseller Name")
def test_filter_by_reseller_name():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by Vendor Name")
def test_filter_by_vendor_name():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by End User Name")
def test_filter_by_end_user_name():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by Order Status")
def test_filter_by_order_status():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by Order Value")
def test_filter_by_order_value():
    pass


@scenario("features/hardware/sales_orders.feature", "Verify filter by Created On")
def test_filter_by_created_on():
    pass


@scenario("features/hardware/sales_orders.feature", "Validate Update and cancel for end user po and reseller po")
def test_update_end_user_po_and_reseller_po():
    pass


@scenario("features/hardware/sales_orders.feature", "Validate ACOP field")
def test_validate_acop_field():
    pass


@scenario("features/hardware/sales_orders.feature", "Validate Update and Cancel for edit order line")
def test_validate_update_order_line():
    pass


@scenario("features/hardware/sales_orders.feature", "Validate unmark cancel order line")
def test_unmark_order_lines():
    pass


@scenario("features/hardware/sales_orders.feature", "logout X4A")
def test_logout_x4a():
    pass


# @scenario("features/hardware/sales_orders.feature", "Search order by BCN from Sales Order")
# def test_search_bcn():
#     pass
#

#
# @scenario("features/hardware/sales_orders.feature", "Search order by Type from Sales Order")
# def test_search_order_type():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Search order by Reseller PO from Sales Order")
# def test_search_vendor_name():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Search order by Vendor name from Sales Order")
# def test_search_vendor_name():
#     pass
#
#
# @scenario("features/hardware/sales_orders.feature", "Search order by Order status from Sales Order")
# def test_search_order_status():
#     pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "sales_orders"
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
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        validate_sales_orers.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@then(parsers.parse('the user traverse to Sales Order menu'))
def click_on_sales_orders_menu(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_sales_orders(feature_file_name, screen_shot):
            raise Exception("Failed to click on Sales Orders menu")
    except Exception as e:
        logger.error("Error while clicking on Sales Orders menu %s", e)
        raise e


@then(parsers.parse('verify that Sales Orders listing page visible'))
def sales_orders_listing_page_visible(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.is_sales_orders_listing_page_visible(feature_file_name, screen_shot):
            raise Exception("Failed to verify that Sales Orders listing page")
    except Exception as e:
        logger.error("Error while verifying that Sales Orders listing page %s", e)
        raise e


@then(parsers.parse('verify that all column should be present'))
def columns_visible_on_sales_orders_listing_page_visible(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.is_all_column_visible(feature_file_name, screen_shot):
            raise Exception("Failed to verify that All column on sales orders page ")
    except Exception as e:
        logger.error("Error while verifying that All column on Sales Orders page %s", e)
        raise e


@when(parsers.parse('search a order with specific IM Order number'))
def search_im_order_number(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        if not validate_sales_orers.do_search_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to search IM Order Number")
    except Exception as e:
        logger.error("Error while searching IM Order Number %s", e)
        raise e


@then(parsers.parse('Validate the IM Order number is listed'))
def validate_im_order_number(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        if not validate_sales_orers.do_validate_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to Validate IM Order Number")
    except Exception as e:
        logger.error("Not able to Validate IM Order Number %s", e)
        raise e


@then(parsers.parse('Validate All orders created on date should be ascending'))
def validate_created_on_date_ascending(init_driver):
    page1 = 1
    page2 = 3
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.do_validate_created_on_ascending(feature_file_name, page1, page2, screen_shot):
            raise Exception("Failed to Validate All orders created on date should be a,scending")
    except Exception as e:
        logger.error("Not able to Validate All orders created on date should be ascending %s", e)
        raise e


@then(parsers.parse('Validate All orders created on date should be descending'))
def validate_created_on_date_descending(init_driver):
    page1 = 1
    page2 = 3
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.do_validate_created_on_descending(feature_file_name, page1, page2, screen_shot):
            raise Exception("Failed to Validate All orders created on date should be descending")
    except Exception as e:
        logger.error("Not able to Validate All orders created on date should be descending %s", e)
        raise e


@when(parsers.parse('search a order with specific BCN'))
def search_bcn(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        reseller_bcn = input_order_data.get("reseller_bcn")

        if not validate_sales_orers.do_search_bcn(reseller_bcn, feature_file_name, screen_shot):
            raise Exception("Failed to search BCN")
    except Exception as e:
        logger.error("Error while searching BCN %s", e)
        raise e


@when(parsers.parse('Click on searched IM order number'))
def click_on_im_order_number(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        logger.info("click")
        if not validate_sales_orers.click_on_im_order_num(feature_file_name):
            raise Exception("Failed to click on searched IM order number")
    except Exception as e:
        logger.error("Error while click on searched IM order number %s", e)
        raise e


@then(parsers.parse('Verify that all tabs should be present'))
def tabs_visible_on_order_details_page(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.is_all_tabs_visible(feature_file_name, screen_shot):
            raise Exception("Failed to verify that All tabs on Order Details page")
    except Exception as e:
        logger.error("Error while verifying that All tabs on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order Details tab on Order Details page'))
def click_on_order_detail_tab(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_order_details_tab(feature_file_name):
            raise Exception("Failed to click on Order Details tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Details tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order lines tab on Order Details page'))
def click_on_order_lines_tab(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_order_lines_tab(feature_file_name):
            raise Exception("Failed to click on Order Lines tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Lines tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order Tracking tab on Order Details page'))
def click_on_order_tracking_tab(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_order_tracking_tab(feature_file_name):
            raise Exception("Failed to click on Order Tracking tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Tracking tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Additional attributes tab on Order Details page'))
def click_on_order_lines_tab(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_additional_attr_tab(feature_file_name):
            raise Exception("Failed to click on Additional attributes tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Additional attributes tab on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate header data contains Order value and Order type'))
def header_data_contain_order_value_order_type(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_value = input_order_data.get("order_value")
        if not validate_sales_orers.is_order_value_header_data_visible(feature_file_name, screen_shot, order_value):
            raise Exception("Failed to verify that Order value header data on Order Details page")
    except Exception as e:
        logger.error("Error while verify that Order value header data on Order Details page %s", e)
        raise e


@then(parsers.parse(
    'Verify that title on the header of the order details page contains Ingram order number and Order Status'))
def title_ingram_order_number_and_order_status(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_status = input_order_data.get("order_status")
        if not validate_sales_orers.is_ingram_order_number_and_order_status_title_shown(feature_file_name, screen_shot,
                                                                                        im_order_number, order_status):
            raise Exception(
                "Failed to Verify that title on the header of the order details page contains Ingram order number and the Order Status")
    except Exception as e:
        logger.error(
            "Error while verifying that title on the header of the order details page contains Ingram order number and the Order Status %s",
            e)
        raise e


@then(parsers.parse('Validate header data contains Order value'))
def header_data_contain_order_value(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_value = input_order_data.get("order_value")

        if not validate_sales_orers.is_order_value_header_data_visible(feature_file_name, screen_shot, order_value):
            raise Exception("Failed to verify that Order value header data on Order Details page")
    except Exception as e:
        logger.error("Error while verify that Order value header data on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate header data contains Order type'))
def header_data_contain_order_type(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_type = input_order_data.get("order_type")

        if not validate_sales_orers.is_order_type_header_data_visible(feature_file_name, screen_shot, order_type):
            raise Exception("Failed to verify that Order type header data on Order Details page")
    except Exception as e:
        logger.error("Error while verify that Order type header data on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under reference number section'))
def fields_under_reference_number_section(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        reference_numbers = input_order_data.get("reference_numbers")
        reference_numbers_list = list(reference_numbers.split(","))
        logger.info(reference_numbers_list)

        if not validate_sales_orers.validate_fields_under_reference_no(feature_file_name, screen_shot,
                                                                       reference_numbers_list):
            raise Exception("Failed to verify the fields under Reference number section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Reference number section on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Billing tab on Order Details page'))
def click_on_billing_tab(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_billing_tab(feature_file_name):
            raise Exception("Failed to click on Billing tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Billing tab on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Bill to info section'))
def fields_under_bill_to_info_section(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        billing_to_info = input_order_data.get("billing_to_info")
        billing_to_info_list = list(billing_to_info.split(","))
        logger.info(billing_to_info_list)
        if not validate_sales_orers.validate_fields_under_bill_to_info(feature_file_name, screen_shot,
                                                                       billing_to_info_list):
            raise Exception("Failed to verify fields under Bill to info section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Bill to info section on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Ship to info section'))
def fields_under_ship_to_info_section(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        ship_to_info = input_order_data.get("ship_to_info")
        ship_to_info_list = list(ship_to_info.split(","))
        logger.info(ship_to_info_list)
        if not validate_sales_orers.validate_fields_under_ship_to_info(feature_file_name, screen_shot,
                                                                       ship_to_info_list):
            raise Exception("Failed to verify fields under Ship to info section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Ship to info section on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under End user info section'))
def fields_under_end_user_info_section(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_info = input_order_data.get("end_user_info")
        end_user_info_list = list(end_user_info.split(","))
        logger.info(end_user_info_list)
        if not validate_sales_orers.validate_fields_under_end_user_info(feature_file_name, screen_shot,
                                                                        end_user_info_list):
            raise Exception("Failed to verify fields under End user info section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under End user info section on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Order lines tab'))
def fields_under_order_lines_tab(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_lines_tab_info = input_order_data.get("order_lines_tab")
        order_lines_tab_info_list = list(order_lines_tab_info.split(","))
        logger.info(order_lines_tab_info_list)
        if not validate_sales_orers.validate_fields_under_order_lines_tab(feature_file_name, screen_shot,
                                                                          order_lines_tab_info_list):
            raise Exception("Failed to verify fields under Order lines on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Order lines section on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Serial numbers view more option'))
def click_on_serial_numbers_view_more_option(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_view_more_option(feature_file_name):
            raise Exception("Failed to click on Serial numbers View more option on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Serial numbers View more option on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Serial Numbers header'))
def fields_under_serial_numbers_tab(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        serial_numbers_info = input_order_data.get("serial_numbers")
        serial_numbers_info_list = list(serial_numbers_info.split(","))
        logger.info(serial_numbers_info_list)
        if not validate_sales_orers.validate_fields_under_serial_numbers_header(feature_file_name, screen_shot,
                                                                                serial_numbers_info_list):
            raise Exception("Failed to verify fields under Serial numbers header on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Serial numbers header on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Additional attributes view more option'))
def click_on_additional_attr_view_more_option(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orers.click_on_additional_attr_view_more_button(feature_file_name):
            raise Exception("Failed to click on Additional Attributes View more option on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Additional Attributes View more option on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Additional attributes header'))
def fields_under_additional_attributes_tab(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        additional_attributes_info = input_order_data.get("additional_attributes")
        additional_attributes_info_list = list(additional_attributes_info.split(","))
        logger.info(additional_attributes_info_list)
        if not validate_sales_orers.validate_fields_under_additional_attribute_header(feature_file_name, screen_shot,
                                                                                      additional_attributes_info_list):
            raise Exception("Failed to verify fields under Additional attributes header on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Additional attributes header on Order Details page %s", e)
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orers = ValidateSalesOrdersData(init_driver)
    try:
        validate_sales_orers.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e


@when(parsers.parse('Filter by IM order'))
def filter_by_im_order(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order = input_order_data.get("im_order_number")
        if not validate_sales_orders.filter_by_im_order(feature_file_name, screen_shot, im_order):
            raise Exception("Failed to filter by IM order")
    except Exception as e:
        logger.error("Error while filtering by IM Order %s", e)
        raise e


@then(parsers.parse('Verify the data for filtered IM order is listed'))
def verify_filter_by_im_order_result(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order = input_order_data.get("im_order_number")
        if not validate_sales_orders.verify_im_order_filter_results(feature_file_name, screen_shot, im_order):
            raise Exception("Failed to verify filter by IM order results")
    except Exception as e:
        logger.error("Error while verifying filter by IM Order results %s", e)
        raise e


@when(parsers.parse('Filter by Order type'))
def filter_by_order_type(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_type = input_order_data.get("filter_order_type")
        if not validate_sales_orders.do_filter_order_type(order_type, feature_file_name, screen_shot):
            raise Exception("Failed to filter by Order type")
    except Exception as e:
        logger.error("Error while filtering by Order type %s", e)
        raise e


@then(parsers.parse('Validate the order Type is listed'))
def validate_filter_by_order_type_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_type = input_order_data.get("filter_order_type")
        if not validate_sales_orders.verify_order_type_filter_results(feature_file_name, screen_shot, order_type):
            raise Exception("Failed to Validate order type")
    except Exception as e:
        logger.error("Not able to Validate order type %s", e)
        raise e


@when(parsers.parse('Filter by BCN'))
def filter_by_bcn(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        bcn = input_order_data.get("reseller_bcn")
        logger.info(bcn)
        if not validate_sales_orders.do_filter_bcn(bcn, feature_file_name, screen_shot):
            raise Exception("Failed to filter by BCN")
    except Exception as e:
        logger.error("Error while filtering by BCN %s", e)
        raise e


@then(parsers.parse('Validate the BCN is listed'))
def validate_filter_by_bcn_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        bcn = input_order_data.get("reseller_bcn")
        if not validate_sales_orders.do_validate_reseller_bcn(bcn, feature_file_name, screen_shot):
            raise Exception("Failed to Validate BCN")
    except Exception as e:
        logger.error("Not able to Validate BCN %s", e)
        raise e


@when(parsers.parse('Filter by Reseller PO'))
def filter_by_reseller_po(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        reseller_po = input_order_data.get("reseller_po")
        if not validate_sales_orders.do_filter_reseller_po(reseller_po, feature_file_name, screen_shot):
            raise Exception("Failed to filter by Reseller PO")
    except Exception as e:
        logger.error("Error while filtering by Reseller PO %s", e)
        raise e


@then(parsers.parse('Validate the Reseller PO is listed'))
def validate_filter_by_reseller_po_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        reseller_po = input_order_data.get("reseller_po")
        if not validate_sales_orders.do_validate_reseller_po(reseller_po, feature_file_name, screen_shot):
            raise Exception("Failed to Validate Reseller PO")
    except Exception as e:
        logger.error("Not able to Validate Reseller PO %s", e)
        raise e


@when(parsers.parse('Filter by Reseller Name'))
def filter_by_reseller_name(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        reseller_name = input_order_data.get("reseller_name")
        if not validate_sales_orders.do_filter_reseller_name(reseller_name, feature_file_name, screen_shot):
            raise Exception("Failed to filter by Reseller Name")
    except Exception as e:
        logger.error("Error while filtering by Reseller Name %s", e)
        raise e


@then(parsers.parse('Validate the Reseller Name is listed'))
def validate_filter_by_reseller_name_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        reseller_name = input_order_data.get("reseller_name")
        if not validate_sales_orders.do_validate_reseller_name(reseller_name, feature_file_name, screen_shot):
            raise Exception("Failed to Validate Reseller Name")
    except Exception as e:
        logger.error("Not able to Validate Reseller Name %s", e)
        raise e


@when(parsers.parse('Filter by Vendor Name'))
def filter_by_vendor_name(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        vendor_name = input_order_data.get("vendor_name")
        if not validate_sales_orders.do_filter_vendor_name(vendor_name, feature_file_name, screen_shot):
            raise Exception("Failed to filter by Vendor Name")
    except Exception as e:
        logger.error("Error while filtering by Vendor Name %s", e)
        raise e


@then(parsers.parse('Validate the Vendor Name is listed'))
def validate_filter_by_vendor_name_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        vendor_name = input_order_data.get("vendor_name")
        if not validate_sales_orders.do_validate_vendor_name(vendor_name, feature_file_name, screen_shot):
            raise Exception("Failed to Validate Vendor Name")
    except Exception as e:
        logger.error("Not able to Validate Vendor Name %s", e)
        raise e


@when(parsers.parse('Filter by End User Name'))
def filter_by_end_user_name(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_name = input_order_data.get("end_user_name")
        if not validate_sales_orders.do_filter_end_user_name(end_user_name, feature_file_name, screen_shot):
            raise Exception("Failed to filter by End User Name")
    except Exception as e:
        logger.error("Error while filtering by End User Name %s", e)
        raise e


@then(parsers.parse('Validate the End User Name is listed'))
def validate_filter_by_end_user_name_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_name = input_order_data.get("end_user_name")
        if not validate_sales_orders.do_validate_end_user_name(end_user_name, feature_file_name, screen_shot):
            raise Exception("Failed to Validate End User Name")
    except Exception as e:
        logger.error("Not able to Validate End User Name %s", e)
        raise e


@when(parsers.parse('Filter by Order Status'))
def filter_by_order_status(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_status = input_order_data.get("filter_order_status")
        if not validate_sales_orders.do_filter_order_status(order_status, feature_file_name, screen_shot):
            raise Exception("Failed to filter by Order Status")
    except Exception as e:
        logger.error("Error while filtering by Order Status %s", e)
        raise e


@then(parsers.parse('Validate the Order Status is listed'))
def validate_filter_by_order_status_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_status = input_order_data.get("filter_order_status")
        if not validate_sales_orders.do_validate_order_status(order_status, feature_file_name, screen_shot):
            raise Exception("Failed to Validate Order Status")
    except Exception as e:
        logger.error("Not able to Validate Order Status %s", e)
        raise e


@when(parsers.parse('Filter by Order Value'))
def filter_by_order_value(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        min_order_value = input_order_data.get("total_revenue_min")
        max_order_value = input_order_data.get("total_revenue_max")
        if not validate_sales_orders.do_filter_order_value(min_order_value, max_order_value, feature_file_name, screen_shot):
            raise Exception("Failed to filter by Order Value")
    except Exception as e:
        logger.error("Error while filtering by Order Value %s", e)
        raise e


@then(parsers.parse('Validate the Order Value is listed'))
def validate_filter_by_order_value_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        min_order_value = input_order_data.get("total_revenue_min")
        max_order_value = input_order_data.get("total_revenue_max")
        if not validate_sales_orders.do_validate_order_value(min_order_value, max_order_value, feature_file_name, screen_shot):
            raise Exception("Failed to Validate Order Value")
    except Exception as e:
        logger.error("Not able to Validate Order Value %s", e)
        raise e


@when(parsers.parse('Filter by Created On'))
def filter_by_created_on(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        created_on = input_order_data.get("created_on")
        if not validate_sales_orders.do_filter_created_on(created_on, feature_file_name, screen_shot):
            raise Exception("Failed to filter by Created On")
    except Exception as e:
        logger.error("Error while filtering by Created On %s", e)
        raise e


@then(parsers.parse('Validate the Created On is listed'))
def validate_filter_by_order_value_results(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        created_on = input_order_data.get("created_on")
        if not validate_sales_orders.do_validate_created_on(created_on, feature_file_name, screen_shot):
            raise Exception("Failed to Validate Created On")
    except Exception as e:
        logger.error("Not able to Validate Created On %s", e)
        raise e


@then(parsers.parse('Validate Update end user po and reseller po'))
def validate_update_end_user_po_and_reseller_po(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_po = input_order_data.get("end_user_po")
        reseller_po = input_order_data.get("reseller_po")
        if not validate_sales_orders.do_validate_update_end_user_po_and_reseller_po(end_user_po, reseller_po, feature_file_name, screen_shot):
            raise Exception("Failed to Validate update for end user po and reseller po")
    except Exception as e:
        logger.error("Not able to Validate update for end user po and reseller po %s", e)
        raise e


@then(parsers.parse('Validate Cancel update of end user po and reseller po'))
def validate_cancel_update_of_end_user_po_and_reseller_po(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        end_user_po = input_order_data.get("end_user_po")
        reseller_po = input_order_data.get("reseller_po")
        if not validate_sales_orders.do_validate_cancel_update_of_end_user_po_and_reseller_po(end_user_po, reseller_po, feature_file_name, screen_shot):
            raise Exception("Failed to Validate Cancel update for end user po and reseller po")
    except Exception as e:
        logger.error("Not able to Validate Cancel update for end user po and reseller po %s", e)
        raise e


@then(parsers.parse('Validate ACOP field is present and has valid value'))
def validate_acop_field(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.do_validate_acop_field(feature_file_name, screen_shot):
            raise Exception("Failed to Validate ACOP field")
    except Exception as e:
        logger.error("Not able to Validate ACOP field %s", e)
        raise e


@when(parsers.parse('Check if the order is editable'))
def check_if_order_is_editable(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_order_status_to_edit(feature_file_name, screen_shot):
            raise Exception("Failed to check if order is editable")
    except Exception as e:
        logger.error("Not able to check if order is editable %s", e)
        raise e


@then(parsers.parse('Update order line and validate it'))
def update_order_line_and_validate(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
                db_file_path, feature_file_name)
        special_bid = input_order_data.get('edit_order_lines').split(",")[0]
        unit_price = input_order_data.get('edit_order_lines').split(",")[1]
        quantity = input_order_data.get('edit_order_lines').split(",")[2]

        if not validate_sales_orders.update_order_line_and_validate_data(special_bid, unit_price, quantity, feature_file_name, screen_shot):
            raise Exception("Failed to update order line")
    except Exception as e:
        logger.error("Not able to update order line %s", e)
        raise e


@then(parsers.parse('Cancel order line changes and validate it'))
def update_order_line_and_validate(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
                db_file_path, feature_file_name)
        special_bid = input_order_data.get('edit_order_lines').split(",")[0]
        unit_price = input_order_data.get('edit_order_lines').split(",")[1]
        quantity = input_order_data.get('edit_order_lines').split(",")[2]
        if not validate_sales_orders.cancel_order_line_changes_and_validate_data(special_bid, unit_price, quantity, feature_file_name, screen_shot):
            raise Exception("Failed to cancel order line changes")
    except Exception as e:
        logger.error("Not able to update order line %s", e)
        raise e


@given(parsers.parse('Check whether the order is in customer hold'))
def validate_order_is_in_customer_hold(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        # input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
        #         db_file_path, feature_file_name)
        # special_bid = input_order_data.get('edit_order_lines').split(",")[0]
        # unit_price = input_order_data.get('edit_order_lines').split(",")[1]
        # quantity = input_order_data.get('edit_order_lines').split(",")[2]
        if not validate_sales_orders.validate_order_status_is_customer_hold(feature_file_name, screen_shot):
            raise Exception("Failed to cancel order line changes")
    except Exception as e:
        logger.error("Not able to update order line %s", e)
        raise e


@when(parsers.parse('Click on three dots and check that the options are correct'))
def validate_order_lines_option(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.validate_options_on_order_lines(feature_file_name, screen_shot):
            raise Exception("Failed to cancel order line changes")
    except Exception as e:
        logger.error("Not able to update order line %s", e)
        raise e


@then(parsers.parse('Click on mark for cancel for order lines'))
def click_mark_for_cancel(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_mark_for_cancel(feature_file_name, screen_shot):
            raise Exception("Failed to click on mark for cancel")
    except Exception as e:
        logger.error("Not able to click on mark for cancel %s", e)
        raise e


@then(parsers.parse('Click on Unmark for cancel order line'))
def click_unmark_for_cancel(init_driver):
    feature_file_name = "sales_orders"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_mark_for_cancel(feature_file_name, screen_shot):
            raise Exception("Failed to click on unmark for cancel")
    except Exception as e:
        logger.error("Not able to click on unmark for cancel %s", e)
        raise e


# We are blocking because filter is applied for all columns.

# @then(parsers.parse('Validate the searched BCN is listed'))
# def validate_bcn(init_driver):
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         page1 = 1
#         page2 = 5
#         page3 = 10000
#         reseller_bcn = order_management_srv_obj.get_bcn_by_feature_file_name(db_file_path, feature_file_name)
#         if not create_order_steps.do_validate_reseller_bcn(reseller_bcn, feature_file_name, screen_shot, page1, page2,
#                                                            page3):
#             raise Exception("Failed to Validate Reseller BCN")
#     except Exception as e:
#         logger.error("Not able to Validate Reseller BCN %s", e)
#         raise e
#
#
#
# @when(parsers.parse('search a order with specific order Type'))
# def search_order_type(init_driver):
#     init_driver.refresh()
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         order_type = order_management_srv_obj.get_order_type_by_feature_file_name(db_file_path,
#                                                                                   feature_file_name)
#         if not create_order_steps.do_search_order_type(order_type, feature_file_name, screen_shot):
#             raise Exception("Failed to search order type")
#     except Exception as e:
#         logger.error("Error while searching order type %s", e)
#         raise e
#
#
# @then(parsers.parse('Validate the order Type is listed'))
# def validate_order_type(init_driver):
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         page1 = 1
#         page2 = 5
#         page3 = 45
#         order_type = order_management_srv_obj.get_order_type_by_feature_file_name(db_file_path,
#                                                                                   feature_file_name)
#         if not create_order_steps.do_validate_order_type(order_type, feature_file_name, screen_shot, page1, page2,
#                                                          page3):
#             raise Exception("Failed to Validate Order Type")
#     except Exception as e:
#         logger.error("Not able to Validate Order Type %s", e)
#         raise e
#
#
# @when(parsers.parse('search a order with specific Reseller PO'))
# def search_reseller_po(init_driver):
#     init_driver.refresh()
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         reseller_po = order_management_srv_obj.get_reseller_po_by_feature_file_name(db_file_path,
#                                                                                     feature_file_name)
#         if not create_order_steps.do_search_reseller_po(reseller_po, feature_file_name, screen_shot):
#             raise Exception("Failed to search Reseller PO")
#     except Exception as e:
#         logger.error("Error while searching Reseller PO %s", e)
#         raise e
#
#
# @then(parsers.parse('Validate the Reseller PO is listed'))
# def validate_reseller_po(init_driver):
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         reseller_po = order_management_srv_obj.get_reseller_po_by_feature_file_name(db_file_path,
#                                                                                     feature_file_name)
#         if not create_order_steps.do_validate_reseller_po(reseller_po, feature_file_name, screen_shot):
#             raise Exception("Failed to Validate Reseller PO")
#     except Exception as e:
#         logger.error("Not able to Validate Reseller PO %s", e)
#         raise e
#
#
# @when(parsers.parse('search a order with specific Vendor name'))
# def search_vendor_name(init_driver):
#     init_driver.refresh()
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         vendor_name = order_management_srv_obj.get_vendor_name_by_feature_file_name(db_file_path,
#                                                                                     feature_file_name)
#         if not create_order_steps.do_search_vendor_name(vendor_name, feature_file_name, screen_shot):
#             raise Exception("Failed to search vendor name")
#     except Exception as e:
#         logger.error("Error while searching vendor name %s", e)
#         raise e
#
#
# @then(parsers.parse('Validate the Vendor name is listed'))
# def validate_vendor_name(init_driver):
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         vendor_name = order_management_srv_obj.get_vendor_name_by_feature_file_name(db_file_path,
#                                                                                     feature_file_name)
#         if not create_order_steps.do_validate_vendor_name(vendor_name, feature_file_name, screen_shot):
#             raise Exception("Failed to Validate Vendor name")
#     except Exception as e:
#         logger.error("Not able to Validate Vendor name %s", e)
#         raise e
#
#
# @when(parsers.parse('search a order with specific Order status'))
# def search_order_status(init_driver):
#     init_driver.refresh()
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         order_status = order_management_srv_obj.get_order_status_by_feature_file_name(db_file_path,
#                                                                                       feature_file_name)
#         if not create_order_steps.do_search_order_status(order_status, feature_file_name, screen_shot):
#             raise Exception("Failed to search Order Status")
#     except Exception as e:
#         logger.error("Error while searching Order Status %s", e)
#         raise e
#
#
# @then(parsers.parse('Validate the Order status is listed'))
# def validate_order_status(init_driver):
#     feature_file_name = "sales_orders"
#     create_order_steps = CreateOrder(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     try:
#         order_status = order_management_srv_obj.get_order_status_by_feature_file_name(db_file_path,
#                                                                                       feature_file_name)
#         if not create_order_steps.do_validate_order_status(order_status, feature_file_name, screen_shot):
#             raise Exception("Failed to Validate Order Status")
#     except Exception as e:
#         logger.error("Not able to Validate Vendor name %s", e)
#         raise e
