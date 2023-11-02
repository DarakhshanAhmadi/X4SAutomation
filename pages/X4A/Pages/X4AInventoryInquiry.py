import time

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage


class X4AInventoryInquiryPage(BasePage):

    INVENTORY_MENU = (By.XPATH, "//div[@data-testid='inventory-MenuItem']")
    INVENTORY_INQUIRY_OPTION = (By.XPATH, "//li[@data-testid='inventory-inventory_inquiry-CategoryName']")
    TABLE_COLUMN_HEADERS_CONTAINER = (By.XPATH, "//div[@class='MuiDataGrid-columnHeadersInner MuiDataGrid-columnHeadersInner--scrollable css-1s0hp0k-MuiDataGrid-columnHeadersInner']")
    VENDOR_SORT_ICON = (By.XPATH, "//*[text()='Vendor']")
    SEARCH_TEXTBOX = (By.XPATH, "//input[@id='search']")
    SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    GRID_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']/div[@role='row']")
    FIRST_ROW_SKU = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='sku']")
    CLOSE_ICON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    TITLE = (By.XPATH, "//h2[@class='MuiTypography-root MuiTypography-h2 css-h794si-MuiTypography-root']")
    PAGE_NAVIGATION = (By.XPATH, "//ol[@class='MuiBreadcrumbs-ol css-4pdmu4-MuiBreadcrumbs-ol']/li")

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
            assert navigation_path == 'Home > Inventory > Inventory Inquiry', 'Navigation path mismatched for inventory inquiry'
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
