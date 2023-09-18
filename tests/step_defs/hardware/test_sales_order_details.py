import re

from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from RestApi.Operations.fetch_order_via_api import FetchOrderViaApi
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from db.service.X4ASalesOrderDetailsDbManagementService import X4ASalesOrderDetailsDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateSalesOrdersData import ValidateSalesOrdersData
from tests.step_defs.hardware.test_apitest import base_test

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
order_management_srv_obj = X4AInputOrderDbManagementService()
sales_order_details_srv_obj = X4ASalesOrderDetailsDbManagementService()


@scenario("features/hardware/sales_order_details.feature", "sales order details check")
def test_sales_order_details():
    pass


@scenario("features/hardware/sales_order_details.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/sales_order_details.feature", "All tabs visible on Order Details page")
def test_all_tabs_on_order_details_tab():
    pass


@scenario("features/hardware/sales_order_details.feature", "Same header display for all tab")
def test_same_header_display_for_all_tab():
    pass


@scenario("features/hardware/sales_order_details.feature", "Ingram order number and Order Status title on Order details page")
def test_ingram_order_number_and_order_status_title_order_details_tab():
    pass


@scenario("features/hardware/sales_order_details.feature", "Header data on Order details page")
def test_header_data_on_order_details_tab():
    pass


@scenario("features/hardware/sales_order_details.feature", "Reference Number fields data validation")
def test_reference_number_fields_data_validation():
    pass


@scenario("features/hardware/sales_order_details.feature", "Bill to info fields data validation")
def test_bill_to_fields_data_validation():
    pass


@scenario("features/hardware/sales_order_details.feature", "Ship to info fields data validation")
def test_ship_to_fields_data_validation():
    pass


@scenario("features/hardware/sales_order_details.feature", "End user info fields data validation")
def test_end_user_fields_data_validation():
    pass

#
# @scenario("features/hardware/sales_order_details.feature", "Order lines tab fields data validation")
# def test_order_lines_fields_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_order_details.feature", "Serial number header data validation")
# def test_serial_number_header_data_validation():
#     pass
#
#
# @scenario("features/hardware/sales_order_details.feature", "Additional Attributes header data validation")
# def test_additional_attributes_header_data_validation():
#     pass


