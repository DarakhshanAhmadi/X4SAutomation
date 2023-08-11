import glob
import os
from pathlib import Path

from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4ALogin import LoginPage
from pages.X4A.Pages.X4ABulkOrderUpload import X4ABulkOrderUploadPage


class ValidateBulkOrderUploadData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

    """constructor of the createOrder Page class"""

    def __init__(self, driver):
        self.driver = driver

    def login(self, feature_file_name, screen_shot):
        clear_browser_and_cache = BrowserSettings(self.driver)
        clear_browser_and_cache.do_clear_browser_history_and_cache()
        login = LoginPage(self.driver)

        try:
            environment = self.parse_config_json.get_data_from_config_json("environment", "environment_type",
                                                                           "config.json")
            if environment == 'Stage':
                username = self.parse_config_json.get_data_from_config_json("x4aStageCredentials", "username",
                                                                            "config.json")
                password = self.parse_config_json.get_data_from_config_json("x4aStageCredentials", "enc_password",
                                                                            "config.json")
            else:
                username = self.parse_config_json.get_data_from_config_json("x4aBetaCredentials", "username",
                                                                            "config.json")
                password = self.parse_config_json.get_data_from_config_json("x4aBetaCredentials", "enc_password",
                                                                            "config.json")
            login.do_login_to_x4a(username, password)
            self.logger.info("Successfully logged in to X4A")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_login_successful.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_login_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_login_error.png"
            self.logger.error("Login unsuccessful!!")
            self.logger.exception(e)
            raise e

    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data

    def click_on_bulk_order_upload_menu(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.go_to_bulk_order_upload()
            self.logger.info("Successfully clicked on error order")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_bulk_order_upload_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_bulk_order_upload_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_bulk_order_upload_clicking_error.png"
            self.logger.error("Error while clicking on error order")
            self.logger.exception(e)
            return False

    def verify_bulk_order_upload_page(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.verify_bulk_order_upload_page()
            self.logger.info("Successfully verified bulk order upload page")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_bulk_order_upload_clicked_verified.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_bulk_order_upload_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_bulk_order_upload_verified_error.png"
            self.logger.error("Error while verifying on bulk order upload page")
            self.logger.exception(e)
            return False

    def click_upload_file(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.click_upload_file()
            self.logger.info("Successfully clicked upload file button")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_upload_file_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_upload_file_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_upload_file_clicking_error.png"
            self.logger.error("Error while clicking upload file button")
            self.logger.exception(e)
            return False

    def verify_upload_file_popup(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.verify_upload_file_popup()
            self.logger.info("Successfully verified bulk order upload page")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_upload_file_popup_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_upload_file_popup_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_upload_file_popup_verified_error.png"
            self.logger.error("Error while verifying on bulk order upload page")


    def do_select_file(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            
            x4a_bulk_order_upload.do_select_file()
            self.logger.info("Successfully selected file")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_file_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_file_selected_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_file_selected_error.png"
            self.logger.error("Error while clicking upload file button")
            self.logger.exception(e)
            return False

    def verify_selected_file_popup(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.verify_selected_file_popup()
            self.logger.info("Successfully verified selected file")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_selected_file_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_selected_file_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_selected_file_verified_error.png"
            self.logger.error("Error while verifying selected file")

    def do_upload_error_file(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.do_upload_error_file()
            self.logger.info("Successfully selected file")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_file_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_file_selected_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_file_selected_error.png"
            self.logger.error("Error while clicking upload file button")
            self.logger.exception(e)
            return False

    def verify_error_popup(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.verify_error_popup()
            self.logger.info("Successfully verified file error")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_selected_file_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_selected_file_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_selected_file_verified_error.png"
            self.logger.error("Error while verifying selected file")


    def do_upload_template_error_file(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.do_upload_template_error_file()
            self.logger.info("Successfully uploaded different template file")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_file_selected_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_file_selected_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_file_selected_error.png"
            self.logger.error("Error while uploading different template file")
            self.logger.exception(e)
            return False

    def verify_template_error_message(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.verify_template_error_message()
            self.logger.info("Successfully verified template error")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_selected_file_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_selected_file_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_selected_file_verified_error.png"
            self.logger.error("Error while verifying selected file")

    def do_delete_file(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.do_delete_file()
            self.logger.info("Successfully deleted file")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_file_deleted_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_file_deleted_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_file_deleted_error.png"
            self.logger.error("Error while clicking delete icon")
            self.logger.exception(e)
            return False

    def do_select_review(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            
            x4a_bulk_order_upload.do_select_review()
            self.logger.info("Successfully clicked review button")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_file_reviewed_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_file_reviewing_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_file_reviewing_error.png"
            self.logger.error("Error while clicking review button")
            self.logger.exception(e)
            return False

    def verify_bulk_order_page(self, feature_file_name, screen_shot):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            x4a_bulk_order_upload.verify_bulk_order_page()
            self.logger.info("Successfully verified bulk order page")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_bulk_order_page_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_bulk_order_page_verified_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_bulk_order_page_verified_error.png"
            self.logger.error("Error while verifying bulk order page")

    def do_click_download_template(self, feature_file_name, screen_shot,no_of_click):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            
            if no_of_click == "single":
                x4a_bulk_order_upload.do_click_download_template()
            elif no_of_click == "multiple":
                x4a_bulk_order_upload.do_download_multiple_template(5)
            self.logger.info("Successfully clicked Download template button")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "_file_downloaded_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "_file_downloading_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "_file_downloading_error.png"
            self.logger.error("Error while clicking Download template button")
            self.logger.exception(e)
            return False

    def validate_file_name(self, feature_file_name, screen_shot):
        try:
            
            self.logger.info("Fetching latest downloaded file")
            download_dir = str(os.path.join(Path.home(), "Downloads"))
            self.logger.info("Download directory is " + str(download_dir))
            list_of_files = glob.glob(download_dir + '/*.xlsx')
            latest_file = max(list_of_files, key=os.path.getmtime)
            self.logger.info("Recent file in the downloads: " + str(latest_file))

            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "downloaded_file_name_verified_successfully.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_downloaded_file_name_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_downloaded_file_name_error.png"
            self.logger.error("Error while verifying the downloaded file name %s", e)
            raise e
        return latest_file

    def validate_multiple_file_name(self, feature_file_name, screen_shot):
        try:
            
            self.logger.info("Fetching latest downloaded file")
            download_dir = str(os.path.join(Path.home(), "Downloads"))
            self.logger.info("Download directory is " + str(download_dir))
            file_list = glob.glob(download_dir + '/Ingram_BulkUpload_Template*.xlsx')
            # latest_file = max(list_of_files, key=os.path.getmtime)
            for i in file_list:
                self.logger.info("Recent file in the downloads: " + str(i))

            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "downloaded_file_name_verified_successfully.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_downloaded_file_name_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_downloaded_file_name_error.png"
            self.logger.error("Error while verifying the downloaded file name %s", e)
            raise e
        return file_list


    def logout_x4a_url(self, feature_file_name):
        x4a_bulk_order_upload = X4ABulkOrderUploadPage(self.driver)
        try:
            if not x4a_bulk_order_upload.logout_x4a():
                self.logger.info("Failed to Logout X4A url")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name
                                            + "_logout_x4a_failed.png")
                return False
            else:
                self.logger.info("Successfully Logout X4A url")
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_logout_x4a_successfully.png")
                return True
        except Exception as e:
            self.logger.error("Error while Logout the X4A url")
            self.logger.exception(e)
            return False

