import time

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage


class X4AInventoryManagementPage(BasePage):

    INVENTORY_MENU = (By.XPATH, "//div[@data-testid='inventory-MenuItem']")
    INVENTORY_MANAGEMENT_OPTION = (By.XPATH, "//*[text()='Inventory management']")
    ACTION_PLANNING = (By.XPATH, "//*[text()='Action planning']")
    TOP_100_UNDERPERFORMING_SKU_TAB = (By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 css-zac9d4-MuiTypography-root'][text()='Top 100 Underperforming (UP) SKU']")
    FIRST_COLUMN = (By.XPATH, "//div[text()='SKU'][@class='MuiDataGrid-columnHeaderTitle css-t89xny-MuiDataGrid-columnHeaderTitle']")
    PAGINATION_TAB = (By.XPATH, "//div[@data-testid='required-showing']")
    TOP_100_UNDERPERFORMING_TABLE_HEADERS = (By.XPATH, "//div[@class='css-yrdy0g-MuiDataGrid-columnHeaderRow'][@aria-rowindex=2]/div")
    ACTION_PLANING_PAGE_ELEMENT = "//div[@data-testid='required-Content']"
    COUNTRY_DROPDOWN = (By.XPATH, "//div[@data-testid='required-SelectOption']")
    COUNTRY_DROPDOWN_OPTIONS = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-6hp17o-MuiList-root-MuiMenu-list']/li")

    def go_to_inventory_management_action_planning(self):
        try:
            self.do_click_by_locator(self.INVENTORY_MENU)
            self.do_double_click(self.INVENTORY_MANAGEMENT_OPTION)
            self.do_double_click(self.ACTION_PLANNING)
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Inventory Inquiry' + str(e))
            raise e

    def click_on_top_100_underperforming_sku(self):
        try:
            self.do_click_by_locator(self.TOP_100_UNDERPERFORMING_SKU_TAB)
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Top 100 underperforming sku tab' + str(e))
            raise e

    def get_table_headers(self, selected_country):
        table_headers = []
        try:
            page_element = self.driver.find_element(By.XPATH, self.ACTION_PLANING_PAGE_ELEMENT)
            self.scroll_down(page_element)
            self.do_click_by_locator(self.COUNTRY_DROPDOWN)
            country_dropdown_options = self.get_all_elements(self.COUNTRY_DROPDOWN_OPTIONS)
            self.logger.info(f'searching for {selected_country} in dropdown')
            for country in country_dropdown_options:
                if country.text == selected_country:
                    self.logger.info(f'{selected_country} found in the dropdown')
                    country.click()
                    break
            for i in range(1, 24):
                xpath = (By.XPATH, "//div[@class='css-yrdy0g-MuiDataGrid-columnHeaderRow'][@aria-rowindex=2]/div[@aria-colindex=" + str(i) + "]")
                if i == 7:
                    self.driver.execute_script(
                        "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
                    time.sleep(2)
                elif i == 15:
                    self.driver.execute_script(
                        "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 3000")
                    time.sleep(2)
                header = self.get_element_text(xpath)
                table_headers.append(header)
            self.logger.info(table_headers)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return table_headers
        except Exception as e:
            self.logger.error('Exception occurred while getting Top 100 underperforming sku table headers' + str(e))
            raise e