@given(parsers.parse('fetch sales order details via api'))
def fetch_order_details(init_driver):
    feature_file_name = "sales_order_details"
    fetch_order_via_api = FetchOrderViaApi()
    prepare_obj = PrepareObject(init_driver)
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = base_test.filtered_orders_by_feature_file(test_data_order, feature_file_name)
        logger.info(filtered_order_data)
        for order_index, test_data_order in filtered_order_data.iterrows():
            x4a_input_order_list.clear()
            logger.info(test_data_order)
            x4a_input_order_data = prepare_obj.prepare_x4a_inp_ord_data_obj(test_data_order)
            x4a_input_order_list.append(x4a_input_order_data)
            order_management_srv_obj.save_x4a_input_order(db_file_path, x4a_input_order_list)
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_date = input_order_data.get("order_date")
        details = fetch_order_via_api.post_request_for_sales_order_detail_fetch(im_order_number, order_date)
        logger.info(details)
        fetch_order_via_api.extract_order_details_data_and_save_in_db(details, feature_file_name)
        fetch_order_via_api.extract_order_lines_and_save_to_db(details)
    except Exception as e:
        logger.error("Failed to fetch order details %s", e)
        raise e


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    feature_file_name = "sales_order_details"
    try:
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
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        validate_sales_orders.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@then(parsers.parse('the user traverse to Sales Order menu'))
def click_on_sales_orders_menu(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_sales_orders(feature_file_name, screen_shot):
            raise Exception("Failed to click on Sales Orders menu")
    except Exception as e:
        logger.error("Error while clicking on Sales Orders menu %s", e)
        raise e


@when(parsers.parse('search a order with specific IM Order number'))
def search_im_order_number(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        if not validate_sales_orders.do_search_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to search IM Order Number")
    except Exception as e:
        logger.error("Error while searching IM Order Number %s", e)
        raise e


@then(parsers.parse('Validate the IM Order number is listed'))
def validate_im_order_number(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        if not validate_sales_orders.do_validate_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to Validate IM Order Number")
    except Exception as e:
        logger.error("Not able to Validate IM Order Number %s", e)
        raise e
    
    
@when(parsers.parse('Click on searched IM order number'))
def click_on_im_order_number(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        logger.info("click")
        if not validate_sales_orders.click_on_im_order_num(feature_file_name):
            raise Exception("Failed to click on searched IM order number")
    except Exception as e:
        logger.error("Error while click on searched IM order number %s", e)
        raise e


@then(parsers.parse('Verify that all tabs should be present'))
def tabs_visible_on_order_details_page(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.is_all_tabs_visible(feature_file_name, screen_shot):
            raise Exception("Failed to verify that All tabs on Order Details page")
    except Exception as e:
        logger.error("Error while verifying that All tabs on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order Details tab on Order Details page'))
def click_on_order_detail_tab(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_order_details_tab(feature_file_name):
            raise Exception("Failed to click on Order Details tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Details tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order lines tab on Order Details page'))
def click_on_order_lines_tab(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_order_lines_tab(feature_file_name):
            raise Exception("Failed to click on Order Lines tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Lines tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Order Tracking tab on Order Details page'))
def click_on_order_tracking_tab(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_order_tracking_tab(feature_file_name):
            raise Exception("Failed to click on Order Tracking tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Order Tracking tab on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Additional attributes tab on Order Details page'))
def click_on_order_lines_tab(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_additional_attr_tab(feature_file_name):
            raise Exception("Failed to click on Additional attributes tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Additional attributes tab on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate header data contains Order value and Order type'))
def header_data_contain_order_value_order_type(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        order_value = sales_order_details.get("order_value")
        order_type = sales_order_details.get("order_type")
        if not validate_sales_orders.is_order_value_header_data_visible(feature_file_name, screen_shot, order_value):
            raise Exception("Failed to verify that Order value header data on Order Details page")
        if not validate_sales_orders.is_order_type_header_data_visible(feature_file_name, screen_shot, order_type):
            raise Exception("Failed to verify that Order type header data on Order Details page")
    except Exception as e:
        logger.error("Error while verify that Order value header data on Order Details page %s", e)
        raise e


@then(parsers.parse(
    'Verify that title on the header of the order details page contains Ingram order number and Order Status'))
def title_ingram_order_number_and_order_status(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        order_number = sales_order_details.get("im_order_number")
        order_status = sales_order_details.get("order_status")
        if not validate_sales_orders.is_ingram_order_number_and_order_status_title_shown(feature_file_name, screen_shot,
                                                                                        order_number, order_status):
            raise Exception(
                "Failed to Verify that title on the header of the order details page contains Ingram order number and the Order Status")
    except Exception as e:
        logger.error(
            "Error while verifying that title on the header of the order details page contains Ingram order number and the Order Status %s",
            e)
        raise e


@then(parsers.parse('Validate header data contains Order value'))
def header_data_contain_order_value(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        order_value = sales_order_details.get("order_value")
        if not validate_sales_orders.is_order_value_header_data_visible(feature_file_name, screen_shot, order_value):
            raise Exception("Failed to verify that Order value header data on Order Details page")
    except Exception as e:
        logger.error("Error while verify that Order value header data on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate header data contains Order type'))
def header_data_contain_order_type(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        order_type = sales_order_details.get("order_type")
        if not validate_sales_orders.is_order_type_header_data_visible(feature_file_name, screen_shot, order_type):
            raise Exception("Failed to verify that Order type header data on Order Details page")
    except Exception as e:
        logger.error("Error while verify that Order type header data on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under reference number section'))
def fields_under_reference_number_section(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        reseller_po = sales_order_details.get("reseller_po")
        end_user_po = sales_order_details.get("end_user_po")

        if not validate_sales_orders.validate_fields_under_reference_no(feature_file_name, screen_shot,
                                                                       reseller_po, end_user_po):
            raise Exception("Failed to verify the fields under Reference number section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Reference number section on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Billing tab on Order Details page'))
def click_on_billing_tab(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_billing_tab(feature_file_name):
            raise Exception("Failed to click on Billing tab on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Billing tab on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Bill to info section'))
def fields_under_bill_to_info_section(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        bill_to_suffix = sales_order_details.get("bill_to_suffix")
        bill_to_name = sales_order_details.get("bill_to_name")
        bill_to_address = sales_order_details.get("bill_to_address")
        bill_to_phone = sales_order_details.get("bill_to_phone")
        bill_to_contact = sales_order_details.get("bill_to_contact")
        bill_to_email = sales_order_details.get("bill_to_email")
        if not validate_sales_orders.validate_fields_under_bill_to_info(feature_file_name, screen_shot,
                                                                       bill_to_suffix, bill_to_name, bill_to_address,
                                                                        bill_to_phone, bill_to_contact, bill_to_email):
            raise Exception("Failed to verify fields under Bill to info section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Bill to info section on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Ship to info section'))
def fields_under_ship_to_info_section(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        ship_to_suffix = sales_order_details.get("ship_to_suffix")
        ship_to_name = sales_order_details.get("ship_to_name")
        ship_to_address = sales_order_details.get("ship_to_address")
        ship_to_phone = sales_order_details.get("ship_to_phone")
        ship_to_contact = sales_order_details.get("ship_to_contact")
        ship_to_email = sales_order_details.get("ship_to_email")
        if not validate_sales_orders.validate_fields_under_ship_to_info(feature_file_name, screen_shot,
                                                                       ship_to_suffix, ship_to_name, ship_to_address,
                                                                        ship_to_phone, ship_to_contact, ship_to_email):
            raise Exception("Failed to verify fields under Ship to info section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Ship to info section on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under End user info section'))
def fields_under_end_user_info_section(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        im_order_number = input_order_data.get("im_order_number")
        order_number = re.findall("^.{2}\-.{5}", im_order_number)[0]
        sales_order_details = sales_order_details_srv_obj.get_order_details(db_file_path, order_number)
        end_user_id = sales_order_details.get("end_user_id")
        end_user_address = sales_order_details.get("end_user_address")
        end_user_contact = sales_order_details.get("end_user_contact")
        if not validate_sales_orders.validate_fields_under_end_user_info(feature_file_name, screen_shot,
                                                                        end_user_id, end_user_address, end_user_contact):
            raise Exception("Failed to verify fields under End user info section on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under End user info section on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Order lines tab'))
def fields_under_order_lines_tab(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        order_lines_tab_info = input_order_data.get("order_lines_tab")
        order_lines_tab_info_list = list(order_lines_tab_info.split(","))
        logger.info(order_lines_tab_info_list)
        if not validate_sales_orders.validate_fields_under_order_lines_tab(feature_file_name, screen_shot,
                                                                          order_lines_tab_info_list):
            raise Exception("Failed to verify fields under Order lines on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Order lines section on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Serial numbers view more option'))
def click_on_serial_numbers_view_more_option(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_view_more_option(feature_file_name):
            raise Exception("Failed to click on Serial numbers View more option on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Serial numbers View more option on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Serial Numbers header'))
def fields_under_serial_numbers_tab(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        serial_numbers_info = input_order_data.get("serial_numbers")
        serial_numbers_info_list = list(serial_numbers_info.split(","))
        logger.info(serial_numbers_info_list)
        if not validate_sales_orders.validate_fields_under_serial_numbers_header(feature_file_name, screen_shot,
                                                                                serial_numbers_info_list):
            raise Exception("Failed to verify fields under Serial numbers header on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Serial numbers header on Order Details page %s", e)
        raise e


@when(parsers.parse('Click on Additional attributes view more option'))
def click_on_additional_attr_view_more_option(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        if not validate_sales_orders.click_on_additional_attr_view_more_button(feature_file_name):
            raise Exception("Failed to click on Additional Attributes View more option on Order Details page")
    except Exception as e:
        logger.error("Error while clicking on Additional Attributes View more option on Order Details page %s", e)
        raise e


@then(parsers.parse('Validate fields under Additional attributes header'))
def fields_under_additional_attributes_tab(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        input_order_data = order_management_srv_obj.get_x4a_input_test_case_order_detail(
            db_file_path, feature_file_name)
        additional_attributes_info = input_order_data.get("additional_attributes")
        additional_attributes_info_list = list(additional_attributes_info.split(","))
        logger.info(additional_attributes_info_list)
        if not validate_sales_orders.validate_fields_under_additional_attribute_header(feature_file_name, screen_shot,
                                                                                      additional_attributes_info_list):
            raise Exception("Failed to verify fields under Additional attributes header on Order Details page")
    except Exception as e:
        logger.error("Error while verify the fields under Additional attributes header on Order Details page %s", e)
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "sales_order_details"
    validate_sales_orders = ValidateSalesOrdersData(init_driver)
    try:
        validate_sales_orders.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url %s", e)
        raise e


