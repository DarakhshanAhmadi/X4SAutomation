import os
from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.IM360InputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateData import CreateOrder

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_input_order_list = []
db_file_path = ReadConfig.get_db_file_path()
x4a_input_order_obj = X4AInputOrderDbManagementService()


@scenario("features/hardware/aged_orders.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/aged_orders.feature", "Verify table columns and quick search options")
def test_verify_columns_and_search_options():
    pass


# @scenario("features/hardware/aged_orders.feature", "Verify quick search is giving proper results")
# def test_verify_order_number_search():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify quick search with vendor name")
# def test_verify_vendor_name_search():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify quick search with BCN account")
# def test_verify_vendor_name_search():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify quick search with Customer PO")
# def test_verify_customer_po_search():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify search with order date")
# def test_verify_order_date_search():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify search with last update date")
# def test_verify_last_update_date_search():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify filter with BCN account")
# def test_verify_filter_with_bcn():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify filter with Vendor")
# def test_verify_filter_with_bcn():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify filter with Customer name")
# def test_verify_filter_with_bcn():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify filter with Order type")
# def test_verify_filter_with_order_type():
#     pass


# @scenario("features/hardware/aged_orders.feature", "Verify filter with Order status")
# def test_verify_filter_with_order_status():
#     pass

