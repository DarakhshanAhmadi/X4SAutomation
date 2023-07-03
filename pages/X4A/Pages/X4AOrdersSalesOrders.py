import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile


class X4ASalesOrdersPage(BasePage):
    parse_config_json = ParseConfigFile()

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
    """constructor of the Login Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def do_click_on_sales_order(self):
        try:
            self.do_click_by_locator(self.ORDER_MENU)
            self.do_double_click(self.SALES_ORDER_OPTION)
        except Exception as e:
            self.logger.error("Exception occurred while clicking the order button %s", e)
            raise e




