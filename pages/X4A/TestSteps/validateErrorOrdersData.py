from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4AOrdersErrorOrders import X4AErrorOrdersPage


class ValidateErrorOrdersData:
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
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_login_error.png"
            self.logger.error("Login unsuccessful!!")
            self.logger.exception(e)
            raise e

    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data

    def click_on_error_orders(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.go_to_error_orders()
            self.logger.info("Successfully clicked on error order")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_error_order_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_error_order_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_error_order_clicking_error.png"
            self.logger.error("Error while clicking on error order")
            self.logger.exception(e)
            return False

    def select_multiple_record(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.select_multiple_record()
            self.logger.info("Successfully selected the multiple record")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_multiple_record_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_sales_orders_listing_page_visible_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_multiple_record_selected_error.png"
            self.logger.error("Error while selecting the multiple record")
            self.logger.exception(e)
            return False

    def single_record_list(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.single_record_list()
            self.logger.info("Successfully verified that cancel button is disabled")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_sales_orders_listing_page_visible_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_sales_orders_listing_page_visible_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_sales_orders_listing_page_visible_error.png"
            self.logger.error("Error while verifying Sales Orders Listing Page")
            self.logger.exception(e)
            return False

    def do_verify_cancel_button(self, feature_file_name, screen_shot, status):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_verify_cancel_button(status)
            self.logger.info("Successfully verified cancel button")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_multiple_record_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_multiple_record_selected_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_multiple_record_selected_error.png"
            self.logger.error("Error while verifing cancel button")
            self.logger.exception(e)
            return False

    def do_click_cancel_button(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_click_cancel_button()
            self.logger.info("Successfully ,clicked the cancel button")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_click_cancel_button_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_click_cancel_button_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_click_cancel_button_error.png"
            self.logger.error("Error while clicking the cancel button")
            self.logger.exception(e)
            return False

    def do_verify_cancel_order_popup(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_verify_cancel_order_popup()
            self.logger.info("Successfully verified cancel order popup")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_cancel_order_popup_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_cancel_order_popup_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_cancel_order_popup_verify_error.png"
            self.logger.error("Error while verifing cancel order popup")
            self.logger.exception(e)
            return False

    def do_click_no_cancel_button(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_click_no_cancel_button()
            self.logger.info("Successfully ,clicked No button of cancel order popup")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_click_cancel_NO_button_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_click_cancel_NO_button_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_click_cancel_NO_button_error.png"
            self.logger.error("Error while clicking No button of cancel order popup")
            self.logger.exception(e)
            return False

    def do_verify_error_details_page(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_verify_error_details_page()
            self.logger.info("Successfully verified cancel order popup is closed")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_cancel_order_popup_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_cancel_order_popup_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_cancel_order_popup_verify_error.png"
            self.logger.error("Error while verifing cancel order popup is closed")
            self.logger.exception(e)
            return False

    def do_click_yes_cancel_button(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_click_yes_cancel_button()
            self.logger.info("Successfully clicked yes Cancel button")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_yes_cancel_order_popup_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_yes_cancel_order_popup_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_yes_cancel_order_popup_verify_error.png"
            self.logger.error("Error while clicked yes Cancel button")
            self.logger.exception(e)
            return False

    def verify_cancel_order_popup_after_yes(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.verify_cancel_order_popup_after_yes()
            self.logger.info("Successfully verified cancel order popup after yes")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_yes_cancel_order_popup_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_yes_cancel_order_popup_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_yes_cancel_order_popup_verify_error.png"
            self.logger.error("Error while verified cancel order popup after yes")
            self.logger.exception(e)
            return False

    def do_click_back_cancel_button(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_click_back_cancel_button()
            self.logger.info("Successfully clicked back Cancel button")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_back_cancel_order_popup_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_back_cancel_order_popup_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_back_cancel_order_popup_verify_error.png"
            self.logger.error("Error while clicked back Cancel button")
            self.logger.exception(e)
            return False

    def do_cancel_order_without_reason(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_cancel_order_without_reason()
            self.logger.info("Successfully clicked cancel order without reason")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_yes_cancel_order_popup_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_yes_cancel_order_popup_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_yes_cancel_order_popup_verify_error.png"
            self.logger.error("Error while clicking cancel order without reason")
            self.logger.exception(e)
            return False

    def do_verify_cancel_order_message(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_verify_cancel_order_message()
            self.logger.info("Successfully verified cancel order message")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_cancel_order_message_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_cancel_order_message_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_cancel_order_message_verify_error.png"
            self.logger.error("Error while verified cancel order message")
            self.logger.exception(e)
            return False

    def do_cancel_order_with_reason(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_cancel_order_with_reason()
            self.logger.info("Successfully canceled order with reason")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_cancel_order_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_cancel_order_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_cancel_order_verify_error.png"
            self.logger.error("Error while canceled order with reason")
            self.logger.exception(e)
            return False

    def do_cancel_order_success_message(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            x4a_error_order.do_cancel_order_success_message()
            self.logger.info("Successfully verified cancel order message")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_cancel_order_message_verify_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_cancel_order_message_verify_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_cancel_order_message_verify_error.png"
            self.logger.error("Error while verified cancel order message")
            self.logger.exception(e)
            return False

    def logout_x4a_url(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.logout_x4a():
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

    def is_fraud_orders_tab_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_fraud_orders_tab():
                self.logger.error("Failed to verify Fraud Orders tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_fraud_orders_tab_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Fraud Orders tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_fraud_orders_tab_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def search_and_select_order(self, feature_file_name, confirmation_id):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_search_and_select_order(confirmation_id):
                self.logger.error("Failed to Search and Select Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_select_order_record_failed.png")
                return False
            else:
                self.logger.info("Successfully Searched and Select Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_select_order_record_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def is_reprocess_order_button_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_reprocess_order_button():
                self.logger.error("Failed to verify Reprocess Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_fraud_reprocess_order_button_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Reprocess Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_fraud_reprocess_order_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_reprocess_order_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_reprocess_order_button():
                self.logger.error("Failed to verify Reprocess Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_fraud_reprocess_order_button_failed.png")
                return False
            else:
                self.logger.info("Successfully ,clicked the cancel button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_fraud_reprocess_order_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_reprocess_order_popup(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_reprocess_order_popup():
                self.logger.error("Failed to verify Reprocess Order order popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_reprocess_order_popup_failed.png")
                return False
            else:
                self.logger.info("Successfully verified Reprocess Order order popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_reprocess_order_popup_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_reprocess_order_review_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_Reprocess_Order_Review_button():
                self.logger.error("Failed to click on Reprocess Order Review button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_click_review_button_error.png")
                return False
            else:
                self.logger.info("Successfully clicked on Reprocess Order Review button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_review_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_details_page(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_details_page():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_order_details_page_verify_error.png")
                self.logger.error("Error while verifing Order Details Page shown")
                return False
            else:
                self.logger.info("Successfully verified Order Details Page shown")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_order_details_page_verify_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_reprocess_order_yes_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_Reprocess_Order_Yes_button():
                self.logger.error("Failed to click on Yes, Reprocess Order button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_click_reprocess_order_yes_button_error.png")
                return False
            else:
                self.logger.info("Successfully clicked Yes, Reprocess Order button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_reprocess_order_yes_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_reprocess_order_success_message(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_reprocess_order_success_message():
                self.logger.error("Error while verified reprocess order message")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_reprocess_order_message_verify_error.png")
                return False
            else:
                self.logger.info("Successfully verified reprocess order message")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_reprocess_order_message_verify_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_in_list(self, feature_file_name, confirmation_id):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_in_list(confirmation_id):
                self.logger.error("Failed to verified that Order should not be there in list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_order_not_present_in_list_error.png")
                return False
            else:
                self.logger.info("Successfully verified that Order should not be there in list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_order_not_present_in_list_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def is_fraud_cancel_order_button_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_fraud_cancel_order_button():
                self.logger.error("Failed to verify Cancel Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_fraud_cancel_order_button_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Cancel Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_fraud_cancel_order_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_cancel_order_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_cancel_order_button():
                self.logger.error("Failed to click on Cancel Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_fraud_cancel_order_button_failed.png")
                return False
            else:
                self.logger.info("Successfully ,clicked on Cancel Order button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_fraud_cancel_order_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_fraud_cancel_order_popup(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_fraud_cancel_order_popup():
                self.logger.error("Failed to verify Fraud Cancel Order order popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_fraud_cancel_order_popup_failed.png")
                return False
            else:
                self.logger.info("Successfully verified Fraud Cancel Order order popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_fraud_cancel_popup_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_fraud_yes_cancel_button(self, feature_file_name, screen_shot):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_fraud_yes_cancel_button():
                self.logger.error("Failed to clicked on YES, Cancel Order button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_fraud_yes_cancel_order_button_error.png")
                return False
            else:
                self.logger.info("Successfully clicked YES, Cancel Order button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_yes_cancel_order_popup_verify_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def search_and_select_data_errors_order(self, feature_file_name, confirmation_id):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_search_and_select_data_error_order(confirmation_id):
                self.logger.error("Failed to Search and Select Data errors Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_select_data_error_order_record_failed.png")
                return False
            else:
                self.logger.info("Successfully Searched and Select Data errors Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_select_data_error_order_record_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def is_resubmit_order_button_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_data_error_resubmit_order_button():
                self.logger.error("Failed to verify Data error Resubmit Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_data_error_resubmit_order_button_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Data error Resubmit Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_data_error_resubmit_order_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def update_reseller_po_data_error_order(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.update_reseller_po_data_error_order():
                self.logger.error("Failed to Updating Reseller PO for Data error Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_reseller_po_data_error_order_failed.png")
                return False
            else:
                self.logger.info("Successfully updated Reseller PO for Data error Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_reseller_po_data_error_order_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def update_end_customer_order_data_error_order(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.update_end_customer_order_data_error_order():
                self.logger.error("Failed to Updating End customer order for Data error Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_end_customer_order_error_order_failed.png")
                return False
            else:
                self.logger.info("Successfully updated End customer order for Data error Order")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_end_customer_order_error_order_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_resubmit_order_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_resubmit_order_button():
                self.logger.error("Failed to verify Resubmit Order Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_data_error_resubmit_order_button_failed.png")
                return False
            else:
                self.logger.info("Successfully ,clicked the Resubmit button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_data_error_resubmit_order_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_content_of_resubmit_order_popup(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_content_of_resubmit_order_popup():
                self.logger.error("Failed to verify contents of Resubmit Order popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_resubmit_order_popup_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of Resubmit Order popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_resubmit_order_popup_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_resubmit_order_review_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_resubmit_order_review_button():
                self.logger.error("Failed to click on Resubmit Order Review button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_click_review_button_error.png")
                return False
            else:
                self.logger.info("Successfully clicked on Resubmit Order Review button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_review_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_resubmit_order_yes_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_resubmit_order_yes_button():
                self.logger.error("Failed to click on Yes, Resubmit Order button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_click_resubmit_order_yes_button_error.png")
                return False
            else:
                self.logger.info("Successfully clicked Yes, Resubmit Order button on popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_resubmit_order_yes_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_resubmitted_order_success_message(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_resubmitted_order_success_message():
                self.logger.error("Error while verified resubmitted order message")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_resubmitted_order_message_verify_error.png")
                return False
            else:
                self.logger.info("Successfully verified resubmitted order message")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_resubmitted_order_message_verify_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_data_error_order_in_list(self, feature_file_name, confirmation_id):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_data_error_order_in_list(confirmation_id):
                self.logger.error("Failed to verified that Data error Order should not be there in list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                            "_order_not_present_in_list_error.png")
                return False
            else:
                self.logger.info("Successfully verified that Data error  Order should not be there in list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_order_not_present_in_list_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def is_reference_details_edit_icon_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_reference_details_edit_icon():
                self.logger.error("Failed to verify Edit icon display beside Reference Details title")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_data_error_reference_details_edit_icon_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Edit icon display beside Reference Details title")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_data_error_reference_details_edit_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_edit_reference_details(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_contents_of_edit_reference_details():
                self.logger.error("Failed to verify contents of Edit Reference Details popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_edit_reference_details_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of Edit Reference Details popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_edit_reference_details_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_more_than_eighteen_char_in_po_field(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_more_than_eighteen_char_in_po_field():
                self.logger.error("Failed to Verify PO # textbox should not allow entering more than 18 characters")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_more_than_eighteen_char_in_po_field_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified PO # textbox should not allow entering more than 18 characters")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_more_than_eighteen_char_in_po_field_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_po_number_invalid_message(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_po_number_invalid_message():
                self.logger.error("Failed to Verify PO number is invalid once add this ^ special character")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_po_number_invalid_message_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified PO number is invalid once add this ^ special character")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_po_number_invalid_message_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_more_than_eighteen_char_in_end_customer_order_field(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_more_than_eighteen_char_in_end_customer_order_field():
                self.logger.error(
                    "Failed to Verify End customer order # textbox should not allow entering more than 18 characters")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_more_than_eighteen_char_in_end_customer_order_field_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified End customer order # textbox should not allow entering more than 18 characters")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_more_than_eighteen_char_in_end_customer_order_field_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_end_customer_order_number_invalid_message(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_end_customer_order_number_invalid_message():
                self.logger.error(
                    "Failed to Verify End customer order number is invalid once add this ^ special character")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_end_customer_order_number_invalid_message_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified End customer order number is invalid once add this ^ special character")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_end_customer_order_number_invalid_message_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_modified_data_after_click_on_x_icon(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_modified_data_after_click_on_x_icon():
                self.logger.error(
                    "Failed to Click on X icon then verify that modified data should not get updated on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_modified_data_after_click_on_x_icon_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on X icon then verified that modified data should not get updated on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_modified_data_after_click_on_x_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_modified_data_after_click_on_cancel_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_modified_data_after_click_on_cancel_button():
                self.logger.error(
                    "Failed to Click on cancel button then verify that modified data should not get updated on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_modified_data_after_click_on_cancel_button_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on cancel button then verified that modified data should not get updated on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_modified_data_after_click_on_cancel_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_updated_po_and_end_customer_order_data(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_updated_po_and_end_customer_order_data():
                self.logger.error(
                    "Failed to Update PO and End customer order number with valid data then validate updated data on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_updated_po_and_end_customer_order_data_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Updateed PO and End customer order number with valid data then validated updated data on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_updated_po_and_end_customer_order_data_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def is_shipping_notes_edit_icon_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_shipping_notes_edit_icon():
                self.logger.error("Failed to verify Edit icon display beside Shipping Notes")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_data_error_shipping_notes_edit_icon_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Edit icon display beside Shipping Notes")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_data_error_shipping_notes_edit_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_edit_shipping_notes(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_contents_of_edit_shipping_notes():
                self.logger.error("Failed to verify contents of Edit Shipping Notes popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_edit_reference_details_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of Edit Shipping Notes popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_edit_reference_details_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def click_on_x_icon(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.click_on_x_icon():
                self.logger.error("Failed to verify to click on X icon")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_x_icon_failed.png")
                return False
            else:
                self.logger.info("Successfully verified to click on X icon")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_x_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def click_on_cancel_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.click_on_cancel_button():
                self.logger.error("Failed to verify to click on Cancel button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_cancel_button_failed.png")
                return False
            else:
                self.logger.info("Successfully verified to click on Cancel button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_cancel_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_validate_maximum_limit_message(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_validate_maximum_limit_message():
                self.logger.error("Failed to Add the more 100 characters and validate message for maximum limit")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_max_limit_message_failed.png")
                return False
            else:
                self.logger.info("Successfully Added the more 100 characters and validated message for maximum limit")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_max_limit_message_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_validate_updated_shipping_notes_data(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_validate_updated_shipping_notes_data():
                self.logger.error(
                    "Failed to Update shipping notes with special characters and validate updated data should get display under shipping notes")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_updated_shipping_notes_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Update shipping notes with special characters and validate updated data should get display under shipping notes")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_updated_shipping_notes_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_filter_icon(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_filter_icon():
                self.logger.error("Failed to Click on Filter Icon")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_filter_icon_failed.png")
                return False
            else:
                self.logger.info("Successfully clicked the Filter Icon")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_filter_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_filter_options(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_filter_options():
                self.logger.error("Failed to verify Filter Options")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_filter_options_failed.png")
                return False
            else:
                self.logger.info("Successfully verify Filter Options")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_filter_options_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_entry_method_options_list(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_entry_method_options_list():
                self.logger.error("Failed to verify Order entry method options list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_entry_method_options_list_failed.png")
                return False
            else:
                self.logger.info("Successfully verified Order entry method options list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_entry_method_options_list_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_country_options_list(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_country_options_list():
                self.logger.error("Failed to verify Country options list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_country_options_list_failed.png")
                return False
            else:
                self.logger.info("Successfully verified Country options list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_country_options_list_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_clear_all_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_clear_all_button():
                self.logger.error("Failed to verify after selected any option clear all button should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_clear_all_button_failed.png")
                return False
            else:
                self.logger.info("Successfully verified after selected any option clear all button should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_clear_all_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_selected_options_ord_entry_mtd_on_header(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_selected_options_ord_entry_mtd_on_header():
                self.logger.error(
                    "Failed to verify Selected multiple order entry method options should get display in header")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_selected_ord_entry_mtd_options_on_header_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully verified Selected multiple order entry method options should get display in header")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_selected_ord_entry_mtd_options_on_header_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_select_order_entry_method(self, feature_file_name, order_entry_method):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_select_order_entry_method(order_entry_method):
                self.logger.error("Failed to Select any option from Order Entry Method dropdown list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_selected_order_entry_method_failed.png")
                return False
            else:
                self.logger.info("Successfully Selected any option from Order Entry Method dropdown list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_selected_order_entry_method_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_update_data_grid_as_per_order_entry_method_filter(self, feature_file_name, order_entry_method):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_update_data_grid_as_per_order_entry_method_filter(order_entry_method):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_updated_data_grid_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Data in grid should get updated as per selected Order Entry Method filter if no data found for selected value No orders found message should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_updated_data_grid_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_select_country(self, feature_file_name, country):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_select_country(country):
                self.logger.error("Failed to Select any option from Country dropdown list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_selected_country_failed.png")
                return False
            else:
                self.logger.info("Successfully Selected any option from Country dropdown list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_selected_country_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_update_data_grid_as_per_country_filter(self, feature_file_name, country):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_update_data_grid_as_per_country_filter(country):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_updated_data_grid_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_updated_data_grid_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_clear_all_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_clear_all_button():
                self.logger.error("Failed to click on Clear all Button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_clear_all_button_failed.png")
                return False
            else:
                self.logger.info("Successfully clicked Clear all button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_clear_all_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_select_option_from_ord_entry_method_and_country(self, feature_file_name, order_entry_method, country):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_select_option_from_ord_entry_method_and_country(order_entry_method, country):
                self.logger.error("Failed to Select any option from Order Entry Method and Country dropdown list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_select_option_from_ord_entry_method_and_country_failed.png")
                return False
            else:
                self.logger.info("Successfully Selected any option from Order Entry Method and Country dropdown list")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_select_option_from_ord_entry_method_and_country_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_selected_values_cleared_from_filter_header(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_selected_values_cleared_from_filter_header():
                self.logger.error(
                    "Failed to verify Selected values should get cleared from filter header and all data should get loaded in grid")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_selected_values_cleared_from_filter_header_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified Selected values should get cleared from filter header and all data should get loaded in grid")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_selected_values_cleared_from_filter_header_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def is_vmf_details_edit_icon_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_vmf_details_edit_icon():
                self.logger.error("Failed to verify Edit icon display beside VMF Details")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_data_error_vmf_details_edit_icon_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Edit icon display beside VMF Details")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_data_error_vmf_details_edit_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_edit_vmf_details(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_contents_of_edit_vmf_details():
                self.logger.error("Failed to verify contents of Edit VMF Details popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_edit_vmf_details_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of Edit VMF Details popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_edit_vmf_details_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_attribute_value_allow_special_character(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_attribute_value_allow_special_characters():
                self.logger.error("Failed to Verify Attribute value should allow special characters")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_attribute_value_allow_special_charcter_failed.png")
                return False
            else:
                self.logger.info("Successfully verified Attribute value should allow special characters")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_attribute_value_allow_special_charcter_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_validate_vmf_saved_data(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_validate_vmf_saved_data():
                self.logger.error("Failed to verify saved data on orders details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_vmf_saved_data_failed.png")
                return False
            else:
                self.logger.info("Successfully verified saved data on orders details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_vmf_saved_data_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_validate_vmf_data_not_saved(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_validate_vmf_data_not_saved():
                self.logger.error("Failed to Verify that VMF entered data should not get saved after click on X icon")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_vmf_data_not_saved_failed.png")
                return False
            else:
                self.logger.info("Successfully verified VMF entered data should not get saved after click on X icon")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_vmf_data_not_saved_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_validate_modified_vmf_data_not_updated(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_validate_modified_vmf_data_not_updated():
                self.logger.error(
                    "Failed to Verify that modified VMF data should not get updated on order details page after click on Cancel button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_modified_vmf_data_not_updated_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully verified that modified VMF data should not get updated on order details page after click on Cancel button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_modified_vmf_data_not_updated_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def is_end_user_details_edit_icon_visible(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_end_user_details_edit_icon():
                self.logger.error("Failed to verify Edit icon display beside End User Details")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_data_error_end_user_details_edit_icon_failed.png")
                return False
            else:
                self.logger.info("Successfully Verified Edit icon display beside End User Details")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_data_error_end_user_details_edit_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_edit_end_user_details(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_contents_of_edit_end_user_details():
                self.logger.error("Failed to verify contents of Edit End User Details popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_edit_vmf_details_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of Edit End User Details popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_edit_end_user_details_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_all_addr_matching_with_entered_text(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_all_addr_matching_with_entered_text():
                self.logger.error("Failed to Verify all address matching with enterd text should get displayed")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_all_addr_matching_with_entered_text_failed.png")
                return False
            else:
                self.logger.info("Successfully verified all address matching with enterd text should get displayed")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_all_addr_matching_with_entered_text_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_edit_button_and_save_button_enable(self, feature_file_name, end_user_with_suffix):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_edit_button_and_save_button_enable(end_user_with_suffix):
                self.logger.error(
                    "Failed to Select the end user with suffix and verify that Edit icon should display for user and Save button should get enabled")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_edit_button_and_save_button_enable_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Selected the end user with suffix and verified Edit icon should display for user and Save button should get enabled")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_edit_button_and_save_button_enable_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_selected_end_user_info_on_order_details_page(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_selected_end_user_info_on_order_details_page():
                self.logger.error(
                    "Failed to Click on Save Button and Verify that selected end user information should get displayed on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_selected_end_user_info_on_order_details_page_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on Save Button and Verified that selected end user information should get displayed on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_selected_end_user_info_on_order_details_page_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_selected_end_user_with_suffix_edit_popup(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_contents_of_selected_end_user_with_suffix_edit_popup():
                self.logger.error("Failed to verify contents of selected end user with suffix edit popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_selected_end_user_with_suffix_edit_popup_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of selected end user with suffix edit popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_selected_end_user_with_suffix_edit_popup_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_modified_end_user_info_on_order_details_page(self, feature_file_name, end_user):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_modified_end_user_info_on_order_details_page(end_user):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_modified_end_user_info_on_order_details_page_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Modified Name Phone Number Email and Click on Add button then Verified updated end user information should display on order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_modified_end_user_info_on_order_details_page_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_validate_message_for_mandatory_fields(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_validate_message_for_mandatory_fields():
                self.logger.error("Failed to verify validation message should display for all mandatory fields")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_message_for_mandatory_fields_failed.png")
                return False
            else:
                self.logger.info("Successfully verified validation message should display for all mandatory fields")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_message_for_mandatory_fields_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_edit_add_new_end_user(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_contents_of_edit_add_new_end_user():
                self.logger.error("Failed to verify contents of Edit Add new end user popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_edit_add_new_end_user_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of Add new end user popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_edit_add_new_end_user_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_add_new_user_with_valid_data(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_add_new_user_with_valid_data():
                self.logger.error(
                    "Failed to verify that added new user should display and user should able to select it")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_add_new_user_with_valid_data_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified that added new user should display and user should able to select it")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_add_new_user_with_valid_data_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_edit_billing_address(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_contents_of_edit_billing_address():
                self.logger.error("Failed to verify contents of Edit Billing Address popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_contents_of_edit_billing_address_failed.png")
                return False
            else:
                self.logger.info("Successfully verified contents of Edit Billing Address popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_contents_of_edit_billing_address_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_details_page_after_click_on_x_icon(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_details_page_after_click_on_x_icon():
                self.logger.error(
                    "Failed to Click on X icon on popup and Verify that Order Details page should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_details_page_after_click_on_x_icon_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on X icon on popup and Verified Order Details page should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_details_page_after_click_on_x_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_details_page_after_click_on_cancel_button(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_details_page_after_click_on_cancel_button():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_details_page_after_click_on_cancel_button_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on Cancel button on popup and Verified that Order Details page should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_details_page_after_click_on_cancel_button_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_search_with_special_character(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_search_with_special_character():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_search_with_special_character_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully searched with special characters then No records found matching your search criteria should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_search_with_special_character_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_search_with_valid_suffix(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_search_with_valid_suffix():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_search_with_valid_suffix_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Searched with valid Suffix and then Billing address details should get loaded in popup")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_search_with_valid_suffix_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_select_searched_addr_and_save_button_enabled(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_select_searched_addr_and_save_button_enabled():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_select_searched_addr_and_save_button_enabled_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Selected the searched address and then Save button should get enabled on selecting address")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_select_searched_addr_and_save_button_enabled_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_selected_billing_addr_on_order_details_page(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_selected_billing_addr_on_order_details_page():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_selected_billing_addr_on_order_details_page_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified selected billing address should get displayed on Order details page")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_selected_billing_addr_on_order_details_page_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_line_remove_icon(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_line_remove_icon():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_line_remove_icon_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified remove icon should display for order line")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_line_remove_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_on_mark_for_cancel_and_line_not_editable(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_on_mark_for_cancel_and_line_not_editable():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_mark_for_cancel_and_line_not_editable_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on Mark for Cancel option and Verify line should grey out and should not allow further edit operations")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_mark_for_cancel_and_line_not_editable_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_on_unmark_for_cancel_and_line_is_editable(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_on_unmark_for_cancel_and_line_is_editable():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_unmark_for_cancel_and_line_is_editable_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on Unmark for Cancel option and Verify line should become enable and it should allow edit operations")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_unmark_for_cancel_and_line_is_editable_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_resubmitted_successfully(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_resubmitted_successfully():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_resubmitted_successfully_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified that Order should get resubmitted succesfully after cancel the Order line")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_resubmitted_successfully_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_on_mark_for_cancel_from_dropdown_and_line_grey_out(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_on_mark_for_cancel_from_dropdown_and_line_grey_out():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_mark_for_cancel_and_line_not_editable_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on Mark for Cancel option from dropdown and Verify line should grey out")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_mark_for_cancel_from_dropdown_and_line_grey_out_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_click_on_unmark_for_cancel_from_dropdown_and_line_get_unable(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_click_on_unmark_for_cancel_from_dropdownn_and_line_get_unable():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_unmark_for_cancel_and_line_is_editable_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on Unmark for Cancel option from dropdown and Verify line should get enable")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_unmark_for_cancel_from_dropdown_and_line_get_unable_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_atleast_one_order_line_required_message(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_atleast_one_order_line_required_message():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_atleast_one_order_line_required_message_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified that At least one order line is required to resubmit the order message")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_atleast_one_order_line_required_message_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_last_order_attempt_on_section(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_last_order_attempt_on_section():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_last_order_attempt_on_section_failed.png")
                return False
            else:
                self.logger.info(
                    f'Successfully Verified that Last order attempt on section should display inside filter panel')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_last_order_attempt_on_section_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_created_on_section(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_created_on_section():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_created_on_section_failed.png")
                return False
            else:
                self.logger.info(f'Successfully Verified that Created on section should display inside filter panel')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_created_on_section_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_last_order_attempt_on_section(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_contents_of_last_order_attempt_on_section():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_contents_of_last_order_attempt_on_section_failed.png")
                return False
            else:
                self.logger.info(f'Successfully Verified that contents of Last order attempt on section')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_contents_of_last_order_attempt_on_section_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_contents_of_created_on_section(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_contents_of_created_on_section():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_contents_of_created_on_section_failed.png")
                return False
            else:
                self.logger.info(f'Successfully Verified that contents of Created on section')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_contents_of_created_on_section_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_last_ord_attempt_on_sec_calender_open_and_able_to_select_date(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_last_ord_attempt_on_sec_calender_open_and_able_to_select_date():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_last_ord_attempt_on_sec_calender_open_and_able_to_select_date_failed.png")
                return False
            else:
                self.logger.info(
                    f'Successfully Verified that Last order attempt on section Calendar should open and it should allow date selection')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_last_ord_attempt_on_sec_calender_open_and_able_to_select_date_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_created_on_sec_calender_open_and_able_to_select_date(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_created_on_sec_calender_open_and_able_to_select_date():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_created_on_sec_calender_open_and_able_to_select_date_failed.png")
                return False
            else:
                self.logger.info(
                    f'Successfully Verified that Created On section Calendar should open and it should allow date selection')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_created_on_sec_calender_open_and_able_to_select_date_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_last_ord_attempt_on_data_get_filter_as_per_selected_date_range(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_last_ord_attempt_on_data_get_filter_as_per_selected_date_range_in_pages():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_last_ord_attempt_on_data_get_filter_as_per_selected_date_range_failed.png")
                return False
            else:
                self.logger.info(
                    f'Successfully Selected the Last order attempt on section From and To date and Verified that Data should get filtered on selected date ranges')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_last_ord_attempt_on_data_get_filter_as_per_selected_date_range_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_created_on_data_get_filter_as_per_selected_date_range(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_created_on_data_get_filter_as_per_selected_date_range_in_pages():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_created_on_data_get_filter_as_per_selected_date_range_failed.png")
                return False
            else:
                self.logger.info(
                    f'Successfully Selected the Created on section From and To date and Verified that Data should get filtered on selected date ranges')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_created_on_data_get_filter_as_per_selected_date_range_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def verify_filter_by_last_ord_attempt_on_data_by_selecting_30_days_in_pages(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_filter_by_last_ord_attempt_on_data_by_selecting_30_days_in_pages():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_filter_by_last_ord_attempt_on_data_by_selecting_30_days_in_pages_failed.png")
                return False
            else:
                self.logger.info(
                    f'Successfully Selected last 30 days checkbox from Last order attempt on section and Verified that Data should get filtered on selected date ranges')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_filter_by_last_ord_attempt_on_data_by_selecting_30_days_in_pages_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def verify_filter_by_created_on_data_by_selecting_30_days_in_pages(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.verify_filter_by_created_on_data_by_selecting_30_days_in_pages():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_filter_by_created_on_data_by_selecting_30_days_in_pages_failed.png")
                return False
            else:
                self.logger.info(
                    f'Successfully Selected last 30 days checkbox from Created on section and Verified that Data should get filtered on selected date ranges')
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_filter_by_created_on_data_by_selecting_30_days_in_pages_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_line_edit_icon(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_line_edit_icon():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_line_edit_icon_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified remove icon should display for order line")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_line_edit_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_update_and_cancel_icon(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_update_and_cancel_icon():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_update_and_cancel_icon_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on edit icon and Verified Update and Cancel Icon should display")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_update_and_cancel_icon_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_editable_order_line_fields(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_editable_order_line_fields():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_editable_order_line_fields_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified Quantity, Reseller price, End user price and End user po# fields become editable")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_editable_order_line_fields_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_line_updated_data_discarded(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_line_updated_data_discarded():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_line_updated_data_discarded_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Clicked on X icon and Verifying that Updated data should get discarded")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_line_updated_data_discarded_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_verify_order_line_fields_not_allow_non_numberic_content(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_verify_order_line_fields_not_allow_non_numberic_content():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_verify_order_line_fields_not_allow_non_numberic_content_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Verified that Quantity, Reseller price, End user price and End user po# fields not allow non numeric content")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_verify_order_line_fields_not_allow_non_numberic_content_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False

    def do_update_order_line_field_value(self, feature_file_name):
        x4a_error_order = X4AErrorOrdersPage(self.driver)
        try:
            if not x4a_error_order.do_update_order_line_field_value():
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_update_order_line_field_value_failed.png")
                return False
            else:
                self.logger.info(
                    "Successfully Updated the Order line Quantity, Reseller price and End User PO value")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_update_order_line_field_value_successfully.png")
                return True
        except Exception as e:
            self.logger.exception(e)
            return False