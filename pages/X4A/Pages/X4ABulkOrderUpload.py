import os

from selenium.webdriver.common.by import By

from CommonUtilities import readWriteTestData
from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig, parse_config_file
from pynput.keyboard import Key, Controller
# from pynput.mouse import Controller, Button
import time


class X4ABulkOrderUploadPage(BasePage):
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()
    file_path = ReadConfig.get_file_path()
    system_path = os.getcwd()

    SALES_MENU = (By.XPATH, "//*[@data-testid='sales-MenuItem']")
    BULK_ORDER_UPLOAD_OPTION = (By.XPATH, "//*[text()='Bulk order upload ']")
    BULK_ORDER_UPLOAD_TEXT = (By.XPATH, "//h3[text()='Bulk order upload']")
    UPLOAD_FILE_BUTTON = (By.XPATH, "//button[text()='Upload file']")
    UPLOAD_FILE_TITLE = (By.XPATH, "//span[text()='Upload file']")
    DOWNLOAD_TEMPLATE_BUTTON = (By.XPATH, "//button[text()='Download template']")
    DISABLED_REVIEW_BUTTON = (By.XPATH, "//button[@disabled and text() = 'Review']")
    DISABLED_PLACE_ORDER_BUTTON = (By.XPATH, "//button[@disabled and text() = 'Place orders']")
    CANCEL_BUTTON = (By.XPATH, "//button[text() = 'Cancel']")
    CLOSE_ICON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    BROWSE_BUTTON = (By.XPATH, '//p[text()="Browse"]')
    ENABLED_CANCEL_BUTTON = (By.XPATH, "//button[not(@disable) and text() = 'Cancel']")
    UPLOAD_FILE_LABEL = (By.XPATH, "//div[@class='MuiBox-root css-zdp87v']")
    CHECKBOX = (By.XPATH, "//div[@data-rowindex='2']/div[@data-field='__check__']")
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BOX_SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    FILE_NAME = (By.XPATH, "//div[@class='MuiBox-root css-1oulfbi']")
    DELETE_ICON = (By.XPATH, "//*[@data-testid='DeleteOutlineIcon']")
    REVIEW_BUTTON = (By.XPATH, "//button[text() = 'Review']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Place orders']")
    FILE_ERROR_MSG = (By.XPATH, "//div[@class='MuiAlert-message css-acap47-MuiAlert-message']")
    TEMPLATE_ERROR_MSG = (By.XPATH, "//div[@class='MuiAlert-message css-acap47-MuiAlert-message']")
    BACK_BUTTON = (By.XPATH, "//button[text() = 'Back']")
    USER_DROPDOWN = (By.XPATH, "//*[@data-testid='KeyboardArrowDownIcon']")
    LOGOUT = (By.XPATH, "//*[text()='LogOut']")

    def go_to_bulk_order_upload(self):
        try:
            self.do_click_by_locator(self.SALES_MENU)
            self.logger.info("Clicked on Order in the menu")
            self.do_double_click(self.BULK_ORDER_UPLOAD_OPTION)
            self.logger.info("Clicked on Bulk Order Upload option")

        except Exception as e:
            self.logger.error('Exception occurred while clicking on Bulk Order Upload ' + str(e))
            raise e

    def verify_bulk_order_upload_page(self):
        try:
            assert 'Bulk order upload' in self.get_element_text(self.BULK_ORDER_UPLOAD_TEXT),"Bulk Order Upload Title not present"
            assert 'Upload file' in self.get_element_text(self.UPLOAD_FILE_BUTTON),"Bulk Order Upload Title not present"
            assert 'Download template' in self.get_element_text(self.DOWNLOAD_TEMPLATE_BUTTON),"Bulk Order Upload Title not present"
            self.logger.info("verified that bulk order upload page")

        except Exception as e:
            self.logger.error('Exception occurred while verifying bulk order upload page ' + str(e))
            raise e

    def click_upload_file(self):
        try:
            self.do_click_by_locator(self.UPLOAD_FILE_BUTTON)
            self.logger.info("Clicked on upload file button")

        except Exception as e:
            self.logger.error('Exception occurred while clicking upload file button ' + str(e))
            raise e

    def verify_upload_file_popup(self):
        try:
            upload_file_label_msg = 'Drag and Drop file here or Browse files from your computer Supported file type: Excel (.xls, .xlsx)'
            address = self.get_element_text(self.UPLOAD_FILE_LABEL).replace("\n", " ")
            assert 'Review' in self.get_element_text(self.DISABLED_REVIEW_BUTTON), "Disabled Review button not present"
            assert 'Place orders' in self.get_element_text(self.DISABLED_PLACE_ORDER_BUTTON), "Disabled Place Order button not present"
            assert 'Cancel' in self.get_element_text(self.CANCEL_BUTTON), "Cancel button not present"
            assert address in upload_file_label_msg, "label message not present"
            self.logger.info("verified that upload file popup")
            time.sleep(5)
            # self.do_click_by_locator(self.CANCEL_BUTTON)

        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order popup is closed ' + str(e))
            raise e

    def do_upload_error_file(self):
        try:
            self.do_click_by_locator(self.BROWSE_BUTTON)
            time.sleep(3)
            keyboard = Controller()
            keyboard.type(self.system_path + '\\TestData\\BulkOrderErrorFile.txt')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(5)

        except Exception as e:
            self.logger.error('Exception occurred while selecting file ' + str(e))
            raise e
    def verify_error_popup(self):
        try:
            file_error_msg = 'File type not supported please try again by uploading an Excel file'
            address = self.get_element_text(self.FILE_ERROR_MSG).replace("\n", " ")

            assert file_error_msg in address,"Bulk Order Upload file error message not present"
            self.logger.info("verified that bulk order upload file error")
            time.sleep(5)

        except Exception as e:
            self.logger.error('Exception occurred while verifying bulk order upload file error ' + str(e))
            raise e

    def do_upload_template_error_file(self):
        try:
            self.do_click_by_locator(self.BROWSE_BUTTON)
            time.sleep(3)
            keyboard = Controller()
            keyboard.type(self.system_path + '\\TestData\\Input_File.xlsx')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(1)

        except Exception as e:
            self.logger.error('Exception occurred while selecting file ' + str(e))
            raise e
    def verify_template_error_message(self):
        try:
            template_error_msg = 'Template mismatch The provided file contains not supported data by the IM standard template, mandatory colums are missing.'
            address = self.get_element_text(self.TEMPLATE_ERROR_MSG).replace("\n", " ")
            assert template_error_msg in address,"Bulk Order Upload file template error message not present"
            assert self.is_present(self.DELETE_ICON), "Delete Icon not found"
            self.logger.info("verified that bulk order upload template file error")
            self.do_click_by_locator(self.DELETE_ICON)
            time.sleep(1)

        except Exception as e:
            self.logger.error('Exception occurred while verifying bulk order upload file error ' + str(e))
            raise e

    def do_select_file(self):
        try:
            bulk_order_file_name = parse_config_file.get_data_from_config_json("inputFile", "bulkOrderInputFileName")
            self.do_click_by_locator(self.BROWSE_BUTTON)
            time.sleep(3)
            keyboard = Controller()
            keyboard.type(self.system_path + bulk_order_file_name)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(1)

        except Exception as e:
            self.logger.error('Exception occurred while selecting file ' + str(e))
            raise e

    def verify_selected_file_popup(self):
        try:
            upload_file_label_msg = 'Your file is ready to be processed to place orders. Testdata_1_QA.xlsx 9.27 KB'
            address = self.get_element_text(self.UPLOAD_FILE_LABEL).replace("\n", " ")
            assert 'Review' in self.get_element_text(self.REVIEW_BUTTON), "Disabled Review button not present"
            assert 'Place orders' in self.get_element_text(self.PLACE_ORDER_BUTTON), "Disabled Place Order button not present"
            assert 'Cancel' in self.get_element_text(self.CANCEL_BUTTON), "Cancel button not present"
            assert self.is_present(self.DELETE_ICON), "Delete Icon not found"
            assert address in upload_file_label_msg, "label message not present"
            self.logger.info("verified that upload file popup")
            time.sleep(1)

        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order popup is closed ' + str(e))
            raise e

    def do_delete_file(self):
        try:
            self.do_click_by_locator(self.DELETE_ICON)
            time.sleep(1)

        except Exception as e:
            self.logger.error('Exception occurred while selecting file ' + str(e))
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