import glob
import os
import time
from pathlib import Path
from pywinauto import application

from CommonUtilities.CSVReader import CSVReader
from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4AOrdersAgedOrders import X4AAgedOrdersPage


class ValidateAgedOrdersData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()
    db_file_path = ReadConfig.get_db_file_path()
    aged_order_table_headers = ['IM Order #', 'BCN account #', 'Customer name', 'Customer PO #', 'Vendor name', 'Order type', 'Order value', 'Order status', 'Order date', 'Last updated', 'IM SKU', 'Country']
    aged_order_quick_search_options = ['IM Order #', 'Vendor name', 'BCN Account #', 'Customer PO Number']
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
                                        + "login_successful.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "login_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "login_error.png"
            self.logger.error("Login unsuccessful!!")
            self.logger.exception(e)
            raise e

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

    def verify_aged_orders_table_columns(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying the Aged order table headers are correct")
            aged_order_columns = x4a_aged_order.get_table_column_header()
            for column in self.aged_order_table_headers:
                if column not in aged_order_columns:
                    raise Exception("Column %s missing in Aged Orders table", column)
            self.logger.info("Successfully verified columns in Aged order table")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "aged_orders_columns_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "aged_orders_columns_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "aged_orders_columns_error.png"
            self.logger.error("Error while verifying columns in Aged order table")
            self.logger.exception(e)
            return False

    def verify_quick_search_options(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying the Aged order quick search options are correct")
            quick_search_options = x4a_aged_order.get_quick_search_options()
            for option in self.aged_order_quick_search_options:
                if option not in quick_search_options:
                    raise Exception("Option %s not found in Aged order quick search options", option)
            self.logger.info("Successfully verified quick search options")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "quick_search_options_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_quick_search_options_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_quick_search_options_error.png"
            self.logger.error("Error while verifying quick search options in Aged order")
            self.logger.exception(e)
            return False

    def search_im_order_number(self, feature_file_name, screen_shot, order_number):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Searching the im order number")
            x4a_aged_order.search_im_order_number(order_number)
            self.logger.info("IM order number searched successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "im_order_number_searched_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "search_im_order_number_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_im_order_number_error.png"
            self.logger.error("Error while searching the im order number")
            self.logger.exception(e)
            return False

    def search_vendor_name(self, feature_file_name, screen_shot, vendor_name):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Searching the im vendor name")
            x4a_aged_order.search_vendor_name(vendor_name)
            self.logger.info("Vendor name searched successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "vendor_name_searched_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "search_vendor_name_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_vendor_name_error.png"
            self.logger.error("Error while searching the vendor_name")
            self.logger.exception(e)
            return False

    def search_bcn_account(self, feature_file_name, screen_shot, bcn_account):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Searching the BCN account")
            x4a_aged_order.search_bcn_account(bcn_account)
            self.logger.info("BCN account searched successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_account_searched_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "search_bcn_account_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "search_bcn_account_error.png"
            self.logger.error("Error while searching the BCN account")
            self.logger.exception(e)
            return False

    def search_customer_po(self, feature_file_name, screen_shot, customer_po):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Searching the Customer PO")
            x4a_aged_order.search_customer_po_number(customer_po)
            self.logger.info("Customer PO searched successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "customer_po_searched_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "search_customer_po_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "search_customer_po_error.png"
            self.logger.error("Error while searching the customer_po")
            self.logger.exception(e)
            return False

    def verify_im_order_number_search_result(self, feature_file_name, screen_shot, order_number):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying the im order number search")
            x4a_aged_order.verify_order_number_quick_search(order_number)
            self.logger.info("IM order number search results verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "im_order_number_search_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_search_im_order_number_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_search_im_order_number_error.png"
            self.logger.error("Error while verifying the im order number search results")
            self.logger.exception(e)
            return False

    def verify_vendor_name_search_result(self, feature_file_name, screen_shot, vendor_name):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying the vendor name search")
            x4a_aged_order.verify_vendor_name_in_pages(vendor_name)
            self.logger.info("Vendor name search results verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "vendor_name_search_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_search_vendor_name_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_search_vendor_name_error.png"
            self.logger.error("Error while verifying the vendor name search results")
            self.logger.exception(e)
            return False

    def verify_bcn_account_search_result(self, feature_file_name, screen_shot, bcn_account):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying the BCN account search")
            x4a_aged_order.verify_bcn_account_in_pages(bcn_account)
            self.logger.info("BCN account search results verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_account_search_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_search_bcn_account_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_search_bcn_account_error.png"
            self.logger.error("Error while verifying the BCN account search results")
            self.logger.exception(e)
            return False

    def verify_customer_po_search_result(self, feature_file_name, screen_shot, customer_po):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying the Customer po search")
            x4a_aged_order.verify_customer_po_in_pages(customer_po)
            self.logger.info("Customer PO search results verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "customer_po_search_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_search_customer_po_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_search_customer_po_error.png"
            self.logger.error("Error while verifying the customer_po search results")
            self.logger.exception(e)
            return False

    def select_order_date_range(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Select date range for order date")
            x4a_aged_order.select_order_date_range()
            self.logger.info("Order date range selected successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "order_date_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "select_order_date_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "select_order_date_error.png"
            self.logger.error("Error while selecting order date range")
            self.logger.exception(e)
            return False

    def verify_order_date_search(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the order date in pages")
            x4a_aged_order.verify_order_date_in_pages()
            self.logger.info("Order date range verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "order_date_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_order_date_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_order_date_error.png"
            self.logger.error("Error while verifying order date range")
            self.logger.exception(e)
            return False

    def select_last_updated_date_range(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Select date range for last updated date")
            x4a_aged_order.select_last_updated_date_range()
            self.logger.info("last updated date range selected successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "last_updated_date_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "select_last_updated date_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "select_last_updated date_error.png"
            self.logger.error("Error while selecting last updated date range")
            self.logger.exception(e)
            return False

    def verify_last_update_date_search(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the last update date in pages")
            x4a_aged_order.verify_last_update_date_in_pages()
            self.logger.info("Last update date range verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "last_update_date_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_last_update_date_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_last_update_date_error.png"
            self.logger.error("Error while verifying last update date range")
            self.logger.exception(e)
            return False

    def filter_by_bcn(self, feature_file_name, screen_shot, bcn_account):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering the BCN account")
            x4a_aged_order.filter_by_bcn(bcn_account)
            self.logger.info("BCN account filtered successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_account_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_bcn_account_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_bcn_account_error.png"
            self.logger.error("Error while filtering the BCN account")
            self.logger.exception(e)
            return False

    def verify_filter_by_bcn(self, feature_file_name, screen_shot, bcn_account):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the BCN in pages")
            x4a_aged_order.verify_filtered_bcn_account_in_pages(bcn_account)
            self.logger.info("BCN verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_bcn_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_bcn_error.png"
            self.logger.error("Error while verifying BCN")
            self.logger.exception(e)
            return False

    def filter_by_vendor(self, feature_file_name, screen_shot, vendor_name):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering the Vendor")
            x4a_aged_order.filter_by_vendor_name(vendor_name)
            self.logger.info("Vendor filtered successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "vendor_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_vendor_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_vendor_error.png"
            self.logger.error("Error while filtering the Vendor")
            self.logger.exception(e)
            return False

    def verify_filter_by_vendor(self, feature_file_name, screen_shot, vendor_name):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the vendor in pages")
            x4a_aged_order.verify_filtered_vendor_in_pages(vendor_name)
            self.logger.info("Vendor verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "vendor_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_vendor_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_vendor_error.png"
            self.logger.error("Error while verifying vendor")
            self.logger.exception(e)
            return False

    def filter_by_customer_name(self, feature_file_name, screen_shot, customer_name):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering the Customer name")
            x4a_aged_order.filter_by_customer_name(customer_name)
            self.logger.info("Customer name filtered successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "customer_name_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_customer_name_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_customer_name_error.png"
            self.logger.error("Error while filtering the customer name")
            self.logger.exception(e)
            return False

    def verify_filter_by_customer_name(self, feature_file_name, screen_shot, customer_name):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the customer name in pages")
            x4a_aged_order.verify_filtered_customer_name_in_pages(customer_name)
            self.logger.info("Customer name verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "customer_name_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_customer_name_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_customer_name_error.png"
            self.logger.error("Error while verifying customer name")
            self.logger.exception(e)
            return False

    def filter_by_order_type(self, feature_file_name, screen_shot, order_type):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering the Order type")
            x4a_aged_order.filter_by_order_type(order_type)
            self.logger.info("Customer name filtered successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "order_type_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_order_type_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_order_type_error.png"
            self.logger.error("Error while filtering the order type")
            self.logger.exception(e)
            return False

    def filter_by_order_status(self, feature_file_name, screen_shot, order_status):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering the Order status")
            x4a_aged_order.filter_by_order_status(order_status)
            self.logger.info("Order status filtered successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "order_status_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_order_status_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_order_status_error.png"
            self.logger.error("Error while filtering the order status")
            self.logger.exception(e)
            return False

    def verify_filter_by_order_type(self, feature_file_name, screen_shot, order_type):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the order type in pages")
            x4a_aged_order.verify_filtered_order_type_in_pages(order_type)
            self.logger.info("order type verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "order_type_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_order_type_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_order_type_error.png"
            self.logger.error("Error while verifying order type")
            self.logger.exception(e)
            return False

    def verify_filter_by_order_status(self, feature_file_name, screen_shot, order_status):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the order status in pages")
            x4a_aged_order.verify_filtered_order_status_in_pages(order_status)
            self.logger.info("order status verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "order_status_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_order_status_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_order_status_error.png"
            self.logger.error("Error while verifying order status")
            self.logger.exception(e)
            return False

    def filter_by_total_revenue(self, feature_file_name, screen_shot, min_total_revenue, max_total_revenue):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering by Total revenue")
            x4a_aged_order.filter_by_total_revenue(min_total_revenue, max_total_revenue)
            self.logger.info("Total revenue filtered successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "total_revenue_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_total_revenue_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_total_revenue_error.png"
            self.logger.error("Error while filtering the total revenue")
            self.logger.exception(e)
            return False

    def verify_filter_by_total_revenue(self, feature_file_name, screen_shot, min_total_revenue, max_total_revenue):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the total revenue in pages")
            x4a_aged_order.verify_total_revenue_in_pages(min_total_revenue, max_total_revenue)
            self.logger.info("total revenue verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "total_revenue_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_total_revenue_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_total_revenue_error.png"
            self.logger.error("Error while verifying total revenue")
            self.logger.exception(e)
            return False

    def filter_by_bcn_vendor_and_order_status(self, feature_file_name, screen_shot, bcn, vendor, order_status):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering by bcn, vendor and order status")
            x4a_aged_order.filter_by_bcn_vendor_and_order_status(bcn, vendor, order_status)
            self.logger.info("bcn, vendor and order status filtered successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_vendor_and_order_status_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_bcn_vendor_and_order_status_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_bcn_vendor_and_order_status_error.png"
            self.logger.error("Error while filtering the bcn, vendor and order status")
            self.logger.exception(e)
            return False

    def verify_filter_by_bcn_vendor_and_order_status(self, feature_file_name, screen_shot, bcn_account, vendor_name, order_status):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the bcn, vendor and order status in pages")
            x4a_aged_order.verify_bcn_vendor_and_order_status_in_pages(bcn_account, vendor_name, order_status)
            self.logger.info("bcn, vendor and order status verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_vendor_and_order_status_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_bcn_vendor_and_order_status_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_bcn_vendor_and_order_status_error.png"
            self.logger.error("Error while verifying bcn, vendor and order status")
            self.logger.exception(e)
            return False

    def logout_x4a_url(self, feature_file_name):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            if not x4a_aged_order.logout_x4a():
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

    def verify_reset_for_order_date(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the reset is working for order date")
            x4a_aged_order.verify_order_date_reset()
            self.logger.info("Reset for order date verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "reset_order_date_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_reset_order_date_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_reset_order_date_error.png"
            self.logger.error("Error while verifying reset for order date")
            self.logger.exception(e)
            return False

    def verify_reset_for_last_update_date(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verify the reset is working for last update date")
            x4a_aged_order.verify_last_update_date_reset()
            self.logger.info("Reset for last update date verified successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "reset_last_update_date_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_reset_last_update_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "verify_reset_last_update_error.png"
            self.logger.error("Error while verifying reset for last update date")
            self.logger.exception(e)
            return False

    def click_on_download(self, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            #breakpoint()
            self.logger.info("verifying download")
            x4a_aged_order.click_aged_orders_download()
            app = application.Application().connect(title_re="Save As", found_index=0)
            time.sleep(2)
            app.SaveAs.Button.click()
            self.logger.info("File downloaded successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "aged_order_data_downloaded_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "aged_order_data_download_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                          "aged_order_data_download_error.png"
            self.logger.error("Error while downloading aged order data")
            self.logger.exception(e)
            return False

    def validate_file_name(self, feature_file_name, screen_shot):
        try:
            time.sleep(3)
            self.logger.info("Fetching latest downloaded file")
            download_dir = str(os.path.join(Path.home(), "Downloads"))
            self.logger.info("Download directory is " + str(download_dir))
            list_of_files = glob.glob(download_dir + '/*.csv')
            latest_file = max(list_of_files, key=os.path.getmtime)
            self.logger.info("Recent file in the downloads: " + str(latest_file))
            # downloaded_file_name_list = os.listdir(download_dir)
            # length_of_list = len(downloaded_file_name_list)
            # try:
            #     for i in range(length_of_list):
            #         file_name = downloaded_file_name_list[i].split(".")
            #         if file_name[1] == "csv":
            #             download_file_name = file_name[0]
            #             self.logger.info(download_file_name)
            #             break
            #         else:
            #             self.logger.info("No file found")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "downloaded_file_name_verified_successfully.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_downloaded_file_name_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_downloaded_file_name_error.png"
            self.logger.error("Error while verifying the downloaded file name %s", e)
            raise e
        return latest_file

    def verify_rows(self, file, feature_file_name, screen_shot):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying downloaded file rows")
            csv_file = CSVReader(file)
            rows = len(csv_file.read_file())
            self.logger.info(rows)
            assert rows == 10000, "Number of rows mismatched"
            self.logger.info("Verified downloaded file rows successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "downloaded_file_rows_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_downloaded_file_rows_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_downloaded_file_rows_error.png"
            self.logger.error("Error while verifying downloaded file rows")
            self.logger.exception(e)
            return False

    def filter_by_bcn_and_order_date(self, feature_file_name, screen_shot, bcn):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Filtering by bcn and order date")
            x4a_aged_order.filter_by_bcn_and_order_date(bcn)
            self.logger.info("filtered by bcn and order date successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_and_order_date_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_bcn_and_order_date_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                        "filter_bcn_and_order_date_error.png"
            self.logger.error("Error while filtering by bcn and order date")
            self.logger.exception(e)
            return False

    def verify_excel_data_with_ui_for_search(self, feature_file_name, screen_shot, bcn, file):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying file data with UI for search with bcn and order date")
            csv_file = CSVReader(file)
            rows = csv_file.read_file()
            file_first_row = rows[0]
            file_last_row = rows[-1]
            self.logger.info("File first row :" + str(file_last_row))
            self.logger.info("File last row :" + str(file_first_row))
            table_header = x4a_aged_order.get_table_column_header()
            ui_first_row, ui_last_row = x4a_aged_order.get_first_and_last_row_data_for_search_with_bcn_and_order_data(table_header, bcn)
            self.verify_data(ui_first_row, ui_last_row, file_first_row, file_last_row)
            self.logger.info("Verified file data with UI successfully for search with bcn and order date")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "file_and_ui_data_verified_for_search_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_file_and_ui_data_for_search_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_file_and_ui_data_for_search_error.png"
            self.logger.error("Error while verifying ui and file data for search")
            self.logger.exception(e)
            return False

    def verify_data(self, ui_first_row, ui_last_row, file_first_row, file_last_row):
        try:
            for header in self.aged_order_table_headers:
                self.logger.info("Verifying the header %s", header)
                if header == 'Vendor name':
                    self.logger.info("assigning vendor name")
                    if 'Multiple Vendors' in ui_first_row[header]:
                        ui_first_row[header] = 'Multiple'
                    if 'Multiple Vendors' in ui_last_row[header]:
                        ui_last_row[header] = 'Multiple'
                    self.logger.info("UI first row :" + str(ui_first_row))
                    self.logger.info("UI last row :" + str(ui_last_row))
                if header != 'Order date' and header != 'Last updated' and header != 'IM SKU':
                    if file_first_row[header] != ui_first_row[header]:
                        self.logger.error("%s mismatched in UI an file for first row of data", header)
                        self.logger.error("File: " + str(file_first_row[header]) + "\n" + "UI: " + str(ui_first_row[header]))
                        raise Exception("value mismatched for first row of data")
                    if file_last_row[header] != ui_last_row[header]:
                        self.logger.error("%s mismatched in UI an file for last row of data", header)
                        self.logger.error("File: " + str(file_last_row[header]) + "\n" + "UI: " + str(ui_last_row[header]))
                        raise Exception("Value mismatched for last row of data")
                elif header == 'IM SKU':
                    if file_first_row[header] != ui_first_row[header]:
                        self.logger.error("%s mismatched in UI an file for first row of data", header)
                        self.logger.error("File: " + str(file_first_row[header]) + "\n" + "UI: " + str(ui_first_row[header]))
                        raise Exception("value mismatched for first row of data")
                    if file_last_row[header] != ui_last_row[header]:
                        self.logger.error("%s mismatched in UI an file for last row of data", header)
                        self.logger.error("File: " + str(file_last_row[header]) + "\n" + "UI: " + str(ui_last_row[header]))
                        raise Exception("Value mismatched for last row of data")
                else:
                    ui_first_row_date = (ui_first_row[header].split(","))[0]
                    ui_first_row_time = (ui_first_row[header].split(","))[1]
                    ui_last_row_date = (ui_last_row[header].split(","))[0]
                    ui_last_row_time = (ui_last_row[header].split(","))[1]
                    file_first_row_date = (file_first_row[header].split(" "))[0]
                    file_first_row_time = (file_first_row[header].split(" "))[1]
                    file_last_row_date = (file_last_row[header].split(" "))[0]
                    file_last_row_time = (file_last_row[header].split(" "))[1]
                    if ui_first_row_date != file_first_row_date:
                        self.logger.error("Date mismatched in UI and file for first row of data for %s", header)
                        self.logger.error(
                            "File: " + str(ui_first_row_date) + "\t" + "UI: " + str(ui_last_row_date))
                        raise Exception("Date value mismatched for first row of data")
                    if ui_first_row_time != file_first_row_time:
                        self.logger.warning("Time mismatched in UI and file for first row of data for %s", header)
                        self.logger.warning(
                            "File: " + str(ui_first_row_time) + "\t" + "UI: " + str(file_first_row_time))
                    if ui_last_row_date != file_last_row_date:
                        self.logger.error("Date mismatched in UI and file for last row of data for %s", header)
                        self.logger.error(
                            "File: " + str(ui_last_row_date) + "\t" + "UI: " + str(file_last_row_date))
                        raise Exception("Date value mismatched for last row of data")
                    if ui_last_row_time != file_last_row_time:
                        self.logger.warning("Time mismatched in UI and file for first row of data for %s", header)
                        self.logger.warning(
                            "File: " + str(ui_last_row_time) + "\t" + "UI: " + str(file_last_row_time))
        except Exception as e:
            self.logger.info("Exception while validating file data with UI data")
            raise e

    def verify_excel_data_with_ui_for_filter(self, feature_file_name, screen_shot, bcn, vendor_name, order_status, file):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Verifying File data with UI for filter with bcn, vendor name and order status")
            csv_file = CSVReader(file)
            rows = csv_file.read_file()
            file_first_row = rows[0]
            file_last_row = rows[-1]
            self.logger.info("File first row :" + str(file_last_row))
            self.logger.info("File last row :" + str(file_first_row))
            table_header = x4a_aged_order.get_table_column_header()
            ui_first_row, ui_last_row = x4a_aged_order.get_first_and_last_row_data_for_filter_bcn_and_vendor_and_status(table_header, bcn, vendor_name, order_status)
            self.verify_data(ui_first_row, ui_last_row, file_first_row, file_last_row)
            self.logger.info("Verified CSV data with UI successfully for filter with bcn, vendor name and order status")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "file_and_ui_data_verified_for_filter_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_file_and_ui_data_for_filter_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_file_and_ui_data_for_filter_error.png"
            self.logger.error("Error while verifying ui and file data for filter")
            self.logger.exception(e)
            return False

    def cancel_order_and_validate(self, feature_file_name, screen_shot, im_order):
        x4a_aged_order = X4AAgedOrdersPage(self.driver)
        try:
            self.logger.info("Cancelling order")
            x4a_aged_order.cancel_aged_order()
            self.logger.info("Validating cancel")
            x4a_aged_order.validate_order_is_not_in_list(im_order)
            self.logger.info("Order cancelled successfully")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "bcn_and_order_date_filtered_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_bcn_and_order_date_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                        "filter_bcn_and_order_date_error.png"
            self.logger.error("Error while cancelling order")
            self.logger.exception(e)
            return False