import time
from selenium.webdriver.common.by import By
from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile
from selenium.webdriver import ActionChains, Keys
from datetime import datetime
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService


class X4ASalesOrdersPage(BasePage):
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

    ORDER_MENU = (By.XPATH, "//*[@data-testid='orders-MenuItem']")
    SALES_ORDER_OPTION = (By.XPATH, "//*[text()='Sales Orders']")
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BOX_SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    ORDER_BCN_ITEM_LIST = (By.XPATH,
                           "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='customerNumber']")
    PAGINATION = (By.XPATH,
                  "//div[@class='MuiInputBase-root MuiInputBase-colorPrimary css-1eyhk8h-MuiInputBase-root-MuiTablePagination-select']")
    ORDER_DATE_XPATH = "//*[@id='root']/div/div[2]/div[1]/div/div[5]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[9]"
    SALES_ORDER_TABLE = "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']"
    IM_ORDER_NUMBER_LIST = (By.XPATH,
                            "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderNumber']")
    ORDER_TYPE_LIST = (By.XPATH,
                       "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderTypeName']")
    VENDOR_NAME_LIST = (By.XPATH,
                        "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='vendorName']")
    RESELLER_PO_LIST = (By.XPATH,
                        "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='customerOrderNumber']")

    ORDER_STATUS_LIST = (By.XPATH,
                         "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderStatus']")

    SALES_ORDER_PAGE = (By.XPATH, "//h2[text()='Sales orders']")
    IM_ORDER = (By.XPATH, "//div[text()='IM Order #']")
    TYPE = (By.XPATH, "//div[text()='Type']")
    BCN = (By.XPATH, "//div[text()='BCN']")
    RESELLER_PO = (By.XPATH, "//div[text()='Reseller PO#']")
    RESELLER_NAME = (By.XPATH, "//div[text()='Reseller name']")
    VENDOR_NAME = (By.XPATH, "//div[text()='Vendor name']")
    END_USER_NAME = (By.XPATH, "//div[text()='End user name']")
    END_USER_PO = (By.XPATH, "//div[text()='End user PO#']")
    ORDER_VALUE = (By.XPATH, "//div[text()='Order value']")
    ORDER_STATUS = (By.XPATH, "//div[text()='Order status']")
    CREATED_ON = (By.XPATH, "//div[text()='Created on']")
    CREATED_ON_FIRST_VALUE = (By.XPATH, "//*[@role='cell'] [@data-field='orderCreateDate'][1]")
    CREATED_ON_LIST = (By.XPATH,
                       "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderCreateDate']")
    ARROWUPWARDICON = (By.XPATH, "//*[text()='Created on']/parent::div//*[@data-testid='ArrowUpwardIcon']")
    USER_DROPDOWN = (By.XPATH, "//*[@data-testid='KeyboardArrowDownIcon']")
    LOGOUT = (By.XPATH, "//*[text()='LogOut']")

    """constructor of the Login Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_sales_orders(self):
        try:
            self.do_click_by_locator(self.ORDER_MENU)
            self.do_double_click(self.SALES_ORDER_OPTION)
            self.logger.info("Clicked on Sales Orders in the menu")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Sales orders ' + str(e))
            raise e

    def is_sales_orders_listing_page_visible(self):
        try:
            self.do_check_visibility(self.SALES_ORDER_PAGE)
            self.logger.info("Successfully verified Sales Orders listing page")
        except Exception as e:
            self.logger.error('Exception occurred while verifying Sales Orders listing page ' + str(e))
            raise e

    def is_im_order_clum_visible(self):
        try:
            self.do_check_visibility(self.IM_ORDER)
            self.logger.info("Successfully verified the IM Order Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying IM Order column Sales Orders listing page ' + str(e))
            return False

    def is_type_clum_visible(self):
        try:
            self.do_check_visibility(self.TYPE)
            self.logger.info("Successfully verified the Type Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Type Column on Sales Orders listing page ' + str(e))
            return False

    def is_bcn_clum_visible(self):
        try:
            self.do_check_visibility(self.BCN)
            self.logger.info("Successfully verified the BCN Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying BCN Column on Sales Orders listing page ' + str(e))
            return False

    def is_reseller_po_clum_visible(self):
        try:
            self.do_check_visibility(self.RESELLER_PO)
            self.logger.info("Successfully verified the BCN Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Reseller PO Column on Sales Orders listing page ' + str(e))
            return False

    def is_reseller_nm_clum_visible(self):
        try:
            self.do_check_visibility(self.RESELLER_NAME)
            self.logger.info("Successfully verified the Reseller number Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying BCN Column on Sales Orders listing page ' + str(e))
            return False

    def is_vendor_nm_clum_visible(self):
        try:
            self.do_check_visibility(self.VENDOR_NAME)
            self.logger.info("Successfully verified the Vendor Name Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Vendor Name Column on Sales Orders listing page ' + str(e))
            return False

    def is_end_user_nm_clum_visible(self):
        try:
            self.do_check_visibility(self.END_USER_NAME)
            self.logger.info("Successfully verified the End User name Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying End User name Column on Sales Orders listing page ' + str(e))
            return False

    def is_end_user_po_clum_visible(self):
        try:
            self.do_check_visibility(self.END_USER_PO)
            self.logger.info("Successfully verified the End User PO Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying End User PO Column on Sales Orders listing page ' + str(e))
            return False

    def is_order_value_clum_visible(self):
        try:
            element = "//div[text()='Order value']"
            order_value_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(order_value_element)
            self.do_check_visibility(self.ORDER_VALUE)
            self.logger.info("Successfully verified the Order Value Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order Value Column on Sales Orders listing page ' + str(e))
            return False

    def is_order_status_clum_visible(self):
        try:
            element = "//div[text()='Order status']"
            order_status_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(order_status_element)
            self.do_check_visibility(self.ORDER_STATUS)
            self.logger.info("Successfully verified the Order Status Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order Status Column on Sales Orders listing page ' + str(e))
            return False

    def is_created_on_clum_visible(self):
        try:
            element = "//div[text()='Created on']"
            created_on_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(created_on_element)
            self.do_check_visibility(self.CREATED_ON)
            self.logger.info("Successfully verified the Created on Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Created on Column on Sales Orders listing page ' + str(e))
            return False

    def search_bcn(self, reseller_bcn):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, reseller_bcn)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_bcn = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Search BCN: {search_bcn}')
            assert str(search_bcn) == str(reseller_bcn)
            self.logger.info("Search Reseller BCN match successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search reseller bcn %s", e)
            raise e

    def do_validate_bcn_on_pages(self, bcn, page1, page2, page3):
        try:
            if self.do_validate_bcn(bcn, page1):
                if self.do_validate_bcn(bcn, page2):
                    if self.do_validate_bcn(bcn, page3):
                        self.logger.info(f'Successfully validate Reseller BCN on {page1}, {page2} and {page3} number')
                        return True
                    else:
                        self.logger.error(f'Failed to validate the Reseller BCN on page {page3} number')
                        return False
                else:
                    self.logger.error(f'Failed to validate the Reseller BCN on page {page2} number')
                    return False
            else:
                self.logger.error(f'Failed to validate the Reseller BCN on page {page1} number')
                return False
        except Exception as e:
            self.logger.error("Not able to validate reseller bcn")
            return False

    def do_validate_bcn(self, bcn, page_number):
        try:
            self.go_to_page(page_number)
            bcn_item_list = self.get_all_elements(self.ORDER_BCN_ITEM_LIST)
            self.logger.info("length of list %s" % len(bcn_item_list))
            self.scroll()
            bcn_item_list = self.get_all_elements(self.ORDER_BCN_ITEM_LIST)
            self.logger.info("length of list %s" % len(bcn_item_list))
            count = 0
            for bcn_item in bcn_item_list:
                if str(bcn) in bcn_item.text:
                    count = count + 1
                else:
                    return False
            if count == len(bcn_item_list):
                return True
            self.logger.info(f'Total number of Reseller BCN count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate reseller bcn")
            return False

    def scroll(self):
        try:
            actions = ActionChains(self.driver)
            target = self.driver.find_element(By.XPATH,
                                              "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']")
            for s in range(2):
                actions.send_keys_to_element(target, Keys.PAGE_DOWN).perform()
            self.logger.info("Scrolled!")
        except Exception as e:
            print('error scrolling down web element', e)

    def search_im_order_number(self, im_order_number):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, im_order_number)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_im_order_no = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Search IM Order No: {search_im_order_no}')
            assert str(search_im_order_no) == str(im_order_number)
            self.logger.info("Searched IM Order No match successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search IM Order No %s", e)
            raise e

    def do_validate_im_order_number(self, im_order_number):
        try:
            im_order_number_list = self.get_all_elements(self.IM_ORDER_NUMBER_LIST)
            self.logger.info("length of list %s" % len(im_order_number_list))
            self.scroll()
            im_order_number_list = self.get_all_elements(self.IM_ORDER_NUMBER_LIST)
            self.logger.info("length of list %s" % len(im_order_number_list))
            count = 0
            for im_order_number_item in im_order_number_list:
                if str(im_order_number) in im_order_number_item.text:
                    count = count + 1
                else:
                    return False
            if count == len(im_order_number_list):
                return True
            self.logger.info(f'Total number of IM Order Number count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate IM Order Number")
            return False

    def search_order_type(self, order_type):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, order_type)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_order_type = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Search Order Type: {search_order_type}')
            assert str(search_order_type) == str(order_type)
            self.logger.info("Searched Order Type match successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search Order Type %s", e)
            raise e

    def do_validate_order_type_on_pages(self, bcn, page1, page2, page3, feature_file_name):
        try:
            if self.do_validate_order_type(bcn, page1):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_order_type_successfully.png")
                if self.do_validate_order_type(bcn, page2):
                    self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                                + "_validate_order_type_successfully.png")
                    if self.do_validate_order_type(bcn, page3):
                        self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                                    + "_validate_order_type_successfully.png")
                        self.logger.info(f'Successfully validate Order Type on {page1}, {page2} and {page3} number')
                        return True
                    else:
                        self.driver.save_screenshot(
                            self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_type_on_page_error.png")
                        self.logger.error(f'Failed to validate the Order Type on page {page3} number')
                        return False
                else:
                    self.driver.save_screenshot(
                        self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_type_on_page_error.png")
                    self.logger.error(f'Failed to validate the Order Type on page {page2} number')
                    return False
            else:
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_order_type_on_page_error.png")
                self.logger.error(f'Failed to validate the Order Type on page {page1} number')
                return False
        except Exception as e:
            self.logger.error("Not able to validate Order Type")
            return False

    def do_validate_order_type(self, order_type, page_number):
        try:
            self.go_to_page(page_number)
            order_type_list = self.get_all_elements(self.ORDER_TYPE_LIST)
            self.logger.info("length of list %s" % len(order_type_list))
            self.scroll()
            order_type_list = self.get_all_elements(self.ORDER_TYPE_LIST)
            self.logger.info("length of list %s" % len(order_type_list))
            count = 0
            for order_type_list_item in order_type_list:
                if str(order_type) in order_type_list_item.text:
                    count = count + 1
                else:
                    return False
            if count == len(order_type_list):
                return True
            self.logger.info(f'Total number of Order Type count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate Order Type")
            return False

    def search_reseller_po(self, reseller_po):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, reseller_po)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_reseller_po = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Search Vendor name: {search_reseller_po}')
            assert str(search_reseller_po) == str(reseller_po)
            self.logger.info("Searched Vendor Name match successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search Vendor name %s", e)
            raise e

    def do_validate_reseller_po(self, reseller_po):
        try:
            reseller_po_list = self.get_all_elements(self.VENDOR_NAME_LIST)
            self.logger.info("length of list %s" % len(reseller_po_list))
            self.scroll()
            reseller_po_list = self.get_all_elements(self.VENDOR_NAME_LIST)
            self.logger.info("length of list %s" % len(reseller_po_list))
            count = 0
            for reseller_po_list_item in reseller_po_list:
                if str(reseller_po) in reseller_po_list_item.text:
                    count = count + 1
                else:
                    return False
            if count == len(reseller_po_list):
                return True
            self.logger.info(f'Total number of Vendor name count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate Vendor name")
            return False

    def search_vendor_name(self, vendor_name):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, vendor_name)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_vendor_name = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Search Vendor name: {search_vendor_name}')
            assert str(search_vendor_name) == str(vendor_name)
            self.logger.info("Searched Vendor Name match successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search Vendor name %s", e)
            raise e

    def do_validate_vendor_name(self, vendor_name):
        try:
            order_type_list = self.get_all_elements(self.VENDOR_NAME_LIST)
            self.logger.info("length of list %s" % len(order_type_list))
            self.scroll()
            order_type_list = self.get_all_elements(self.VENDOR_NAME_LIST)
            self.logger.info("length of list %s" % len(order_type_list))
            count = 0
            for order_type_list_item in order_type_list:
                if str(vendor_name) in order_type_list_item.text:
                    count = count + 1
                else:
                    return False
            if count == len(order_type_list):
                return True
            self.logger.info(f'Total number of Vendor name count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate Vendor name")
            return False

    def search_order_status(self, order_status):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, order_status)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_order_status = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Searched Order Status: {search_order_status}')
            assert str(search_order_status) == str(order_status)
            self.logger.info("Searched Order status match successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search Order status %s", e)
            raise e

    def do_validate_order_status(self, order_status):
        try:
            element = "//div[text()='Order status']"
            order_status_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(order_status_element)
            order_status_list = self.get_all_elements(self.ORDER_STATUS_LIST)
            self.logger.info("length of list %s" % len(order_status_list))
            self.scroll()
            order_status_list = self.get_all_elements(self.ORDER_STATUS_LIST)
            self.logger.info("length of list %s" % len(order_status_list))
            count = 0
            for order_status_list_item in order_status_list:
                if str(order_status) in order_status_list_item.text:
                    count = count + 1
                    self.logger.info(f'Count: {count}')
                else:
                    return False
            if count == len(order_status_list):
                return True
            self.logger.info(f'Total number of Order Status count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate Order Status")
            return False

    def do_validate_created_on_ascending_on_pages(self, page1, page2, feature_file_name):
        try:
            if self.do_validate_created_on_ascending(page1):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_created_on_date_ascending_successfully.png")
                if self.do_validate_created_on_ascending(page2):
                    self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                                + "_validate_created_on_date_ascending_successfully.png")
                    self.logger.info(
                        f'Successfully validate Created on date is in ascending order on {page1} and {page2} number')
                    return True
                else:
                    self.driver.save_screenshot(
                        self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_ascending_error.png")
                    self.logger.error(f'Failed to Created on date is in ascending order on {page2} number')
                    return False
            else:
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_ascending_error.png")
                self.logger.error(f'Failed to validate Created on date is in ascending order on {page1} number')
                return False
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in ascending order")
            return False

    def do_validate_created_on_ascending(self, page_number):
        try:
            element = "//div[@class='MuiDataGrid-row'] [@data-id='1']/div[@data-field='orderCreateDate']"
            created_on_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(created_on_element)
            self.do_check_visibility(self.CREATED_ON)
            self.go_to_page(page_number)

            created_on_date = self.get_element_text(self.CREATED_ON_FIRST_VALUE)
            self.logger.info(created_on_date)
            dt_obj1 = datetime.strptime(created_on_date, "%m/%d/%Y %H:%M:%S")
            self.logger.info(dt_obj1)

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            self.scroll()

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            count = 0
            for created_on_list_item in created_on_list:
                created_on_date1 = created_on_list_item.text
                dt_obj2 = datetime.strptime(created_on_date1, "%m/%d/%Y %H:%M:%S")
                self.logger.info(dt_obj2)
                if dt_obj1 == dt_obj2:
                    count = count + 1
                    pass
                else:
                    if dt_obj1 > dt_obj2:
                        count = count + 1
                        self.logger.info(f'Count: {count}')
                    else:
                        return False
            if count == len(created_on_list):
                self.logger.info(f'Total number of create on date count is: {count}')
                return True
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in ascending order")
            return False

    def do_validate_created_on_descending_on_pages(self, page1, page2, feature_file_name):
        try:
            time.sleep(3)
            element = "//div[@class='MuiDataGrid-row'] [@data-id='1']/div[@data-field='orderCreateDate']"
            created_on_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(created_on_element)
            self.do_click_by_locator(self.CREATED_ON)
            if self.do_validate_created_on_descending(page1):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_created_on_date_descending_successfully.png")
                if self.do_validate_created_on_descending(page2):
                    self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                                + "_validate_created_on_date_descending_successfully.png")
                    self.logger.info(
                        f'Successfully validate Created on date is in descending order on {page1} and {page2} number')
                    return True
                else:
                    self.driver.save_screenshot(
                        self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_descending_error.png")
                    self.logger.error(f'Failed to Created on date is in descending order on {page2} number')
                    return False
            else:
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_descending_error.png")
                self.logger.error(f'Failed to validate Created on date is in descending order on {page1} number')
                return False
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in descending order")
            return False

    def do_validate_created_on_descending(self, page_number):
        try:
            time.sleep(3)
            self.go_to_page(page_number)
            created_on_date = self.get_element_text(self.CREATED_ON_FIRST_VALUE)
            self.logger.info(created_on_date)
            dt_obj1 = datetime.strptime(created_on_date, "%m/%d/%Y %H:%M:%S")
            self.logger.info(dt_obj1)

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            self.scroll()

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            count = 0
            for created_on_list_item in created_on_list:
                created_on_date1 = created_on_list_item.text
                dt_obj2 = datetime.strptime(created_on_date1, "%m/%d/%Y %H:%M:%S")
                self.logger.info(dt_obj2)
                if dt_obj1 == dt_obj2:
                    count = count + 1
                    pass
                else:
                    if dt_obj1 < dt_obj2:
                        count = count + 1
                        self.logger.info(f'Count: {count}')
                    else:
                        return False
            if count == len(created_on_list):
                self.logger.info(f'Total number of create on date count is: {count}')
                return True
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in descending order")
            return False

    def logout_x4a(self):
        try:
            self.do_click_by_locator(self.USER_DROPDOWN)
            self.do_click_by_locator(self.LOGOUT)
            self.logger.info("Logout Successfully")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Logout X4A ' + str(e))
            return False