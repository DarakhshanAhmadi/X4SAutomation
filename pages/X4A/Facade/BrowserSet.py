from CommonUtilities.baseSet.BasePage import BasePage

class BrowserSettings(BasePage):

    """constructor of the Login Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ Clear browser cache and cookies """

    def do_clear_browser_history_and_cache(self):
        self.driver.delete_all_cookies()
        # self.do_sleep(5)
        # self.driver.get("chrome://settings/clearBrowserData")
        # self.do_sleep(5)
        # keyboard.send("Enter")

