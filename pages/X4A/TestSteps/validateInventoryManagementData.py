import time

from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4AInventoryManagement import X4AInventoryManagementPage
from pages.X4A.Pages.X4ALogin import LoginPage


class ValidateInventoryManagementData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()
    top_100_under_performing_sku_table_headers = ['SKU', 'Actions', 'Vendor business manager', 'Vendor name', 'Vendor number', 'MFR Part number', 'Product description', 'Inventory value', 'Improvement opportunity', 'Value on order', 'Actual 121', 'Actual 151', 'Actual 181', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
    country_list = ['AU', 'FR', 'BR', 'MD', 'MX']
    top_100_sku_filter_options = ['SKU', 'MFN Part number', 'Vendor business manager', 'Vendor name']
    action_dropdown_options = ['CM - Pricing', 'CM - Cost Structure', 'DIO - RMA', 'DIO - Sell through', 'DIO - Customer forecast', 'DIO - Customer commitment (non-cancellable)', 'DIO - Customer commitment (cancellable)', 'DIO - Liquidate', 'DIO - Terminate', 'VM - Terminated - RMA', 'DF - Defective', 'Completed']
    top_100_aging_sku_table_headers = ['SKU', 'Actions', 'Vendor business manager', 'Vendor name', 'Vendor number', 'MFR Part number', 'Product description', 'Inventory value',  'Value on order', 'Actual 121', 'Actual 151', 'Actual 181', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']

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
                                        + "login_successful.png")
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "login_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "login_error.png"
            self.logger.error("Login unsuccessful!!")
            self.logger.exception(e)
            raise e

    def click_on_inventory_management_action_planning(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.go_to_inventory_management_action_planning()
            self.logger.info("Successfully clicked on Action planning under Inventory Management")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_management_action_planning_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_management_action_planning_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "inventory_management_action_planning_clicking_error.png"
            self.logger.error("Error while clicking on Action planning under Inventory Management")
            self.logger.exception(e)
            return False

    def click_on_top_100_under_performing_sku(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.click_on_top_100_underperforming_sku()
            self.logger.info("Successfully clicked on Top 100 under performing sku tab")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "top_100_underperforming_tab_clicked_successfully.png")
            return True

        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "top_100_underperforming_tab_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "top_100_underperforming_tab_clicking_error.png"
            self.logger.error("Error while clicking on Top 100 under performing sku tab")
            self.logger.exception(e)
            return False

    def validate_top_100_underperforming_sku_table_headers(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            for country in self.country_list:
                self.logger.info(f'validating table headers for {country}')
                table_headers_list = x4a_inventory_management.get_table_headers(country)
                assert len(self.top_100_under_performing_sku_table_headers) == len(
                    table_headers_list), "Number of columns mismatched"
                for column in self.top_100_under_performing_sku_table_headers:
                    if column not in table_headers_list:
                        self.logger.error(f'column {column} is missing')
                        return False
                self.logger.info(f'successfully validated table headers for {country}')
            time.sleep(2)
            self.logger.info("Successfully validated Top 100 underperforming sku table headers")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "top_100_underperforming_table_headers_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "top_100_underperforming_table_header_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "top_100_underperforming_table_header_validation_error.png"
            self.logger.error("Error while validating Top 100 underperforming sku table headers")
            self.logger.exception(e)
            return False

    def validate_filter_options(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            filter_options = x4a_inventory_management.get_filters_list()
            for option in self.top_100_sku_filter_options:
                if option not in filter_options:
                    self.logger.error(f'filter option {option} is missing')
                    return False
            self.logger.info("Successfully validated Top 100 sku filter options")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "top_100_sku_filters_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "top_100_sku_filters_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "top_100_sku_filters_validation_error.png"
            self.logger.error("Error while validating Top 100 sku filter options")
            self.logger.exception(e)
            return False

    def filter_by_country(self, country, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.filter_by_country(country)
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "filtered_by_country_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filtered_by_country_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filtered_by_country_error.png"
            self.logger.error("Error while validating Filter the country")
            self.logger.exception(e)
            return False

    def validate_filter_by_sku(self, sku, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.filter_by_sku(sku)
            if not x4a_inventory_management.verify_filter_by_sku_results(sku):
                return False
            self.logger.info(f'Successfully validated filter by SKU:{sku}')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "filter_by_sku_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_by_sku_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                              ".png"
            self.logger.error("Error while validating Filter by SKU")
            self.logger.exception(e)
            return False

    def validate_filter_by_mfn_part_number(self, mfn_part_number, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.filter_by_mfn_part_number(mfn_part_number)
            if not x4a_inventory_management.verify_filter_by_mfn_part_number_in_pages(mfn_part_number):
                return False
            self.logger.info(f'Successfully validated filter by MFN part number:{mfn_part_number}')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "filter_by_mfn_part_number_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_by_mfn_part_number_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                              "filter_by_mfn_part_number_validation_error.png"
            self.logger.error("Error while validating Filter by MFN Part number")
            self.logger.exception(e)
            return False

    def validate_filter_by_vendor_business_manager(self, vendor_business_manager, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.filter_by_vendor_business_manager(vendor_business_manager)
            if not x4a_inventory_management.verify_filter_by_vendor_business_manager_in_pages(vendor_business_manager):
                return False
            self.logger.info(f'Successfully validated filter by Vendor business manager:{vendor_business_manager}')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "filter_by_vendor_business_manager_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_by_vendor_business_manager_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_by_vendor_business_manager_validation_error.png"
            self.logger.error("Error while validating Filter by Vendor business manager")
            self.logger.exception(e)
            return False

    def validate_filter_by_vendor_name(self, vendor_name, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.filter_by_vendor_name(vendor_name)
            if not x4a_inventory_management.verify_filter_by_vendor_name_in_pages(vendor_name):
                return False
            self.logger.info(f'Successfully validated filter by Vendor name:{vendor_name}')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "filter_by_vendor_name_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_by_vendor_name_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "filter_by_vendor_name_validation_error.png"
            self.logger.error("Error while validating Filter by Vendor name")
            self.logger.exception(e)
            return False

    def check_is_improvement_opportunity_is_descending_by_default(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_improvement_opportunity_in_pages():
                return False
            self.logger.info(f'Successfully validated Improvement opportunity is descending by default')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "improvement_opportunity_descending_by_default_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "improvement_opportunity_descending_by_default_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "improvement_opportunity_descending_by_default_validation_error.png"
            self.logger.error("Error while validating Improvement opportunity is descending by default")
            self.logger.exception(e)
            return False

    def validate_sort_for_inventory_value(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_inventory_value_ascending_in_pages():
                return False
            if not x4a_inventory_management.validate_inventory_value_descending_in_pages():
                return False
            self.logger.info(f'Successfully validated sort for Inventory value')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_value_sort_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_value_sort_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "inventory_value_sort_validation_error.png"
            self.logger.error("Error while validating sort for Inventory value")
            self.logger.exception(e)
            return False

    def validate_sort_for_value_on_order(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_value_on_order_ascending_in_pages():
                return False
            if not x4a_inventory_management.validate_value_on_order_descending_in_pages():
                return False
            self.logger.info(f'Successfully validated sort for Value on order')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "value_on_order_sort_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "value_on_order_sort_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "value_on_order_sort_validation_error.png"
            self.logger.error("Error while validating sort for Value on order")
            self.logger.exception(e)
            return False

    def validate_sort_for_actual_121(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_actual_121_ascending_in_pages():
                return False
            if not x4a_inventory_management.validate_actual_121_descending_in_pages():
                return False
            self.logger.info(f'Successfully validated sort for Actual 121')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "actual_121_sort_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "actual_121_sort_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "actual_121_sort_validation_error.png"
            self.logger.error("Error while validating sort for Actual 121")
            self.logger.exception(e)
            return False

    def validate_sort_for_actual_151(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_actual_151_ascending_in_pages():
                return False
            if not x4a_inventory_management.validate_actual_151_descending_in_pages():
                return False
            self.logger.info(f'Successfully validated sort for Actual 151')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "actual_151_sort_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "actual_151_sort_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "actual_151_sort_validation_error.png"
            self.logger.error("Error while validating sort for Actual 151")
            self.logger.exception(e)
            return False

    def validate_sort_for_improvement_opportunity(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_improvement_opportunity_ascending_in_pages():
                return False
            self.logger.info(f'Successfully validated sort for Improvement opportunity')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "improvement_opportunity_sort_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "improvement_pooprtunity_sort_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "improvement_opportunity_sort_validation_error.png"
            self.logger.error("Error while validating sort for Improvement opportunity")
            self.logger.exception(e)
            return False

    def filter_by_sku(self, sku, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.filter_by_sku(sku)
            self.logger.info(f'Successfully filtered by sku')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "filtered_sku_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "filter_by_sku_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                              "filter_by_sku_error.png"
            self.logger.error("Error while Filtering by SKU")
            self.logger.exception(e)
            return False

    def validate_action_popup_contents(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            action_options = x4a_inventory_management.validate_action_popup_contents()
            for action in self.action_dropdown_options:
                if action not in action_options:
                    self.logger.error(f'{action} not present in dropdown')
                    return False
            self.logger.info(f'Successfully validated Action popup contents')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "action_popup_contents_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "action_popup_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                              "action_popup_validation_error.png"
            self.logger.error("Error while validating action popup content")
            self.logger.exception(e)
            return False

    def update_action_and_comment(self, action, comment, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.update_action_and_comment(action, comment)
            self.logger.info(f'Successfully updated action and comments')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "action_and_comments_updated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "update_action_and_comment_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                              "update_action_and_comment_error.png"
            self.logger.error("Error while updating Action and comment")
            self.logger.exception(e)
            return False

    def validate_action_and_comment(self, action, comment, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            ui_action, ui_comment = x4a_inventory_management.get_action_and_comment()
            assert action == ui_action, 'Action mismatched'
            assert comment == ui_comment, 'Comment mismatched'
            self.logger.info(f'Successfully validated action and comments')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "action_and_comments_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "validate_action_and_comment_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                              "validate_action_and_comment_error.png"
            self.logger.error("Error while validating Action and comment")
            self.logger.exception(e)
            return False

    def click_on_top_100_aging_sku_tab(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            x4a_inventory_management.click_on_top_100_aging_sku()
            self.logger.info("Successfully clicked on Top 100 aging sku tab")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "top_100_aging_tab_clicked_successfully.png")
            return True

        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "top_100_aging_tab_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "top_100_aging_tab_clicking_error.png"
            self.logger.error("Error while clicking on Top 100 aging sku tab")
            self.logger.exception(e)
            return False

    def validate_top_100_aging_sku_table_headers(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            for country in self.country_list:
                self.logger.info(f'validating table headers for {country}')
                table_headers_list = x4a_inventory_management.get_table_headers_for_top_100_aging_table(country)
                assert len(self.top_100_aging_sku_table_headers) == len(
                    table_headers_list), "Number of columns mismatched"
                for column in self.top_100_aging_sku_table_headers:
                    if column not in table_headers_list:
                        self.logger.error(f'column {column} is missing')
                        return False
                self.logger.info(f'successfully validated table headers for {country}')
            time.sleep(2)
            self.logger.info("Successfully validated Top 100 aging sku table headers")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "top_100_aging_table_headers_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "top_100_aging_table_header_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "top_100_aging_table_header_validation_error.png"
            self.logger.error("Error while validating Top 100 aging sku table headers")
            self.logger.exception(e)
            return False

    def validate_actual_151_is_descending_by_default(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_actual_151_in_pages():
                return False
            self.logger.info("Successfully validated Actual 151 is descending by default in top 100 aging sku table")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "actual_151_descending_by_default_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "actual_151_descending_by_default_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "actual_151_descending_by_default_validation_error.png"
            self.logger.error("Error while validating Actual 151 is descending by default in top 100 aging sku table")
            self.logger.exception(e)
            return False

    def validate_sort_for_actual_181(self, feature_file_name, screen_shot):
        x4a_inventory_management = X4AInventoryManagementPage(self.driver)
        try:
            if not x4a_inventory_management.validate_actual_181_ascending_in_pages():
                return False
            if not x4a_inventory_management.validate_actual_181_descending_in_pages():
                return False
            self.logger.info(f'Successfully validated sort for Actual 181')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "actual_181_sort_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "actual_181_sort_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "actual_181_sort_validation_error.png"
            self.logger.error("Error while validating sort for Actual 181")
            self.logger.exception(e)
            return False

