import time

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage


class X4AInventoryManagementPage(BasePage):

    INVENTORY_MENU = (By.XPATH, "//div[@data-testid='inventory-MenuItem']")
    INVENTORY_MANAGEMENT_OPTION = (By.XPATH, "//*[text()='Inventory management']")
    ACTION_PLANNING = (By.XPATH, "//*[text()='Action planning']")
    TOP_100_UNDERPERFORMING_SKU_TAB = (By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h5 css-9fomdi-MuiTypography-root'][text()='Top 100 Underperforming (UP) SKU']")

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
            self.do_click_by_locator(self.INVENTORY_MENU)
            self.do_double_click(self.INVENTORY_MANAGEMENT_OPTION)
            self.do_click_by_locator(self.ACTION_PLANNING)
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Inventory Inquiry' + str(e))
            raise e


