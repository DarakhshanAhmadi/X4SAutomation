from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AInventoryDbManagementService import X4AInventoryDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateInventoryInquiryData import ValidateInventoryInquiryData
from tests.test_base_x4a import BaseTest

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_inventory_list = []
db_file_path = ReadConfig.get_db_file_path()
inventory_management_srv_obj = X4AInventoryDbManagementService()


@scenario("features/hardware/inventory_inquiry.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/inventory_inquiry.feature", "Verify table columns and quick search options")
def test_verify_columns_and_search_options():
    pass


@scenario("features/hardware/inventory_inquiry.feature", "Verify search")
def test_verify_search():
    pass


@scenario("features/hardware/inventory_inquiry.feature", "Verify customer selection in list page")
def test_verify_customer_selection_in_list_page():
    pass


@scenario("features/hardware/inventory_inquiry.feature", "Verify customer selection in details page")
def test_verify_customer_selection_in_details_page():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "inventory_inquiry"
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_inventory_test_data_file(),
                                                                     "Inventory_data")
        filtered_data = BaseTest().filtered_orders_by_feature_file(test_data_order, feature_file_name)
        logger.info(filtered_data)
        for order_index, test_data_order in filtered_data.iterrows():
            x4a_inventory_list.clear()
            logger.info(test_data_order)
            x4a_inventory_data = prepare_obj.prepare_x4a_inventory_data_obj(test_data_order)
            x4a_inventory_list.append(x4a_inventory_data)
            inventory_management_srv_obj.save_x4a_inventory_data(db_file_path, x4a_inventory_list)
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


@when(parsers.parse('provide user ID and Password to login'))
def login(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        validate_inventory_inquiry.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@then(parsers.parse('the user traverse to Inventory Inquiry menu'))
def click_on_inventory_inquiry_menu(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.click_on_inventory_inquiry(feature_file_name, screen_shot):
            raise Exception("Failed to click on Inventory Inquiry menu")
    except Exception as e:
        logger.error("Error while clicking on Inventory Inquiry menu %s", e)
        raise e


@then(parsers.parse('verify the columns in the table are correct'))
def check_table_columns(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.verify_inventory_inquiry_table_columns(feature_file_name, screen_shot):
            raise Exception("Failed to verify Inventory Inquiry table columns")
    except Exception as e:
        logger.error("Error while verifying Inventory Inquiry table columns %s", e)
        raise e


@when(parsers.parse('search a sku'))
def search_sku(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        sku = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("under_performing_sku")
        if not validate_inventory_inquiry.search(sku, feature_file_name, screen_shot):
            raise Exception("Failed to search in Inventory inquiry listing")
    except Exception as e:
        logger.error("Not able to search %s", e)
        raise e


@then(parsers.parse('Verify search result'))
def verify_search_result(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        sku = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get( "under_performing_sku")
        if not validate_inventory_inquiry.verify_sku_search_result(sku, feature_file_name, screen_shot):
            raise Exception("Failed to verify Inventory Inquiry search result")
    except Exception as e:
        logger.error("Error while verifying Inventory Inquiry search result %s", e)
        raise e


@given(parsers.parse('verify reseller price is empty and no customer present by default'))
def verify_reseller_is_empty(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.validate_reseller_price_is_empty_and_no_customer_by_default(feature_file_name, screen_shot):
            raise Exception("Failed to validate reseller price is empty by default")
    except Exception as e:
        logger.error("Not able to verify Reseller price is empty by default %s", e)
        raise e


@then(parsers.parse('verify reseller price is populated'))
def verify_reseller_is_not_empty(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.validate_reseller_price_is_not_empty(feature_file_name, screen_shot):
            raise Exception("Failed to validate Reseller price are not empty")
    except Exception as e:
        logger.error("Not able to verify Reseller price is not empty %s", e)
        raise e


@given(parsers.parse('verify customer selection popup contents'))
def verify_customer_select_popup(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.verify_customer_selection_popup_contents(feature_file_name, screen_shot):
            raise Exception("Failed to validate customer selection popup contents")
    except Exception as e:
        logger.error("Not able to verify Customer selection popup contents %s", e)
        raise e


@given(parsers.parse('verify customer selection skip functionality'))
def verify_customer_select_popup(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        customer = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("customer")
        if not validate_inventory_inquiry.validate_customer_select_skip_functionality(customer, feature_file_name, screen_shot):
            raise Exception("Failed to validate customer selection skip")
    except Exception as e:
        logger.error("Not able to verify Customer selection popup skip functionality %s", e)
        raise e


@when(parsers.parse('verify customer selection'))
def verify_customer_select_popup(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        customer = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("customer")
        if not validate_inventory_inquiry.validate_customer_selection(customer, feature_file_name, screen_shot):
            raise Exception("Failed to validate customer selection")
    except Exception as e:
        logger.error("Not able to verify Customer selection %s", e)
        raise e


@then(parsers.parse('go to details page and validate selected customer is displayed'))
def search_and_go_to_details(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        sku = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("under_performing_sku")
        customer = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("edit_customer")
        if not validate_inventory_inquiry.go_to_details_page_and_validate_customer(sku, customer, feature_file_name, screen_shot):
            raise Exception("Failed to go to sku details page and validate data")
    except Exception as e:
        logger.error("Not able to go to sku details page and validate data %s", e)
        raise e


@then(parsers.parse('edit customer and verify'))
def search_and_go_to_details(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        customer = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("edit_customer")
        if not validate_inventory_inquiry.edit_customer_and_validate_data(customer, feature_file_name, screen_shot):
            raise Exception("failed to edit customer and validate data")
    except Exception as e:
        logger.error("Not able to edit customer and validate data %s", e)
        raise e


@given(parsers.parse('the user traverse to Inventory Inquiry list page'))
def verify_customer_select_popup(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.go_to_list_page_from_details_page(feature_file_name, screen_shot):
            raise Exception("Failed to go to inventory inquiry page")
    except Exception as e:
        logger.error("Not able to traverse to inventory inquiry listing page %s", e)
        raise e


@given(parsers.parse('verify no data present under inventory visibility'))
def verify_customer_select_popup(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.validate_inventory_visibility_data_not_present(feature_file_name, screen_shot):
            raise Exception("Failed to validate no inventory visibility data present in details page")
    except Exception as e:
        logger.error("Not able to validate no inventory visibility data present in details page %s", e)
        raise e


@then(parsers.parse('verify data present under inventory visibility'))
def verify_customer_select_popup(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        if not validate_inventory_inquiry.validate_inventory_visibility_data_present(feature_file_name, screen_shot):
            raise Exception("Failed to validate inventory visibility data present in details page")
    except Exception as e:
        logger.error("Not able to validate inventory visibility data present in details page %s", e)
        raise e


@given(parsers.parse('search sku and go to details page'))
def search_and_go_to_details(init_driver):
    feature_file_name = "inventory_inquiry"
    validate_inventory_inquiry = ValidateInventoryInquiryData(init_driver)
    try:
        sku = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("under_performing_sku")
        if not validate_inventory_inquiry.search_and_go_to_sku_details(sku, feature_file_name, screen_shot):
            raise Exception("Failed to go to sku details page and validate data")
    except Exception as e:
        logger.error("Not able to go to sku details page and validate data %s", e)
        raise e
