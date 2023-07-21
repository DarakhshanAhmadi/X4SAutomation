from selenium.webdriver.common.by import By
from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig

class X4AErrorOrdersPage(BasePage):
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

    ORDER_MENU = (By.XPATH, "//*[@data-testid='orders-MenuItem']")
    ERROR_ORDER_OPTION = (By.XPATH, "//*[text()='Error Orders']")
    ERROR_ORDER_TEXT = (By.XPATH, "//*[text()='Error orders ']")
    DATA_ERROR_OPTION = (By.XPATH, "//div[text()='Data errors']")
    SYSTEM_ERROR_OPTION = (By.XPATH, "//div[text()='System errors']")
    DISABLED_CANCEL_BUTTON = (By.XPATH, "//button[@disabled and text() = 'Cancel']")
    ENABLED_CANCEL_BUTTON = (By.XPATH, "//button[not(@disable) and text() = 'Cancel']")
    CANCEL_BUTTON = (By.XPATH, "//button[text() = 'Cancel']")
    CHECKBOX = (By.XPATH, "//div[@data-rowindex='2']/div[@data-field='__check__']")
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BOX_SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    CANCEL_ORDER_TITLE = (By.XPATH, "//div[@class = 'ModelTitle']")
    CANCEL_ORDER_MSG = (By.XPATH, "//div[text()='Cancel order']/parent::div/div[@class='modelBody']")
    CANCEL_NO_BUTTON = (By.XPATH, "//button[text() = 'No, Keep order']")
    CANCEL_YES_BUTTON = (By.XPATH, "//button[text() = 'Yes, cancel order']")

    REASON_MSG = (By.XPATH, "//div[text()='Cancel order']/parent::div/div[@class='modelBody']/div")
    REASON_TEXTAERA = (By.XPATH, "//div[text()='Cancel order']/parent::div/div[@class='modelBody']/div/following-sibling::textarea")
    BACK_BUTTON = (By.XPATH, "//button[text() = 'Back']")
    CANCEL_ORDER_BUTTON = (By.XPATH, "//button[text() = 'cancel order']")
    CANCEL_ORDER_MESSAGE = (By.XPATH, "//div[text() = 'Cancel notes required!.']")
    CANCEL_ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[text() = 'Cancelled! order was successfully cancelled.']")

    def go_to_error_orders(self):
        try:
            self.do_click_by_locator(self.ORDER_MENU)
            self.logger.info("Clicked on Order in the menu")
            self.do_double_click(self.ERROR_ORDER_OPTION)
            self.logger.info("Clicked on Error Orders option")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Error orders ' + str(e))
            raise e

    def select_multiple_record(self):
        try:
            self.do_click_by_locator(self.SYSTEM_ERROR_OPTION)
            self.logger.info("Clicked on system error list")
            for i in range(0, 2):
                checkbox = (By.XPATH, "//div[@data-rowindex='" + str(i) + "']/div[@data-field='__check__']")
                self.do_click_by_locator(checkbox)

            self.logger.info("Selected multiple record")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on multiple record ' + str(e))
            raise e

    def single_record_list(self):
        try:
            self.go_to_error_orders()
            self.do_click_by_locator(self.DATA_ERROR_OPTION)
            self.logger.info("Clicked on data error list")
            self.do_click_by_locator(self.SYSTEM_ERROR_OPTION)
            self.logger.info("Clicked on system error list")
            self.do_click_by_locator(self.CHECKBOX)
            self.logger.info("Selected single record")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on single record ' + str(e))
            raise e

    def do_verify_cancel_button(self, status):
        try:
            #
            if status == 'disabled':
                assert self.do_check_visibility(self.DISABLED_CANCEL_BUTTON),"Cancel button is not disabled"
                self.logger.info("Successfully verified cancel button is disabled")
            else:
                assert self.do_check_visibility(self.ENABLED_CANCEL_BUTTON),"Cancel button is not enabled"
                self.logger.info("Successfully verified cancel button is enabled")
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel button ' + str(e))
            raise e

    def do_click_cancel_button(self):
        try:
            self.do_click_by_locator(self.CANCEL_BUTTON)
            self.logger.info("Successfully clicked on cancel button")
        except Exception as e:
            self.logger.eror('Exception occurred while clicking on cancel button ' + str(e))
            raise e

    def do_verify_cancel_order_popup(self):
        try:
            cancel_order = 'Cancel order'
            cancel_order_msg = 'Are you sure you want to cancel order? Order will be cancelled permanently,' \
                               ' and you cannot undo this action.'
            cancel_no_button = 'NO, KEEP ORDER'
            cancel_yes_button = 'YES, CANCEL ORDER'
            address = self.get_element_text(self.CANCEL_ORDER_MSG).replace("\n", " ")
            assert cancel_order in self.get_element_text(self.CANCEL_ORDER_TITLE),"Cancel Order Title not present"
            assert cancel_no_button in self.get_element_text(self.CANCEL_NO_BUTTON),"Cancel No button is not present"
            assert cancel_yes_button in self.get_element_text(self.CANCEL_YES_BUTTON),"Cancel Yes button is not present"
            assert cancel_order_msg in address, "Cancel Order message not present"
            
            self.logger.info("Successfully verified cancel order title, No button ,Yes button and message in popup menu")
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel button ' + str(e))
            raise e

    def do_click_no_cancel_button(self):
        try:
            self.do_click_by_locator(self.CANCEL_NO_BUTTON)
            self.logger.info("Successfully clicked on No button")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on NO button from cancel order popup ' + str(e))
            raise e

    def do_verify_error_details_page(self):
        try:
            assert 'Error orders' in self.get_element_text(self.ERROR_ORDER_TEXT),"Cancel Order Title not present"
            self.logger.info("verified that cancel order popup is closed")
            self.do_click_by_locator(self.CANCEL_BUTTON)

        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order popup is closed ' + str(e))
            raise e

    def do_click_yes_cancel_button(self):
        try:
            self.do_click_by_locator(self.CANCEL_YES_BUTTON)
            self.logger.info("Clicked on YES button from cancel order popup")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on YES button from cancel order popup ' + str(e))
            raise e


    def verify_cancel_order_popup_after_yes(self):
        try:
            assert 'Cancel order' in self.get_element_text(self.CANCEL_ORDER_TITLE),"Cancel Order Title not present"
            assert 'CANCEL ORDER' in self.get_element_text(self.CANCEL_ORDER_BUTTON),"Cancel order button is not present"
            assert 'BACK' in self.get_element_text(self.BACK_BUTTON),"Back button is not present"
            assert 'Reason for cancelling *' in self.get_element_text(self.REASON_MSG), "Reason for cancelling message is not present"
            self.logger.info(
                "Successfully verified cancel order title, cancel order button ,back button and message in popup menu")
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order popup is closed ' + str(e))
            raise e


    def do_click_back_cancel_button(self):
        try:
            self.do_click_by_locator(self.BACK_BUTTON)
            self.logger.info("Clicked on back button")

        except Exception as e:
            self.logger.error('Exception occurred while clicking on YES button from cancel order popup ' + str(e))
            raise e

    def do_cancel_order_without_reason(self):
        try:
            self.do_click_by_locator(self.CANCEL_YES_BUTTON)
            self.logger.info("Clicked on YES button from cancel order popup")
            self.do_click_by_locator(self.CANCEL_ORDER_BUTTON)
            self.logger.info("Clicked on cancel order button from cancel order popup")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on back button from cancel order popup ' + str(e))
            raise e

    def do_verify_cancel_order_message(self):
        try:
            cancel_order_message = 'Cancel notes required!.'
            assert cancel_order_message in self.get_element_text(self.CANCEL_ORDER_MESSAGE),"Cancel note not present"
            self.logger.info("Successfully verified cancel message")
            self.do_click_by_locator(self.BACK_BUTTON)
            self.logger.info("Clicked on back button")

        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order message ' + str(e))
            raise e

    def do_cancel_order_with_reason(self):
        try:
            self.do_click_by_locator(self.CANCEL_YES_BUTTON)
            self.logger.info("Clicked on YES button from cancel order popup")
            self.do_click_by_locator(self.REASON_TEXTAERA)
            self.do_send_keys(self.REASON_TEXTAERA, 'Order is invalid')
            self.logger.info("Reason mentioned for cancelling order")
            self.do_click_by_locator(self.CANCEL_ORDER_BUTTON)
            self.logger.info("Clicked on cancel order button from cancel order popup")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on back button from cancel order popup ' + str(e))
            raise e


    def do_cancel_order_success_message(self):
        try:
            
            cancel_order_message = 'Cancelled! order was successfully cancelled.'
            assert cancel_order_message in self.get_element_text(self.CANCEL_ORDER_SUCCESS_MESSAGE),"successfull Cancel Order message not present"
            self.logger.info("order cancelled successfully")

        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order success message ' + str(e))
            raise e



