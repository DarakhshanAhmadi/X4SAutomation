import time
from datetime import datetime

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile


class X4AAgedOrdersPage(BasePage):

    ORDER_MENU = (By.XPATH, "//*[@data-testid='orders-MenuItem']")
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
    link = (By.XPATH, "//div[@class='MuiBox-root css-7g6ps3']/p[@id='modal-modal-description']/div")
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


    def go_to_aged_orders(self):
        try:
            self.do_click_by_locator(self.ORDER_MENU)
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
            self.logger.info(aged_order_table_column_header)
            for i in range(1, 13):
                if i == 9 or i == 12:
                    time.sleep(1)
                    column = "//div[@class='MuiDataGrid-row'] [@data-id='0']/div[@data-colindex='" + str(i) + "']"
                    scroll_element = self.driver.find_element(By.XPATH, column)
                    self.scroll_horizontally(scroll_element)
                    column_headers = self.get_element_text(self.TABLE_COLUMN_HEADERS_CONTAINER)
                    aged_order = column_headers.split("\n")
                    self.logger.info(aged_order)
                    for column_header in aged_order:
                        if column_header not in aged_order_table_column_header:
                            aged_order_table_column_header.append(column_header)
            self.logger.info(aged_order_table_column_header)
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
        except Exception as e:
            self.logger.error("Exception occurred while order number quick search" + str(e))
            raise e

    def verify_order_number_quick_search(self, order_number):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                raise Exception("No order found")
            rows = self.get_all_elements(self.ORDER_NUMBER_ROWS)
            if len(rows) == 1:
                self.logger.info("Order found")
                for row in rows:
                    assert row.text == order_number
            else:
                raise Exception("Order number search failed")
            self.do_click_by_locator(self.CLOSE_SEARCH)
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
            time.sleep(5)
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
        except Exception as e:
            self.logger.error("Exception occurred while searching customer po number" + str(e))
            raise e

    def verify_vendor_name_in_pages(self, vendor_name):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched vendor name")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying vendor name in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_vendor_name_quick_search(vendor_name)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying vendor name in page %s", str(random_page))
                    self.search_vendor_name(vendor_name)
                    self.go_to_page(random_page)
                    self.verify_vendor_name_quick_search(vendor_name)
                self.logger.info("verifying vendor name in page %s", str(last_page_number))
                self.search_vendor_name(vendor_name)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_vendor_name_quick_search(vendor_name)
            self.logger.info("Successfully verified vendor name")
        except Exception as e:
            self.logger.error("Exception occurred verifying the vendor name quick search" + str(e))
            raise e

    def verify_vendor_name_quick_search(self, vendor_name):
        try:
            self.logger.info("verifying the vendor name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching vendor name")
                vendor_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='vendorName']")
                try:
                    ui_vendor_name = self.get_element_text(vendor_name_xpath)
                    self.logger.info("fetched ui ven name" + str(ui_vendor_name))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                if "Multiple Vendors" in ui_vendor_name:
                    self.logger.info("multiple vens")
                    link_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='"+str(i)+"']/div/div/button[contains(text(), 'Multiple Vendors')]")
                    self.do_click_by_locator(link_xpath)
                    popup_vendor_names = self.get_element_text(self.link)
                    if vendor_name in popup_vendor_names:
                        self.logger.info(popup_vendor_names)
                    else:
                        raise Exception("vendor name mismatched")
                    self.do_click_by_locator(self.LINK_CLOSE_BUTTON)
                else:
                    self.logger.info("single vendor")
                    assert ui_vendor_name.strip() == vendor_name.strip(), "Vendor Name mismatched"
            self.do_click_by_locator(self.CLOSE_SEARCH)
        except Exception as e:
            self.logger.error("Exception occurred verifying the vendor name quick search" + str(e))
            raise e

    def verify_bcn_account_in_pages(self, bcn_account):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched bcn account")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying bcn account in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_bcn_account_quick_search(bcn_account)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying bcn account in page %s", str(random_page))
                    self.search_bcn_account(bcn_account)
                    self.go_to_page(random_page)
                    self.verify_bcn_account_quick_search(bcn_account)
                self.logger.info("verifying bcn account in page %s", str(last_page_number))
                self.search_bcn_account(bcn_account)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_bcn_account_quick_search(bcn_account)
            self.logger.info("Successfully verified bcn account")
        except Exception as e:
            self.logger.error("Exception occurred verifying the bcn account quick search" + str(e))
            raise e

    def verify_bcn_account_quick_search(self, bcn_account):
        try:
            self.logger.info("verifying the BCN account in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching BCN account")
                bcn_account_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerNumber']")
                try:
                    ui_bcn_account = self.get_element_text(bcn_account_xpath)
                    self.logger.info("fetched ui bcn account " + str(ui_bcn_account))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                assert str(ui_bcn_account).strip() == str(bcn_account).strip(), "BCN Account mismatched"
            self.do_click_by_locator(self.CLOSE_SEARCH)
        except Exception as e:
            self.logger.error("Exception occurred verifying the BCN account quick search" + str(e))
            raise e

    def verify_customer_po_in_pages(self, customer_po):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched customer po")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying customer po in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_customer_po_quick_search(customer_po)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying customer po in page %s", str(random_page))
                    self.search_customer_po_number(customer_po)
                    self.go_to_page(random_page)
                    self.verify_customer_po_quick_search(customer_po)
                self.logger.info("verifying customer po in page %s", str(last_page_number))
                self.search_customer_po_number(customer_po)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_customer_po_quick_search(customer_po)
            self.logger.info("Successfully verified customer po")
        except Exception as e:
            self.logger.error("Exception occurred verifying the customer po quick search" + str(e))
            raise e

    def verify_customer_po_quick_search(self, customer_po):
        try:
            self.logger.info("verifying the customer po in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching customer po")
                bcn_account_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerOrderNumber']")
                try:
                    ui_customer_po = self.get_element_text(bcn_account_xpath)
                    self.logger.info("fetched ui customer po " + str(ui_customer_po))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
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
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            self.logger.info(date_range)
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
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            self.logger.info(date_range)
        except Exception as e:
            self.logger.error("Error while selecting order date range " + str(e))
            raise e

    def verify_order_date_in_pages(self):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched order date")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying order date in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_order_date()
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying order date in page %s", str(random_page))
                    self.select_order_date_range()
                    self.go_to_page(random_page)
                    self.verify_order_date()
                self.logger.info("verifying order date in page %s", str(last_page_number))
                self.select_order_date_range()
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_order_date()
            self.logger.info("Successfully verified order date")
            self.verify_order_date_reset()
        except Exception as e:
            self.logger.error("Exception occurred verifying the order date quick search" + str(e))
            raise e

    def verify_order_date(self):
        try:
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            dates = date_range.split("to")
            from_date = datetime.strptime(dates[0].strip(), '%Y-%m-%d').date()
            to_date = datetime.strptime(dates[-1].strip(), '%Y-%m-%d').date()
            self.logger.info(date_range)
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching order date")
                bcn_account_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderCreateDate']")
                try:
                    ui_customer_po = self.get_element_text(bcn_account_xpath)
                    self.logger.info("fetched ui order date " + str(ui_customer_po))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                ui_customer_po = datetime.strptime(self.format_date(ui_customer_po), '%Y-%m-%d').date()
                if not from_date <= ui_customer_po <= to_date:
                    raise Exception("Date filter results are incorrect")
        except Exception as e:
            self.logger.error("Error while selecting order date range " + str(e))
            raise e

    def verify_order_date_reset(self):
        try:
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            dates = date_range.split("to")
            from_date = datetime.strptime(dates[0].strip(), '%Y-%m-%d').date()
            to_date = datetime.strptime(dates[-1].strip(), '%Y-%m-%d').date()
            self.do_click_by_locator(self.CALENDAR_ICON)
            self.do_click_by_locator(self.RESET_CALENDAR_OPTION)
            self.do_click_by_locator(self.DATE_RANGE_TEXTBOX)
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            assert date_range == "", "Date is search box is not empty after reset"
            time.sleep(2)
            ele = self.get_all_elements(self.ORDER_DATE_ROWS)
            for e in ele:
                ui_date = e.text
                self.logger.info(ui_date)
                formatted_date = datetime.strptime(self.format_date(ui_date), '%Y-%m-%d').date()
                if from_date <= formatted_date <= to_date:
                    raise Exception("Reset of date is working")
        except Exception as e:
            self.logger.error("Error while selecting order date range " + str(e))
            raise e

    def format_date(self, date):
        try:
            self.logger.info("Going to format date"+ str(date))
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
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched last update date")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying order date in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_last_update_date()
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying order date in page %s", str(random_page))
                    self.select_last_updated_date_range()
                    self.go_to_page(random_page)
                    self.verify_last_update_date()
                self.logger.info("verifying order date in page %s", str(last_page_number))
                self.select_last_updated_date_range()
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_last_update_date()
            self.logger.info("Successfully verified order date")
            self.verify_last_update_date_reset()
        except Exception as e:
            self.logger.error("Exception occurred verifying the order date quick search" + str(e))
            raise e

    def verify_last_update_date(self):
        try:
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            dates = date_range.split("to")
            from_date = datetime.strptime(dates[0].strip(), '%Y-%m-%d').date()
            to_date = datetime.strptime(dates[-1].strip(), '%Y-%m-%d').date()
            self.logger.info(date_range)
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching last update date")
                last_update_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderUpdateDate']")
                try:
                    last_update_date = self.get_element_text(last_update_xpath)
                    self.logger.info("fetched ui last update date " + str(last_update_date))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                last_update_date = datetime.strptime(self.format_date(last_update_date), '%Y-%m-%d').date()
                if not from_date <= last_update_date <= to_date:
                    raise Exception("Date filter results are incorrect")
        except Exception as e:
            self.logger.error("Error while selecting last update date range " + str(e))
            raise e

    def verify_last_update_date_reset(self):
        try:
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            dates = date_range.split("to")
            from_date = datetime.strptime(dates[0].strip(), '%Y-%m-%d').date()
            to_date = datetime.strptime(dates[-1].strip(), '%Y-%m-%d').date()
            self.do_click_by_locator(self.CALENDAR_ICON)
            self.do_click_by_locator(self.RESET_CALENDAR_OPTION)
            self.do_click_by_locator(self.DATE_RANGE_TEXTBOX)
            date_range = self.do_get_attribute(self.DATE_RANGE_TEXTBOX, 'value')
            assert date_range == "", "Date is search box is not empty after reset"
            time.sleep(2)
            ele = self.get_all_elements(self.LAST_UPDATE_DATE_ROWS)
            for e in ele:
                ui_date = e.text
                self.logger.info(ui_date)
                formatted_date = datetime.strptime(self.format_date(ui_date), '%Y-%m-%d').date()
                if from_date <= formatted_date <= to_date:
                    raise Exception("Reset of date is working")
        except Exception as e:
            self.logger.error("Error while selecting last update date range " + str(e))
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
        except Exception as e:
            self.logger.error("Error while filtering by order status " + str(e))
            raise e

    def verify_filtered_bcn_account_in_pages(self, bcn_account):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched bcn account")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying bcn account in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_bcn_account_quick_search(bcn_account)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying bcn account in page %s", str(random_page))
                    self.filter_by_bcn(bcn_account)
                    self.go_to_page(random_page)
                    self.verify_bcn_account_quick_search(bcn_account)
                self.logger.info("verifying bcn account in page %s", str(last_page_number))
                self.filter_by_bcn(bcn_account)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_bcn_account_quick_search(bcn_account)
            self.logger.info("Successfully verified bcn account")
        except Exception as e:
            self.logger.error("Exception occurred verifying the bcn account quick search" + str(e))
            raise e

    def verify_filtered_vendor_in_pages(self, vendor_name):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched vendor")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying vendor in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_vendor_name_quick_search(vendor_name)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying vendor in page %s", str(random_page))
                    self.filter_by_vendor_name(vendor_name)
                    self.go_to_page(random_page)
                    self.verify_vendor_name_quick_search(vendor_name)
                self.logger.info("verifying vendor in page %s", str(last_page_number))
                self.filter_by_vendor_name(vendor_name)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_vendor_name_quick_search(vendor_name)
            self.logger.info("Successfully verified vendor")
        except Exception as e:
            self.logger.error("Exception occurred verifying the vendor" + str(e))
            raise e

    def verify_customer_name(self, customer_name):
        try:
            self.logger.info("verifying the name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching customer name")
                customer_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerName']")
                try:
                    ui_customer_name = self.get_element_text(customer_name_xpath)
                    self.logger.info("fetched ui customer name " + str(ui_customer_name))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                assert str(ui_customer_name).strip() == str(customer_name).strip(), "Customer Name mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying the customer name quick search" + str(e))
            raise e

    def verify_filtered_customer_name_in_pages(self, customer_name):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched vendor")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying vendor in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_customer_name(customer_name)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying customer name in page %s", str(random_page))
                    self.filter_by_customer_name(customer_name)
                    self.go_to_page(random_page)
                    self.verify_customer_name(customer_name)
                self.logger.info("verifying vendor in page %s", str(last_page_number))
                self.filter_by_customer_name(customer_name)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_customer_name(customer_name)
            self.logger.info("Successfully verified customer name")
        except Exception as e:
            self.logger.error("Exception occurred verifying the customer name" + str(e))
            raise e

    def verify_filtered_order_type_in_pages(self, order_type):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched order type")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying order type in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_order_type(order_type)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying order type in page %s", str(random_page))
                    self.filter_by_order_type(order_type)
                    self.go_to_page(random_page)
                    self.verify_order_type(order_type)
                self.logger.info("verifying order type in page %s", str(last_page_number))
                self.filter_by_order_type(order_type)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_order_type(order_type)
            self.logger.info("Successfully verified order type")
        except Exception as e:
            self.logger.error("Exception occurred verifying the order type quick search" + str(e))
            raise e

    def verify_order_type(self, order_type):
        try:
            self.logger.info("verifying the order type in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching order type")
                order_type_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderTypeName']")
                try:
                    ui_order_type = self.get_element_text(order_type_xpath)
                    self.logger.info("fetched ui order type " + str(ui_order_type))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                assert str(ui_order_type).strip() == str(order_type).strip(), "Order type mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying the order type" + str(e))
            raise e

    def verify_filtered_order_status_in_pages(self, order_type):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched order status")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying order status in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_order_status(order_type)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying order status in page %s", str(random_page))
                    self.filter_by_order_status(order_type)
                    self.go_to_page(random_page)
                    self.verify_order_status(order_type)
                self.logger.info("verifying order status in page %s", str(last_page_number))
                self.filter_by_order_status(order_type)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_order_status(order_type)
            self.logger.info("Successfully verified order status")
        except Exception as e:
            self.logger.error("Exception occurred verifying the order status" + str(e))
            raise e

    def verify_order_status(self, order_status):
        try:
            self.logger.info("verifying the order status in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching order status")
                order_status_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderStatus']")
                try:
                    ui_order_status = self.get_element_text(order_status_xpath)
                    self.logger.info("fetched ui order status " + str(ui_order_status))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                assert str(ui_order_status).strip() == str(order_status).strip(), "Order status mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying the order status" + str(e))
            raise e

    def verify_last_total_revenue_in_pages(self, min_total_revenue, max_total_revenue):
        try:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No order found for searched total revenue")
                raise Exception("No order found")
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("verifying total revenue in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_total_revenue(min_total_revenue, max_total_revenue)
            if first_page_number != last_page_number:
                random_page = first_page_number + 10
                self.logger.info(random_page)
                if random_page < last_page_number:
                    self.logger.info("verifying total revenue in page %s", str(random_page))
                    self.filter_by_total_revenue(min_total_revenue, max_total_revenue)
                    self.go_to_page(random_page)
                    self.verify_total_revenue(min_total_revenue, max_total_revenue)
                self.logger.info("verifying total revenue in page %s", str(last_page_number))
                self.filter_by_total_revenue(min_total_revenue, max_total_revenue)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.verify_total_revenue(min_total_revenue, max_total_revenue)
            self.logger.info("Successfully verified total revenue")
        except Exception as e:
            self.logger.error("Exception occurred verifying the total revenue" + str(e))
            raise e

    def verify_total_revenue(self, min_total_revenue, max_total_revenue):
        try:
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info(max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i % 2 == 0:
                    self.logger.info("going to scroll")
                    table = self.driver.find_element(By.XPATH, self.AGED_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("fetching order value")
                order_value_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderTotalValue']")
                try:
                    order_value = float(self.get_element_text(order_value_xpath))
                    self.logger.info("fetched ui order value " + str(order_value))
                except:
                    self.logger.info("there are only " + str(i) + " elements")
                    break
                if not float(min_total_revenue) <= order_value <= float(max_total_revenue):
                    raise Exception("Order value filter results are incorrect")
        except Exception as e:
            self.logger.error("Error while verifying order value " + str(e))
            raise e
