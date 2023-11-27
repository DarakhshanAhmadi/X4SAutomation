import time
import random
from datetime import datetime
from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage


class X4AInventoryInquiryPage(BasePage):

    INVENTORY_MENU = (By.XPATH, "//div[@data-testid='sales-MenuItem']")
    INVENTORY_INQUIRY_OPTION = (By.XPATH, "//li[@data-testid='sales-inventory_inquiry-CategoryName']")
    TABLE_COLUMN_HEADERS_CONTAINER = (By.XPATH, "//div[@class='MuiDataGrid-columnHeadersInner MuiDataGrid-columnHeadersInner--scrollable css-1s0hp0k-MuiDataGrid-columnHeadersInner']")
    VENDOR_SORT_ICON = (By.XPATH, "//*[text()='Vendor']")
    SEARCH_TEXTBOX = (By.XPATH, "//input[@id='search']")
    SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    GRID_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']/div[@role='row']")
    FIRST_ROW_SKU = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='sku']")
    CLOSE_ICON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    TITLE = (By.XPATH, "//h2[@class='MuiTypography-root MuiTypography-h2 css-h794si-MuiTypography-root']")
    PAGE_NAVIGATION = (By.XPATH, "//ol[@class='MuiBreadcrumbs-ol css-4pdmu4-MuiBreadcrumbs-ol']/li")
    SELECT_CUSTOMER_BUTTON = (By.XPATH, "//button[text()='Select customer']")
    POPUP_SKIP_BUTTON= (By.XPATH, "//button[text()='Skip']")
    POPUP_SELECT_BUTTON = (By.XPATH, "//button[text()='Select']")
    CUSTOMER_TEXTBOX = (By.XPATH, "//input[@placeholder='Search by customer name, or BCN number']")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//button[@aria-label='close']/*[@data-testid='CloseIcon']")
    POPUP_SEARCH_ICON = (By.XPATH, "(//button/*[@data-testid='SearchIcon'])[2]")
    SELECTED_CUSTOMER = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div[1]/div/span/span")
    EDIT_CUSTOMER_BUTTON = (By.XPATH, "//button[@aria-label='edit']")
    CUSTOMER_SELECTION_POPUP_TEXT = (By.XPATH, "//div[@class='MuiDialogContent-root css-4bso5q-MuiDialogContent-root']/p")
    INVENTORY_INQUIRY_GRID_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']/div[@role='row']")
    INVENTORY_INQUIRY_ROWS_RESELLER_PRICE = (By.XPATH, "//div[@data-field='resellerPrice'][@role='cell']")
    INVENTORY_INQUIRY_TABLE = "//div[@class='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']"
    ITEMS_PER_PAGE = (By.XPATH, "//div[@class='MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-d2iqo8-MuiSelect-select-MuiInputBase-input']")
    SKUS_IN_GRID = (By.XPATH, "//div[@class='MuiDataGrid-row']/div[@data-field='sku']/a")
    DETAILS_PAGE_SKU = (By.XPATH, "//h2")
    INVENTORY_VISIBILITY_TEXT = (By.XPATH, "//div[@class='css-4sov5v-MuiStack-root']/span[text()='Please Select a Customer']")
    INVENTORY_INQUIRY_LIST_PAGE_LINK = (By.XPATH, "//a[text()='Inventory Inquiry']")
    INVENTORY_DETAILS_PAGE_HEADERS = (By.XPATH, "//div[@class='MuiBox-root css-1jbdlot']/div")
    INVENTORY_DETAILS_PAGE_HEADER_VALUES = (By.XPATH, "//div[@class='MuiBox-root css-1jbdlot']")
    FIRST_ROW_DESCRIPTION = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='shortdescription']")
    FIRST_ROW_VPN = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='vpn']")
    FIRST_ROW_VENDOR = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='vendor']")
    FIRST_ROW_CLASS = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='class']")
    FIRST_ROW_VENDOR_CODE = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='vendorCode']")
    PRODUCT_DETAILS_EXPAND_ICON = (By.XPATH, "(//div[@id='panel1a-header'])[1]/div[2]/*[@data-testid='ExpandMoreIcon']")
    ADDITIONAL_INVENTORY_DETAILS_EXPAND_ICON = (By.XPATH, "(//div[@id='panel1a-header'])[2]/div[2]/*[@data-testid='ExpandMoreIcon']")
    ADDITIONAL_ATTRIBUTES_EXPAND_ICON = (By.XPATH, "(//div[@id='panel1a-header'])[2]/div[2]/*[@data-testid='ExpandMoreIcon']")
    PRODUCT_DETAILS_SECTION_NAME = (By.XPATH, "(//p[@class='MuiTypography-root MuiTypography-body1 css-1otm1we-MuiTypography-root'])[1]")
    ADDITIONAL_INVENTORY_DETAILS = (By.XPATH, "(//p[@class='MuiTypography-root MuiTypography-body1 css-1otm1we-MuiTypography-root'])[3]")
    PRODUCT_DETAILS_SECTIONS = (By.XPATH, "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[1]/div/div[@class='css-sovzj7-MuiStack-root']/div[1]")
    PRODUCT_DETAILS_CODE_HEADER = (By.XPATH, "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[1]/div[@class='css-6ywy1y-MuiStack-root']/div[1]")
    PRODUCT_DETAILS_CATEGORIES_HEADER = (By.XPATH, "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[1]/div[3]/div[1]")
    DESCRIPTION_VALUE = (By.XPATH,
                         "((//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[1]/div/div[@class='css-sovzj7-MuiStack-root']/div[2]/div[2])[1]")
    VENDOR_DETAILS_SECTIONS = (By.XPATH,
                               "((//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[1]/div/div[@class='css-sovzj7-MuiStack-root']/div[2])[2]/div")
    CODES_SECTIONS = (By.XPATH,
                      "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[1]/div[@class='css-6ywy1y-MuiStack-root']/div[2]/div")
    PRODUCT_COSTS_SECTION = (By.XPATH,
                           "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[1]/div[@class='css-s8byg9-MuiStack-root']/div[2]/div")
    CATEGORIES_HEADER = (By.XPATH, "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[2]/div/div[@class='css-sovzj7-MuiStack-root']/div[1]")
    GENERAL_INFORMATION_HEADER = (By.XPATH, "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[2]/div/div/p")
    CATEGORIES_SECTIONS = (By.XPATH, "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[2]/div/div/div[2]/div")
    GENERAL_INFORMATION_SECTIONS = (By.XPATH, "(//div[@class='MuiAccordionDetails-root css-1v80q3j-MuiAccordionDetails-root'])[2]/div/div[2]/div")
    INVENTORY_VISIBILITY_TABLE_HEADERS = (By.XPATH, "//div[@class='MuiDataGrid-columnHeaderTitleContainer']")
    INVENTORY_VISIBILITY_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-row']")
    AVAILABLE_SORT = (By.XPATH, "//div[text()='Available']")
    AVAILABLE_ROWS = (By.XPATH, "//div[@data-field='warehouseAvailableQuantity'][@role='cell']")
    COMMITED_SORT = (By.XPATH, "//div[text()='Commited']")
    COMMITED_ROWS = (By.XPATH, "//div[@data-field='committedQuantity'][@role='cell']")
    FUTURE_SORT = (By.XPATH, "//div[text()='Future']")
    FUTURE_ROWS = (By.XPATH, "//div[@data-field='futureQuantity'][@role='cell']")
    ON_ORDER_SORT = (By.XPATH, "//strong[text()='On Order']")
    ON_ORDER_ROWS = (By.XPATH, "//div[@data-field='onOrderQuantity'][@role='cell']")
    IN_TRANSIT_SORT = (By.XPATH, "//div[text()='In transit']")
    IN_TRANSIT_ROWS = (By.XPATH, "//div[@data-field='inTransitQuantity'][@role='cell']")
    ON_HOLD_SORT = (By.XPATH, "//div[text()='On hold']")
    ON_HOLD_ROWS = (By.XPATH, "//div[@data-field='onholdQuantity'][@role='cell']")
    ON_HAND_SORT = (By.XPATH, "//div[text()='On hand']")
    ON_HAND_ROWS = (By.XPATH, "//div[@data-field='onHandQuantity'][@role='cell']")
    AVERAGE_COST_SORT = (By.XPATH, "//strong[text()='Average cost']")
    AVERAGE_COST_ROWS = (By.XPATH, "//div[@data-field='averageCost'][@role='cell']")
    ETA_SORT = (By.XPATH, "//div[text()='ETA']")
    ETA_ROWS = (By.XPATH, "//div[@data-field='etaDate'][@role='cell']")
    WAREHOUSE_LOCATION_SORT = (By.XPATH, "//strong[text()='Warehouse location']")

    def go_to_inventory_inquiry(self):
        path = []
        try:
            self.do_click_by_locator(self.INVENTORY_MENU)
            self.do_double_click(self.INVENTORY_INQUIRY_OPTION)
            navigation = self.get_all_elements(self.PAGE_NAVIGATION)
            for e in navigation:
                if e.text != '':
                    path.append(e.text)
            navigation_path = ' > '.join(path)
            assert navigation_path == 'Home > Inventory Inquiry', 'Navigation path mismatched for inventory inquiry'
            title = self.get_element_text(self.TITLE)
            assert title == "Inventory inquiry", 'Page title mismatched for inventory inquiry'
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Inventory Inquiry' + str(e))
            raise e

    def get_table_column_header(self):
        inventory_inquiry_table_column_header = []
        try:
            time.sleep(3)
            for i in range(1, 16):
                if i == 8:
                    self.driver.execute_script(
                        "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1100")
                column_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-columnHeadersInner MuiDataGrid-columnHeadersInner--scrollable css-1s0hp0k-MuiDataGrid-columnHeadersInner']/div[@aria-colindex=" + str(i) + "]")
                column_name = self.get_element_text(column_name_xpath)
                inventory_inquiry_table_column_header.append(column_name)
            self.logger.info("Inventory Inquiry column headers :" + str(inventory_inquiry_table_column_header))
            self.logger.info("Inventory Inquiry table column headers fetched successfully")
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return inventory_inquiry_table_column_header
        except Exception as e:
            self.logger.error("Exception occurred while retrieving the column header of Inventory Inquiry " + str(e))
            raise e

    def search(self, search_item):
        try:
            self.do_send_keys(self.SEARCH_TEXTBOX, search_item)
            self.do_click_by_locator(self.SEARCH_ICON)
        except Exception as e:
            self.logger.error("Exception occurred while performing search in Inventory Inquiry " + str(e))
            raise e

    def verify_sku_search_result(self, sku):
        try:
            rows = self.get_all_elements(self.GRID_ROWS)
            assert len(rows) == 1, 'More than 1 result found for searched sku'
            ui_sku = self.get_element_text(self.FIRST_ROW_SKU)
            assert ui_sku == sku, 'SKU mismatched for search'
            self.do_click_by_locator(self.CLOSE_ICON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Exception occurred while performing search in Inventory Inquiry " + str(e))
            raise e

    def verify_reseller_price_is_empty(self):
        try:
            # items_per_page = self.get_element_text(self.ITEMS_PER_PAGE)
            # for i in range(int(items_per_page)):
            #     reseller_price_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-rowindex='" + str(
            #         i) + "']/div[@data-field='resellerPrice']")
            #     try:
            #         ui_reseller_price = self.get_element_text_for_filter(reseller_price_xpath)
            #     except:
            #         table = self.driver.find_element(By.XPATH, self.INVENTORY_INQUIRY_TABLE)
            #         self.scroll_down(table)
            #         try:
            #             self.logger.info(i)
            #             ui_reseller_price = self.get_element_text_for_filter(reseller_price_xpath)
            #         except:
            #             self.logger.info("There are only " + str(i) + " rows")
            #             break
            #     if str(ui_reseller_price) != '':
            for i in range(10):
                if i > 0:
                    table = self.driver.find_element(By.XPATH, self.INVENTORY_INQUIRY_TABLE)
                    self.scroll_down(table)
                rows = self.get_all_elements(self.INVENTORY_INQUIRY_ROWS_RESELLER_PRICE)
                for ele in rows:
                    if ele.text != '':
                        self.logger.error(f'reseller price is not empty. UI:{ele.text}')
                        raise Exception("Reseller price is not empty")
            for i in range(10):
                table = self.driver.find_element(By.XPATH, self.INVENTORY_INQUIRY_TABLE)
                self.scroll_up(table)
        except Exception as e:
            self.logger.error("Exception occurred while checking reseller price is empty by default in Inventory Inquiry " + str(e))
            raise e

    def verify_reseller_price_is_empty_in_pages(self):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 700")
            time.sleep(5)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying reseller price in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_reseller_price_is_empty()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying reseller price in page %s", str(random_page))
                    self.go_to_page(random_page)
                    self.verify_reseller_price_is_empty()
                self.logger.info("Verifying reseller price in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.verify_reseller_price_is_empty()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified reseller price is empty by default")
        except Exception as e:
            self.logger.error("Exception occurred verifying reseller price is empty by default" + str(e))
            raise e


    def verify_reseller_price_is_not_empty(self):
        try:
            # items_per_page = self.get_element_text(self.ITEMS_PER_PAGE)
            # for i in range(int(items_per_page)):
            #     reseller_price_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-rowindex='" + str(
            #         i) + "']/div[@data-field='resellerPrice']")
            #     try:
            #         ui_reseller_price = self.get_element_text_for_filter(reseller_price_xpath)
            #     except:
            #         table = self.driver.find_element(By.XPATH, self.INVENTORY_INQUIRY_TABLE)
            #         self.scroll_down(table)
            #         try:
            #             self.logger.info(i)
            #             ui_reseller_price = self.get_element_text_for_filter(reseller_price_xpath)
            #         except:
            #             self.logger.info("There are only " + str(i) + " rows")
            #             break
            #     if str(ui_reseller_price) != '':
            for i in range(10):
                if i > 0:
                    table = self.driver.find_element(By.XPATH, self.INVENTORY_INQUIRY_TABLE)
                    self.scroll_down(table)
                    time.sleep(1)
                rows = self.get_all_elements(self.INVENTORY_INQUIRY_ROWS_RESELLER_PRICE)
                for ele in rows:
                    if ele.text == '':
                        self.logger.error(f'reseller price is empty. UI:{ele.text}')
                        raise Exception("Reseller price is empty")
            for i in range(10):
                table = self.driver.find_element(By.XPATH, self.INVENTORY_INQUIRY_TABLE)
                self.scroll_up(table)
        except Exception as e:
            self.logger.error("Exception occurred while checking reseller price is not empty in Inventory Inquiry " + str(e))
            raise e

    def verify_reseller_price_is_not_empty_in_pages(self):
        try:
            time.sleep(5)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 700")
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying reseller price in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.verify_reseller_price_is_not_empty()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying reseller price in page %s", str(random_page))
                    self.go_to_page(random_page)
                    self.verify_reseller_price_is_not_empty()
                self.logger.info("Verifying reseller price in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.verify_reseller_price_is_not_empty()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified reseller price is not empty")
        except Exception as e:
            self.logger.error("Exception occurred verifying reseller price is not empty" + str(e))
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

    def verify_customer_selection_popup_contents(self):
        try:
            self.do_click_by_locator(self.SELECT_CUSTOMER_BUTTON)
            popup_text = self.get_element_text(self.CUSTOMER_SELECTION_POPUP_TEXT)
            assert popup_text == 'To check inventory for a customer please start by typing the reseller customer name or BCN.', "Customer selection popup text mismatched"
            assert self.do_check_visibility(self.CUSTOMER_TEXTBOX) is True, "Customer popup textbox"
            assert self.do_check_visibility(self.POPUP_SELECT_BUTTON) is True, "Select button not found in popup"
            self.do_click_by_locator(self.POPUP_CLOSE_BUTTON)
        except Exception as e:
            self.logger.error("Exception while verifying customer selection popup contents" + str(e))
            raise e

    def verify_customer_selection_skip(self, customer):
        try:
            self.do_click_by_locator(self.SELECT_CUSTOMER_BUTTON)
            self.do_send_keys(self.CUSTOMER_TEXTBOX, customer)
            option = (By.XPATH, "//*[contains(text(),'" + customer + "')]")
            self.do_click_by_locator(option)
            self.do_click_by_locator(self.POPUP_CLOSE_BUTTON)
            assert self.do_check_visibility_for_validation(self.SELECTED_CUSTOMER) is False, "Customer is selected in list page"
        except Exception as e:
            self.logger.error("Exception while verifying customer selection skip" + str(e))
            raise e

    def select_customer(self, customer):
        try:
            self.do_click_by_locator(self.SELECT_CUSTOMER_BUTTON)
            self.do_send_keys(self.CUSTOMER_TEXTBOX, customer)
            option = (By.XPATH, "//*[contains(text(),'" + customer + "')]")
            self.do_click_by_locator(option)
            self.do_click_by_locator(self.POPUP_SELECT_BUTTON)
            selected_customer = self.get_element_text(self.SELECTED_CUSTOMER)
            assert selected_customer == customer, "Selected customer mismatched"
        except Exception as e:
            self.logger.error("Exception while selecting customer" + str(e))
            raise e

    def click_on_sku_and_validate_customer(self, search_sku, customer):
        try:
            skus = self.get_all_elements(self.SKUS_IN_GRID)
            for sku in skus:
                if sku.text == search_sku:
                    sku.click()
                    break
            details_page_sku_name = self.get_element_text(self.DETAILS_PAGE_SKU).split(": ")[-1]
            details_page_customer = self.get_element_text(self.SELECTED_CUSTOMER)
            assert details_page_sku_name == search_sku, "SKU name is in details page is different than searched one"
            assert details_page_customer == customer, "Customer in details page is different than selected one"
        except Exception as e:
            self.logger.error("Exception while clicking sku and validating data" + str(e))
            raise e

    def no_customer_by_default(self):
        try:
            assert self.do_check_visibility_for_validation(self.SELECTED_CUSTOMER) is False, "No customer present by default"
        except Exception as e:
            self.logger.error("Exception while checking no customer present by default" + str(e))
            raise e

    def verify_edit_customer_selection_skip(self, customer):
        try:
            previous_customer = self.get_element_text(self.SELECTED_CUSTOMER)
            self.do_click_by_locator(self.EDIT_CUSTOMER_BUTTON)
            self.do_send_keys(self.CUSTOMER_TEXTBOX, customer)
            option = (By.XPATH, "//*[contains(text(),'" + customer + "')]")
            self.do_click_by_locator(option)
            self.do_click_by_locator(self.POPUP_CLOSE_BUTTON)
            current_customer = self.get_element_text(self.SELECTED_CUSTOMER)
            if current_customer != previous_customer or current_customer == customer:
                raise Exception("Customer mismatch for skip edited customer")
        except Exception as e:
            self.logger.error("Exception while verifying skip edited customer" + str(e))
            raise e

    def verify_edit_customer_selection_save(self, customer):
        try:
            previous_customer = self.get_element_text(self.SELECTED_CUSTOMER)
            self.do_click_by_locator(self.EDIT_CUSTOMER_BUTTON)
            self.do_send_keys(self.CUSTOMER_TEXTBOX, customer)
            option = (By.XPATH, "//*[contains(text(),'" + customer + "')]")
            self.do_click_by_locator(option)
            self.do_click_by_locator(self.POPUP_SELECT_BUTTON)
            current_customer = self.get_element_text(self.SELECTED_CUSTOMER)
            if current_customer != customer or current_customer == previous_customer:
                raise Exception("Customer mismatch for save edited customer")
        except Exception as e:
            self.logger.error("Exception while verifying save edited customer " + str(e))
            raise e

    def verify_inventory_visibility_data_not_present(self):
        try:
            if not self.do_check_visibility_for_validation(self.INVENTORY_VISIBILITY_TEXT):
                raise Exception("Data is present under inventory visibility")
        except Exception as e:
            self.logger.error("Exception while verifying no data present under inventory visibility " + str(e))
            raise e

    def verify_inventory_visibility_data_present(self):
        try:
            if self.do_check_visibility_for_validation(self.INVENTORY_VISIBILITY_TEXT):
                raise Exception("Data is present under inventory visibility")
        except Exception as e:
            self.logger.error("Exception while verifying data present under inventory visibility " + str(e))
            raise e

    def click_on_sku(self, search_sku):
        try:
            skus = self.get_all_elements(self.SKUS_IN_GRID)
            for sku in skus:
                if sku.text == search_sku:
                    sku.click()
                    break
            details_page_sku_name = self.get_element_text(self.DETAILS_PAGE_SKU).split(": ")[-1]
            assert details_page_sku_name == search_sku, "SKU name is in details page is different than searched one"
        except Exception as e:
            self.logger.error("Exception while clicking sku and validating data" + str(e))
            raise e

    def go_back_to_listing_page_from_details(self):
        try:
            self.do_click_by_locator(self.INVENTORY_INQUIRY_LIST_PAGE_LINK)
            title = self.get_element_text(self.TITLE)
            assert title == "Inventory inquiry", 'Page title mismatched for inventory inquiry'
        except Exception as e:
            self.logger.error("Exception while going back to Inventory Inquiry list page from details page" + str(e))
            raise e

    def get_details_page_headers(self):
        headers_dict = {}
        try:
            header_names = self.get_all_elements(self.INVENTORY_DETAILS_PAGE_HEADERS)
            header_values = self.get_all_elements(self.INVENTORY_DETAILS_PAGE_HEADER_VALUES)
            for i in range(len(header_names)):
                headers_dict[(header_names[i].text).replace(':','')] = (header_values[i].text).split('\n')[-1]
            return headers_dict
        except Exception as e:
            self.logger.error("Exception while fetching inventory details page headers" + str(e))
            raise e

    def collect_sku_data(self):
        sku_data = {}
        try:
            sku_data['description'] = self.get_element_text(self.FIRST_ROW_DESCRIPTION)
            sku_data['vpn'] = self.get_element_text(self.FIRST_ROW_VPN)
            sku_data['vendor'] = self.get_element_text(self.FIRST_ROW_VENDOR)
            sku_data['class'] = self.get_element_text(self.FIRST_ROW_CLASS)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1100")
            sku_data['vendor code'] = self.get_element_text(self.FIRST_ROW_VENDOR_CODE)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return sku_data
        except Exception as e:
            self.logger.error("Exception while fetching sku data" + str(e))
            raise e

    def get_product_details(self):
        product_details_sections_headers = []
        description_section = {}
        vendor_details_section = {}
        codes_section = {}
        product_costs_section = {}
        try:
            header = self.get_element_text(self.PRODUCT_DETAILS_SECTION_NAME)
            assert header == 'Product Details', 'Product details header mismatched'
            self.logger.info("Getting section names under product details")
            self.do_click_by_locator(self.PRODUCT_DETAILS_EXPAND_ICON)
            section_names = self.get_all_elements(self.PRODUCT_DETAILS_SECTIONS)
            for section in section_names:
                product_details_sections_headers.append(section.text)
            product_details_sections_headers.append(self.get_element_text(self.PRODUCT_DETAILS_CODE_HEADER))
            product_details_sections_headers.append(self.get_element_text(self.PRODUCT_DETAILS_CATEGORIES_HEADER))
            self.logger.info("Getting data under product details")
            description_section['Description'] = self.get_element_text(self.DESCRIPTION_VALUE).split('\n')[0]
            vendor_data = self.get_all_elements(self.VENDOR_DETAILS_SECTIONS)
            for data in vendor_data:
                details = (data.text).split(':\n')
                vendor_details_section[details[0]] = details[1]
            codes_data = self.get_all_elements(self.CODES_SECTIONS)
            for data in codes_data:
                details = (data.text).split(':\n')
                codes_section[details[0]] = details[1]
            product_costs_data = self.get_all_elements(self.PRODUCT_COSTS_SECTION)
            for data in product_costs_data:
                details = (data.text).split(':\n')
                product_costs_section[details[0]] = details[1]
            self.do_click_by_locator(self.PRODUCT_DETAILS_EXPAND_ICON)
            self.logger.info("Successfully fetched data under product details")
            return product_details_sections_headers, description_section, vendor_details_section, codes_section, product_costs_section
        except Exception as e:
            self.logger.error("Exception while fetching product details data + str(e)")
            raise e

    def get_additional_attributes_details(self):
        additional_inventory_details_sections_headers = []
        categories_sections = {}
        general_information_sections = {}
        try:
            header = self.get_element_text(self.ADDITIONAL_INVENTORY_DETAILS)
            assert header == 'Additional inventory details', 'Additional inventory details header mismatched'
            self.logger.info("Getting section names under Additional inventory details")
            self.do_click_by_locator(self.ADDITIONAL_INVENTORY_DETAILS_EXPAND_ICON)
            additional_inventory_details_sections_headers.append(self.get_element_text(self.CATEGORIES_HEADER))
            additional_inventory_details_sections_headers.append(self.get_element_text(self.GENERAL_INFORMATION_HEADER))
            self.logger.info("Getting data under categories")
            categories_data = self.get_all_elements(self.CATEGORIES_SECTIONS)
            for data in categories_data:
                details = (data.text).split(':\n')
                categories_sections[details[0]] = details[1]
            general_information_data = self.get_all_elements(self.GENERAL_INFORMATION_SECTIONS)
            for data in general_information_data:
                details = (data.text).split(':\n')
                general_information_sections[details[0]] = details[1]
            self.do_click_by_locator(self.ADDITIONAL_INVENTORY_DETAILS_EXPAND_ICON)
            self.logger.info("Successfully fetched data under additional inventory details")
            return additional_inventory_details_sections_headers, categories_sections, general_information_sections
        except Exception as e:
            self.logger.error("Exception while fetching additional inventory details + str(e)")
            raise e

    def validate_inventory_visibility_table(self):
        columns = []
        try:
            self.logger.info("Fetching inventory visibility table headers")
            table_headers = self.get_all_elements(self.INVENTORY_VISIBILITY_TABLE_HEADERS)
            for column in table_headers:
                columns.append(column.text)
            self.logger.info("Successfully fetched inventory visibility table headers")
            self.logger.info("Validating sort for inventory visibility table")
            self.sort_availability()
            self.sort_commited()
            self.sort_future()
            self.sort_on_order()
            self.sort_in_transit()
            self.sort_on_hold()
            self.sort_on_hand()
            self.sort_average_cost()
            self.sort_eta()
            return columns
        except Exception as e:
            self.logger.error("Exception while validating inventory visibility + str(e)")
            raise e

    def sort_availability(self):
        availability_value_ascending = []
        availability_value_descending = []
        try:
            self.logger.info("Validating ascending sort for Availability column")
            self.do_click_by_locator(self.AVAILABLE_SORT)
            rows = self.get_all_elements(self.AVAILABLE_ROWS)
            for row in rows:
                availability_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(availability_value_ascending)-1):
                    if availability_value_ascending[i] <= availability_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Availability is not in Ascending. Current value:{availability_value_ascending[i]} Next value:{availability_value_ascending[i + 1]}')
                        raise Exception('Availability is not in Ascending')
            self.logger.info("Validating descending sort for Availability column")
            self.do_click_by_locator(self.AVAILABLE_SORT)
            rows = self.get_all_elements(self.AVAILABLE_ROWS)
            for row in rows:
                availability_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(availability_value_descending)-1):
                    if availability_value_descending[i] >= availability_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Availability is not in Desscending. Current value:{availability_value_descending[i]} Next value:{availability_value_descending[i + 1]}')
                        raise Exception('Availability is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for Availability + str(e)")
            raise e

    def sort_commited(self):
        commited_value_ascending = []
        commited_value_descending = []
        try:
            self.logger.info("Validating ascending sort for Commited column")
            self.do_click_by_locator(self.COMMITED_SORT)
            rows = self.get_all_elements(self.COMMITED_ROWS)
            for row in rows:
                commited_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(commited_value_ascending)-1):
                    if commited_value_ascending[i] <= commited_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Commited is not in Ascending. Current value:{commited_value_ascending[i]} Next value:{commited_value_ascending[i + 1]}')
                        raise Exception('Commited is not in Ascending')
            self.logger.info("Validating descending sort for Commited column")
            self.do_click_by_locator(self.COMMITED_SORT)
            rows = self.get_all_elements(self.COMMITED_ROWS)
            for row in rows:
                commited_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(commited_value_descending)-1):
                    if commited_value_descending[i] >= commited_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Commited is not in Descending. Current value:{commited_value_descending[i]} Next value:{commited_value_descending[i + 1]}')
                        raise Exception('Commited is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for Commited column + str(e)")
            raise e

    def sort_future(self):
        future_value_ascending = []
        future_value_descending = []
        try:
            self.logger.info("Validating ascending sort for Future column")
            self.do_click_by_locator(self.FUTURE_SORT)
            rows = self.get_all_elements(self.FUTURE_ROWS)
            for row in rows:
                future_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(future_value_ascending)-1):
                    if future_value_ascending[i] <= future_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Future is not in Ascending. Current value:{future_value_ascending[i]} Next value:{future_value_ascending[i + 1]}')
                        raise Exception('Future is not in Ascending')
            self.logger.info("Validating descending sort for Future column")
            self.do_click_by_locator(self.FUTURE_SORT)
            rows = self.get_all_elements(self.FUTURE_ROWS)
            for row in rows:
                future_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(future_value_descending)-1):
                    if future_value_descending[i] >= future_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Future is not in Descending. Current value:{future_value_descending[i]} Next value:{future_value_descending[i + 1]}')
                        raise Exception('Future is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for Future column + str(e)")
            raise e

    def sort_on_order(self):
        on_order_value_ascending = []
        on_order_value_descending = []
        try:
            self.logger.info("Validating ascending sort for On order column")
            self.do_click_by_locator(self.ON_ORDER_SORT)
            rows = self.get_all_elements(self.ON_ORDER_ROWS)
            for row in rows:
                on_order_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(on_order_value_ascending)-1):
                    if on_order_value_ascending[i] <= on_order_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'On order is not in Ascending. Current value:{on_order_value_ascending[i]} Next value:{on_order_value_ascending[i + 1]}')
                        raise Exception('On order is not in Ascending')
            self.logger.info("Validating descending sort for On order column")
            self.do_click_by_locator(self.ON_ORDER_SORT)
            rows = self.get_all_elements(self.ON_ORDER_ROWS)
            for row in rows:
                on_order_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(on_order_value_descending)-1):
                    if on_order_value_descending[i] >= on_order_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'On order is not in Descending. Current value:{on_order_value_descending[i]} Next value:{on_order_value_descending[i + 1]}')
                        raise Exception('On order is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for On order column + str(e)")
            raise e

    def sort_in_transit(self):
        in_transit_value_ascending = []
        in_transit_value_descending = []
        try:
            self.logger.info("Validating ascending sort for In transit column")
            self.do_click_by_locator(self.IN_TRANSIT_SORT)
            rows = self.get_all_elements(self.IN_TRANSIT_ROWS)
            for row in rows:
                in_transit_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(in_transit_value_ascending)-1):
                    if in_transit_value_ascending[i] <= in_transit_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'In transit is not in Ascending. Current value:{in_transit_value_ascending[i]} Next value:{in_transit_value_ascending[i + 1]}')
                        raise Exception('In transit is not in Ascending')
            self.logger.info("Validating descending sort for In transit column")
            self.do_click_by_locator(self.IN_TRANSIT_SORT)
            rows = self.get_all_elements(self.IN_TRANSIT_ROWS)
            for row in rows:
                in_transit_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(in_transit_value_descending)-1):
                    if in_transit_value_descending[i] >= in_transit_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'In transit is not in Descending. Current value:{in_transit_value_descending[i]} Next value:{in_transit_value_descending[i + 1]}')
                        raise Exception('In transit is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for In transit column + str(e)")
            raise e

    def sort_on_hold(self):
        on_hold_value_ascending = []
        on_hold_value_descending = []
        try:
            self.logger.info("Validating ascending sort for On hold column")
            self.do_click_by_locator(self.ON_HOLD_SORT)
            rows = self.get_all_elements(self.ON_HOLD_ROWS)
            for row in rows:
                on_hold_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(on_hold_value_ascending)-1):
                    if on_hold_value_ascending[i] <= on_hold_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'On hold is not in Ascending. Current value:{on_hold_value_ascending[i]} Next value:{on_hold_value_ascending[i + 1]}')
                        raise Exception('On hold is not in Ascending')
            self.logger.info("Validating descending sort for On hold column")
            self.do_click_by_locator(self.ON_HOLD_SORT)
            rows = self.get_all_elements(self.ON_HOLD_ROWS)
            for row in rows:
                on_hold_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(on_hold_value_descending)-1):
                    if on_hold_value_descending[i] >= on_hold_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'On hold is not in Descending. Current value:{on_hold_value_descending[i]} Next value:{on_hold_value_descending[i + 1]}')
                        raise Exception('On hold is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for On hold column + str(e)")
            raise e

    def sort_on_hand(self):
        on_hand_value_ascending = []
        on_hand_value_descending = []
        try:
            self.logger.info("Validating ascending sort for On hand column")
            self.do_click_by_locator(self.ON_HAND_SORT)
            rows = self.get_all_elements(self.ON_HAND_ROWS)
            for row in rows:
                on_hand_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(on_hand_value_ascending)-1):
                    if on_hand_value_ascending[i] <= on_hand_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'On hand is not in Ascending. Current value:{on_hand_value_ascending[i]} Next value:{on_hand_value_ascending[i + 1]}')
                        raise Exception('On hand is not in Ascending')
            self.logger.info("Validating descending sort for On hand column")
            self.do_click_by_locator(self.ON_HAND_SORT)
            rows = self.get_all_elements(self.ON_HAND_ROWS)
            for row in rows:
                on_hand_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(on_hand_value_descending)-1):
                    if on_hand_value_descending[i] >= on_hand_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'On hand is not in Descending. Current value:{on_hand_value_descending[i]} Next value:{on_hand_value_descending[i + 1]}')
                        raise Exception('On hand is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for On hand column + str(e)")
            raise e

    def sort_average_cost(self):
        average_cost_value_ascending = []
        average_cost_value_descending = []
        try:
            self.logger.info("Validating ascending sort for Average cost column")
            self.do_click_by_locator(self.AVERAGE_COST_SORT)
            rows = self.get_all_elements(self.AVERAGE_COST_ROWS)
            for row in rows:
                average_cost_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(average_cost_value_ascending)-1):
                    if average_cost_value_ascending[i] <= average_cost_value_ascending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Average cost is not in Ascending. Current value:{average_cost_value_ascending[i]} Next value:{average_cost_value_ascending[i + 1]}')
                        raise Exception('Average cost is not in Ascending')
            self.logger.info("Validating descending sort for Average cost column")
            self.do_click_by_locator(self.AVERAGE_COST_SORT)
            rows = self.get_all_elements(self.AVERAGE_COST_ROWS)
            for row in rows:
                average_cost_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(average_cost_value_descending)-1):
                    if average_cost_value_descending[i] >= average_cost_value_descending[i + 1]:
                        continue
                    else:
                        self.logger.error(
                            f'Average cost is not in Descending. Current value:{average_cost_value_descending[i]} Next value:{average_cost_value_descending[i + 1]}')
                        raise Exception('Average cost is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for Average cost column + str(e)")
            raise e

    def sort_eta(self):
        eta_value_ascending = []
        eta_value_descending = []
        try:
            self.logger.info("Validating ascending sort for ETA column")
            self.do_click_by_locator(self.ETA_SORT)
            rows = self.get_all_elements(self.ETA_ROWS)
            for row in rows:
                eta_value_ascending.append(row.text)
            if len(rows) > 1:
                for i in range(len(eta_value_ascending)-1):
                    if datetime.strptime(eta_value_ascending[i], '%Y-%m-%d') <= datetime.strptime(eta_value_ascending[i+1], '%Y-%m-%d'):
                        continue
                    else:
                        self.logger.error(f'ETA is not in Ascending. Current value:{eta_value_ascending[i]} Next value:{eta_value_ascending[i + 1]}')
                        raise Exception('ETA is not in Ascending')
            self.logger.info("Validating descending sort for ETA column")
            self.do_click_by_locator(self.ETA_SORT)
            rows = self.get_all_elements(self.ETA_ROWS)
            for row in rows:
                eta_value_descending.append(row.text)
            if len(rows) > 1:
                for i in range(len(eta_value_descending)-1):
                    if datetime.strptime(eta_value_descending[i], '%Y-%m-%d') >= datetime.strptime(eta_value_descending[i+1], '%Y-%m-%d'):
                        continue
                    else:
                        self.logger.error(
                            f'ETA is not in Descending. Current value:{eta_value_descending[i]} Next value:{eta_value_descending[i + 1]}')
                        raise Exception('ETA is not in Descending')
        except Exception as e:
            self.logger.error("Exception while validating sort for ETA column + str(e)")
            raise e
