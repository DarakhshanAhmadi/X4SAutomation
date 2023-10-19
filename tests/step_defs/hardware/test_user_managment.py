import os

from pytest_bdd import scenario, parsers, when, then, given

from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AUserDataDbManagementService import X4AUserDataDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateUserData import UserValidateData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
user_data_list = []
db_file_path = ReadConfig.get_db_file_path()
user_data_management_srv_obj = X4AUserDataDbManagementService()

user_email = ""
user_name = ""
role_db_list = []
role_list = []
associate_role = ""
country_db_list = []

@scenario("features/hardware/user_managment.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass

@scenario("features/hardware/user_managment.feature", "Search Associate details from Associate management page")
def test_search_associate_details():
    pass

@scenario("features/hardware/user_managment.feature", "Manage Associate role from Associate management page")
def test_manage_associate_roles():
    pass

@scenario("features/hardware/user_managment.feature", "Manage Associate country from Associate management page")
def test_manage_associate_country():
    pass

@scenario("features/hardware/user_managment.feature", "Deactivate Associate from Associate management page")
def test_deactivate_associate():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    user_data_steps = UserValidateData(init_driver)
    user_data_management_srv_obj = X4AUserDataDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "user_managment"
    try:
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = user_data_steps.filtered_orders_by_feature_file(test_data_order, feature_file_name)
        logger.info(filtered_order_data)
        for order_index, test_data_order in filtered_order_data.iterrows():
            user_data_list.clear()
            logger.info(test_data_order)
            x4a_user_data = prepare_obj.prepare_x4a_user_data_obj(test_data_order)
            user_data_list.append(x4a_user_data)
            user_data_management_srv_obj.save_associate_details(db_file_path, user_data_list)
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
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    try:

        User_data_steps.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a %s", e)
        raise e


@when(parsers.parse('Traverse to associate management page'))
def traverse_to_associate_management(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    try:
        if not User_data_steps.go_to_associate_management(feature_file_name, screen_shot):
            raise Exception("Failed to traverse to associate management")
    except Exception as e:
        logger.error("Error while traversing to associate management %s", e)
        raise e

@then(parsers.parse('Verify the Associate Header List'))
def verify_associate_header_list(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    try:
        if not User_data_steps.do_validate_coloumn_header(feature_file_name, screen_shot):
            raise Exception("Failed to search Associate")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while searching Associate %s", e)
        raise e

@when(parsers.parse('Open the associate detail page'))
def search_associate(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    # breakpoint()
    user_email = associate_detail_list[0][3]
    user_name = associate_detail_list[0][2]
    try:
        if not User_data_steps.do_search_associate(feature_file_name, screen_shot, user_email, user_name):
            raise Exception("Failed to search Associate")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while searching Associate %s", e)
        raise e


@then(parsers.parse('Verify that Associate is Active'))
def verify_associate_details_page(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    user_email = associate_detail_list[0][3]
    user_name = associate_detail_list[0][2]
    try:
        if not User_data_steps.do_validate_associate_page(feature_file_name, screen_shot, user_email, user_name):
            raise Exception("Failed to validate Associate details")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while validating Associate details %s", e)
        raise e

@then(parsers.parse('Verify the associates roles'))
def verify_associate_role(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    role_db_list = associate_detail_list[4].split(",")
    try:
        if not User_data_steps.do_validate_associate_role(feature_file_name, screen_shot, role_db_list):
            raise Exception("Failed to validate Associate role")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while validating Associate role %s", e)
        raise e

@then(parsers.parse('Verify associate country'))
def verify_associate_country(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    country_db_list = associate_detail_list[5].split(",")
    try:
        if not User_data_steps.do_validate_associate_country(feature_file_name, screen_shot, country_db_list):
            raise Exception("Failed to validate Associate country")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while validating Associate country %s", e)
        raise e

@when(parsers.parse('A role is deleted'))
def do_manage_associate_role(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    role_db_list = associate_detail_list[4].split(",")
    role_list = role_db_list[1].split(" - ")
    associate_role = role_list[1]
    try:
        if not User_data_steps.do_manage_associate_role(feature_file_name, screen_shot, associate_role):
            raise Exception("Failed to manage Associate role")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while managing Associate role %s", e)
        raise e

@then(parsers.parse('Verify the roles deleted properly'))
def verify_associate_role_after_deletion(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    role_db_list = associate_detail_list[4].split(",")
    try:
        if not User_data_steps.do_validate_associate_role_after_deletion(feature_file_name, screen_shot, role_db_list):
            raise Exception("Failed to validate Associate role after deletion")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while validating Associate role after deletion: %s", e)
        raise e

@when(parsers.parse('A new role is added'))
def do_add_associate_role(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    role_db_list = associate_detail_list[4].split(",")
    role_list = role_db_list[1].split(" - ")
    try:
        if not User_data_steps.do_add_associate_role(feature_file_name, screen_shot,role_list):
            raise Exception("Failed to add Associate role")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while adding Associate role %s", e)
        raise e

@when(parsers.parse('A country is deleted'))
def do_manage_associate_country(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    country_db_list = associate_detail_list[5].split(",")
    try:
        if not User_data_steps.do_manage_associate_country(feature_file_name, screen_shot,country_db_list):
            raise Exception("Failed to manage Associate country")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while managing Associate country %s", e)
        raise e

@then(parsers.parse('Verify the country deleted properly'))
def verify_associate_country_after_deletion(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    country_db_list = associate_detail_list[5].split(",")
    try:
        if not User_data_steps.do_validate_associate_country_after_deletion(feature_file_name, screen_shot,country_db_list):
            raise Exception("Failed to validate Associate country after deletion")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while validating Associate country after deletion %s", e)
        raise e

@when(parsers.parse('A new country is added'))
def do_add_associate_country(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    country_db_list = associate_detail_list[5].split(",")
    try:
        if not User_data_steps.do_add_associate_country(feature_file_name, screen_shot,country_db_list):
            raise Exception("Failed to add Associate country")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while add Associate country %s", e)
        raise e

@when(parsers.parse('Associate is deactivated'))
def do_deactivate_account(init_driver):
    feature_file_name = 'user_management'
    User_data_steps = UserValidateData(init_driver)
    try:
        if not User_data_steps.do_deactivate_account(feature_file_name, screen_shot):
            raise Exception("Failed to search Associate country")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while searching Associate country %s", e)
        raise e

@then(parsers.parse('Verify the Associate is deactivated'))
def verify_account_deactivation(init_driver):
    feature_file_name = "user_management"
    User_data_steps = UserValidateData(init_driver)
    try:
        if not User_data_steps.do_validate_account_deactivation(feature_file_name, screen_shot):
            raise Exception("Failed to validate Associate is deactivated")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while validating Associate deactivation %s", e)
        raise e

@when(parsers.parse('Associate is Activated'))
def do_activate_account(init_driver):
    feature_file_name = 'user_management'
    User_data_steps = UserValidateData(init_driver)
    try:
        if not User_data_steps.do_activate_account(feature_file_name, screen_shot):
            raise Exception("Failed to activate the account")
        init_driver.refresh()
    except Exception as e:
        logger.error("Error while activating the account %s", e)
        raise e
