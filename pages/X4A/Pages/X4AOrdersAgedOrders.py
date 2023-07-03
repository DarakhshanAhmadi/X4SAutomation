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

    def go_to_aged_orders(self):
        try:
            self.do_click_by_locator(self.ORDER_MENU)
            self.do_click_by_locator(self.AGED_ORDER_OPTION)
            self.logger.info("Clicked on Aged orders in the menu.")
        except Exception as e:
            self.logger.error('Exception occured while clicking on Aged orders ' + str(e))
            raise e

