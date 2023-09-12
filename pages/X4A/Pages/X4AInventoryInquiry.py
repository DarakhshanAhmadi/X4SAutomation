import time

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage


class X4AInventoryInquiryPage(BasePage):

    INVENTORY_MENU = (By.XPATH, "//div[@data-testid='inventory-MenuItem']")
    INVENTORY_INQUIRY_OPTION = (By.XPATH, "//li[@data-testid='inventory-inventory_inquiry-CategoryName']")
    TABLE_COLUMN_HEADERS_CONTAINER = (By.XPATH, "//div[@class='MuiDataGrid-columnHeadersInner MuiDataGrid-columnHeadersInner--scrollable css-1s0hp0k-MuiDataGrid-columnHeadersInner']")
    VENDOR_SORT_ICON = (By.XPATH, "//*[text()='Vendor']")

    def go_to_inventory_inquiry(self):
        try:
            self.do_click_by_locator(self.INVENTORY_MENU)
            self.do_double_click(self.INVENTORY_INQUIRY_OPTION)
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Inventory Inquiry' + str(e))
            raise e

    def get_table_column_header(self):
        inventory_inquiry_table_column_header = []
        try:
            time.sleep(1)
            column_headers = self.get_element_text(self.TABLE_COLUMN_HEADERS_CONTAINER)
            inventory_inquiry_table_column_header = column_headers.split("\n")
            time.sleep(3)
            for i in range(1, 15):
                if i == 9:
                    # manually intervene and scroll horizontally
                    time.sleep(10)
                if i == 8 or i == 12 or i == 14:
                    column = "//div[@class='MuiDataGrid-row']/div[@data-colindex='" + str(i) + "']"
                    scroll_element = self.driver.find_element(By.XPATH, column)
                    self.scroll_horizontally(scroll_element)
                    column_headers = self.get_element_text(self.TABLE_COLUMN_HEADERS_CONTAINER)
                    inventory_inquiry = column_headers.split("\n")
                    for column_header in inventory_inquiry:
                        if column_header not in inventory_inquiry_table_column_header:
                            inventory_inquiry_table_column_header.append(column_header)
            self.logger.info("Inventory Inquiry column headers :" + str(inventory_inquiry_table_column_header))
            self.logger.info("Inventory Inquiry table column headers fetched successfully")
            return inventory_inquiry_table_column_header
        except Exception as e:
            self.logger.error("Exception occurred while retrieving the column header of Inventory Inquiry " + str(e))
            raise e




        
