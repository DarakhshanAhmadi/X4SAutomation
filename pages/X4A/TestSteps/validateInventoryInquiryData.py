from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4AInventoryInquiry import X4AInventoryInquiryPage
from pages.X4A.Pages.X4ALogin import LoginPage


class ValidateInventoryInquiryData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()
    inventory_inquiry_table_headers = ['SKU#', 'Description', 'VPN#', 'UPC', 'Vendor', 'Language', 'CLASS', 'Restricted Code', 'Available Qty', 'Status', 'MSRP', 'ACOP', 'Reseller Price', 'Vendor Message', 'Vendor Code']

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

    def click_on_inventory_inquiry(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.go_to_inventory_inquiry()
            self.logger.info("Successfully clicked on Inventory Inquiry")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_inquiry_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_inquiry_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "inventory_inquiry_clicking_error.png"
            self.logger.error("Error while clicking on inventory inquiry")
            self.logger.exception(e)
            return False


    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data

    def verify_inventory_inquiry_table_columns(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            self.logger.info("Verifying the Inventory Inquiry table headers are correct")
            inventory_inquiry_columns = x4a_inventory_inquiry.get_table_column_header()
            for column in self.inventory_inquiry_table_headers:
                if column not in inventory_inquiry_columns:
                    raise Exception("Column %s missing in Inventory Inquiry table", column)
            self.logger.info("Successfully verified columns in Inventory Inquiry table")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_inquiry_columns_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_inquiry_columns_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "inventory_inquiry_columns_error.png"
            self.logger.error("Error while verifying columns in Inventory Inquiry table")
            self.logger.exception(e)
            return False
