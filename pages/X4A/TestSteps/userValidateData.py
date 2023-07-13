import time

from selenium.webdriver.common.by import By

from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AUserDataDbManagementService import X4AUserDataDbManagementService
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4AOrdersAgedOrders import X4AAgedOrdersPage
from pages.X4A.Pages.X4AOrdersSalesOrders import X4ASalesOrdersPage
from pages.X4A.Pages.X4AUserManagement import X4AUserManagementPage


class UserValidateData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

    """constructor of the createOrder Page class"""

    def __init__(self, driver):
        self.driver = driver

    def login(self, feature_file_name, screen_shot):
        clear_browser_and_cache = BrowserSettings(self.driver)
        clear_browser_and_cache.do_clear_browser_history_and_cache()
        login = LoginPage(self.driver)
        # breakpoint()
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

    def click_on_sales_order(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.do_click_on_sales_order()
            self.logger.info("Successfully clicked on sales order")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "sales_order_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "sales_order_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "sales_order_clicking_error.png"
            self.logger.error("Error while clicking on sales order")
            self.logger.exception(e)
            return False

    def click_on_aged_order(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            x4a_aged_order.go_to_aged_orders()
            self.logger.info("Successfully clicked on aged orders")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "aged_orders_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "aged_orders_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "aged_orders_clicking_error.png"
            self.logger.error("Error while clicking on aged orders")
            self.logger.exception(e)
            return False

    """ This method filters order by feature file name and returns order data """
    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data

    def click_on_administration_associate_management(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            x4a_associate_management.go_to_associate_management()
            self.logger.info("Successfully clicked on aged orders")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "aged_orders_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "aged_orders_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "aged_orders_clicking_error.png"
            self.logger.error("Error while clicking on aged orders")
            self.logger.exception(e)
            return False

    def do_search_associate(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            x4a_associate_management.do_search_associate()
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

    def do_validate_associate_page(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)

        try:
            # breakpoint()
            user_status = 'Activated'
            status = x4a_associate_management.do_validate_associate_page(user_status)
            if status:
                self.logger.info("Successfully searched Associate role")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "searched_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Associate_role_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_Associate_role_error.png"
            self.logger.error("Error while searching Associate role")
            self.logger.exception(e)
            return False
            # breakpoint()
    def do_validate_associate_role(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            status = x4a_associate_management.do_validate_associate_role()
            if status:
                self.logger.info("Successfully searched Associate role")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "searched_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Associate_role_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_Associate_role_error.png"
            self.logger.error("Error while searching Associate role")
            self.logger.exception(e)
            return False

    def do_validate_associate_role_after_deletion(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            status = x4a_associate_management.do_validate_associate_role_after_deletion()
            if status:
                self.logger.info("Successfully validated Associate role")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "searched_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Associate_role_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_Associate_role_error.png"
            self.logger.error("Error while searching Associate role")
            self.logger.exception(e)
            return False

    def do_validate_associate_country(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            status = x4a_associate_management.do_validate_associate_country()
            if status:
                self.logger.info("Successfully searched Associate country")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "searched_Associate_country_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Associate_country_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_Associate_country_error.png"
            self.logger.error("Error while searching Associate country")
            self.logger.exception(e)
            return False

    def do_validate_associate_country_after_deletion(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            status = x4a_associate_management.do_validate_associate_country_after_deletion()
            if status:
                self.logger.info("Successfully searched Associate country")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "searched_Associate_country_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Associate_country_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_Associate_country_error.png"
            self.logger.error("Error while searching Associate country")
            self.logger.exception(e)
            return False

    def do_manage_associate_role(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            status = x4a_associate_management.do_manage_associate_role()
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
            self.logger.error("Error while searching Associate country")
            self.logger.exception(e)
            return False

    def do_add_associate_role(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            status = x4a_associate_management.do_add_associate_role()
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

    def do_manage_associate_country(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            status = x4a_associate_management.do_manage_associate_country()
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
            self.logger.error("Error while searching Associate country")
            self.logger.exception(e)
            return False

    def do_add_associate_country(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            status = x4a_associate_management.do_add_associate_country()
            if status:
                self.logger.info("Successfully added Associate country")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "add_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "add_Associate_country_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "add_Associate_country_error.png"
            self.logger.error("Error while adding Associate country")
            self.logger.exception(e)
            return False

    def do_validate_account_deactivation(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
            user_status = 'Deactivated'
            status = x4a_associate_management.do_validate_associate_page(user_status)
            if status:
                self.logger.info("Successfully searched Associate role")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "searched_Associate_role_successfully.png")
            return status
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Associate_role_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_Associate_role_error.png"
            self.logger.error("Error while searching Associate role")
            self.logger.exception(e)
            return False
    def do_deactivate_account(self, feature_file_name, screen_shot):
        x4a_associate_management = X4AUserManagementPage(self.driver)
        try:
            # breakpoint()
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
            # breakpoint()
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

