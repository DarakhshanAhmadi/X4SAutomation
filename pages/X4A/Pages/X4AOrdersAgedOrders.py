import glob
import os
import random
import time
from datetime import datetime

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile


class X4AAgedOrdersPage(BasePage):

    SALES_MENU = (By.XPATH, "//*[@data-testid='sales-MenuItem']")
    AGED_ORDER_OPTION = (By.XPATH, "//*[text()='Aged Orders']")
    FILTER_ICON = (By.XPATH, "//span[@class='MuiButton-startIcon MuiButton-iconSizeSmall css-cstir9-MuiButton-startIcon']")
    DOWNLOAD_ICON = (By.XPATH, "//*[@data-testid='FileDownloadIcon']")
    PAGINATION_NEXT_PAGE_ARROW = (By.XPATH, "//div[@class='MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-1cl35i1-MuiButtonBase-root-MuiListItemButton-root']/*[@data-testid='NavigateNextIcon']")
    PAGINATION_PREVIOUS_PAGE_ARROW = (By.XPATH, "//div[@class='MuiListItemButton-root MuiListItemButton-gutters Mui-disabled MuiButtonBase-root Mui-disabled css-1u0qvcd-MuiButtonBase-root-MuiListItemButton-root']/*[@data-testid='NavigateBeforeIcon']")
    PAGINATION_TABS = (By.XPATH, "//div[@class='MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-37enk1-MuiButtonBase-root-MuiListItemButton-root']")
    TABLE_HEADER = (By.XPATH, "//div[@role='columnheader']")
    TABLE_COLUMN_HEADERS_CONTAINER = (By.XPATH, "//div[@class='MuiDataGrid-columnHeadersInner MuiDataGrid-columnHeadersInner--scrollable css-1s0hp0k-MuiDataGrid-columnHeadersInner']")
    QUICK_SEARCH_OPTIONS = (By.XPATH, "//li[contains(@class,'MuiMenuItem-root MuiMenuItem-gutters ')]")
    QUICK_SEARCH_DROPDOWN = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div/div/div")
    IM_ORDER_QUICK_SEARCH_OPTION = (By.XPATH, "//li[text()='IM Order #']")
    VENDOR_NAME_QUICK_SEARCH_OPTION = (By.XPATH, "//li[text()='Vendor name']")
    BCN_ACCOUNT_QUICK_SEARCH_OPTION = (By.XPATH, "//li[text()='BCN Account #']")
    CUSTOMER_PO_QUICK_SEARCH_OPTION = (By.XPATH, "//li[text()='Customer PO Number']")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search']")
    SEARCH_BAR = (By.XPATH, "//input[@class='MuiOutlinedInput-input MuiInputBase-input MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd css-17ogsb7-MuiInputBase-input-MuiOutlinedInput-input']")
    CLOSE_SEARCH = (By.XPATH, "//*[@data-testid='CloseIcon']")
    TABLE_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-row']")
    NO_RESULT_TEXT = (By.XPATH, "//span[text()='No aged orders found.']")
    ORDER_NUMBER_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-row']/div[@data-field='orderNumber']")
    VENDOR_NAME_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-row']/div[@data-field='vendorName']")
    AGED_ORDER_TABLE = "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']"
    ITEMS_PER_PAGE = (By.XPATH, "//div[@class='MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-d2iqo8-MuiSelect-select-MuiInputBase-input']")
    MULTIPLE_VENDOR_LINK = (By.XPATH, "//div[@class='MuiBox-root css-7g6ps3']/p[@id='modal-modal-description']/div")
    LINK_CLOSE_BUTTON = (By.XPATH, "//button[text()='Close']")
    DATE_SEARCH_DROP_DOWN = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div")
    ORDER_DATE_MENU_ITEM = (By.XPATH, "//li[@data-testid='ordercreatedate-MenuItem']")
    LAST_UPDATE_MENU_ITEM = (By.XPATH, "//li[@data-testid='orderupdatedate-MenuItem']")
    CALENDAR_ICON = (By.XPATH, "//button[@aria-label='calendar icon button']")
    LAST_SIX_MONTHS_CALENDER_OPTION = (By.XPATH, "//span[text()='last 6-9 months']")
    DATE_RANGE_TEXTBOX = (By.XPATH, "//input[@id='range-picker']")
    RESET_CALENDAR_OPTION = (By.XPATH, "//span[text()='Reset']")
    ORDER_DATE_ROWS = (By.CSS_SELECTOR, "div[data-field='orderCreateDate'][role='cell']")
    LAST_UPDATE_DATE_ROWS = (By.CSS_SELECTOR, "div[data-field='orderUpdateDate'][role='cell']")
    FILTER_BY_BCN = (By.XPATH, "//p[text()='BCN Account #']")
    FILTER_BY_CUSTOMER_NAME = (By.XPATH, "//p[text()='Customer name']")
    FILTER_BY_VENDOR_NAME = (By.XPATH, "//p[text()='Vendor name']")
    FILTER_BY_ORDER_TYPE = (By.XPATH, "//button[text()='Order Type']")
    FILTER_BY_TOTAL_REVENUE = (By.XPATH, "//p[text()='Total Revenue']")
    FILTER_BY_ORDER_STATUS = (By.XPATH, "//button[text()='Order Status']")
    FILTER_BCN_SEARCH_BOX = (By.XPATH, "//div[@id='panel2-content']/div/div/div/input[@id='bcnCustomer']")
    FILTER_CUSTOMER_SEARCH_BOX = (By.XPATH, "//div[@id='panel1-content']/div/div/div/input[@id='bcnCustomer']")
    FILTER_VENDOR_SEARCH_BOX = (By.XPATH, "//div[@id='panel3-content']/div/div/div/input[@id='bcnCustomer']")
    FILTER_ORDER_TYPE_SEARCH_BOX = (By.XPATH, "//input[@placeholder='Search Order Type']")
    FILTER_ORDER_STATUS_SEARCH_BOX = (By.XPATH, "//input[@placeholder='Search Order Status']")
    FILTER_CHECK_ICON = (By.XPATH, "//*[@data-testid='CheckCircleIcon']")
    FILTER_ORDER_TYPE_CHECKBOX = (By.XPATH, "//label[@data-testid='OrderType-0-Label']/span[@data-testid='OrderType-0-checkbox']")
    FILTER_ORDER_STATUS_CHECKBOX = (By.XPATH, "//label[@data-testid='OrderStatus-0-Label']/span[@data-testid='OrderStatus-0-checkbox']")
    FILTER_TOTAL_REVENUE_MIN_TEXTBOX = (By.ID, "totalRevenuMin")
    FILTER_TOTAL_REVENUE_MAX_TEXTBOX = (By.ID, "totalRevenuMxn")
    FILTER_APPLY_BUTTON = (By.XPATH, "//button[text()='Apply']")
    FILTER_CLEAR_BUTTON = (By.XPATH, "//button[text()='Clear all']")
    USER_DROPDOWN = (By.XPATH, "//*[@data-testid='KeyboardArrowDownIcon']")
    LOGOUT = (By.XPATH, "//*[text()='LogOut']")
    DOWNLOAD_CANCEL = (By.XPATH, "//div[@class='MuiBox-root css-1vfajb6']//button[contains(text(), 'Cancel')]")
    DOWNLOAD_CONTINUE = (By.XPATH, "//div[@class='MuiBox-root css-1vfajb6']//button[contains(text(), 'Continue')]")
    DOWNLOAD_POPUP_MESSAGE = (By.XPATH, "//div//p[@id='modal-modal-description']")
    TABLE_FIRST_ROW = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='0']")
    SKU_POPUP_CLOSE = (By.XPATH, "//div[@class='MuiBox-root css-7g6ps3']/div/button/*[@data-testid='CloseIcon']")
    ORDER_VALUE_SORT = (By.XPATH, "//*[text()='Order value']")
    FIRST_ROW_CHECKBOX = (By.XPATH, "//div[@data-rowindex='0']/div")
    CANCEL_AGED_ORDER = (By.XPATH, "//button[text()='Cancel Order']")
    CANCEL_ORDER_POPUP_MESSAGE = (By.XPATH, "//div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/p")
    CANCEL_CONTINUE = (By.XPATH, "//button[text()='Continue']")
    CANCEL_STATUS = (By.XPATH, "//div[@class='MuiBox-root css-4y84eq']")
    CANCEL_STATUS_OK_BUTTON = (By.XPATH, "//button[text()='Ok']")

    def go_to_aged_orders(self):
        try:
            self.do_click_by_locator(self.SALES_MENU)
            self.do_double_click(self.AGED_ORDER_OPTION)
            self.logger.info("Clicked on Aged orders in the menu.")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Aged orders ' + str(e))
            raise e

    def get_table_column_header(self):
        aged_order_table_column_header = []
        try:
            time.sleep(1)
            column_headers = self.get_element_text(self.TABLE_COLUMN_HEADERS_CONTAINER)
            aged_order_table_column_header = column_headers.split("\n")
            for i in range(1, 13):
                if i == 9 or i == 12:
                    time.sleep(1)
                    column = "//div[@class='MuiDataGrid-row'] [@data-id='0']/div[@data-colindex='" + str(i) + "']"
                    scroll_element = self.driver.find_element(By.XPATH, column)
                    self.scroll_horizontally(scroll_element)
                    column_headers = self.get_element_text(self.TABLE_COLUMN_HEADERS_CONTAINER)
                    aged_order = column_headers.split("\n")
                    for column_header in aged_order:
                        if column_header not in aged_order_table_column_header:
                            aged_order_table_column_header.append(column_header)
            self.logger.info("Aged order column headers :" + str(aged_order_table_column_header))
            self.logger.info("Aged order table column headers fetched successfully")
            return aged_order_table_column_header
        except Exception as e:
            self.logger.error("Exception occurred while retrieving the column header " + str(e))
            raise e

    def get_quick_search_options(self):
        quick_search_options = []
        try:
            self.do_click_by_locator(self.QUICK_SEARCH_DROPDOWN)
            search_options = self.get_all_elements(self.QUICK_SEARCH_OPTIONS)
            for ele in search_options:
                quick_search_options.append(ele.text)
            self.logger.info(quick_search_options)
            self.do_click_by_locator(self.IM_ORDER_QUICK_SEARCH_OPTION)
            return quick_search_options
        except Exception as e:
            self.logger.error("Exception occurred while getting the quick search options" + str(e))
            raise e

    def search_im_order_number(self, order_number):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.QUICK_SEARCH_DROPDOWN)
            self.do_click_by_locator(self.IM_ORDER_QUICK_SEARCH_OPTION)
            self.do_send_keys(self.SEARCH_BAR, order_number)
            self.do_click_by_locator(self.SEARCH_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Exception occurred while order number quick search" + str(e))
            raise e

    def verify_order_number_quick_search(self, order_number):
        try:
            self.check_if_result_found()
            rows = self.get_all_elements(self.ORDER_NUMBER_ROWS)
            if len(rows) == 1:
                self.logger.info("Order found")
                for row in rows:
                    assert row.text == order_number
            else:
                raise Exception("Multiple orders found for searched order")
            # self.do_click_by_locator(self.CLOSE_SEARCH)
        except Exception as e:
            self.logger.error("Exception occurred verifying the order number quick search" + str(e))
            raise e

    def search_vendor_name(self, vendor_name):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.QUICK_SEARCH_DROPDOWN)
            self.do_click_by_locator(self.VENDOR_NAME_QUICK_SEARCH_OPTION)
            self.do_send_keys(self.SEARCH_BAR, vendor_name)
            self.do_click_by_locator(self.SEARCH_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Exception occurred while vendor name quick search" + str(e))
            raise e

    def search_bcn_account(self, bcn_account_number):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.QUICK_SEARCH_DROPDOWN)
            self.do_click_by_locator(self.BCN_ACCOUNT_QUICK_SEARCH_OPTION)
            self.do_send_keys(self.SEARCH_BAR, bcn_account_number)
            self.do_click_by_locator(self.SEARCH_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Exception occurred while searching bcn account" + str(e))
            raise e

    def search_customer_po_number(self, customer_po_number):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.QUICK_SEARCH_DROPDOWN)
            self.do_click_by_locator(self.CUSTOMER_PO_QUICK_SEARCH_OPTION)
            self.do_send_keys(self.SEARCH_BAR, customer_po_number)
            self.do_click_by_locator(self.SEARCH_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Exception occurred while searching customer po number" + str(e))
            raise e

    def verify_vendor_name_in_pages(self, vendor_name):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying vendor name in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_vendor_name_quick_search(vendor_name)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying vendor name in page %s", str(random_page))
                    self.search_vendor_name(vendor_name)
                    self.go_to_page(random_page)
                    self.verify_vendor_name_quick_search(vendor_name)
                self.logger.info("Verifying vendor name in page %s", str(last_page_number))
                self.search_vendor_name(vendor_name)
                self.go_to_page(last_page_number)
                time.sleep(4)
                self.verify_vendor_name_quick_search(vendor_name)
            self.logger.info("Successfully verified vendor name")
        except Exception as e:
            self.logger.error("Exception occurred verifying the vendor name quick search" + str(e))
            raise e

    def verify_vendor_name_quick_search(self, vendor_name):
        try:
            self.logger.info("Verifying the vendor name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching vendor name")
                vendor_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='vendorName']")
                try:
                    ui_vendor_name = self.get_element_text_for_filter(vendor_name_xpath)
                    self.logger.info("Fetched ui vendor name :" + str(ui_vendor_name))
                except:
                    self.logger.info("There are only " + str(i) + " rows in table")
                    break
                if "Multiple Vendors" in ui_vendor_name:
                    self.logger.info("Multiple vendors present")
                    multiple_vendor_link_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='"+str(i)+"']/div/div/button[contains(text(), 'Multiple Vendors')]")
                    self.do_click_by_locator(multiple_vendor_link_xpath)
                    popup_vendor_names = self.get_element_text(self.MULTIPLE_VENDOR_LINK)
                    self.do_click_by_locator(self.LINK_CLOSE_BUTTON)
                    if vendor_name not in popup_vendor_names:
                        raise Exception("Vendor name mismatched")
                else:
                    self.logger.info("Single vendor present")
                    assert ui_vendor_name.strip() == vendor_name.strip(), "Vendor Name mismatched"
            self.do_click_by_locator(self.CLOSE_SEARCH)
        except Exception as e:
            self.logger.error("Exception occurred verifying the vendor name quick search" + str(e))
            raise e

    def verify_bcn_account_in_pages(self, bcn_account):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying BCN account in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_bcn_account_quick_search(bcn_account)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying BCN account in page %s", str(random_page))
                    self.search_bcn_account(bcn_account)
                    self.go_to_page(random_page)
                    self.verify_bcn_account_quick_search(bcn_account)
                self.logger.info("Verifying BCN account in page %s", str(last_page_number))
                self.search_bcn_account(bcn_account)
                self.go_to_page(last_page_number)
                self.verify_bcn_account_quick_search(bcn_account)
            self.logger.info("Successfully verified bcn account")
        except Exception as e:
            self.logger.error("Exception occurred verifying the bcn account quick search" + str(e))
            raise e

    def verify_bcn_account_quick_search(self, bcn_account):
        try:
            self.logger.info("Verifying the BCN account in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching BCN account")
                bcn_account_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerNumber']")
                try:
                    ui_bcn_account = self.get_element_text_for_filter(bcn_account_xpath)
                    self.logger.info("Fetched ui bcn account :" + str(ui_bcn_account))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_bcn_account).strip() == str(bcn_account).strip(), "BCN Account mismatched"
            self.do_click_by_locator(self.CLOSE_SEARCH)
        except Exception as e:
            self.logger.error("Exception occurred verifying the BCN account quick search" + str(e))
            raise e

    def verify_customer_po_in_pages(self, customer_po):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying customer po in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_customer_po_quick_search(customer_po)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying customer po in page %s", str(random_page))
                    self.search_customer_po_number(customer_po)
                    self.go_to_page(random_page)
                    self.verify_customer_po_quick_search(customer_po)
                self.logger.info("Verifying customer po in page %s", str(last_page_number))
                self.search_customer_po_number(customer_po)
                self.go_to_page(last_page_number)
                self.verify_customer_po_quick_search(customer_po)
            self.logger.info("Successfully verified customer po")
        except Exception as e:
            self.logger.error("Exception occurred verifying the customer po quick search" + str(e))
            raise e

    def verify_customer_po_quick_search(self, customer_po):
        try:
            self.logger.info("Verifying the customer po in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching customer po")
                bcn_account_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerOrderNumber']")
                try:
                    ui_customer_po = self.get_element_text_for_filter(bcn_account_xpath)
                    self.logger.info("Fetched ui customer po :" + str(ui_customer_po))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_customer_po).strip() == str(customer_po).strip(), "Customer PO mismatched"
            self.do_click_by_locator(self.CLOSE_SEARCH)
        except Exception as e:
            self.logger.error("Exception occurred verifying the customer po quick search" + str(e))
            raise e

    def select_order_date_range(self):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.DATE_SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.ORDER_DATE_MENU_ITEM)
            self.do_click_by_locator(self.CALENDAR_ICON)
            self.do_click_by_locator(self.LAST_SIX_MONTHS_CALENDER_OPTION)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while selecting order date range " + str(e))
            raise e

    def select_last_updated_date_range(self):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.DATE_SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.LAST_UPDATE_MENU_ITEM)
            self.do_click_by_locator(self.CALENDAR_ICON)
            self.do_click_by_locator(self.LAST_SIX_MONTHS_CALENDER_OPTION)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while selecting order date range " + str(e))
            raise e

    def verify_order_date_in_pages(self):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying order date in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_order_date()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying order date in page %s", str(random_page))
                    self.select_order_date_range()
                    self.go_to_page(random_page)
                    self.verify_order_date()
                self.logger.info("Verifying order date in page %s", str(last_page_number))
                self.select_order_date_range()
                self.go_to_page(last_page_number)
                self.verify_order_date()
            self.logger.info("Successfully verified order date")
        except Exception as e:
            self.logger.error("Exception occurred verifying the order date quick search" + str(e))
            raise e

    def verify_order_date(self):
        try:
            from_date, to_date = self.get_from_date_and_to_date()
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching order date")
                bcn_account_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderCreateDate']")
                try:
                    ui_customer_po = self.get_element_text_for_filter(bcn_account_xpath)
                    self.logger.info("Fetched ui order date " + str(ui_customer_po))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                ui_customer_po = datetime.strptime(self.format_date(ui_customer_po), '%Y-%m-%d').date()
                if not from_date <= ui_customer_po <= to_date:
                    raise Exception("Date filter results are incorrect")
        except Exception as e:
            self.logger.error("Error while selecting order date range " + str(e))
            raise e

    def verify_order_date_reset(self):
        try:
            from_date, to_date = self.get_from_date_and_to_date()
            self.do_click_by_locator(self.CALENDAR_ICON)
            self.do_click_by_locator(self.RESET_CALENDAR_OPTION)
            self.do_click_by_locator(self.DATE_RANGE_TEXTBOX)
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            assert date_range == "", "Date is search box is not empty after reset"
            # time.sleep(2)
            # ele = self.get_all_elements(self.ORDER_DATE_ROWS)
            # for e in ele:
            #     ui_date = e.text
            #     self.logger.info(ui_date)
            #     formatted_date = datetime.strptime(self.format_date(ui_date), '%Y-%m-%d').date()
            #     if from_date <= formatted_date <= to_date:
            #         raise Exception("Reset of date is not working")
        except Exception as e:
            self.logger.error("Error while resetting order date range " + str(e))
            raise e

    def format_date(self, date):
        try:
            self.logger.info("Going to format date : " + str(date))
            date = date.split(",")
            date_parts = date[0].split("/")
            month = date_parts[0]
            day = date_parts[1]
            year = date_parts[2]
            formatted_date = year + "-" + month + "-" + day
            self.logger.info(" Formatted date: " + str(formatted_date))
            return formatted_date
        except Exception as e:
            self.logger.error("Error while formatting the date")
            raise e

    def verify_last_update_date_in_pages(self):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying order date in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_last_update_date()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying order date in page %s", str(random_page))
                    self.select_last_updated_date_range()
                    self.go_to_page(random_page)
                    self.verify_last_update_date()
                self.logger.info("Verifying order date in page %s", str(last_page_number))
                self.select_last_updated_date_range()
                self.go_to_page(last_page_number)
                self.verify_last_update_date()
            self.logger.info("Successfully verified order date")
        except Exception as e:
            self.logger.error("Exception occurred verifying the order date quick search" + str(e))
            raise e

    def verify_last_update_date(self):
        try:
            from_date, to_date = self.get_from_date_and_to_date()
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching last update date")
                last_update_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderUpdateDate']")
                try:
                    last_update_date = self.get_element_text_for_filter(last_update_xpath)
                    self.logger.info("Fetched ui last update date " + str(last_update_date))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                last_update_date = datetime.strptime(self.format_date(last_update_date), '%Y-%m-%d').date()
                if not from_date <= last_update_date <= to_date:
                    raise Exception("Date filter results are incorrect")
        except Exception as e:
            self.logger.error("Error while selecting last update date range " + str(e))
            raise e

    def verify_last_update_date_reset(self):
        try:
            from_date, to_date = self.get_from_date_and_to_date()
            self.do_click_by_locator(self.CALENDAR_ICON)
            self.do_click_by_locator(self.RESET_CALENDAR_OPTION)
            self.do_click_by_locator(self.DATE_RANGE_TEXTBOX)
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            assert date_range == "", "Date is search box is not empty after reset"
            # time.sleep(2)
            # ele = self.get_all_elements(self.LAST_UPDATE_DATE_ROWS)
            # for e in ele:
            #     ui_date = e.text
            #     self.logger.info(ui_date)
            #     formatted_date = datetime.strptime(self.format_date(ui_date), '%Y-%m-%d').date()
            #     if from_date <= formatted_date <= to_date:
            #         raise Exception("Reset of date is not working")
        except Exception as e:
            self.logger.error("Error while resetting last update date range " + str(e))
            raise e

    def filter_by_bcn(self, bcn):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_BCN)
            self.do_send_keys(self.FILTER_BCN_SEARCH_BOX, bcn)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_BCN)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while filtering by bcn " + str(e))
            raise e

    def filter_by_customer_name(self, customer_name):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_CUSTOMER_NAME)
            self.do_send_keys(self.FILTER_CUSTOMER_SEARCH_BOX, customer_name)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_CUSTOMER_NAME)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while filtering by customer name " + str(e))
            raise e

    def filter_by_vendor_name(self, vendor_name):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_NAME)
            self.do_send_keys(self.FILTER_VENDOR_SEARCH_BOX, vendor_name)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_NAME)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while filtering by vendor name " + str(e))
            raise e

    def filter_by_order_type(self, order_type):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_ORDER_TYPE)
            self.do_send_keys(self.FILTER_ORDER_TYPE_SEARCH_BOX, order_type)
            self.do_click_by_locator(self.FILTER_ORDER_TYPE_CHECKBOX)
            self.do_click_by_locator(self.FILTER_BY_ORDER_TYPE)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while filtering by order type " + str(e))
            raise e

    def filter_by_total_revenue(self, min_total_revenue, max_total_revenue):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_TOTAL_REVENUE)
            self.do_send_keys(self.FILTER_TOTAL_REVENUE_MIN_TEXTBOX, min_total_revenue)
            self.do_send_keys(self.FILTER_TOTAL_REVENUE_MAX_TEXTBOX, max_total_revenue)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_TOTAL_REVENUE)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            self.do_double_click(self.ORDER_VALUE_SORT)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while filtering by total revenue " + str(e))
            raise e

    def filter_by_order_status(self, order_status):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_ORDER_STATUS)
            self.do_send_keys(self.FILTER_ORDER_STATUS_SEARCH_BOX, order_status)
            self.do_click_by_locator(self.FILTER_ORDER_STATUS_CHECKBOX)
            self.do_click_by_locator(self.FILTER_BY_ORDER_STATUS)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while filtering by order status " + str(e))
            raise e

    def verify_filtered_bcn_account_in_pages(self, bcn_account):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying BCN account in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_bcn_account_quick_search(bcn_account)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying BCN account in page %s", str(random_page))
                    self.filter_by_bcn(bcn_account)
                    self.go_to_page(random_page)
                    self.verify_bcn_account_quick_search(bcn_account)
                self.logger.info("Verifying BCN account in page %s", str(last_page_number))
                self.filter_by_bcn(bcn_account)
                self.go_to_page(last_page_number)
                self.verify_bcn_account_quick_search(bcn_account)
            self.logger.info("Successfully verified bcn account")
        except Exception as e:
            self.logger.error("Exception occurred verifying the bcn account quick search" + str(e))
            raise e

    def verify_filtered_vendor_in_pages(self, vendor_name):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying vendor in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_vendor_name_quick_search(vendor_name)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying vendor in page %s", str(random_page))
                    self.filter_by_vendor_name(vendor_name)
                    self.go_to_page(random_page)
                    self.verify_vendor_name_quick_search(vendor_name)
                self.logger.info("Verifying vendor in page %s", str(last_page_number))
                self.filter_by_vendor_name(vendor_name)
                self.go_to_page(last_page_number)
                time.sleep(4)
                self.verify_vendor_name_quick_search(vendor_name)
            self.logger.info("Successfully verified vendor")
        except Exception as e:
            self.logger.error("Exception occurred verifying the vendor" + str(e))
            raise e

    def verify_customer_name(self, customer_name):
        try:
            self.logger.info("Verifying the Customer name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching customer name")
                customer_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerName']")
                try:
                    ui_customer_name = self.get_element_text_for_filter(customer_name_xpath)
                    self.logger.info("Fetched ui customer name " + str(ui_customer_name))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_customer_name).strip() == str(customer_name).strip(), "Customer Name mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying the customer name quick search" + str(e))
            raise e

    def verify_filtered_customer_name_in_pages(self, customer_name):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Customer name in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_customer_name(customer_name)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("verifying customer name in page %s", str(random_page))
                    self.filter_by_customer_name(customer_name)
                    self.go_to_page(random_page)
                    self.verify_customer_name(customer_name)
                self.logger.info("Verifying Customer name in page %s", str(last_page_number))
                self.filter_by_customer_name(customer_name)
                self.go_to_page(last_page_number)
                self.verify_customer_name(customer_name)
            self.logger.info("Successfully verified customer name")
        except Exception as e:
            self.logger.error("Exception occurred verifying the customer name" + str(e))
            raise e

    def verify_filtered_order_type_in_pages(self, order_type):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying order type in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_order_type(order_type)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying order type in page %s", str(random_page))
                    self.filter_by_order_type(order_type)
                    self.go_to_page(random_page)
                    self.verify_order_type(order_type)
                self.logger.info("Verifying order type in page %s", str(last_page_number))
                self.filter_by_order_type(order_type)
                self.go_to_page(last_page_number)
                self.verify_order_type(order_type)
            self.logger.info("Successfully verified order type")
        except Exception as e:
            self.logger.error("Exception occurred verifying the order type quick search" + str(e))
            raise e

    def verify_order_type(self, order_type):
        try:
            self.logger.info("Verifying the order type in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching order type")
                order_type_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderTypeName']")
                try:
                    ui_order_type = self.get_element_text_for_filter(order_type_xpath)
                    self.logger.info("Fetched ui order type " + str(ui_order_type))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_order_type).strip() == str(order_type).strip(), "Order type mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying the order type" + str(e))
            raise e

    def verify_filtered_order_status_in_pages(self, order_type):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying order status in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_order_status(order_type)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying order status in page %s", str(random_page))
                    self.filter_by_order_status(order_type)
                    self.go_to_page(random_page)
                    self.verify_order_status(order_type)
                self.logger.info("Verifying order status in page %s", str(last_page_number))
                self.filter_by_order_status(order_type)
                self.go_to_page(last_page_number)
                self.verify_order_status(order_type)
            self.logger.info("Successfully verified order status")
        except Exception as e:
            self.logger.error("Exception occurred verifying the order status" + str(e))
            raise e

    def verify_order_status(self, order_status):
        try:
            self.logger.info("Verifying the order status in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching order status")
                order_status_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderStatus']")
                try:
                    ui_order_status = self.get_element_text_for_filter(order_status_xpath)
                    self.logger.info("Fetched ui order status " + str(ui_order_status))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_order_status).strip() == str(order_status).strip(), "Order status mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying the order status" + str(e))
            raise e

    def verify_total_revenue_in_pages(self, min_total_revenue, max_total_revenue):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying total revenue in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_total_revenue(min_total_revenue, max_total_revenue)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying total revenue in page %s", str(random_page))
                    self.filter_by_total_revenue(min_total_revenue, max_total_revenue)
                    self.go_to_page(random_page)
                    self.verify_total_revenue(min_total_revenue, max_total_revenue)
                self.logger.info("Verifying total revenue in page %s", str(last_page_number))
                self.filter_by_total_revenue(min_total_revenue, max_total_revenue)
                self.go_to_page(last_page_number)
                self.verify_total_revenue(min_total_revenue, max_total_revenue)
            self.logger.info("Successfully verified total revenue")
        except Exception as e:
            self.logger.error("Exception occurred verifying the total revenue" + str(e))
            raise e

    def verify_total_revenue(self, min_total_revenue, max_total_revenue):
        try:
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching order value")
                order_value_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderTotalValue']")
                try:
                    order_value = float(self.get_element_text_for_filter(order_value_xpath))
                    self.logger.info("Fetched ui order value " + str(order_value))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                if not float(min_total_revenue) <= order_value <= float(max_total_revenue):
                    raise Exception("Order value filter results are incorrect")
        except Exception as e:
            self.logger.error("Error while verifying order value " + str(e))
            raise e

    def filter_by_bcn_vendor_and_order_status(self, bcn_account, vendor_name, order_status):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_BCN)
            self.do_send_keys(self.FILTER_BCN_SEARCH_BOX, bcn_account)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_BCN)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_NAME)
            self.do_send_keys(self.FILTER_VENDOR_SEARCH_BOX, vendor_name)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_NAME)
            self.do_click_by_locator(self.FILTER_BY_ORDER_STATUS)
            self.do_send_keys(self.FILTER_ORDER_STATUS_SEARCH_BOX, order_status)
            self.do_click_by_locator(self.FILTER_ORDER_STATUS_CHECKBOX)
            self.do_click_by_locator(self.FILTER_BY_ORDER_STATUS)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Error while applying filters " + str(e))
            raise e

    def verify_bcn_vendor_and_order_status_in_pages(self, bcn_account, vendor_name, order_status):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying bcn, vendor and order status in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_bcn_vendor_and_order_status(bcn_account, vendor_name, order_status)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying bcn, vendor and order status in page %s", str(random_page))
                    self.filter_by_bcn_vendor_and_order_status(bcn_account, vendor_name, order_status)
                    self.go_to_page(random_page)
                    self.verify_bcn_vendor_and_order_status(bcn_account, vendor_name, order_status)
                self.logger.info("Verifying bcn, vendor and order status in page %s", str(last_page_number))
                self.filter_by_bcn_vendor_and_order_status(bcn_account, vendor_name, order_status)
                self.go_to_page(last_page_number)
                self.verify_bcn_vendor_and_order_status(bcn_account, vendor_name, order_status)
            self.logger.info("Successfully verified bcn, vendor and order status")
            self.driver.refresh()
        except Exception as e:
            self.driver.refresh()
            self.logger.error("Exception occurred verifying the bcn, vendor and order status" + str(e))
            raise e

    def verify_bcn_vendor_and_order_status(self, bcn_account, vendor_name, order_status):
        try:
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching bcn, vendor and order status")
                bcn_account_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerNumber']")
                vendor_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='vendorName']")
                order_status_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderStatus']")
                try:
                    ui_bcn_account = self.get_element_text_for_filter(bcn_account_xpath)
                    ui_vendor_name = self.get_element_text_for_filter(vendor_name_xpath)
                    ui_order_status = self.get_element_text_for_filter(order_status_xpath)
                    self.logger.info("Fetched ui bcn, vendor and order status " + str(ui_bcn_account) + "," + str(ui_vendor_name) + "," + str(ui_order_status))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                if "Multiple Vendors" in ui_vendor_name:
                    self.logger.info("Multiple vendors present")
                    multiple_vendor_link_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='"+str(i)+"']/div/div/button[contains(text(), 'Multiple Vendors')]")
                    self.do_click_by_locator(multiple_vendor_link_xpath)
                    popup_vendor_names = self.get_element_text_for_filter(self.MULTIPLE_VENDOR_LINK)
                    self.do_click_by_locator(self.LINK_CLOSE_BUTTON)
                    if vendor_name not in popup_vendor_names:
                        raise Exception("vendor name mismatched")
                else:
                    self.logger.info("Single vendor present")
                    assert ui_vendor_name.strip() == vendor_name.strip(), "Vendor Name mismatched"
                assert str(ui_bcn_account) == str(bcn_account), "BCN mismatched"
                assert str(ui_order_status) == str(order_status), "Order status mismatched"
        except Exception as e:
            self.logger.error("Error while verifying bcn, vendor and order status " + str(e))
            raise e

    def logout_x4a(self):
        try:
            self.do_click_by_locator(self.USER_DROPDOWN)
            self.do_click_by_locator(self.LOGOUT)
            self.logger.info("Logout Successfully")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Logout X4A ' + str(e))
            return False

    def check_if_result_found(self):
        try:
            self.logger.info("Checking if result found for Aged order")
            table_rows = self.get_all_elements_without_visibility(self.TABLE_ROWS)
        except Exception as e:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No result found for the search or filter")
                raise e
            else:
                self.logger.error("Exception while checking the Aged order search result")
                raise e

    def get_from_date_and_to_date(self):
        try:
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            self.logger.info(date_range)
            dates = date_range.split("to")
            from_date = datetime.strptime(dates[0].strip(), '%Y-%m-%d').date()
            to_date = datetime.strptime(dates[-1].strip(), '%Y-%m-%d').date()
            return from_date, to_date
        except Exception as e:
            self.logger.error("Error while getting from and to date")
            raise e

    def get_pagination_first_and_last_page(self):
        try:
            time.sleep(2)
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            return first_page_number, last_page_number
        except Exception as e:
            self.logger.erro("Exception while getting pagination first and last page")
            raise e

    def get_random_page(self, first, last):
        try:
            if last > 10:
                return random.randint(2, 10)
            elif last <= 10:
                return random.randint(first + 1, last - 1)
        except Exception as e:
            self.logger.error("Exception while generating random number" + str(e))
            raise e

    def click_aged_orders_download(self):
        try:
            self.do_click_by_locator(self.DOWNLOAD_ICON)
            self.logger.info("Clicked on Aged orders download button.")
            pop_up_message = self.get_element_text(self.DOWNLOAD_POPUP_MESSAGE)
            self.logger.info(pop_up_message)
            assert pop_up_message == "Only the first 10,000 items will be downloaded. You may filter to minimize number of items being downloaded as, needed.", "pop up message is not correct"
            self.do_click_by_locator(self.DOWNLOAD_CONTINUE)
            self.logger.info("Clicked on Continue download button.")
            self.wait_till_element_is_not_available(self.DOWNLOAD_POPUP_MESSAGE)
        except Exception as e:
            self.logger.error('Exception occurred while downloading on Aged orders ' + str(e))
            raise e

    def filter_by_bcn_and_order_date(self, bcn):
        try:
            self.search_bcn_account(bcn)
            self.do_click_by_locator(self.DATE_SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.ORDER_DATE_MENU_ITEM)
            self.do_click_by_locator(self.CALENDAR_ICON)
            self.do_click_by_locator(self.LAST_SIX_MONTHS_CALENDER_OPTION)
            time.sleep(2)
            self.logger.info("Filter by bcn %s and order date of 6-9 months applied", bcn)
        except Exception as e:
            self.logger.error('Exception occurred while applying filter by bcn and order date ' + str(e))
            raise e

    def get_first_and_last_row_data_for_search_with_bcn_and_order_data(self, header_row, bcn):
        try:
            first_page, last_page = self.get_pagination_first_and_last_page()
            self.filter_by_bcn_and_order_date(bcn)
            self.go_to_page(first_page)
            first_row = self.get_first_row(header_row)
            self.filter_by_bcn_and_order_date(bcn)
            self.go_to_page(last_page)
            last_row = self.get_last_row(header_row)
            return first_row, last_row
        except Exception as e:
            self.logger.error('Exception occurred while applying filter by bcn and order date ' + str(e))
            raise e

    def get_first_row(self, header_row):
        row_data = []
        try:
            time.sleep(2)
            for i in range(1, 13):
                column_xpath = "//div[@class='MuiDataGrid-row'] [@data-id='0']/div[@data-colindex='" + str(i) + "']"
                column_element = (By.XPATH, column_xpath)
                column_data = self.get_element_text_for_filter(column_element)
                column_name = self.do_get_attribute(column_element, 'data-field')
                if column_name == 'ingramPartNumbers':
                    if "..." in column_data:
                        column_data = self.get_multiple_sku_data(column_data, column_xpath)
                row_data.append(column_data)
                if i == 9 or i == 12:
                    time.sleep(1)
                    scroll_element = self.driver.find_element(By.XPATH, column_xpath)
                    self.scroll_horizontally(scroll_element)
            self.logger.info("Fetched first row data successfully")
            self.logger.info("First row data :" + str(row_data))
            if len(header_row) != len(row_data):
                self.logger.error("Please check the data")
                raise Exception("Length of header did not match with length of data")
            row_dict = dict(zip(header_row, row_data))
            self.logger.info("First row dictionary :" + str(row_dict))
        except Exception as e:
            self.logger.error("Exception occurred while retrieving the first row data" + str(e))
            raise e
        return row_dict

    def get_last_row(self, header_row):
        row_data = []
        row_index = 0
        try:
            time.sleep(2)
            max_rows = self.get_element_text_for_filter(self.ITEMS_PER_PAGE)
            table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.scroll_down(table)
                    time.sleep(2)
                row_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'][@data-id='" + str(i) + "']")
                if not self.do_check_availability(row_xpath):
                    self.logger.info("There are only %s elements", str(i))
                    row_index = i - 1
                    break
                row_index = i
            for i in range(1, 13):
                column_xpath = "//div[@class='MuiDataGrid-row'] [@data-id='" + str(row_index) + "']/div[@data-colindex='" + str(i) + "']"
                column_element = (By.XPATH, column_xpath)
                column_data = self.get_element_text_for_filter(column_element)
                column_name = self.do_get_attribute(column_element, 'data-field')
                if column_name == 'ingramPartNumbers':
                    if "..." in column_data:
                        column_data = self.get_multiple_sku_data(column_data, column_xpath)
                row_data.append(column_data)
                if i == 9 or i == 12:
                    scroll_element = self.driver.find_element(By.XPATH, column_xpath)
                    self.scroll_horizontally(scroll_element)
                    time.sleep(1)
            self.logger.info("Aged order table last row fetched successfully")
            self.logger.info("Last row data :" + str(row_data))
            if len(header_row) != len(row_data):
                self.logger.error("Please check the data")
                raise Exception("Length of header did not match with length of data")
            row_dict = dict(zip(header_row, row_data))
            self.logger.info("Last row dictionary :" + str(row_dict))
        except Exception as e:
            self.logger.error("Exception occurred while retrieving the last row data " + str(e))
            raise e
        return row_dict

    def get_multiple_sku_data(self, column_data, column_xpath):
        sku_list = []
        try:
            self.logger.info("Getting the multiple skus")
            self.do_click_by_locator((By.XPATH, column_xpath))
            for i in range(1, 100):
                s = "/html/body/div[2]/div[3]"
                e = self.driver.find_element(By.XPATH, s)
                if i == 13 or i == 18 or i == 24:
                    self.scroll_down(e)
                xpath = (By.XPATH, "//*[@id='modal-modal-description']/div/div/div/div[2]/div[2]/div/div/div//div[@class='MuiDataGrid-row'][@data-id=" + str(i) + "]")
                try:
                    sku = self.get_element_text_for_filter(xpath)
                except:
                    self.logger.info("There are only %s skus", str(i-1))
                    break
                sku_list.append(sku)
                if i % 3 == 0:
                    self.scroll_down(e)
            self.do_click_by_locator(self.LINK_CLOSE_BUTTON)
            sku_list = ",".join(sku_list)
        except Exception as e:
            self.logger.error("Error while getting multiple sku data from link " + str(e))
            raise e
        return sku_list

    def get_first_and_last_row_data_for_filter_bcn_and_vendor_and_status(self, header_row, bcn, vendor_name, order_status):
        try:
            first_page, last_page = self.get_pagination_first_and_last_page()
            self.filter_by_bcn_vendor_and_order_status(bcn, vendor_name, order_status)
            self.go_to_page(first_page)
            first_row = self.get_first_row(header_row)
            self.filter_by_bcn_vendor_and_order_status(bcn, vendor_name, order_status)
            self.go_to_page(last_page)
            last_row = self.get_last_row(header_row)
            return first_row, last_row
        except Exception as e:
            self.logger.error('Exception occurred while applying filter by bcn and vendor and order status' + str(e))
            raise e

    def cancel_aged_order(self):
        try:
            self.do_click_by_locator(self.FIRST_ROW_CHECKBOX)
            self.do_click_by_locator(self.CANCEL_AGED_ORDER)
            popup_message = self.get_element_text(self.CANCEL_ORDER_POPUP_MESSAGE)
            assert popup_message == 'Are you sure you want to cancel selected order/s? Once the orders are cancelled, they cannot be undone. You can only cancel up to 25 orders at a time.'
            self.do_click_by_locator(self.CANCEL_CONTINUE)
            cancel_status = self.get_element_text(self.CANCEL_STATUS)
            assert cancel_status == 'SUCCESS'
            self.do_click_by_locator(self.CANCEL_STATUS_OK_BUTTON)
        except Exception as e:
            self.do_click_by_locator(self.CANCEL_STATUS_OK_BUTTON)
            self.logger.error('Exception occurred while cancelling order' + str(e))
            raise e

    def validate_order_is_not_in_list(self, order_number):
        try:
            self.search_im_order_number(order_number)
            for retry in range(2):
                self.do_click_by_locator(self.SEARCH_BUTTON)
                if self.do_check_visibility(self.NO_RESULT_TEXT):
                    self.logger.info('order successfully cancelled')
                    break
                elif retry == 1:
                    raise Exception(f'Cancelled order is still in aged order list: {order_number}')
        except Exception as e:
            self.logger.error('Exception occurred while validating order is cancelled' + str(e))
            raise e
