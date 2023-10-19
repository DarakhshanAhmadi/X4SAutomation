from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from db.service.X4AInventoryDbManagementService import X4AInventoryDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateInventoryInquiryData import ValidateInventoryInquiryData
from pages.X4A.TestSteps.validateInventoryManagementData import ValidateInventoryManagementData
from tests.test_base_x4a import BaseTest

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_inventory_list = []
db_file_path = ReadConfig.get_db_file_path()
inventory_management_srv_obj = X4AInventoryDbManagementService()


@scenario("features/hardware/inventory_management_action_planning.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/inventory_management_action_planning.feature", "Verify table columns under top 100 under performing tab")
def test_verify_table_headers():
    pass


@scenario("features/hardware/inventory_management_action_planning.feature", "Verify Filter results")
def test_verify_filter_results():
    pass


@scenario("features/hardware/inventory_management_action_planning.feature", "Verify Sort results")
def test_verify_sort_results():
    pass


@scenario("features/hardware/inventory_management_action_planning.feature", "Verify Action on SKU")
def test_verify_action_on_sku():
    pass


@scenario("features/hardware/inventory_management_action_planning.feature", "Verify table columns under top 100 aging sku tab")
def test_verify_table_headers():
    pass


@scenario("features/hardware/inventory_management_action_planning.feature", "Verify Filter results for top 100 aging sku")
def test_verify_filter():
    pass


