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
    create_order_steps = CreateOrder(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "sales_orders"
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
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        create_order_steps.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('the user traverse to Sales Order menu'))
def click_on_sales_orders_menu(init_driver):
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.click_on_sales_orders(feature_file_name, screen_shot):
            raise Exception("Failed to click on Sales Orders menu")
    except Exception as e:
        logger.error("Error while clicking on Sales Orders menu %s", e)
        raise e


@then(parsers.parse('verify that Sales Orders listing page visible'))
def sales_orders_listing_page_visible(init_driver):
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.is_sales_orders_listing_page_visible(feature_file_name, screen_shot):
            raise Exception("Failed to verify that Sales Orders listing page")
    except Exception as e:
        logger.error("Error while verifying that Sales Orders listing page %s", e)
        raise e


@then(parsers.parse('verify that all column should be present'))
def columns_visible_on_sales_orders_listing_page_visible(init_driver):
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.is_all_column_visible(feature_file_name, screen_shot):
            raise Exception("Failed to verify that All column on sales orders page ")
    except Exception as e:
        logger.error("Error while verifying that All column on Sales Orders page %s", e)
        raise e


@when(parsers.parse('search a order with specific IM Order number'))
def search_im_order_number(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        im_order_number = order_management_srv_obj.get_im_order_number_by_feature_file_name(db_file_path,
                                                                                            feature_file_name)
        if not create_order_steps.do_search_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to search IM Order Number")
    except Exception as e:
        logger.error("Error while searching IM Order Number %s", e)
        raise e


@then(parsers.parse('Validate the IM Order number is listed'))
def validate_im_order_number(init_driver):
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        im_order_number = order_management_srv_obj.get_im_order_number_by_feature_file_name(db_file_path,
                                                                                            feature_file_name)
        if not create_order_steps.do_validate_im_order_number(im_order_number, feature_file_name, screen_shot):
            raise Exception("Failed to Validate IM Order Number")
    except Exception as e:
        logger.error("Not able to Validate IM Order Number %s", e)
        raise e


@then(parsers.parse('Validate All orders created on date should be ascending'))
def validate_created_on_date_ascending(init_driver):
    page1 = 1
    page2 = 3
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_validate_created_on_ascending(feature_file_name, page1, page2, screen_shot):
            raise Exception("Failed to Validate All orders created on date should be a,scending")
    except Exception as e:
        logger.error("Not able to Validate All orders created on date should be ascending %s", e)
        raise e


@then(parsers.parse('Validate All orders created on date should be descending'))
def validate_created_on_date_descending(init_driver):
    page1 = 1
    page2 = 3
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    try:
        if not create_order_steps.do_validate_created_on_descending(feature_file_name, page1, page2, screen_shot):
            raise Exception("Failed to Validate All orders created on date should be descending")
    except Exception as e:
        logger.error("Not able to Validate All orders created on date should be descending %s", e)
        raise e


@when(parsers.parse('search a order with specific BCN'))
def search_bcn(init_driver):
    init_driver.refresh()
    feature_file_name = "sales_orders"
    create_order_steps = CreateOrder(init_driver)
    order_management_srv_obj = X4AInputOrderDbManagementService()
    try:
        reseller_bcn = order_management_srv_obj.get_bcn_by_feature_file_name(db_file_path, feature_file_name)
        if not create_order_steps.do_search_bcn(reseller_bcn, feature_file_name, screen_shot):
            raise Exception("Failed to search BCN")
    except Exception as e:
        logger.error("Error while searching BCN %s", e)
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
