import time
import random
import string
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig


class X4AErrorOrdersPage(BasePage):
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

    SALES_ICON = (By.XPATH, "//*[@data-testid='SalesIcon']")
    SALES_MENU = (By.XPATH, "//*[@data-testid='sales-MenuItem']")
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
    REASON_TEXTAERA = (
        By.XPATH, "//div[text()='Cancel order']/parent::div/div[@class='modelBody']/div/following-sibling::textarea")
    BACK_BUTTON = (By.XPATH, "//button[text() = 'Back']")
    CANCEL_ORDER_BUTTON = (By.XPATH, "//button[text() = 'cancel order']")
    CANCEL_ORDER_MESSAGE = (By.XPATH, "//div[text() = 'Cancel notes required!.']")
    CANCEL_ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[text() = 'Cancelled! order was successfully cancelled.']")
    USER_DROPDOWN = (By.XPATH, "//*[@data-testid='KeyboardArrowDownIcon']")
    LOGOUT = (By.XPATH, "//*[text()='LogOut']")

    """Fraud Orders tab"""
    FRAUD_ORDERS_TAB = (By.XPATH, "//div[text()='Fraud orders']")
    FRAUD_FIRST_RECORD = (
        By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='orderConfirmationNumber']/div/a")
    FRAUD_REPROCESS_ORDER_BUTTON = (By.XPATH, "//button[text()='Reprocess Order']")
    REPROCESS_ORDER_TITLE = (By.XPATH, "//div[@class = 'ModelTitle']")
    REPROCESS_ORDER_POPUP_MSG = (By.XPATH, "//div[text()='Reprocess Order']/parent::div/div[@class='modelBody']")
    REPROCESS_ORDER_REVIEW_BUTTON = (By.XPATH, "//*[@class='ModelTitle']/parent::div/div/button[1]")
    YES_REPROCESS_ORDER_BUTTON = (By.XPATH, "//*[@class='ModelTitle']/parent::div/div/button[2]")
    ORDER_DETAILS_PAGE = (By.XPATH, "//*[@aria-label='breadcrumb']/ol/li[5]/p")
    REPROCESS_ORDER_SUCCESS_MESSAGE = (By.XPATH, "//*[@class='MuiAlert-message css-acap47-MuiAlert-message']")
    ERROR_ORDER_PAGE = (By.XPATH, "//*[text()='Error orders']")
    DROP_DOWN = (By.XPATH, "//*[@data-testid='search-dropdown-SelectOption']")
    SEARCH_DROP_DOWN = (By.XPATH, "//div[@data-testid='SearchBar']//div[@data-testid='search-dropdown-SelectOption']")
    CONFRIMATION_ID_OPTION = (By.XPATH, "//*[@data-testid='confirmationId-MenuItem']")
    FRAUD_SEARCH_BOX = (By.XPATH, "//*[@data-testid='SearchBar']/div/input")
    FRAUD_CANCEL_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Cancel Order']")
    ORDER_NOT_FOUND = (By.XPATH, "//*[text()='No failed orders found.']")

    """Data errors Orders tab"""

    DATA_ERRORS_SEARCH_BOX = (By.XPATH, "//*[@data-testid='SearchBar']/div/input")
    DATA_ERRORS_RESUBMIT_ORDER_BUTTON = (By.XPATH, "//*[text()='Resubmit Order']")
    RESELLER_PO_VALUE = (By.XPATH, "//*[@id='reference-details-po-number']")
    REFERENCE_DETAILS_EDIT_BUTTON = (
        By.XPATH, "//*[text()='Reference Details']/parent::div/*[@data-testid='ModeEditOutlineOutlinedIcon']")
    END_CUSTOMER_ORDER_VALUE = (By.XPATH, "//*[@id='reference-details-edit-customer-number']")
    DATA_ERROR_ORDER_UPDATE_BUTTON = (By.XPATH, "//button[text()='Update']")
    RESUBMIT_ORDER_TITLE = (By.XPATH, "//div[@class = 'ModelTitle']")
    RESUBMIT_ORDER_POPUP_MSG = (By.XPATH, "//div[text()='Resubmit Order']/parent::div/div[@class='modelBody']")
    RESUBMIT_ORDER_REVIEW_BUTTON = (By.XPATH, "//*[@class='ModelTitle']/parent::div/div/button[1]")
    YES_RESUBMIT_ORDER_BUTTON = (By.XPATH, "//*[@class='ModelTitle']/parent::div/div/button[2]")
    RESUBMITTED_ORDER_SUCCESS_MESSAGE = (By.XPATH, "//*[@class='MuiAlert-message css-acap47-MuiAlert-message']")

    """Edit Reference numbers popup"""

    EDIT_REFERENCE_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/p")
    REFERENCE_DETAILS_PO_FIELD = (
        By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/following-sibling::div/div/div[1]/label")
    REFERENCE_DETAILS_MANDATORY_FIELD = (
        By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/following-sibling::div/div/div/label/span")
    REFERENCE_DETAILS_END_USER_CUSTOMER_FIELD = (
        By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/following-sibling::div/div/div[2]/label")
    REFERENCE_DETAILS_CANCEL_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../div[3]/button[1]")
    REFERENCE_DETAILS_UPDATE_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../div[3]/button[2]")
    REFERENCE_DETAILS_ClOSE_ICON_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    REFERENCE_DETAILS_PO_CHAR_COUNT_RATIO_BUTTON = (By.XPATH, "//*[@id='reference-details-po-number-helper-text']")
    END_CUSTOMER_ORDER_CHAR_COUNT_RATIO_BUTTON = (
        By.XPATH, "//*[@id='reference-details-edit-customer-number-helper-text']")
    REFERENCE_DETAILS_PO_FIELD_VALUE = (By.XPATH, "//*[text()='PO #:']/parent::div/p/strong")
    REFERENCE_DETAILS_END_CUSTOMER_ORDER_FIELD_VALUE = (
        By.XPATH, "//*[text()='End customer order #:']/parent::div/p/strong")

    """Shipping Notes"""

    BILLING_SHIPPING_TAB = (By.XPATH, "//div[text()='Billing/Shipping']")
    SHIPPING_NOTES_EDIT_BUTTON = (
        By.XPATH, "//*[text()='Shipping Notes']/parent::div/*[@data-testid='ModeEditOutlineOutlinedIcon']")
    EDIT_SHIPPING_NOTES_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/p")
    SHIPPING_NOTES_CANCEL_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../div[3]/button[1]")
    SHIPPING_NOTES_UPDATE_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../div[3]/button[2]")
    SHIPPING_NOTES_ClOSE_ICON_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    EDIT_SHIPPING_NOTES_TEXT_AREA = (
        By.XPATH, "//*[text()='Edit Shipping Notes']/parent::div/following-sibling::div/div/textarea")
    SHIPPING_NOTES_CHARACTER_COUNTER = (
        By.XPATH, "//*[text()='Edit Shipping Notes']/parent::div/following-sibling::div/div/div")
    SHIPPING_NOTES_MAXIMUM_LIMIT_MESSAGE = (By.XPATH, "//textarea/parent::div/span")
    SHIPPING_NOTES_TEXT_AREA = (By.XPATH, "//*[text()='Shipping Notes']/parent::div/parent::div/textarea")

    """Filter Icon"""

    FILTER_ICON = (By.XPATH, "//*[@data-testid='FilterListIcon']")
    FILTER_TITLE = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::button/../parent::div/div/h2")
    ORDER_ENTRY_METHOD_OPTION = (By.XPATH, "//*[@data-testid='orderEntryMethod-SearchedText']/div")
    COUNTRY_OPTION = (By.XPATH, "//*[@data-testid='country-SearchedText']/div")
    APPLY_BUTTON = (By.XPATH, "//button[text()='Apply']")
    ORDER_ENTRY_METHOD_DROPDOWN_BUTTON = (
        By.XPATH, "//*[@data-testid='orderEntryMethod-SearchedText']/span/*[@data-testid='KeyboardArrowDownIcon']")
    COUNTRY_DROPDOWN_BUTTON = (
        By.XPATH, "//*[@data-testid='country-SearchedText']/span/*[@data-testid='KeyboardArrowDownIcon']")
    ORDER_ENTRY_METHOD_OPTION_LIST = (By.XPATH, "//*[@data-testid='orderEntryMethod-accordionData']/div/label/span[2]")
    ORDER_ENTRY_METHOD_OPTION_SEE_MORE_LESS_BUTTON = (By.XPATH, "//*[@data-testid='orderEntryMethod-SeeMoreLess']")
    COUNTRY_OPTION_SEE_MORE_LESS_BUTTON = (By.XPATH, "//*[@data-testid='country-SeeMoreLess']")
    COUNTRY_OPTION_LIST = (By.XPATH, "//*[@data-testid='country-accordionData']/div/label/span")
    ORDER_ENTRY_METHOD_TEXTBOX = (By.XPATH, "//*[@placeholder='Search Order entry method']")
    SELECT_FIRST_COUNTRY = (By.XPATH, "//*[@data-testid='country-0-Label']/span")
    HEADER_CLEAR_ALL_BUTTON = (
        By.XPATH, "//*[text()='Filters']/parent::div/following-sibling::div/button[text()='Clear all']")
    BITTOM_CLEAR_ALL_BUTTON = (By.XPATH, "//*[text()='Apply']/parent::div/button[text()='Clear all']")
    SELECT_FIRST_ORDER_ENTRY_METHOD = (By.XPATH, "//*[@data-testid='orderEntryMethod-0-Label']/span[2]")
    SELECT_SECOND_ORDER_ENTRY_METHOD = (By.XPATH, "//*[@data-testid='orderEntryMethod-1-Label']/span[2]")
    ORDER_ENTRY_METHOD_HEADER_SELECTED_OPTION_LIST = (By.XPATH, "//*[text()='order Entry Method']/parent::div/div/span")
    COUNTRY_HEADER_SELECTED_OPTION_LIST = (By.XPATH, "//*[text()='country']/parent::div/div/span")
    ORDER_ENTRY_METHOD_SELECTED_OPTION_LIST = (
        By.XPATH, "//*[@data-testid='CheckBoxIcon']/parent::span/following-sibling::span")
    COUNTRY_ITEM_LIST = (By.XPATH,
                         "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='country']")
    NO_FAILED_ORDER_FOUND_MESSAGE = (By.XPATH, "//*[@data-testid='required-GridLayout']/div/div[2]/div/span")
    CHANNEL_ITEM_LIST = (By.XPATH,
                         "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='channel']")
    DATA_GRID_INFO = (
        By.XPATH,
        "//*[@class='MuiDataGrid-virtualScrollerContent css-jz7yqw-MuiDataGrid-virtualScrollerContent']/div/div")
    FILTER_CLOSE_ICON = (
        By.XPATH, "//*[text()='Filters']/parent::div/following-sibling::div/button/*[@data-testid='CloseIcon']")

    """VMF Details"""

    VMF_DETAILS_EDIT_BUTTON = (
        By.XPATH, "//*[text()='VMF Details']/*[@data-testid='ModeEditOutlineOutlinedIcon']")
    EDIT_VMF_DETAILS_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/p")
    VMF_DETAILS_CANCEL_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../div[3]/button[1]")
    VMF_DETAILS_UPDATE_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../div[3]/button[2]")
    VMF_DETAILS_ClOSE_ICON_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    VMF_DETAILS_ATTRIBUTE_VALUE = (By.XPATH, "//*[text()='Attribute value']")
    VMF_DETAILS_ATTRIBUTE_NAME = (By.XPATH, "//*[text()='Attribute name']")
    SHIP_CONTACT_PHONE = (
        By.XPATH, "//*[@value='shipctacphone']/parent::div/../../following-sibling::div/div/div/input")
    SHIP_CONTACT_EMAIL = (
        By.XPATH, "//*[@value='shipctacemail']/parent::div/../../following-sibling::div/div/div/input")
    RESELLER_CONTACT_EMAIL = (
        By.XPATH, "//*[@value='resellerctacemail']/parent::div/../../following-sibling::div/div/div/input")
    VMF_SHIP_CONTACT_PHONE = (By.XPATH, "//*[text()='shipctacphone']/following-sibling::div")
    VMF_SHIP_CONTACT_EMAIL = (By.XPATH, "//*[text()='shipctacemail']/following-sibling::div")
    VMF_RESELLER_CONTACT_EMAIL = (By.XPATH, "//*[text()='resellerctacemail']/following-sibling::div")

    def go_to_error_orders(self):
        try:
            self.do_click_by_locator(self.SALES_MENU)
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
                assert self.do_check_visibility(self.DISABLED_CANCEL_BUTTON), "Cancel button is not disabled"
                self.logger.info("Successfully verified cancel button is disabled")
            else:
                assert self.do_check_visibility(self.ENABLED_CANCEL_BUTTON), "Cancel button is not enabled"
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
            assert cancel_order in self.get_element_text(self.CANCEL_ORDER_TITLE), "Cancel Order Title not present"
            assert cancel_no_button in self.get_element_text(self.CANCEL_NO_BUTTON), "Cancel No button is not present"
            assert cancel_yes_button in self.get_element_text(
                self.CANCEL_YES_BUTTON), "Cancel Yes button is not present"
            assert cancel_order_msg in address, "Cancel Order message not present"

            self.logger.info(
                "Successfully verified cancel order title, No button ,Yes button and message in popup menu")
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
            assert 'Error orders' in self.get_element_text(self.ERROR_ORDER_TEXT), "Cancel Order Title not present"
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
            assert 'Cancel order' in self.get_element_text(self.CANCEL_ORDER_TITLE), "Cancel Order Title not present"
            assert 'CANCEL ORDER' in self.get_element_text(
                self.CANCEL_ORDER_BUTTON), "Cancel order button is not present"
            assert 'BACK' in self.get_element_text(self.BACK_BUTTON), "Back button is not present"
            assert 'Reason for cancelling *' in self.get_element_text(
                self.REASON_MSG), "Reason for cancelling message is not present"
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
            assert cancel_order_message in self.get_element_text(self.CANCEL_ORDER_MESSAGE), "Cancel note not present"
            self.logger.info("Successfully verified cancel message")
            self.do_click_by_locator(self.BACK_BUTTON)
            self.logger.info("Clicked on BACK button")
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
            assert cancel_order_message in self.get_element_text(
                self.CANCEL_ORDER_SUCCESS_MESSAGE), "successfull Cancel Order message not present"
            self.logger.info("order cancelled successfully")

        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order success message ' + str(e))
            raise e

    def logout_x4a(self):
        try:
            self.do_click_by_locator(self.USER_DROPDOWN)
            self.do_click_by_locator(self.LOGOUT)
            self.logger.info("Logout Successfully")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Logout X4A ' + str(e))
            return False

    def do_verify_fraud_orders_tab(self):
        try:
            self.do_check_visibility(self.FRAUD_ORDERS_TAB)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order success message ' + str(e))
            return False

    def do_search_and_select_order(self, confirmation_id):
        try:
            self.do_click_by_locator(self.FRAUD_ORDERS_TAB)
            self.do_click_by_locator(self.SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.CONFRIMATION_ID_OPTION)
            self.do_send_keys(self.FRAUD_SEARCH_BOX, confirmation_id)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            time.sleep(5)
            self.do_click_by_locator(self.FRAUD_FIRST_RECORD)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Searching and Selection Order ' + str(e))
            return False

    def do_verify_reprocess_order_button(self):
        try:
            time.sleep(5)
            self.do_check_visibility(self.FRAUD_REPROCESS_ORDER_BUTTON)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Reprocess Order button ' + str(e))
            return False

    def do_click_reprocess_order_button(self):
        try:
            self.do_click_by_locator(self.FRAUD_REPROCESS_ORDER_BUTTON)
            self.logger.info("Successfully clicked on Reprocess Order button")
            return True
        except Exception as e:
            self.logger.eror('Exception occurred while clicking on Reprocess Order button ' + str(e))
            return False

    def do_verify_reprocess_order_popup(self):
        try:
            reprocess_order_title = 'Reprocess Order'
            reprocess_order_message_msg = 'It is crucial to ensure that you have thoroughly reviewed all available information and evidence before proceeding. Please exercise caution when reprocessing, as this will mark the order as "Not Fraud”.'
            reprocess_order_review_button = 'Review'
            reprocess_order_yes_button = 'Yes, Reprocess Order'
            message = self.get_element_text(self.REPROCESS_ORDER_POPUP_MSG).replace("\n", " ")

            assert reprocess_order_title in self.get_element_text(
                self.REPROCESS_ORDER_TITLE), "Reprocess Order Title not present"
            assert reprocess_order_message_msg in message, "Reprocess order popup message not present"
            assert reprocess_order_review_button in self.get_element_text(
                self.REPROCESS_ORDER_REVIEW_BUTTON), "Reprocess Order Review Button is not present"
            assert reprocess_order_yes_button in self.get_element_text(
                self.YES_REPROCESS_ORDER_BUTTON), "Reprocess order Yes button is not present"

            self.logger.info(
                "Successfully verified Reprocess Order title, No button ,Yes button and message in popup menu")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel button ' + str(e))
            return False

    def do_click_Reprocess_Order_Review_button(self):
        try:
            self.do_click_by_locator(self.REPROCESS_ORDER_REVIEW_BUTTON)
            self.logger.info("Successfully clicked on Review button")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Review button on Reprocess Order popup ' + str(e))
            return False

    def do_verify_order_details_page(self):
        try:
            assert 'Order Details' in self.get_element_text(self.ORDER_DETAILS_PAGE), "Order Details Title not present"
            self.logger.info("verified that Reprocess Order popup is closed and Order Details page is shown")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Rerocess order popup is closed and Order Details page is shown' + str(
                    e))
            return False

    def do_click_Reprocess_Order_Yes_button(self):
        try:
            self.do_click_by_locator(self.YES_REPROCESS_ORDER_BUTTON)
            self.logger.info("Successfully clicked on Yes, Reprocess Order button")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while clicking on Yes, Reprocess Order button on Reprocess Order popup ' + str(e))
            return False

    def do_reprocess_order_success_message(self):
        try:
            cancel_order_message = 'Reprocessed! Order was successfully resubmitted.'
            assert cancel_order_message in self.get_element_text(
                self.REPROCESS_ORDER_SUCCESS_MESSAGE), "Successfully submitted Reprocess Order message not present"
            self.logger.info("Order reprocessed successfully")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying reprocess order success message ' + str(e))
            return False

    def do_verify_order_in_list(self, confirmation_id):
        try:
            self.do_click_by_locator(self.ERROR_ORDER_PAGE)
            self.do_click_by_locator(self.FRAUD_ORDERS_TAB)
            self.do_click_by_locator(self.SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.CONFRIMATION_ID_OPTION)
            self.do_send_keys(self.FRAUD_SEARCH_BOX, confirmation_id)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            self.do_check_visibility(self.ORDER_NOT_FOUND)
            self.logger.info("Successfully verified that Order should not be there in list")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order should not be there in list')
            return False

    def do_verify_fraud_cancel_order_button(self):
        try:
            time.sleep(5)
            self.do_check_visibility(self.FRAUD_CANCEL_ORDER_BUTTON)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Fraud Cancel Order button ' + str(e))
            return False

    def do_click_cancel_order_button(self):
        try:
            self.do_click_by_locator(self.FRAUD_CANCEL_ORDER_BUTTON)
            self.logger.info("Successfully clicked on Cancel Order button")
            return True
        except Exception as e:
            self.logger.eror('Exception occurred while clicking on Cancel Order button ' + str(e))
            return False

    def do_verify_fraud_cancel_order_popup(self):
        try:
            cancel_order = 'Cancel order'
            cancel_order_msg = 'Are you sure you want to cancel order? Order will be cancelled permanently,' \
                               ' and you cannot undo this action.'
            cancel_no_button = 'NO, KEEP ORDER'
            cancel_yes_button = 'YES, CANCEL ORDER'
            address = self.get_element_text(self.CANCEL_ORDER_MSG).replace("\n", " ")
            assert cancel_order in self.get_element_text(self.CANCEL_ORDER_TITLE), "Cancel Order Title not present"
            assert cancel_no_button in self.get_element_text(self.CANCEL_NO_BUTTON), "Cancel No button is not present"
            assert cancel_yes_button in self.get_element_text(
                self.CANCEL_YES_BUTTON), "Cancel Yes button is not present"
            assert cancel_order_msg in address, "Cancel Order message not present"

            self.logger.info(
                "Successfully verified cancel order title, No button ,Yes button and message in popup menu")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying fraud cancel order popup ' + str(e))
            return False

    def do_click_fraud_yes_cancel_button(self):
        try:
            self.do_click_by_locator(self.FRAUD_CANCEL_ORDER_BUTTON)
            self.do_click_by_locator(self.CANCEL_YES_BUTTON)
            self.logger.info("Clicked on YES, Cancel Order button from cancel order popup")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while clicking on YES, Cancel Order button from cancel order popup ' + str(e))
            return False

    def do_search_and_select_data_error_order(self, confirmation_id):
        try:
            time.sleep(5)
            self.do_click_by_locator(self.DATA_ERROR_OPTION)
            self.do_click_by_locator(self.SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.CONFRIMATION_ID_OPTION)
            self.do_send_keys(self.DATA_ERRORS_SEARCH_BOX, confirmation_id)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            time.sleep(5)
            self.do_click_by_locator(self.FRAUD_FIRST_RECORD)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Searching and Selection Data error Order ' + str(e))
            return False

    def do_verify_data_error_resubmit_order_button(self):
        try:
            time.sleep(5)
            self.do_check_visibility(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Data Error Resubmit Order button ' + str(e))
            return False

    def update_reseller_po_data_error_order(self):
        try:
            self.do_click_by_locator(self.REFERENCE_DETAILS_EDIT_BUTTON)
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            special_symbols = ['!', '@', '$', '%', '^', '&', '*']
            for x in range(len(special_symbols)):
                symbol = str(special_symbols[x])
                if symbol in reseller_po:
                    reseller_po = reseller_po.replace(symbol, "")
            self.logger.info(reseller_po)
            self.do_send_keys(self.RESELLER_PO_VALUE, reseller_po)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while updating Reseller Po for Data Error order' + str(e))
            return False

    def update_end_customer_order_data_error_order(self):
        try:
            end_customer_order = self.do_get_attribute(self.END_CUSTOMER_ORDER_VALUE, "value")
            special_symbols = ['!', '@', '$', '%', '^', '&', '*']
            for x in range(len(special_symbols)):
                symbol = str(special_symbols[x])
                if symbol in end_customer_order:
                    end_customer_order = end_customer_order.replace(symbol, "")
            self.logger.info(end_customer_order)
            self.do_send_keys(self.END_CUSTOMER_ORDER_VALUE, end_customer_order)
            self.do_click_by_locator(self.DATA_ERROR_ORDER_UPDATE_BUTTON)
            time.sleep(3)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while updating End customer order for Data Error order' + str(e))
            return False

    def do_click_resubmit_order_button(self):
        try:
            self.do_click_by_locator(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            self.logger.info("Successfully clicked on Resubmit Order button")
            return True
        except Exception as e:
            self.logger.eror('Exception occurred while clicking on Resubmit Order button ' + str(e))
            return False

    def verify_content_of_resubmit_order_popup(self):
        try:
            resubmit_order_title = 'Resubmit Order'
            resubmit_order_message_msg = 'Are you sure you want to resubmit order? Order will be resubmitted, cannot undo this action. You may review prior to resubmitting.'
            resubmit_order_review_button = 'Review'
            resubmit_order_yes_button = 'Yes, Resubmit Order'
            message = self.get_element_text(self.RESUBMIT_ORDER_POPUP_MSG).replace("\n", " ")

            assert resubmit_order_title in self.get_element_text(
                self.RESUBMIT_ORDER_TITLE), "Resubmit Order Title not present"
            assert resubmit_order_message_msg in message, "Resubmit order popup message not present"
            assert resubmit_order_review_button in self.get_element_text(
                self.RESUBMIT_ORDER_REVIEW_BUTTON), "Resubmit Order Review Button is not present"
            assert resubmit_order_yes_button in self.get_element_text(
                self.YES_RESUBMIT_ORDER_BUTTON), "Resubmit order Yes button is not present"
            self.logger.info(
                "Successfully verified Resubmit Order title, No button ,Yes button and message in popup menu")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel button ' + str(e))
            return False

    def do_click_resubmit_order_review_button(self):
        try:
            self.do_click_by_locator(self.RESUBMIT_ORDER_REVIEW_BUTTON)
            self.logger.info("Successfully clicked on Resubmit Order Review button")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Review button on Resubmit Order popup ' + str(e))
            return False

    def do_click_resubmit_order_yes_button(self):
        try:
            self.do_click_by_locator(self.YES_RESUBMIT_ORDER_BUTTON)
            self.logger.info("Successfully clicked on Yes, Resubmit Order button")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while clicking on Yes, Resubmit Order button on Resubmit Order popup ' + str(e))
            return False

    def do_resubmitted_order_success_message(self):
        try:
            cancel_order_message = 'Order has been successfully resubmitted.'
            assert cancel_order_message in self.get_element_text(
                self.RESUBMITTED_ORDER_SUCCESS_MESSAGE), "Successfully Resubmitted Order message not present"
            time.sleep(3)
            self.do_click_by_locator(self.ERROR_ORDER_PAGE)
            self.logger.info("Order reprocessed successfully")
            time.sleep(3)
            self.do_click_by_locator(self.ERROR_ORDER_PAGE)
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Resubmitted order success message ' + str(e))
            return False

    def do_verify_data_error_order_in_list(self, confirmation_id):
        try:
            time.sleep(5)
            self.do_click_by_locator(self.DATA_ERROR_OPTION)
            self.do_click_by_locator(self.SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.CONFRIMATION_ID_OPTION)
            self.do_send_keys(self.FRAUD_SEARCH_BOX, confirmation_id)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            self.do_check_visibility(self.ORDER_NOT_FOUND)
            self.logger.info("Successfully verified that resubmitted Order should not be there in list")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying resubmitted Order should not be there in list')
            return False

    def do_verify_reference_details_edit_icon(self):
        try:
            time.sleep(5)
            self.do_check_visibility(self.REFERENCE_DETAILS_EDIT_BUTTON)
            return True
        except Exception as e:
            return False

    def verify_contents_of_edit_reference_details(self):
        try:
            self.do_click_by_locator(self.REFERENCE_DETAILS_EDIT_BUTTON)
            edit_reference_details_title = 'Edit reference numbers'
            mandatory_field_po_field = 'PO #*'
            non_mandatory_field_end_user_customer_field = 'End customer order #'
            edit_reference_details_cancel_button = 'CANCEL'
            edit_reference_details_update_button = 'UPDATE'

            mandatory_po_number_field = self.get_element_text(self.REFERENCE_DETAILS_PO_FIELD).replace("\u2009", "")

            assert edit_reference_details_title in self.get_element_text(
                self.EDIT_REFERENCE_POPUP_TITLE), "Edit Reference Numbers Title not present"

            assert mandatory_field_po_field in mandatory_po_number_field, "PO #* fields not present"

            assert non_mandatory_field_end_user_customer_field in self.get_element_text(
                self.REFERENCE_DETAILS_END_USER_CUSTOMER_FIELD), "End customer order # is not present"

            assert edit_reference_details_cancel_button in self.get_element_text(
                self.REFERENCE_DETAILS_CANCEL_BUTTON), "Reference Details CANCEL button is not present"

            assert edit_reference_details_update_button in self.get_element_text(
                self.REFERENCE_DETAILS_UPDATE_BUTTON), "Reference Details UPDATE button is not present"

            self.do_check_visibility(self.REFERENCE_DETAILS_ClOSE_ICON_BUTTON)

            self.logger.info(
                "Successfully verified Edit Reference Numbers Popup title, PO #*, End customer order #, Cancel, Update fields on popup")
            return True
        except Exception as e:
            return False

    def verify_more_than_eighteen_char_in_po_field(self):
        try:
            po_number_character_count_ratio = '18/18'
            self.do_clear_textfield(self.RESELLER_PO_VALUE)
            po_number = "Reference*&#$PoNumber"
            self.do_send_keys(self.RESELLER_PO_VALUE, po_number)
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            reseller_po_char_count = len(reseller_po)
            self.logger.info(f'Reseller Po character count: {reseller_po_char_count}')
            if reseller_po_char_count == 18:
                assert po_number_character_count_ratio in self.get_element_text(
                    self.REFERENCE_DETAILS_PO_CHAR_COUNT_RATIO_BUTTON), "Reference Details PO # number 18/18 count not present"
                self.logger.info("Verified that PO # textbox should not allow more than 18 characters ")
                return True
            else:
                return False
        except Exception as e:
            return False

    def verify_po_number_invalid_message(self):
        try:
            self.do_clear_textfield(self.RESELLER_PO_VALUE)
            po_number = "Reference^PoNumber"
            self.do_send_keys(self.RESELLER_PO_VALUE, po_number)
            po_number_invalid_message = self.get_element_text(self.REFERENCE_DETAILS_PO_CHAR_COUNT_RATIO_BUTTON)
            if "PO number is invalid" in po_number_invalid_message:
                self.logger.info("Verified that PO number is invalid once add this ^ special character")
                return True
        except Exception as e:
            return False

    def verify_more_than_eighteen_char_in_end_customer_order_field(self):
        try:
            end_customer_order_character_count_ratio = '18/18'
            self.do_clear_textfield(self.END_CUSTOMER_ORDER_VALUE)
            end_customer_order_count = "EndCustomer*&#$Order"
            self.do_send_keys(self.END_CUSTOMER_ORDER_VALUE, end_customer_order_count)
            end_customer_order_number = self.do_get_attribute(self.END_CUSTOMER_ORDER_VALUE, "value")
            end_customer_order_number_char_count = len(end_customer_order_number)
            self.logger.info(f'End Customer Order Number character count: {end_customer_order_number_char_count}')
            if end_customer_order_number_char_count == 18:
                assert end_customer_order_character_count_ratio in self.get_element_text(
                    self.END_CUSTOMER_ORDER_CHAR_COUNT_RATIO_BUTTON), "Reference Details End customer order # number 18/18 count not present"
                self.logger.info("Verified that End customer order # textbox should not allow more than 18 characters ")
                return True
            else:
                return False
        except Exception as e:
            return False

    def verify_end_customer_order_number_invalid_message(self):
        try:
            self.do_clear_textfield(self.END_CUSTOMER_ORDER_VALUE)
            end_customer_order_number = "EndCust^OrderNo"
            self.do_send_keys(self.END_CUSTOMER_ORDER_VALUE, end_customer_order_number)
            end_customer_order_invalid_message = self.get_element_text(self.END_CUSTOMER_ORDER_CHAR_COUNT_RATIO_BUTTON)
            if "End Cusomter order number is invalid" in end_customer_order_invalid_message:
                self.logger.info("Verified that End customer order number is invalid once add this ^ special character")
                return True
        except Exception as e:
            return False

    def verify_modified_data_after_click_on_x_icon(self):
        try:
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            end_customer_order_number = self.do_get_attribute(self.END_CUSTOMER_ORDER_VALUE, "value")
            self.do_click_by_locator(self.REFERENCE_DETAILS_ClOSE_ICON_BUTTON)
            reference_details_po_field_value = self.get_element_text(self.REFERENCE_DETAILS_PO_FIELD_VALUE)
            reference_details_end_customer_order_field_value = self.get_element_text(
                self.REFERENCE_DETAILS_END_CUSTOMER_ORDER_FIELD_VALUE)
            if reseller_po != reference_details_po_field_value:
                self.logger.info(
                    "Successfully verified that modified PO number data is not updated after click on X icon")
                if end_customer_order_number != reference_details_end_customer_order_field_value:
                    self.logger.info(
                        "Successfully verified that modified End Customer Order number data is not updated after click on X icon")
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False

    def verify_modified_data_after_click_on_cancel_button(self):
        try:
            self.do_click_by_locator(self.REFERENCE_DETAILS_EDIT_BUTTON)
            self.do_send_keys(self.RESELLER_PO_VALUE, "Po Number")
            self.do_send_keys(self.END_CUSTOMER_ORDER_VALUE, "End Customer No")
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            end_customer_order_number = self.do_get_attribute(self.END_CUSTOMER_ORDER_VALUE, "value")
            self.do_click_by_locator(self.REFERENCE_DETAILS_CANCEL_BUTTON)
            reference_details_po_field_value = self.get_element_text(self.REFERENCE_DETAILS_PO_FIELD_VALUE)
            reference_details_end_customer_order_field_value = self.get_element_text(
                self.REFERENCE_DETAILS_END_CUSTOMER_ORDER_FIELD_VALUE)
            if reseller_po != reference_details_po_field_value:
                self.logger.info(
                    "Successfully verified that modified PO number data is not updated after click on Cancel button")
                if end_customer_order_number != reference_details_end_customer_order_field_value:
                    self.logger.info(
                        "Successfully verified that modified End Customer Order number data is not updated after click on Cancel button")
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False

    def do_verify_updated_po_and_end_customer_order_data(self):
        try:
            self.do_click_by_locator(self.REFERENCE_DETAILS_EDIT_BUTTON)
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            special_symbols = ['!', '@', '$', '%', '^', '&', '*']
            for x in range(len(special_symbols)):
                symbol = str(special_symbols[x])
                if symbol in reseller_po:
                    reseller_po = reseller_po.replace(symbol, "")
            self.logger.info(reseller_po)
            self.do_send_keys(self.RESELLER_PO_VALUE, reseller_po)

            end_customer_order = self.do_get_attribute(self.END_CUSTOMER_ORDER_VALUE, "value")
            special_symbols = ['!', '@', '$', '%', '^', '&', '*']
            for x in range(len(special_symbols)):
                symbol = str(special_symbols[x])
                if symbol in end_customer_order:
                    end_customer_order = end_customer_order.replace(symbol, "")
            self.logger.info(end_customer_order)
            self.do_send_keys(self.END_CUSTOMER_ORDER_VALUE, end_customer_order)
            self.do_click_by_locator(self.DATA_ERROR_ORDER_UPDATE_BUTTON)

            reference_details_po_field_value = self.get_element_text(self.REFERENCE_DETAILS_PO_FIELD_VALUE)
            reference_details_end_customer_order_field_value = self.get_element_text(
                self.REFERENCE_DETAILS_END_CUSTOMER_ORDER_FIELD_VALUE)
            if reseller_po == reference_details_po_field_value:
                self.logger.info(
                    "Successfully verified that updated PO number data is updated on Order Details page")
                if end_customer_order == reference_details_end_customer_order_field_value:
                    self.logger.info(
                        "Successfully verified that updated End Customer Order number data is updated on Order Details page")
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False

    def do_verify_shipping_notes_edit_icon(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.BILLING_SHIPPING_TAB)
            time.sleep(2)
            self.do_check_visibility(self.SHIPPING_NOTES_EDIT_BUTTON)
            return True
        except Exception as e:
            return False

    def verify_contents_of_edit_shipping_notes(self):
        try:
            self.do_click_by_locator(self.SHIPPING_NOTES_EDIT_BUTTON)
            edit_shipping_notes_title = 'Edit Shipping Notes'
            edit_shipping_notes_cancel_button = 'CANCEL'
            edit_shipping_notes_update_button = 'UPDATE'

            assert edit_shipping_notes_title in self.get_element_text(
                self.EDIT_SHIPPING_NOTES_POPUP_TITLE), "Edit Reference Numbers Title not present"

            assert edit_shipping_notes_cancel_button in self.get_element_text(
                self.SHIPPING_NOTES_CANCEL_BUTTON), "Shipping Notes CANCEL button is not present"

            assert edit_shipping_notes_update_button in self.get_element_text(
                self.SHIPPING_NOTES_UPDATE_BUTTON), "Shipping Notes UPDATE button is not present"

            self.do_check_visibility(self.SHIPPING_NOTES_ClOSE_ICON_BUTTON)
            self.do_check_visibility(self.EDIT_SHIPPING_NOTES_TEXT_AREA)
            self.do_check_visibility(self.SHIPPING_NOTES_CHARACTER_COUNTER)
            self.logger.info(
                "Successfully verified Edit Shipping Notes Popup title, CANCEL, UPDATE button, X icon, Text area and character counter fields on popup")
            return True
        except Exception as e:
            return False

    def click_on_x_icon(self):
        try:
            self.do_click_by_locator(self.SHIPPING_NOTES_ClOSE_ICON_BUTTON)
            return True
        except Exception as e:
            return False

    def click_on_cancel_button(self):
        try:
            self.do_click_by_locator(self.SHIPPING_NOTES_EDIT_BUTTON)
            self.do_click_by_locator(self.SHIPPING_NOTES_CANCEL_BUTTON)
            return True
        except Exception as e:
            return False

    def do_validate_maximum_limit_message(self):
        try:
            self.do_click_by_locator(self.SHIPPING_NOTES_EDIT_BUTTON)
            maximum_limit_message = "You have exceeded the maximum number of 100 characters"
            char_count = 100
            random_str = ''.join(random.choices(string.ascii_uppercase, k=char_count))
            print("The randomly generated string is : " + str(random_str))  # print the random data
            self.do_send_keys(self.EDIT_SHIPPING_NOTES_TEXT_AREA, random_str)
            assert maximum_limit_message in self.get_element_text(
                self.SHIPPING_NOTES_MAXIMUM_LIMIT_MESSAGE), "Maximum limit message not present"
            return True
        except Exception as e:
            return False

    def do_validate_updated_shipping_notes_data(self):
        try:
            data = "Testing@#$%"
            self.do_clear_textfield(self.EDIT_SHIPPING_NOTES_TEXT_AREA)
            self.do_send_keys(self.EDIT_SHIPPING_NOTES_TEXT_AREA, data)
            self.do_click_by_locator(self.SHIPPING_NOTES_UPDATE_BUTTON)
            time.sleep(3)
            shipping_notes_data = self.get_element_text(self.SHIPPING_NOTES_TEXT_AREA)
            if data == shipping_notes_data:
                self.do_click_by_locator(self.ERROR_ORDER_PAGE)
                self.logger.info("Successfully validate the updated shipping notes on Order Details page")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_click_filter_icon(self):
        try:
            self.do_check_visibility(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_ICON)
            self.logger.info("Successfully clicked on Filter Icon")
            return True
        except Exception as e:
            return False

    def do_verify_filter_options(self):
        try:
            filter_title = 'Filters'
            order_entry_method_option = 'Order entry method'
            country_options = 'Country'
            assert filter_title in self.get_element_text(self.FILTER_TITLE), "Filter title not present"
            assert order_entry_method_option in self.get_element_text(
                self.ORDER_ENTRY_METHOD_OPTION), "Order entry method option is not present"
            assert country_options in self.get_element_text(self.COUNTRY_OPTION), "Country option is not present"
            self.do_check_visibility(self.APPLY_BUTTON)
            self.logger.info(
                "Successfully verified Filter title, Order Entry Method, Country option and Apply button in Filter icon")
            return True
        except Exception as e:
            return False

    def do_verify_order_entry_method_options_list(self):
        try:
            self.do_click_by_locator(self.ORDER_ENTRY_METHOD_DROPDOWN_BUTTON)
            self.do_check_visibility(self.ORDER_ENTRY_METHOD_TEXTBOX)
            self.do_click_by_locator(self.ORDER_ENTRY_METHOD_OPTION_SEE_MORE_LESS_BUTTON)
            order_options = ['ACTO', 'AQ2O', 'ARNW', 'AWEB', 'G360', 'TCTO', 'TPLA', 'TQ2O', 'TREG', 'TRNW', 'TWEB',
                             'XCTO', 'XPLA', 'XQ2O', 'XREG', 'XRNW', 'XWEB']
            order_option_list = self.get_all_elements(self.ORDER_ENTRY_METHOD_OPTION_LIST)
            order_option_method_list = []
            for element in order_option_list:
                self.logger.info(element.text)
                text = element.text
                order_option_method_list.append(text)
            order_option_method_list.pop(0)
            self.logger.info(order_option_method_list)
            result = all(elem in order_options for elem in order_option_method_list)
            if result:
                self.logger.info("Successfully verified Order entry method options list")
                self.do_click_by_locator(self.ORDER_ENTRY_METHOD_OPTION_SEE_MORE_LESS_BUTTON)
                return True
            else:
                self.logger.info("Failed to verify Order entry method options list")
                return False
        except Exception as e:
            return False

    def do_verify_country_options_list(self):
        try:
            self.do_click_by_locator(self.COUNTRY_DROPDOWN_BUTTON)
            self.do_click_by_locator(self.COUNTRY_OPTION_SEE_MORE_LESS_BUTTON)
            country_options = ['Canada', 'France', 'Germany', 'India', 'Italy', 'Mexico', 'Spain', 'United Kingdom',
                               'United States']
            country_list = self.get_all_elements(self.COUNTRY_OPTION_LIST)
            country_options_list = []
            for element in country_list:
                self.logger.info(element.text)
                text = element.text
                country_options_list.append(text)
            result = all(elem in country_options for elem in country_options_list)
            if result:
                self.logger.info("Successfully verified Order entry method options list")
                return True
            else:
                self.logger.info("Failed to verify Country options list")
                return False
        except Exception as e:
            return False

    def do_verify_clear_all_button(self):
        try:
            self.do_click_by_locator(self.SELECT_FIRST_COUNTRY)
            self.do_check_visibility(self.HEADER_CLEAR_ALL_BUTTON)
            self.do_check_visibility(self.BITTOM_CLEAR_ALL_BUTTON)
            self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
            return True
        except Exception as e:
            return False

    def do_verify_selected_options_ord_entry_mtd_on_header(self):
        try:
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.ORDER_ENTRY_METHOD_DROPDOWN_BUTTON)
            self.do_click_by_locator(self.SELECT_FIRST_ORDER_ENTRY_METHOD)
            self.do_click_by_locator(self.SELECT_SECOND_ORDER_ENTRY_METHOD)

            selected_option_list = self.get_all_elements(self.ORDER_ENTRY_METHOD_SELECTED_OPTION_LIST)
            list1 = []
            for element in selected_option_list:
                self.logger.info(element.text)
                text = element.text
                list1.append(text)

            order_entry_method_selected_list = self.get_all_elements(
                self.ORDER_ENTRY_METHOD_HEADER_SELECTED_OPTION_LIST)
            options_list = []
            for element in order_entry_method_selected_list:
                self.logger.info(element.text)
                text = element.text
                options_list.append(text)
            result = all(elem in list1 for elem in options_list)
            if result:
                self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_select_order_entry_method(self, order_entry_method):
        try:
            self.do_click_by_locator(self.ORDER_ENTRY_METHOD_DROPDOWN_BUTTON)
            self.do_click_by_locator(self.ORDER_ENTRY_METHOD_OPTION_SEE_MORE_LESS_BUTTON)
            element = "//span[text()='" + order_entry_method + "']"
            order_entry_method_value_element = self.driver.find_element(By.XPATH, element)
            self.do_click_by_locator(order_entry_method_value_element)
            self.do_click_by_locator(self.APPLY_BUTTON)
            return True
        except Exception as e:
            return False

    def do_verify_update_data_grid_as_per_order_entry_method_filter(self, order_entry_method):
        try:
            time.sleep(5)
            message = "No failed orders found."
            if self.do_check_visibility(self.NO_FAILED_ORDER_FOUND_MESSAGE):
                if message == (self.get_element_text(self.NO_FAILED_ORDER_FOUND_MESSAGE)):
                    self.logger.info("Successfully verify updated grid as per country")
                    return True
                else:
                    return False
            elif self.get_all_elements(self.CHANNEL_ITEM_LIST):
                channel_list = self.get_all_elements(self.CHANNEL_ITEM_LIST)
                self.logger.info("length of Country list %s" % len(channel_list))
                self.scroll()
                channel_list = self.get_all_elements(self.CHANNEL_ITEM_LIST)
                self.logger.info("length of Country list %s" % len(channel_list))
                count = 0
                for channel_item in channel_list:
                    if str(order_entry_method) in channel_item.text:
                        count = count + 1
                    else:
                        return False
                if count == len(channel_list):
                    return True
                self.logger.info(f'Total number of Channel count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate Order Entry method")
            return False

    def do_select_country(self, country):
        try:
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.HEADER_CLEAR_ALL_BUTTON)
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.COUNTRY_DROPDOWN_BUTTON)
            self.do_click_by_locator(self.COUNTRY_OPTION_SEE_MORE_LESS_BUTTON)
            element = "//span[text()='" + country + "']"
            order_value_element = self.driver.find_element(By.XPATH, element)
            self.do_click_by_locator(order_value_element)
            self.do_click_by_locator(self.APPLY_BUTTON)
            return True
        except Exception as e:
            return False

    def scroll(self):
        try:
            actions = ActionChains(self.driver)
            target = self.driver.find_element(By.XPATH,
                                              "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']")
            for s in range(2):
                actions.send_keys_to_element(target, Keys.PAGE_DOWN).perform()
            self.logger.info("Scrolled!")
        except Exception as e:
            print('error scrolling down web element', e)

    def do_verify_update_data_grid_as_per_country_filter(self, country):
        try:
            message = "No failed orders found."
            if message == (self.get_element_text(self.NO_FAILED_ORDER_FOUND_MESSAGE)):
                self.logger.info("Successfully verify updated grid as per country")
            else:
                element = "//*[text()='Line items']"
                line_items_element = self.driver.find_element(By.XPATH, element)
                self.scroll_horizontally(line_items_element)

                element = "//*[text()='Order revenue']"
                order_revenue_element = self.driver.find_element(By.XPATH, element)
                self.scroll_horizontally(order_revenue_element)

                element = "//*[text()='Last order attempt date/time']"
                last_order_attempt_date_element = self.driver.find_element(By.XPATH, element)
                self.scroll_horizontally(last_order_attempt_date_element)
                self.scroll_horizontally(last_order_attempt_date_element)

                element = "//*[text()='Days aged']"
                days_aged_element = self.driver.find_element(By.XPATH, element)
                self.scroll_horizontally(days_aged_element)

                element = "//*[text()='Retry attempt']"
                retry_element = self.driver.find_element(By.XPATH, element)
                self.scroll_horizontally(retry_element)

                element = "//*[text()='Country']"
                country_element = self.driver.find_element(By.XPATH, element)
                self.scroll_horizontally(country_element)

                country_list = self.get_all_elements(self.COUNTRY_ITEM_LIST)
                self.logger.info("length of Country list %s" % len(country_list))
                self.scroll()

                country_list = self.get_all_elements(self.COUNTRY_ITEM_LIST)
                self.logger.info("length of Country list %s" % len(country_list))
                count = 0
                for country_item in country_list:
                    if str(country) in country_item.text:
                        count = count + 1
                    else:
                        return False
                if count == len(country_list):
                    return True
                self.logger.info(f'Total number of Reseller BCN count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate reseller bcn")
            return False

    def do_click_clear_all_button(self):
        try:
            self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
            self.logger.info("Successfully clicked on Clear all button")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Clear all button ' + str(e))
            return False

    def do_select_option_from_ord_entry_method_and_country(self, order_entry_method, country):
        try:
            self.do_click_by_locator(self.ORDER_ENTRY_METHOD_DROPDOWN_BUTTON)
            self.do_click_by_locator(self.ORDER_ENTRY_METHOD_OPTION_SEE_MORE_LESS_BUTTON)
            element = "//span[text()='" + order_entry_method + "']"
            order_entry_method_value_element = self.driver.find_element(By.XPATH, element)
            self.do_click_by_locator(order_entry_method_value_element)

            self.do_click_by_locator(self.COUNTRY_DROPDOWN_BUTTON)
            self.do_click_by_locator(self.COUNTRY_OPTION_SEE_MORE_LESS_BUTTON)
            element = "//span[text()='" + country + "']"
            order_value_element = self.driver.find_element(By.XPATH, element)
            self.do_click_by_locator(order_value_element)
            return True
        except Exception as e:
            return False

    def do_verify_selected_values_cleared_from_filter_header(self):
        try:
            self.do_click_by_locator(self.FILTER_ICON)
            if not self.wait_till_element_is_not_available(self.ORDER_ENTRY_METHOD_HEADER_SELECTED_OPTION_LIST):
                if not self.wait_till_element_is_not_available(self.COUNTRY_HEADER_SELECTED_OPTION_LIST):
                    self.do_click_by_locator(self.FILTER_CLOSE_ICON)
                    self.do_check_visibility(self.DATA_GRID_INFO)
                    self.logger.info("Successfully Verified that Selected values should get cleared from filter header")
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False

    def do_verify_vmf_details_edit_icon(self):
        try:
            time.sleep(3)
            self.do_check_visibility(self.VMF_DETAILS_EDIT_BUTTON)
            return True
        except Exception as e:
            return False

    def verify_contents_of_edit_vmf_details(self):
        try:
            self.do_click_by_locator(self.VMF_DETAILS_EDIT_BUTTON)
            edit_vmf_details_title = 'Edit VMF Details'
            edit_vmf_details_cancel_button = 'CANCEL'
            edit_vmf_details_update_button = 'UPDATE'

            assert edit_vmf_details_title in self.get_element_text(
                self.EDIT_VMF_DETAILS_POPUP_TITLE), "Edit VMF Details Title not present"

            assert edit_vmf_details_cancel_button in self.get_element_text(
                self.VMF_DETAILS_CANCEL_BUTTON), "VMF Details CANCEL button is not present"

            assert edit_vmf_details_update_button in self.get_element_text(
                self.VMF_DETAILS_UPDATE_BUTTON), "VMF Details UPDATE button is not present"

            self.do_check_visibility(self.VMF_DETAILS_ClOSE_ICON_BUTTON)
            self.do_check_visibility(self.VMF_DETAILS_ATTRIBUTE_VALUE)
            self.do_check_visibility(self.VMF_DETAILS_ATTRIBUTE_NAME)

            self.logger.info(
                "Successfully verified Edit VMF Details Popup title, CANCEL, UPDATE button, X icon, Attribute Name and Attribute value fields on popup")
            return True
        except Exception as e:
            return False

    def verify_attribute_value_allow_special_characters(self):
        try:
            special_char = '#$%@^%$'
            self.do_clear_textfield(self.SHIP_CONTACT_PHONE)
            self.do_send_keys(self.SHIP_CONTACT_PHONE, special_char)
            abc = self.do_get_attribute(self.SHIP_CONTACT_PHONE, "value")
            assert special_char in self.do_get_attribute(self.SHIP_CONTACT_PHONE,
                                                         "value"), "Attribute value not allowed special Characters"

            return True
        except Exception as e:
            return False

    def do_validate_vmf_saved_data(self):
        try:
            ship_contact_phone = '77769823'
            ship_contact_email = 'TEST@GMAIL.COM'
            reseller_contact_email = 'TEST@INGRAMMICRO.COM'
            self.do_clear_textfield(self.SHIP_CONTACT_PHONE)
            self.do_send_keys(self.SHIP_CONTACT_PHONE, ship_contact_phone)
            self.do_clear_textfield(self.SHIP_CONTACT_EMAIL)
            self.do_send_keys(self.SHIP_CONTACT_EMAIL, ship_contact_email)
            self.do_clear_textfield(self.RESELLER_CONTACT_EMAIL)
            self.do_send_keys(self.RESELLER_CONTACT_EMAIL, reseller_contact_email)

            self.do_click_by_locator(self.VMF_DETAILS_UPDATE_BUTTON)

            assert ship_contact_phone in self.get_element_text(
                self.VMF_SHIP_CONTACT_PHONE), "Ship Contact Phone is not updated"

            assert ship_contact_email in self.get_element_text(
                self.VMF_SHIP_CONTACT_EMAIL), "Ship Contact Email is not updated"

            assert reseller_contact_email in self.get_element_text(
                self.VMF_RESELLER_CONTACT_EMAIL), "Reseller Contact Email is not updated"
            return True
        except Exception as e:
            return False

    def do_validate_vmf_data_not_saved(self):
        try:
            self.do_click_by_locator(self.VMF_DETAILS_EDIT_BUTTON)

            ship_contact_phone = '987654'
            ship_contact_email = 'TEST123@GMAIL.COM'
            reseller_contact_email = 'TESTING@INGRAMMICRO.COM'
            self.do_clear_textfield(self.SHIP_CONTACT_PHONE)
            self.do_send_keys(self.SHIP_CONTACT_PHONE, ship_contact_phone)
            self.do_clear_textfield(self.SHIP_CONTACT_EMAIL)
            self.do_send_keys(self.SHIP_CONTACT_EMAIL, ship_contact_email)
            self.do_clear_textfield(self.RESELLER_CONTACT_EMAIL)
            self.do_send_keys(self.RESELLER_CONTACT_EMAIL, reseller_contact_email)

            self.do_click_by_locator(self.VMF_DETAILS_ClOSE_ICON_BUTTON)

            vmf_ship_contact_phone = self.get_element_text(self.VMF_SHIP_CONTACT_PHONE)
            vmf_ship_contact_email = self.get_element_text(self.VMF_SHIP_CONTACT_EMAIL)
            vmf_reseller_contact_email = self.get_element_text(self.VMF_RESELLER_CONTACT_EMAIL)

            if (ship_contact_phone != vmf_ship_contact_phone) & (ship_contact_email != vmf_ship_contact_email) & (
                    reseller_contact_email != vmf_reseller_contact_email):
                self.logger.info(
                    "Successfully verified that modified VMF shipcontactphone, shipcontactemail and resellercontactemail data is not updated after click on X icon")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_validate_modified_vmf_data_not_updated(self):
        try:
            self.do_click_by_locator(self.VMF_DETAILS_EDIT_BUTTON)

            ship_contact_phone = '987654'
            ship_contact_email = 'TEST123@GMAIL.COM'
            reseller_contact_email = 'TESTING@INGRAMMICRO.COM'
            self.do_clear_textfield(self.SHIP_CONTACT_PHONE)
            self.do_send_keys(self.SHIP_CONTACT_PHONE, ship_contact_phone)
            self.do_clear_textfield(self.SHIP_CONTACT_EMAIL)
            self.do_send_keys(self.SHIP_CONTACT_EMAIL, ship_contact_email)
            self.do_clear_textfield(self.RESELLER_CONTACT_EMAIL)
            self.do_send_keys(self.RESELLER_CONTACT_EMAIL, reseller_contact_email)

            self.do_click_by_locator(self.VMF_DETAILS_CANCEL_BUTTON)

            vmf_ship_contact_phone = self.get_element_text(self.VMF_SHIP_CONTACT_PHONE)
            vmf_ship_contact_email = self.get_element_text(self.VMF_SHIP_CONTACT_EMAIL)
            vmf_reseller_contact_email = self.get_element_text(self.VMF_RESELLER_CONTACT_EMAIL)

            if (ship_contact_phone != vmf_ship_contact_phone) & (ship_contact_email != vmf_ship_contact_email) & (
                    reseller_contact_email != vmf_reseller_contact_email):
                self.logger.info(
                    "Successfully verified that modified VMF shipcontactphone, shipcontactemail and resellercontactemail data is not updated after click on Cancel button")
                return True
            else:
                return False
        except Exception as e:
            return False
