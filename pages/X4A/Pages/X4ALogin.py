from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile


class LoginPage(BasePage):
    parse_config_json = ParseConfigFile()

    """By locators"""
    USERNAME_TEXTBOX = (By.NAME, "loginfmt")
    PASSWORD_TEXTBOX = (By.NAME, "passwd")
    SUBMIT_BUTTON = (By.ID, "idSIButton9")

    """constructor of the Login Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for login page"""

    """
    This is used to login to IM360
    Author: Soumi Ghosh
    """

    def do_login_to_x4a(self, username, password):
        try:
            self.do_send_keys(self.USERNAME_TEXTBOX, username)
            self.logger.info("Successfully posted the username: %s" % username)
            self.do_click_by_locator(self.SUBMIT_BUTTON)
            self.logger.info("Successfully submitted the username")
            self.do_send_keys(self.PASSWORD_TEXTBOX, password)
            self.logger.info("Successfully posted the password")
            self.do_click_by_locator(self.SUBMIT_BUTTON)
            self.logger.info("Successfully submitted the password")
            self.do_click_by_locator(self.SUBMIT_BUTTON)
            self.logger.info("Proceeding for App selection page")
            self.logger.info("Login successfully")
        except Exception as e:
            self.logger.error("Exception occurred while login the x4a %s", e)
            raise e
