import time

from selenium.webdriver.common.by import By

from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AUserDataDbManagementService import X4AUserDataDbManagementService
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4AUserManagement import X4AUserManagementPage


class UserValidateData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

    """constructor of the UserValidateData Page class"""

    def __init__(self, driver):
        self.driver = driver

    def login(self, feature_file_name, screen_shot):
        clear_browser_and_cache = BrowserSettings(self.driver)
        clear_browser_and_cache.do_clear_browser_history_and_cache()
        login = LoginPage(self.driver)
        
        try:
            environment = self.parse_config_json.get_data_from_config_json("environment", "environment_type",
                                                                           "config.json")
            if environment == 'Stage':
                username = self.parse_config_json.get_data_from_config_json("x4aStageCredentials", "username",
                                                                            "config.json")
                password = self.parse_config_json.get_data_from_config_json("x4aStageCredentials", "enc_password",
                                                                            "config.json")
            else:
                username = self.parse_config_json.get_data_from_config_json("x4aBetaCredentials", "username",
                                                                            "config.json")
                password = self.parse_config_json.get_data_from_config_json("x4aBetaCredentials", "enc_password",
                                                                            "config.json")
            login.do_login_to_x4a(username, password)
            self.logger.info("Successfully logged in to X4A")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "login_successful.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "login_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "login_error.png"
            self.logger.error("Login unsuccessful!!")
            self.logger.exception(e)
            raise e


    """ This method filters order by feature file name and returns order data """
    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data

    def go_to_associate_management(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            x4a_associate_management.go_to_associate_management()
            self.logger.info("Successfully traverse to associate management")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "associate_management_traverse_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "associate_management_traverse_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "associate_management_traverse_error.png"
            self.logger.error("Error while traversing to associate management")
            self.logger.exception(e)
            return False

    def do_search_associate(self, feature_file_name, screen_shot, user_email, user_name):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            x4a_associate_management.do_search_associate(user_email, user_name)
            self.logger.info("Successfully searched Associate")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "searched_Associate_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Associate_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_Associate_error.png"
            self.logger.error("Error while searching Associate")
            self.logger.exception(e)
            return False
    def do_validate_coloumn_header(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            x4a_associate_management.do_validate_coloumn_header()
            self.logger.info("Successfully validated coloumn header")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "validate_coloumn_header_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validate_coloumn_header_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "validate_coloumn_header_error.png"
            self.logger.error("Error while validating coloumn header")
            self.logger.exception(e)
            return False

    def do_validate_associate_page(self, feature_file_name, screen_shot, user_email, user_name):
        x4a_associate_management = X4AUserManagementPage(self.driver)

        try:
            user_status = 'Activated'
            status = x4a_associate_management.do_validate_associate_page(user_status, user_email, user_name)
            if status:
                self.logger.info("Successfully validating associate page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "validate_associate_page_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validate_associate_page_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "validate_associate_page_error.png"
            self.logger.error("Error while validating associate page")
            self.logger.exception(e)
            return False
            
    def do_validate_associate_role(self, feature_file_name, screen_shot, role_db_list):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            status = x4a_associate_management.do_validate_associate_role(role_db_list)
            if status:
                self.logger.info("Successfully validate Associate role")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "validate_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validated_Associate_role_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "validate_Associate_role_error.png"
            self.logger.error("Error while validating Associate role")
            self.logger.exception(e)
            return False

    def do_validate_associate_country(self, feature_file_name, screen_shot, country_db_list):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            status = x4a_associate_management.do_validate_associate_country(country_db_list)
            if status:
                self.logger.info("Successfully validated Associate country")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "validated_Associate_country_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validated_Associate_country_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "validated_Associate_country_error.png"
            self.logger.error("Error while validating Associate country")
            self.logger.exception(e)
            return False

    def do_manage_associate_role(self, feature_file_name, screen_shot, associate_role):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            status = x4a_associate_management.do_manage_associate_role(associate_role)
            if status:
                self.logger.info("Successfully accessed manage option in Associate role")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "manage_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "manage_Associate_role_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "manage_Associate_role_error.png"
            self.logger.error("Error while managing Associate roles")
            self.logger.exception(e)
            return False

    def do_validate_associate_role_after_deletion(self, feature_file_name, screen_shot,role_db_list):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            status = x4a_associate_management.do_validate_associate_role_after_deletion(role_db_list)
            if status:
                self.logger.info("Successfully validated Associate after role deletion")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "validated_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validated_Associate_role_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "validated_Associate_role_error.png"
            self.logger.error("Error while validating Associate after role deletion")
            self.logger.exception(e)
            return False

    def do_add_associate_role(self, feature_file_name, screen_shot, role_list):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:

            status = x4a_associate_management.do_add_associate_role(role_list)
            if status:
                self.logger.info("Successfully added Associate role")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "add_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "add_Associate_role_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "add_Associate_role_error.png"
            self.logger.error("Error while adding Associate role")
            self.logger.exception(e)
            return False

    def do_manage_associate_country(self, feature_file_name, screen_shot, country_db_list):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            status = x4a_associate_management.do_manage_associate_country(country_db_list)
            if status:
                self.logger.info("Successfully accessed manage option in Associate country")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "manage_Associate_country_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "manage_Associate_country_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "manage_Associate_country_error.png"
            self.logger.error("Error while managing Associate country")
            self.logger.exception(e)
            return False

    def do_validate_associate_country_after_deletion(self, feature_file_name, screen_shot, country_db_list):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:

            status = x4a_associate_management.do_validate_associate_country_after_deletion(country_db_list)
            if status:
                self.logger.info("Successfully validated Associate after country deletion")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "validated_Associate_after_country_deletion_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validated_Associate_after_country_deletion_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "validated_Associate_after_country_deletion_error.png"
            self.logger.error("Error while validating Associate after country deletion")
            self.logger.exception(e)
            return False

    def do_add_associate_country(self, feature_file_name, screen_shot,country_db_list):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            status = x4a_associate_management.do_add_associate_country(country_db_list)
            if status:
                self.logger.info("Successfully added Associate country")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "add_Associate_country_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "add_Associate_country_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "add_Associate_country_error.png"
            self.logger.error("Error while adding Associate country")
            self.logger.exception(e)
            return False

    def do_validate_account_deactivation(self, feature_file_name, screen_shot, user_email, user_name):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            user_status = 'Deactivated'
            status = x4a_associate_management.do_validate_associate_page(user_status, user_email, user_name)
            if status:
                self.logger.info("Successfully validated Associate is deactivated")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "validate_Associate_deactivation_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validate_Associate_deactivation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "validate_Associate_deactivation_error.png"
            self.logger.error("Error while validating Associate's deactivation")
            self.logger.exception(e)
            return False

    def do_deactivate_account(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            status = x4a_associate_management.do_deactivate_account()
            if status:
                self.logger.info("Successfully deactivated account")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "deactivate_account_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "deactivate_account_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "deactivate_account_error.png"
            self.logger.error("Error while deactivating account")
            self.logger.exception(e)
            return False

    def do_activate_account(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            
            status = x4a_associate_management.do_activate_account()
            if status:
                self.logger.info("Successfully activated account")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "activate_account_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "activate_account_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "activate_account_error.png"
            self.logger.error("Error while activating account")
            self.logger.exception(e)
            return False

