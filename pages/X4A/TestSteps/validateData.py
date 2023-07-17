from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4AOrdersAgedOrders import X4AAgedOrdersPage
from pages.X4A.Pages.X4AOrdersSalesOrders import X4ASalesOrdersPage


class CreateOrder:
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

    def click_on_sales_orders(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.go_to_sales_orders()
            self.logger.info("Successfully clicked on sales order")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_sales_order_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_sales_order_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_sales_order_clicking_error.png"
            self.logger.error("Error while clicking on sales order")
            self.logger.exception(e)
            return False


    """ This method filters order by feature file name and returns order data """

    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data

    def is_sales_orders_listing_page_visible(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.is_sales_orders_listing_page_visible()
            self.logger.info("Successfully verified Sales Orders Listing Page")
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

    def is_all_column_visible(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if (x4a_sales_order.is_im_order_clum_visible() & x4a_sales_order.is_type_clum_visible() & x4a_sales_order.is_bcn_clum_visible() &
                    x4a_sales_order.is_reseller_po_clum_visible() & x4a_sales_order.is_reseller_nm_clum_visible() & x4a_sales_order.is_vendor_nm_clum_visible()
                    & x4a_sales_order.is_end_user_nm_clum_visible() & x4a_sales_order.is_end_user_po_clum_visible() & x4a_sales_order.is_end_user_po_clum_visible() &
                    x4a_sales_order.is_order_value_clum_visible() & x4a_sales_order.is_order_status_clum_visible() & x4a_sales_order.is_created_on_clum_visible()):
                self.logger.info(
                    "Successfully verified Im order, Type, BCN, Reseller PO, Reseller name, Vendor name, End User name, End User po, Order value, Order status, Created on coulmns on Sales Orders Listing page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_all_column_on_sales_orders_listing_page_visible_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_all_column_on_sales_orders_listing_page_visible_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_all_column_on_sales_orders_listing_page_visible_error.png"
            self.logger.error("Error while verifying all column on Sales Orders Listing Page")
            self.logger.exception(e)
            return False

    def do_search_bcn(self, reseller_bcn, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.search_bcn(reseller_bcn)
            self.logger.info("Successfully searched BCN")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_searched_reseller_bcn_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_searched_reseller_bcn_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_searched_reseller_bcn_error.png"
            self.logger.error("Error while searching Reseller BCN")
            self.logger.exception(e)
            return False

    def do_validate_reseller_bcn(self, reseller_bcn, feature_file_name, screen_shot, page1, page2, page3):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_bcn_on_pages(reseller_bcn, page1, page2, page3):
                self.logger.error("Failed to validate Reseller BCN")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_bcn_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_bcn_error.png"
                return False
            else:
                self.logger.info("Successfully validate Reseller BCN successfully")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_bcn_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Reseller BCN")
            self.logger.exception(e)
            return False

    def do_search_im_order_number(self, im_order_number, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.search_im_order_number(im_order_number)
            self.logger.info("Successfully searched BCN")
            self.logger.info("Successfully searched IM Order number")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_searched_im_order_no_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_searched_im_order_no_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_searched_im_order_no_error.png"
            self.logger.error("Error while searching IM Order number")
            self.logger.exception(e)
            return False

    def do_validate_im_order_number(self, im_order_number, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_im_order_number(im_order_number):
                self.logger.error("Failed to validate IM Order Number")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_im_order_number_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_im_order_number_error.png"
                return False
            else:
                self.logger.info("Successfully validate IM Order Number successfully")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_im_order_number_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating the IM Order Number")
            self.logger.exception(e)
            return False

    def do_search_order_type(self, order_type, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.search_order_type(order_type)
            self.logger.info("Successfully searched Order Type")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_searched_order_type_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_searched_order_type_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_searched_order_type_error.png"
            self.logger.error("Error while searching Order Type")
            self.logger.exception(e)
            return False

    def do_validate_order_type(self, order_type, feature_file_name, screen_shot, page1, page2, page3):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_order_type_on_pages(order_type, page1, page2, page3, feature_file_name):
                self.logger.error("Failed to validate Order Type")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_type_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_type_error.png"
                return False
            else:
                self.logger.info("Successfully validate Order Type successfully")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_order_type_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Order Type")
            self.logger.exception(e)
            return False

    def do_search_reseller_po(self, reseller_po, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.search_reseller_po(reseller_po)
            self.logger.info("Successfully searched Reseller PO")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_searched_reseller_po_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_searched_reseller_po_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_searched_reseller_po_error.png"
            self.logger.error("Error while searching Reseller PO")
            self.logger.exception(e)
            return False

    def do_validate_reseller_po(self, reseller_po, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_reseller_po(reseller_po):
                self.logger.error("Failed to validate Reseller PO")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_reseller_po_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_reseller_po_error.png"
                return False
            else:
                self.logger.info("Successfully validate Reseller PO successfully")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_reseller_po_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Reseller PO")
            self.logger.exception(e)
            return False

    def do_search_vendor_name(self, vendor_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.search_vendor_name(vendor_name)
            self.logger.info("Successfully searched Vendor Name")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_searched_vendor_name_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_searched_vendor_name_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_searched_vendor_name_error.png"
            self.logger.error("Error while searching Vendor name")
            self.logger.exception(e)
            return False

    def do_validate_vendor_name(self, vendor_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_vendor_name(vendor_name):
                self.logger.error("Failed to validate Vendor name")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_vendor_name_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_vendor_name_error.png"
                return False
            else:
                self.logger.info(f"Successfully validate the Vendor name")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_vendor_name_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Vendor Name")
            self.logger.exception(e)
            return False

    def do_search_order_status(self, order_status, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.search_order_status(order_status)
            self.logger.info("Successfully searched Order status")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_searched_order_status_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_searched_order_status_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_searched_order_status_error.png"
            self.logger.error("Error while searching Order Status")
            self.logger.exception(e)
            return False

    def do_validate_order_status(self, order_status, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_order_status(order_status):
                self.logger.error("Failed to validate Order Status")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_status_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_status_error.png"
                return False
            else:
                self.logger.info("Successfully validate Order Status successfully")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_order_status_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Order Status")
            self.logger.exception(e)
            return False

    def do_validate_created_on_ascending(self, feature_file_name, page1, page2, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_created_on_ascending_on_pages(page1, page2, feature_file_name):
                self.logger.error("Failed to validate Order Status")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_ascending_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_ascending_error.png"
                return False
            else:
                self.logger.info("Successfully validate Order Status successfully")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_created_on_ascending_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Created On date in ascending order")
            self.logger.exception(e)
            return False

    def do_validate_created_on_descending(self, feature_file_name, page1, page2, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.do_validate_created_on_descending_on_pages(page1, page2, feature_file_name):
                self.logger.error("Failed to validate Created On date in descending order")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_descending_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_ascending_error.png"
                return False
            else:
                self.logger.info("Successfully validate Created On date in descending order")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_created_on_descending_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Created On date in descending order")
            self.logger.exception(e)
            return False

    def logout_x4a_url(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.logout_x4a():
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