@scenario("features/hardware/aged_orders.feature", "Verify filter with Total revenue")
def test_verify_filter_with_total_revenue():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    create_order_steps = CreateOrder(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "aged_orders"
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = create_order_steps.filtered_orders_by_feature_file(test_data_order, feature_file_name)
        logger.info(filtered_order_data)
        for order_index, test_data_order in filtered_order_data.iterrows():
            x4a_input_order_list.clear()
            logger.info(test_data_order)
            x4a_input_order_data = prepare_obj.prepare_x4a_inp_ord_data_obj(test_data_order)
            x4a_input_order_list.append(x4a_input_order_data)
            order_management_srv_obj.save_im360_input_order(db_file_path, x4a_input_order_list)
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
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        create_order_steps.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('the user traverse to Aged Order Tab'))
def click_on_aged_orders(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.click_on_aged_order(feature_file_name, screen_shot):
            raise Exception("Failed to click on aged orders")
    except Exception as e:
        logger.error("Error while clicking on aged orders %s", e)
        raise e


@then(parsers.parse('verify the columns in the table are correct'))
def check_table_columns(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.verify_aged_orders_table_columns(feature_file_name, screen_shot):
            raise Exception("Failed to verify Aged order table columns")
    except Exception as e:
        logger.error("Error while verifying Aged order table columns %s", e)
        raise e


@then(parsers.parse('Verify quick search options'))
def check_quick_search_options(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.verify_quick_search_options(feature_file_name, screen_shot):
            raise Exception("Failed to verify Aged order quick search options")
    except Exception as e:
        logger.error("Error while verifying Aged order quick search options %s", e)
        raise e


@when(parsers.parse('search IM order number'))
def search_order_number(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        order_number = x4a_input_order_obj.get_order_number_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.search_im_order_number(feature_file_name, screen_shot, order_number):
            raise Exception("Failed to search im order number")
    except Exception as e:
        logger.error("Error while searching im order number %s", e)
        raise e


@then(parsers.parse('verify the data for searched order is listed'))
def verify_search_order_number(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        order_number = x4a_input_order_obj.get_order_number_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_im_order_number_search_result(feature_file_name, screen_shot, order_number):
            raise Exception("Failed to verify im order number results")
    except Exception as e:
        logger.error("Error while verifying order number search results %s", e)
        raise e


@when(parsers.parse('search vendor name'))
def search_vendor_name(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        vendor_name = x4a_input_order_obj.get_vendor_name_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.search_vendor_name(feature_file_name, screen_shot, vendor_name):
            raise Exception("Failed to search vendor name")
    except Exception as e:
        logger.error("Error while searching vendor name %s", e)
        raise e


@then(parsers.parse('verify the data for searched vendor name is listed'))
def verify_search_vendor_name(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        vendor_name = x4a_input_order_obj.get_vendor_name_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_vendor_name_search_result(feature_file_name, screen_shot, vendor_name):
            raise Exception("Failed to verify vendor name search results")
    except Exception as e:
        logger.error("Error while verifying vendor name search results %s", e)
        raise e


@when(parsers.parse('search bcn account'))
def search_bcn_account(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        bcn_account = x4a_input_order_obj.get_bcn_account_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.search_bcn_account(feature_file_name, screen_shot, bcn_account):
            raise Exception("Failed to search BCN account")
    except Exception as e:
        logger.error("Error while searching BCN account %s", e)
        raise e


@then(parsers.parse('verify the data for searched bcn account is listed'))
def verify_search_bcn_account(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        bcn_account = x4a_input_order_obj.get_bcn_account_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_bcn_account_search_result(feature_file_name, screen_shot, bcn_account):
            raise Exception("Failed to verify BCN account search results")
    except Exception as e:
        logger.error("Error while verifying BCN account search results %s", e)
        raise e


@when(parsers.parse('search customer po'))
def search_customer_po(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        customer_po = x4a_input_order_obj.get_customer_po_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.search_customer_po(feature_file_name, screen_shot, customer_po):
            raise Exception("Failed to search Customer PO")
    except Exception as e:
        logger.error("Error while searching Customer PO %s", e)
        raise e


@then(parsers.parse('verify the data for searched customer po is listed'))
def verify_search_customer_po(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        customer_po = x4a_input_order_obj.get_customer_po_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_customer_po_search_result(feature_file_name, screen_shot, customer_po):
            raise Exception("Failed to verify Customer PO search results")
    except Exception as e:
        logger.error("Error while verifying Customer PO search results %s", e)
        raise e


@when(parsers.parse('select order date range'))
def select_order_date(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.select_order_date_range(feature_file_name, screen_shot):
            raise Exception("Failed to search order date")
    except Exception as e:
        logger.error("Error while searching order date %s", e)
        raise e


@then(parsers.parse('verify the date for searched order date is listed'))
def verify_search_order_date(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.verify_order_date_search(feature_file_name, screen_shot):
            raise Exception("Failed to verify order date search results")
    except Exception as e:
        logger.error("Error while verifying order datesearch results %s", e)
        raise e


@when(parsers.parse('select last update date range'))
def select_last_update_date(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.select_last_updated_date_range(feature_file_name, screen_shot):
            raise Exception("Failed to search last updated date")
    except Exception as e:
        logger.error("Error while searching last updated date %s", e)
        raise e


@then(parsers.parse('verify the date for searched last update date is listed'))
def verify_search_last_update_date(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.verify_last_update_date_search(feature_file_name, screen_shot):
            raise Exception("Failed to verify last update date search results")
    except Exception as e:
        logger.error("Error while verifying last update datesearch results %s", e)
        raise e


@when(parsers.parse('filter with bcn'))
def filter_bcn_account(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        bcn_account = x4a_input_order_obj.get_bcn_account_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.filter_by_bcn(feature_file_name, screen_shot, bcn_account):
            raise Exception("Failed to search BCN account")
    except Exception as e:
        logger.error("Error while searching BCN account %s", e)
        raise e


@then(parsers.parse('verify the data for filtered bcn account is listed'))
def verify_filter_by_bcn(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        bcn_account = x4a_input_order_obj.get_bcn_account_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_filter_by_bcn(feature_file_name, screen_shot, bcn_account):
            raise Exception("Failed to verify filter by bcn results")
    except Exception as e:
        logger.error("Error while verifying filter by bcn results %s", e)
        raise e


@when(parsers.parse('filter with vendor'))
def filter_bcn_account(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        vendor_name = x4a_input_order_obj.get_vendor_name_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.filter_by_vendor(feature_file_name, screen_shot, vendor_name):
            raise Exception("Failed to filter by Vendor")
    except Exception as e:
        logger.error("Error while filtering by Vendor %s", e)
        raise e


@then(parsers.parse('verify the data for filtered vendor is listed'))
def verify_filter_by_bcn(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        vendor_name = x4a_input_order_obj.get_vendor_name_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_filter_by_vendor(feature_file_name, screen_shot, vendor_name):
            raise Exception("Failed to verify filter by vendor results")
    except Exception as e:
        logger.error("Error while verifying filter by vendor results %s", e)
        raise e


@when(parsers.parse('filter with customer name'))
def filter_customer_name(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        vendor_name = x4a_input_order_obj.get_customer_name_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.filter_by_customer_name(feature_file_name, screen_shot, vendor_name):
            raise Exception("Failed to filter by Customer name")
    except Exception as e:
        logger.error("Error while filtering by Customer name %s", e)
        raise e


@then(parsers.parse('verify the data for filtered customer name is listed'))
def verify_filter_by_customer_name(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        vendor_name = x4a_input_order_obj.get_customer_name_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_filter_by_customer_name(feature_file_name, screen_shot, vendor_name):
            raise Exception("Failed to verify filter by customer name results")
    except Exception as e:
        logger.error("Error while verifying filter by customer name results %s", e)
        raise e


@when(parsers.parse('filter with order type'))
def filter_by_order_type(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        order_type = x4a_input_order_obj.get_order_type_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.filter_by_order_type(feature_file_name, screen_shot, order_type):
            raise Exception("Failed to filter by Order type")
    except Exception as e:
        logger.error("Error while filtering by Order type %s", e)
        raise e


@then(parsers.parse('verify the data for filtered order type is listed'))
def verify_filter_by_order_type(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        order_type = x4a_input_order_obj.get_order_type_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_filter_by_order_type(feature_file_name, screen_shot, order_type):
            raise Exception("Failed to verify filter by order type results")
    except Exception as e:
        logger.error("Error while verifying filter by order type  results %s", e)
        raise e


@when(parsers.parse('filter with order status'))
def filter_by_order_status(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        order_status = x4a_input_order_obj.get_order_status_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.filter_by_order_status(feature_file_name, screen_shot, order_status):
            raise Exception("Failed to filter by Order status")
    except Exception as e:
        logger.error("Error while filtering by Order status %s", e)
        raise e


@then(parsers.parse('verify the data for filtered order status is listed'))
def verify_filter_by_order_status(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        order_status = x4a_input_order_obj.get_order_status_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.verify_filter_by_order_status(feature_file_name, screen_shot, order_status):
            raise Exception("Failed to verify filter by order status results")
    except Exception as e:
        logger.error("Error while verifying filter by order status  results %s", e)
        raise e


@when(parsers.parse('filter with total revenue'))
def filter_by_total_revenue(init_driver):
    feature_file_name = "aged_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        min_total_revenue = x4a_input_order_obj.get_min_total_revenue_by_feature_file_name(db_file_path, feature_file_name)
        max_total_revenue = x4a_input_order_obj.get_max_total_revenue_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.filter_by_total_revenue(feature_file_name, screen_shot, min_total_revenue, max_total_revenue):
            raise Exception("Failed to filter by Total revenue")
    except Exception as e:
        logger.error("Error while filtering by Total revenue %s", e)
        raise e
