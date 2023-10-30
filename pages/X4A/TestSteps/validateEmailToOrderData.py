import glob
import os
import time
from pathlib import Path

from openpyxl.reader.excel import load_workbook

from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4AEmailToOrder import X4AEmailToOrderPage


class ValidateEmailToOrderData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()
    mandatory_template_fields = ["Operator ID", "Country Code", "Order Type", "Reseller PO#", "Carrier Code", "Ingram SKU", "Qty"]
    template_column = []
    """constructor of the createOrder Page class"""

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
                                        + "_login_successful.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_login_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_login_error.png"
            self.logger.error("Login unsuccessful!!")
            self.logger.exception(e)
            raise e

    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data

    def click_on_email_to_order_menu(self, feature_file_name, screen_shot):
        x4a_email_to_order = X4AEmailToOrderPage(self.driver)
        try:
            x4a_email_to_order.go_to_email_to_order()
            self.logger.info("Successfully clicked on email to order")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_email_to_order_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_email_to_order_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_email_to_order_clicking_error.png"
            self.logger.error("Error while clicking on error order")
            self.logger.exception(e)
            return False

    def verify_email_to_order_page(self, feature_file_name, screen_shot):
        x4a_email_to_order = X4AEmailToOrderPage(self.driver)
        try:
            x4a_email_to_order.verify_email_to_order_page()
            self.logger.info("Successfully verified Email Orders page")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_Email_to_order_clicked_verified.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_Email_to_order_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_Email_to_order_verified_error.png"
            self.logger.error("Error while verifying on Email Orders page")
            self.logger.exception(e)
            return False

    def do_eto_select_order(self, feature_file_name, screen_shot):
        x4a_email_to_order = X4AEmailToOrderPage(self.driver)
        try:
            x4a_email_to_order.do_eto_select_order()
            self.logger.info("Successfully selected ETO order")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_ETO_order_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_ETO_order_selecting_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_ETO_order_selecting_error.png"
            self.logger.error("Error while selecting ETO order")
            self.logger.exception(e)
            return False

    def verify_ETO_order_page_haeder(self, feature_file_name, screen_shot):
        x4a_email_to_order = X4AEmailToOrderPage(self.driver)
        try:
            x4a_email_to_order.verify_ETO_order_page_haeder()
            self.logger.info("Successfully verified ETO order page headers")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_ETO_order_page_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_ETO_order_page_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_ETO_order_page_verified_error.png"
            self.logger.error("Error while verifying on ETO order page %s" + str(e))

    def logout_x4a_url(self, feature_file_name):
        x4a_email_to_order = X4AEmailToOrderPage(self.driver)
        try:
            if not x4a_email_to_order.logout_x4a():
                self.logger.info("Failed to Logout X4A url")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_logout_x4a_failed.png")
                return False
            else:
                self.logger.info("Successfully Logout X4A url")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_logout_x4a_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Logout the X4A url")
            self.logger.exception(e)
            return False
