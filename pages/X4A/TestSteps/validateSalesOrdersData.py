from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4AOrdersSalesOrders import X4ASalesOrdersPage


class ValidateSalesOrdersData:
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
                    & x4a_sales_order.is_end_user_nm_clum_visible() & x4a_sales_order.is_end_user_po_clum_visible()  &
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

    def do_validate_reseller_bcn(self, reseller_bcn, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_bcn_in_pages(reseller_bcn):
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

    def do_validate_reseller_po(self, reseller_po, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_reseller_po_in_pages(reseller_po):
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

    def do_validate_vendor_name(self, vendor_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_vendor_name_in_pages(vendor_name):
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

    def do_validate_order_status(self, order_status, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_order_status_in_pages(order_status):
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

    def click_on_im_order_num(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_im_order_num():
                self.logger.info("Failed to Click on Searched Im order number")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_im_order_number_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Searched Im order number")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_im_order_number_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Searched Im order number")
            self.logger.exception(e)
            return False

    def is_all_tabs_visible(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if (
                    x4a_sales_order.is_order_details_tab_visible() & x4a_sales_order.is_billing_tab_visible() & x4a_sales_order.is_order_lines_tab_visible() &
                    x4a_sales_order.is_order_tracking_tab_visible() & x4a_sales_order.is_addition_attributes_visible()):
                self.logger.info(
                    "Successfully verified that Order Details, Billing, Order Lines, Order Tracking and Additional attributes tabs on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_all_tabs_on_order_details_page_visible_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_all_tabs_on_order_details_page_visible_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_all_tabs_on_order_details_page_visible_error.png"
            self.logger.error("Error while verifying all tabs on Order Details Page")
            self.logger.exception(e)
            return False

    def is_ingram_order_number_and_order_status_title_shown(self, feature_file_name, screen_shot, im_order_number, order_status):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.is_ingram_order_number_and_order_status_title_shown(im_order_number, order_status):
                self.logger.info(
                    "Successfully Verify that title on the header of the order details page contains Ingram order number and the Order Status")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_title_on_order_details_page_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_title_on_order_details_page_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_title_on_order_details_page_error.png"
            self.logger.error(
                "Error while verifying all title on the header of the order details page contains Ingram order number and the Order Status")
            self.logger.exception(e)
            return False

    def is_order_value_header_data_visible(self, feature_file_name, screen_shot, order_value):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.is_order_value_header_data_visible(order_value):
                self.logger.info(
                    "Successfully verified that Order Value header data on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_order_value_header_data_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_order_value_header_data_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_order_value_header_data_error.png"
            self.logger.error("Error while verifying Order Value header data")
            self.logger.exception(e)
            return False

    def is_order_type_header_data_visible(self, feature_file_name, screen_shot, order_type):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.is_order_type_header_data_visible(order_type):
                self.logger.info(
                    "Successfully verified that Order Type header data on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_order_type_header_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_order_type_header_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_order_type_header_error.png"
            self.logger.error("Error while verifying Order Type header data")
            self.logger.exception(e)
            return False

    def validate_fields_under_reference_no(self, feature_file_name, screen_shot, reference_numbers_list):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            end_user_po = reference_numbers_list[0]
            reseller_po = reference_numbers_list[1]
            vendor_order = reference_numbers_list[2]
            vendor_sales_order = reference_numbers_list[3]

            if (x4a_sales_order.is_end_user_po_field_visible(
                    end_user_po) & x4a_sales_order.is_reseller_po_field_visible(
                reseller_po) & x4a_sales_order.is_vendor_order_field_visible(vendor_order) &
                    x4a_sales_order.is_vendor_sales_order_field_visible(vendor_sales_order)):
                self.logger.info(
                    "Successfully verified that End user PO, Reseller PO, Vendor Order, Vendor ales Order fields under Reference number on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_fields_under_reference_num_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_fields_under_reference_num_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_fields_under_reference_num_error.png"
            self.logger.error(
                "Error while verifying End user PO, Reseller PO, Vendor Order, Vendor ales Order fields under Reference number on Order Details page")
            self.logger.exception(e)
            return False

    def click_on_billing_tab(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_billing_tab():
                self.logger.info("Failed to Click on Billing tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_billing_tab_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Searched Im order number")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_billing_tab_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Billing tab")
            self.logger.exception(e)
            return False

    def click_on_order_details_tab(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_order_details_tab():
                self.logger.info("Failed to Click on Order Details tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_order_details_tab_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Order Details tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_order_details_tab_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Order Details tab")
            self.logger.exception(e)
            return False

    def click_on_order_lines_tab(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_order_lines_tab():
                self.logger.info("Failed to Click on Order lines tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_order_lines_tab_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Order lines tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_order_lines_tab_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Order Details tab")
            self.logger.exception(e)
            return False

    def click_on_order_tracking_tab(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_order_tracking_details_tab():
                self.logger.info("Failed to Click on Order Tracking tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_order_tracking_tab_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Order Tracking tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_order_tracking_tab_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Order Tracking tab")
            self.logger.exception(e)
            return False

    def click_on_additional_attr_tab(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_additional_attr_tab():
                self.logger.info("Failed to Click on Additional attributes tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_additional_attr_tab_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Additional attributes tab")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_additional_attr_tab_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Additional attributes tab")
            self.logger.exception(e)
            return False

    def validate_fields_under_bill_to_info(self, feature_file_name, screen_shot, billing_to_info_list):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            bill_to_id = billing_to_info_list[0]
            bill_to_company_name = billing_to_info_list[1]
            bill_to_address = billing_to_info_list[2]
            bill_to_contact = billing_to_info_list[3]
            bill_to_phone_no = billing_to_info_list[4]
            bill_to_email = billing_to_info_list[5]

            if (x4a_sales_order.is_bill_to_id_field_visible(
                    bill_to_id) & x4a_sales_order.is_company_nm_bill_field_visible(bill_to_company_name) &
                    x4a_sales_order.is_address_bill_field_visible(
                        bill_to_address) & x4a_sales_order.is_contact_bill_field_visible(bill_to_contact) &
                    x4a_sales_order.is_phone_no_bill_field_visible(
                        bill_to_phone_no) & x4a_sales_order.is_email_bill_field_visible(bill_to_email)):
                self.logger.info(
                    "Successfully verified that fields under Bill to info section on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_fields_under_bill_to_info_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_fields_under_bill_to_info_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_fields_under_bill_to_info_error.png"
            self.logger.error(
                "Error while verifying fields under Bill to info section on Order Details page")
            self.logger.exception(e)
            return False

    def validate_fields_under_ship_to_info(self, feature_file_name, screen_shot, ship_to_info_list):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            ship_to_id = ship_to_info_list[0]
            ship_to_cmp_nm = ship_to_info_list[1]
            ship_to_addr = ship_to_info_list[2]
            ship_to_contact = ship_to_info_list[3]
            ship_to_phn_no = ship_to_info_list[4]
            ship_to_email = ship_to_info_list[5]
            ship_to_shipping_comment = ship_to_info_list[6]

            if (x4a_sales_order.is_ship_to_id_field_visible(
                    ship_to_id) & x4a_sales_order.is_company_nm_ship_field_visible(ship_to_cmp_nm) &
                    x4a_sales_order.is_address_ship_field_visible(
                        ship_to_addr) & x4a_sales_order.is_contact_ship_field_visible(ship_to_contact) &
                    x4a_sales_order.is_phone_no_ship_field_visible(
                        ship_to_phn_no) & x4a_sales_order.is_email_ship_field_visible(ship_to_email) &
                    x4a_sales_order.is_shipping_comment_ship_field_visible(ship_to_shipping_comment)):
                self.logger.info(
                    "Successfully verified that fields under Bill to info section on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_fields_under_bill_to_info_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_fields_under_bill_to_info_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_fields_under_bill_to_info_error.png"
            self.logger.error(
                "Error while verifying fields under Bill to info section on Order Details page")
            self.logger.exception(e)
            return False

    def validate_fields_under_end_user_info(self, feature_file_name, screen_shot, end_user_info_list):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            end_user_id = end_user_info_list[0]
            end_user_cmp_nm = end_user_info_list[1]
            end_user_addr = end_user_info_list[2]
            end_user_contact = end_user_info_list[3]
            end_user_phn_no = end_user_info_list[4]
            end_user_email = end_user_info_list[5]

            if (x4a_sales_order.is_end_user_id_field_visible(
                    end_user_id) & x4a_sales_order.is_company_nm_end_user_field_visible(end_user_cmp_nm) &
                    x4a_sales_order.is_address_end_user_field_visible(
                        end_user_addr) & x4a_sales_order.is_contact_end_user_field_visible(end_user_contact) &
                    x4a_sales_order.is_phone_no_end_user_field_visible(
                        end_user_phn_no) & x4a_sales_order.is_email_end_user_field_visible(end_user_email)):
                self.logger.info(
                    "Successfully verified that fields under End user info section on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_fields_under_end_user_info_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_fields_under_end_user_info_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_fields_under_end_user_info_error.png"
            self.logger.error(
                "Error while verifying fields under End user info section on Order Details page")
            self.logger.exception(e)
            return False

    def validate_fields_under_order_lines_tab(self, feature_file_name, screen_shot, order_lines_tab_info_list):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            order_line = order_lines_tab_info_list[0]
            order_line_status = order_lines_tab_info_list[1]
            order_line_description = order_lines_tab_info_list[2]
            order_line_vpn_no = order_lines_tab_info_list[3]
            order_line_im_part = order_lines_tab_info_list[4]
            order_line_special_bid_no = order_lines_tab_info_list[5]
            order_line_unit_price = order_lines_tab_info_list[6]
            order_line_extended_price = order_lines_tab_info_list[7]
            order_line_cost = order_lines_tab_info_list[8]
            order_line_extended_cost = order_lines_tab_info_list[9]
            order_line_margin = order_lines_tab_info_list[10]
            order_line_currency_code = order_lines_tab_info_list[11]
            order_line_quantity = order_lines_tab_info_list[12]
            order_line_quantity_confirmed = order_lines_tab_info_list[13]
            order_line_quantity_backordered = order_lines_tab_info_list[14]
            Order_line_notes = order_lines_tab_info_list[15]

            if (x4a_sales_order.is_order_line_field_visible(order_line) &
                    x4a_sales_order.is_order_line_status_field_visible(
                        order_line_status) & x4a_sales_order.is_order_line_description_field_visible(
                        order_line_description) &
                    x4a_sales_order.is_contact_vpn_no_field_visible(order_line_vpn_no) &
                    x4a_sales_order.is_order_line_im_part_field_visible(
                        order_line_im_part) & x4a_sales_order.is_order_line_special_bid_field_visible(
                        order_line_special_bid_no) &
                    x4a_sales_order.is_order_line_unit_price_field_visible(
                        order_line_unit_price) & x4a_sales_order.is_order_line_extended_price_field_visible(
                        order_line_extended_price) &
                    x4a_sales_order.is_order_line_cost_field_visible(
                        order_line_cost) & x4a_sales_order.is_order_line_ext_cost_field_visible(
                        order_line_extended_cost) &
                    x4a_sales_order.is_order_line_margin_field_visible(
                        order_line_margin) & x4a_sales_order.is_order_line_currency_code_field_visible(
                        order_line_currency_code) &
                    x4a_sales_order.is_order_line_quantity_field_visible(order_line_quantity) &
                    x4a_sales_order.is_order_line_qty_confirmed_field_visible(
                        order_line_quantity_confirmed) & x4a_sales_order.is_order_line_qty_backordered_field_visible(
                        order_line_quantity_backordered) &
                    x4a_sales_order.is_order_line_notes_field_visible(Order_line_notes)):
                self.logger.info(
                    "Successfully verified that fields under Order lines tab on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_fields_under_end_user_info_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_fields_under_order_lines_atb_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_fields_under_order_lines_tab_error.png"
            self.logger.error(
                "Error while verifying fields under Order lines tab on Order Details page")
            self.logger.exception(e)
            return False

    def click_on_view_more_option(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_view_more_option():
                self.logger.info("Failed to Click on Serial numbers View more option")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_serial_no_view_more_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Serial numbers View more option")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_serial_no_view_more_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Serial numbers View more option")
            self.logger.exception(e)
            return False

    def validate_fields_under_serial_numbers_header(self, feature_file_name, screen_shot, serial_numbers_info_list):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            serial_no_line_number = serial_numbers_info_list[0]
            serial_no_description = serial_numbers_info_list[1]
            serial_no_vpn_no = serial_numbers_info_list[2]
            serial_no_im_part = serial_numbers_info_list[3]
            serial_no_quantity = serial_numbers_info_list[4]

            if (x4a_sales_order.is_serial_line_no_field_visible(
                    serial_no_line_number) & x4a_sales_order.is_serial_no_description_field_visible(
                    serial_no_description) &
                    x4a_sales_order.is_serial_no_vpn_no_field_visible(
                        serial_no_vpn_no) & x4a_sales_order.is_serial_no_im_part_field_visible(serial_no_im_part) &
                    x4a_sales_order.is_serial_no_quantity_field_visible(serial_no_quantity)):
                self.logger.info(
                    "Successfully verified that fields under Order lines tab on Order Details page")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_fields_under_end_user_info_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_fields_under_order_lines_atb_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_fields_under_order_lines_tab_error.png"
            self.logger.error(
                "Error while verifying fields under Order lines tab on Order Details page")
            self.logger.exception(e)
            return False

    def click_on_additional_attr_view_more_button(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_on_additional_attr_view_more_button():
                self.logger.info("Failed to Click on Additional attribute View more option")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_click_on_additional_attr_view_more_failed.png")
                return False
            else:
                self.logger.info("Successfully Click on Additional attribute View more option")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_click_on_additional_attr_view_more_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Click on Additional attribute View more option")
            self.logger.exception(e)
            return False

    def validate_fields_under_additional_attribute_header(self, feature_file_name, screen_shot,
                                                          additional_attr_info_list):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            icmstaxamount_name_value = additional_attr_info_list[0]
            othertaxamount_name_value = additional_attr_info_list[1]
            rollswitch_name_value = additional_attr_info_list[2]

            if (x4a_sales_order.is_icmstaxamount_nm_and_value_visible(icmstaxamount_name_value) &
                    x4a_sales_order.is_othertaxamount_nm_and_value_visible(othertaxamount_name_value) &
                    x4a_sales_order.is_rollswitch_nm_and_value_visible(rollswitch_name_value)):
                self.logger.info(
                    "Successfully verified that Additional attribute name and Value")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_additional_attr_nm_value_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_additional_attr_nm_value_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_additional_attr_nm_value_error.png"
            self.logger.error(
                "Error while verifying fields under Additional attribute name and Value")
            self.logger.exception(e)
            return False

    def filter_by_im_order(self, feature_file_name, screen_shot, im_order):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.filter_by_im_order(im_order):
                self.logger.info(
                    "Successfully filtered by im order")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_filtered_by_im_order_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_by_im_order_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_filter_by_im_order_error.png"
            self.logger.error(
                "Error while filtering by im order")
            self.logger.exception(e)
            return False

    def verify_im_order_filter_results(self, feature_file_name, screen_shot, im_order):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.verify_im_order(im_order):
                self.logger.info(
                    "Successfully verified filter by im order result")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_verified_filter_by_im_order_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_verify_filter_by_im_order_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_verify_filter_by_im_order_error.png"
            self.logger.error(
                "Error while verifying filter by im order results")
            self.logger.exception(e)
            return False

    def do_filter_order_type(self, order_type, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_order_type(order_type)
            self.logger.info("Successfully filtered Order Type")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_order_type_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_order_type_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_order_type_error.png"
            self.logger.error("Error while filtering Order Type")
            self.logger.exception(e)
            return False

    def verify_order_type_filter_results(self, feature_file_name, screen_shot, order_type):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.verify_filter_order_type_in_pages(order_type):
                self.logger.info(
                    "Successfully verified filter by order type result")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_verified_filter_by_order_type_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_verify_filter_by_order_type_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_verify_filter_by_order_type_error.png"
            self.logger.error(
                "Error while verifying filter by order type results")
            self.logger.exception(e)
            return False

    def do_filter_bcn(self, bcn, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_bcn(bcn)
            self.logger.info("Successfully filtered BCN")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_bcn_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_bcn_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_bcn_error.png"
            self.logger.error("Error while filtering BCN")
            self.logger.exception(e)
            return False

    def do_filter_reseller_po(self, reseller_po, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_reseller_po(reseller_po)
            self.logger.info("Successfully filtered Reseller PO")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_reseller_po_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_reseller_po_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_reseller_po_error.png"
            self.logger.error("Error while filtering Reseller PO")
            self.logger.exception(e)
            return False

    def do_validate_reseller_name(self, reseller_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_reseller_name_in_pages(reseller_name):
                self.logger.error("Failed to validate Reseller Name")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_reseller_name_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_reseller_name_error.png"
                return False
            else:
                self.logger.info("Successfully validate Reseller Name")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_reseller_name_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Reseller Name")
            self.logger.exception(e)
            return False

    def do_filter_reseller_name(self, reseller_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_reseller_name(reseller_name)
            self.logger.info("Successfully filtered Reseller Name")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_reseller_name_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_reseller_name_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_reseller_name_error.png"
            self.logger.error("Error while filtering Reseller Name")
            self.logger.exception(e)
            return False

    def do_filter_vendor_name(self, vendor_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_vendor_name(vendor_name)
            self.logger.info("Successfully filtered Vendor Name")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_vendor_name_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_vendor_name_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_vendor_name_error.png"
            self.logger.error("Error while filtering Vendor Name")
            self.logger.exception(e)
            return False

    def do_filter_end_user_name(self, end_user_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_end_user_name(end_user_name)
            self.logger.info("Successfully filtered End User Name")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_end_user_name_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_end_user_name_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_end_user_name_error.png"
            self.logger.error("Error while filtering End User Name")
            self.logger.exception(e)
            return False

    def do_validate_end_user_name(self, end_user_name, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_end_user_name_in_pages(end_user_name):
                self.logger.error("Failed to validate End User Name")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_end_user_name_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_end_user_name_error.png"
                return False
            else:
                self.logger.info("Successfully validate End User Name")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_end_user_name_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating End User Name")
            self.logger.exception(e)
            return False

    def do_filter_order_status(self, order_status, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_order_status(order_status)
            self.logger.info("Successfully filtered Order Status")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_order_status_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_order_status_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_order_status_error.png"
            self.logger.error("Error while filtering Order Status")
            self.logger.exception(e)
            return False

    def do_filter_order_value(self, min_order_value, max_order_value, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_order_value(min_order_value, max_order_value)
            self.logger.info("Successfully filtered Order Value")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_order_value_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_order_value_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_order_value_error.png"
            self.logger.error("Error while filtering Order Value")
            self.logger.exception(e)
            return False

    def do_validate_order_value(self, min_order_value, max_order_value , feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_order_value_in_pages(min_order_value, max_order_value):
                self.logger.error("Failed to validate Order Value")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_value_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_value_error.png"
                return False
            else:
                self.logger.info("Successfully validate Order Value")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_order_value_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Order Value")
            self.logger.exception(e)
            return False

    def do_filter_created_on(self, created_on, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            x4a_sales_order.filter_by_created_on(created_on)
            self.logger.info("Successfully filtered Created On")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_filtered_created_on_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_filter_created_on_error.png")
            screen_shot[
                "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_filter_created_on_error.png"
            self.logger.error("Error while filtering Created On")
            self.logger.exception(e)
            return False

    def do_validate_created_on(self, created_on, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_filter_by_created_on_in_pages(created_on):
                self.logger.error("Failed to validate Created On")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_error.png"
                return False
            else:
                self.logger.info("Successfully validate Created On")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_created_on_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Created On")
            self.logger.exception(e)
            return False


    def do_validate_update_end_user_po_and_reseller_po(self, end_user_po, reseller_po, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.validate_update_end_user_po_and_reseller_po(end_user_po, reseller_po):
                self.logger.error("Failed to validate Update for end user po and reseller po")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_update_end_user_and_reseller_po_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_update_end_user_and_reseller_po_error.png"
                return False
            else:
                self.logger.info("Successfully validated Update for end user po and reseller po")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_update_end_user_and_reseller_po_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating Update for end user po and reseller po")
            self.logger.exception(e)
            return False

    def do_validate_cancel_update_of_end_user_po_and_reseller_po(self, end_user_po, reseller_po, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.validate_cancel_end_user_po_and_reseller_po(end_user_po, reseller_po):
                self.logger.error("Failed to validate cancel Update for end user po and reseller po")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_cancel_update_end_user_and_reseller_po_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_cancel_update_end_user_and_reseller_po_error.png"
                return False
            else:
                self.logger.info("Successfully validated cancel Update for end user po and reseller po")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validate_cancel_update_end_user_and_reseller_po_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating cancel Update for end user po and reseller po")
            self.logger.exception(e)
            return False

    def do_validate_acop_field(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.validate_acop_field():
                self.logger.error("Failed to validate ACOP field")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_acop_field_error.png")
                screen_shot[
                    "path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_acop_field_error.png"
                return False
            else:
                self.logger.info("Successfully validated ACOP field")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name + "_validated_acop_field_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating ACOP field")
            self.logger.exception(e)
            return False

    def validate_order_status_to_edit(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.validate_order_status_to_check_if_editable():
                self.logger.info(
                    "Successfully Verified the Order Status, order can be edited")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_validated_order_details_status_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_title_on_order_details_page_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_order_details_status_error.png"
            self.logger.error(
                "Error while verifying Order Status")
            self.logger.exception(e)
            return False

    def update_order_line_and_validate_data(self, special_bid, unit_price, quantity, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if (x4a_sales_order.update_order_line(special_bid, unit_price,quantity) & x4a_sales_order.click_order_line_edit_check_icon()):
                self.logger.info(
                    "Successfully updated the order line")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_updated_order_line_successfully.png")
            ui_data = x4a_sales_order.get_order_line_data()
            self.logger.info("Validating data for order line")
            calculated_margin = round(((float(unit_price)-float(ui_data['cost']))/float(unit_price)) * 100, 2)
            assert str(special_bid) == str(ui_data['special_bid']), "Special bid mismatched"
            assert str(unit_price) == str(ui_data['unit_price']), "Unit price mismatched"
            assert str(quantity) == str(ui_data['quantity']), "Quantity mismatched"
            assert str(calculated_margin) == str(ui_data['margin']), "Margin Mismatched"
            # assert int(ui_data['quantity']) == (int(ui_data['quantity_confirmed']) + int(ui_data['quantity_backordered'])), "Quantity calculation mismatched"
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_update_order_line_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_update_order_line_error.png"
            self.logger.error(
                "Error while updating order line")
            self.logger.exception(e)
            return False

    def cancel_order_line_changes_and_validate_data(self, special_bid, unit_price, quantity, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if (x4a_sales_order.update_order_line(special_bid, unit_price,quantity) & x4a_sales_order.click_order_line_edit_cancel_icon()):
                self.logger.info(
                    "Successfully cancelled updated the order line")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_cancel_updated_order_line_successfully.png")
            ui_data = x4a_sales_order.get_order_line_data()
            self.logger.info("Validating data for order line")
            calculated_margin = round(((float(unit_price)-float(ui_data['cost']))/float(unit_price)) * 100, 2)
            assert str(special_bid) != str(ui_data['special_bid']), "Special bid matched"
            assert str(unit_price) != str(ui_data['unit_price']), "Unit price matched"
            assert str(quantity) != str(ui_data['quantity']), "Quantity matched"
            assert str(calculated_margin) != str(ui_data['margin']), "Margin matched"
            # assert int(ui_data['quantity']) == (int(ui_data['quantity_confirmed']) + int(ui_data['quantity_backordered'])), "Quantity calculation mismatched"
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_cancel_updated_order_line_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_cancel_updated_order_line_error.png"
            self.logger.error(
                "Error while updating order line")
            self.logger.exception(e)
            return False


    def validate_options_on_order_lines(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.check_cancel_options_are_correct_in_order_lines():
                self.logger.info(
                    "Successfully Verified that Order lines options")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_validated_order_status_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_order_status_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_order_status_error.png"
            self.logger.error(
                "Error while verifying Order lines options")
            self.logger.exception(e)
            return False

    def click_on_mark_for_cancel(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.click_on_mark_for_cancel():
                self.logger.info(
                    "Successfully clicked on mark for order")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_mark_for_cancel_clicked_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_click_mark_for_cancel_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_click_mark_for_cancel_error.png"
            self.logger.error(
                "Error while clicking on mark for cancel")
            self.logger.exception(e)
            return False

    def click_on_unmark_for_cancel(self, feature_file_name, screen_shot):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if x4a_sales_order.click_on_unmark_for_cancel():
                self.logger.info(
                    "Successfully clicked on unmark for order")
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                    + "_unmark_for_cancel_clicked_successfully.png")
                return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_click_unmark_for_cancel_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_click_unmark_for_cancel_error.png"
            self.logger.error(
                "Error while clicking on unmark for cancel")

    def validate_order_status(self, feature_file_name, status):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.order_status_validate(status):
                self.logger.info("Failed to validate order status")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_order_status_failed.png")
                return False
            else:
                self.logger.info("Successfully validated order status")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_order_status_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating order status")
            self.logger.exception(e)
            return False

    def validate_cancel_order_button_displayed(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.verify_cancel_order_button():
                self.logger.info("Failed to verify cancel order button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_validate_cancel_order_failed.png")
                return False
            else:
                self.logger.info("Successfully validated cancel order button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_cancel_order_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while validating cancel order button")
            self.logger.exception(e)
            return False

    def click_on_cancel_order_btn(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.click_cancel_order_btn():
                self.logger.info("Failed to click cancel order button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "cancel_order_click_failed.png")
                return False
            else:
                self.logger.info("Successfully clicked cancel order button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "cancel_order_click_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while clicking cancel order button")
            self.logger.exception(e)
            return False

    def cancel_order_alert_elements(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.validate_cancel_order_alert_elements():
                self.logger.info("Failed to verify cancel order alert elements")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "cancel_order_alert_elements_failed.png")
                return False
            else:
                self.logger.info("Successfully verified cancel order alert elements")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "cancel_order_alert_elements_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while verifying cancel order alert elements")
            self.logger.exception(e)
            return False

    def click_cancel_order(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.cancel_order_click():
                self.logger.info("Failed to click cancel order confirmation button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "cancel_order_confirmation_click_failed.png")
                return False
            else:
                self.logger.info("Successfully clicked cancel order confirmation button")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "cancel_order_confirmation_click_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while clicking cancel order confirmation button")
            self.logger.exception(e)
            return False

    def success_message_verify(self, feature_file_name):
        x4a_sales_order = X4ASalesOrdersPage(self.driver)
        try:
            if not x4a_sales_order.validate_toast_notification():
                self.logger.info("Failed to verify success notification")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "success_notification_verification_failed.png")
                return False
            else:
                self.logger.info("Successfully verified notification message")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "success_notification_verification_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while verifying success toast notification")
            self.logger.exception(e)
            return False