@scenario("features/hardware/inventory_management_action_planning.feature", "Verify Sort results for top 100 aging sku")
def test_verify_sort():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "inventory_management_action_planning"
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_inventory_test_data_file(), "Inventory_data")
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
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        validate_inventory_management.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@then(parsers.parse('the user traverse to Action planning under Inventory Management menu'))
def click_on_inventory_inquiry_menu(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.click_on_inventory_management_action_planning(feature_file_name, screen_shot):
            raise Exception("Failed to click on Action planning under Inventory Management menu")
    except Exception as e:
        logger.error("Error while clicking on Action planning under Inventory Management menu %s", e)
        raise e


@given(parsers.parse('click on top 100 under performing sku'))
def click_in_top_100_underperforming_sku(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.click_on_top_100_under_performing_sku(feature_file_name, screen_shot):
            raise Exception("Failed to click on Top 100 under performing sku tab")
    except Exception as e:
        logger.error("Error while clicking on Top 100 under performing sku tab %s", e)
        raise e


@then(parsers.parse('verify the columns in the table are correct'))
def verify_top_100_underperforming_sku_table_headers(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_top_100_underperforming_sku_table_headers(feature_file_name, screen_shot):
            raise Exception("Failed to validate Top 100 underperforming sku table headers")
    except Exception as e:
        logger.error("Error while validating Top 100 underperforming sku table headers %s", e)
        raise e


@then(parsers.parse('verify filter options are correct'))
def verify_top_100_underperforming_sku_filter_options(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_filter_options(feature_file_name, screen_shot):
            raise Exception("Failed to validate Top 100 underperforming sku filter options")
    except Exception as e:
        logger.error("Error while validating Top 100 underperforming sku filter options %s", e)
        raise e


@given(parsers.parse('filter by country'))
def filter_by_country(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        country = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("country")
        if not validate_inventory_management.filter_by_country(country, feature_file_name, screen_shot):
            raise Exception("Failed to filter the country")
    except Exception as e:
        logger.error("Error while filtering the country %s", e)
        raise e


@then(parsers.parse('filter by  MFN part number and validate data'))
def validate_filter_by_sku(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        mfn_part_number = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("mfn_part_number")
        if not validate_inventory_management.validate_filter_by_mfn_part_number(mfn_part_number, feature_file_name, screen_shot):
            raise Exception("Failed to validate filter by MFN part number")
    except Exception as e:
        logger.error("Error while validating filter by MFN part number %s", e)
        raise e


@then(parsers.parse('filter by sku and validate data'))
def validate_filter_by_sku(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        sku = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("sku")
        if not validate_inventory_management.validate_filter_by_sku(sku, feature_file_name, screen_shot):
            raise Exception("Failed to validate filter by sku")
    except Exception as e:
        logger.error("Error while validating filter by sku %s", e)
        raise e


@then(parsers.parse('filter by vendor business manager and validate data'))
def validate_filter_by_vendor_business_manager(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        vendor_business_manager = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("vendor_business_manager")
        if not validate_inventory_management.validate_filter_by_vendor_business_manager(vendor_business_manager, feature_file_name, screen_shot):
            raise Exception("Failed to validate filter by vendor business manager")
    except Exception as e:
        logger.error("Error while validating filter by vendor business manager %s", e)
        raise e


@then(parsers.parse('filter by vendor name and validate data'))
def validate_filter_by_vendor_name(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        vendor_name = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("vendor_name")
        if not validate_inventory_management.validate_filter_by_vendor_name(vendor_name, feature_file_name, screen_shot):
            raise Exception("Failed to validate filter by vendor name")
    except Exception as e:
        logger.error("Error while validating filter by vendor name %s", e)
        raise e


@given(parsers.parse('validate improvement opportunity is in descending by default'))
def filter_by_country(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.check_is_improvement_opportunity_is_descending_by_default(feature_file_name, screen_shot):
            raise Exception("Failed to check Improvement opportunity is descending by default")
    except Exception as e:
        logger.error("Error while checking Improvement opportunity is descending by default %s", e)
        raise e


@then(parsers.parse('sort inventory values and validate data'))
def validate_sort_inventory_value(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_sort_for_inventory_value(feature_file_name, screen_shot):
            raise Exception("Failed to validate sort for Inventory value")
    except Exception as e:
        logger.error("Error while validating sort for Inventory Value %s", e)
        raise e


@then(parsers.parse('sort value on order and validate data'))
def validate_sort_value_on_order(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_sort_for_value_on_order(feature_file_name, screen_shot):
            raise Exception("Failed to validate sort for Value on order")
    except Exception as e:
        logger.error("Error while validating sort for Value on order %s", e)
        raise e


@then(parsers.parse('sort actual 121 and validate data'))
def validate_sort_value_on_order(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_sort_for_actual_121(feature_file_name, screen_shot):
            raise Exception("Failed to validate sort for Actual 121")
    except Exception as e:
        logger.error("Error while validating sort for Actual 121 %s", e)
        raise e


@then(parsers.parse('sort actual 151 and validate data'))
def validate_sort_value_on_order(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_sort_for_actual_151(feature_file_name, screen_shot):
            raise Exception("Failed to validate sort for Actual 151")
    except Exception as e:
        logger.error("Error while validating sort for Actual 151 %s", e)
        raise e


@then(parsers.parse('sort improvement opportunity and validate data'))
def validate_sort_value_on_order(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_sort_for_improvement_opportunity(feature_file_name, screen_shot):
            raise Exception("Failed to validate sort for improvement opportunity")
    except Exception as e:
        logger.error("Error while validating sort for improvement opportunity %s", e)
        raise e


@given(parsers.parse('filter by sku'))
def filter_by_sku(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        sku = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("sku")
        if not validate_inventory_management.filter_by_sku(sku, feature_file_name, screen_shot):
            raise Exception("Failed to filter by sku")
    except Exception as e:
        logger.error("Error while filtering by sku %s", e)
        raise e


@when(parsers.parse('validate popup text and action options are correct'))
def validate_action_popup(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_action_popup_contents(feature_file_name, screen_shot):
            raise Exception("Action popup contents are incorrect")
    except Exception as e:
        logger.error("Not able to validate Action Popup contents %s", e)
        raise e


@then(parsers.parse('update the action and comment for sku'))
def validate_sort_value_on_order(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        action = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("actions")
        comment = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("comment")
        if not validate_inventory_management.update_action_and_comment(action, comment, feature_file_name, screen_shot):
            raise Exception("Failed to update Action and Comment")
    except Exception as e:
        logger.error("Error while updating Action and Comment %s", e)
        raise e


@then(parsers.parse('validate the updated action and comments are reflecting for sku'))
def validate_action_and_comment(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        action = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("actions")
        comment = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("comment")
        if not validate_inventory_management.validate_action_and_comment(action, comment, feature_file_name, screen_shot):
            raise Exception("Failed to validate Action and Comment")
    except Exception as e:
        logger.error("Error while validating Action and Comment %s", e)
        raise e


@given(parsers.parse('click on top 100 aging sku tab'))
def click_in_top_100_aging_sku(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.click_on_top_100_aging_sku_tab(feature_file_name, screen_shot):
            raise Exception("Failed to click on Top 100 aging sku tab")
    except Exception as e:
        logger.error("Error while clicking on Top 100 aging sku tab %s", e)
        raise e


@then(parsers.parse('verify the columns in top 100 aging sku table are correct'))
def verify_top_100_aging_sku_table_headers(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_top_100_aging_sku_table_headers(feature_file_name, screen_shot):
            raise Exception("Failed to validate Top 100 aging sku table headers")
    except Exception as e:
        logger.error("Error while validating Top 100 aging sku table headers %s", e)
        raise e


@then(parsers.parse('filter by sku and verify data'))
def validate_filter_by_sku(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        sku = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("aging_sku")
        if not validate_inventory_management.validate_filter_by_sku(sku, feature_file_name, screen_shot):
            raise Exception("Failed to validate filter by sku ")
    except Exception as e:
        logger.error("Error while validating filter by sku%s", e)
        raise e


@then(parsers.parse('filter by  MFN part number and verify data'))
def validate_filter_by_sku(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        mfn_part_number = inventory_management_srv_obj.get_x4a_inventory_test_case_detail(db_file_path, feature_file_name).get("aging_mfn_part_number")
        if not validate_inventory_management.validate_filter_by_mfn_part_number(mfn_part_number, feature_file_name, screen_shot):
            raise Exception("Failed to validate filter by MFN part number")
    except Exception as e:
        logger.error("Error while validating filter by MFN part number %s", e)
        raise e


@given(parsers.parse('validate actual 151 is in descending by default'))
def actual_151_sort_by_default(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_actual_151_is_descending_by_default(feature_file_name, screen_shot):
            raise Exception("Failed to validate Actual 151 is descending by default in Top 100 Aging table")
    except Exception as e:
        logger.error("Error while Actual 151 is descending by default in Top 100 Aging table %s", e)
        raise e


@then(parsers.parse('sort actual 181 and validate data'))
def validate_sort_actual_181(init_driver):
    feature_file_name = "inventory_management_action_planning"
    validate_inventory_management = ValidateInventoryManagementData(init_driver)
    try:
        if not validate_inventory_management.validate_sort_for_actual_181(feature_file_name, screen_shot):
            raise Exception("Failed to validate sort for Actual 181")
    except Exception as e:
        logger.error("Error while validating sort for Actual 181 %s", e)
        raise e