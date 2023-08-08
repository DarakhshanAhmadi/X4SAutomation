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
                self.logger.info("Successfully ,clicked the 3cancel button")
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
                self.logger.error("Error while verifing Reprocess order popup is closed  and Order Details Page shown")
            else:
                self.logger.info("Successfully verified Reprocess order popup is closed  and Order Details Page shown")
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
