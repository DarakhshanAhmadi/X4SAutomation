from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4AInventoryInquiry import X4AInventoryInquiryPage
from pages.X4A.Pages.X4AInventoryManagement import X4AInventoryManagementPage
from pages.X4A.Pages.X4ALogin import LoginPage


class ValidateInventoryManagementData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

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

    def click_on_inventory_management_action_planning(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.go_to_inventory_management_action_planning()
            self.logger.info("Successfully clicked on Action planning under Inventory Management")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_management_action_planning_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_management_action_planning_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "inventory_management_action_planning_clicking_error.png"
            self.logger.error("Error while clicking on Action planning under Inventory Management")
            self.logger.exception(e)
            return False

    def click_on_top_100_under_performing_sku(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.click_on_top_100_underperforming_sku()
            self.logger.info("Successfully clicked on Top 100 under performing sku tab")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "top_100_underperforming_tab_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "top_100_underperforming_tab_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "top_100_underperforming_tab_clicking_error.png"
            self.logger.error("Error while clicking on Top 100 under performing sku tab")
            self.logger.exception(e)
            return False