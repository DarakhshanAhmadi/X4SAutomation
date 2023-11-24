from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from pages.X4A.Facade.BrowserSet import BrowserSettings
from pages.X4A.Pages.X4AInventoryInquiry import X4AInventoryInquiryPage
from pages.X4A.Pages.X4ALogin import LoginPage


class ValidateInventoryInquiryData:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()
    inventory_inquiry_table_headers = ['SKU#', 'Description', 'VPN#', 'UPC', 'Vendor', 'Status', 'Language', 'Class', 'Restricted code', 'Available Qty', 'MSRP', 'ACOP', 'Reseller price', 'Vendor message', 'Vendor code']
    inventory_details_page_headers = ['Country', 'Currency', 'Vendor code', 'Vendor part', 'Restricted', 'Substitute SKU']
    product_details_sections = ['Description', 'Vendor details', 'Codes', 'Product costs']
    additional_inventory_details_sections = ['Categories', 'Genral information']
    inventory_visibility_table_headers = ['Branch', 'Available', 'Commited', 'Future', 'On Order', 'In transit', 'On hold', 'On hand', 'Average cost', 'ETA', 'Warehouse location']

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

    def click_on_inventory_inquiry(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.go_to_inventory_inquiry()
            self.logger.info("Successfully clicked on Inventory Inquiry")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_inquiry_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_inquiry_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "inventory_inquiry_clicking_error.png"
            self.logger.error("Error while clicking on inventory inquiry")
            self.logger.exception(e)
            return False

    def verify_inventory_inquiry_table_columns(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            self.logger.info("Verifying the Inventory Inquiry table headers are correct")
            inventory_inquiry_columns = x4a_inventory_inquiry.get_table_column_header()
            for column in self.inventory_inquiry_table_headers:
                if column not in inventory_inquiry_columns:
                    raise Exception("Column %s missing in Inventory Inquiry table", column)
            self.logger.info("Successfully verified columns in Inventory Inquiry table")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_inquiry_columns_verified_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_inquiry_columns_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "inventory_inquiry_columns_error.png"
            self.logger.error("Error while verifying columns in Inventory Inquiry table")
            self.logger.exception(e)
            return False

    def search(self, search_item, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.search(search_item)
            self.logger.info(f'Successfully searched {search_item}')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "search_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "search_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "search_error.png"
            self.logger.error("Error while searching in inventory inquiry")
            self.logger.exception(e)
            return False

    def verify_sku_search_result(self, sku, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.verify_sku_search_result(sku)
            self.logger.info(f'Successfully verified search result')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "search_result_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_search_result_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "verify_search_result_error.png"
            self.logger.error("Error while verifying search result")
            self.logger.exception(e)
            return False

    def validate_reseller_price_is_empty_and_no_customer_by_default(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.no_customer_by_default()
            x4a_inventory_inquiry.verify_reseller_price_is_empty_in_pages()
            self.logger.info(f'Successfully verified reseller price is empty and no customer present by default')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "reseller_price_empty_and_no_customer_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_reseller_price_empty_and_no_customer_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_reseller_price_empty_and_no_customer_error.png"
            self.logger.error("Error while verifying  reseller price is empty and  no customer present by default")
            self.logger.exception(e)
            return False


    def validate_reseller_price_is_not_empty(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.verify_reseller_price_is_not_empty_in_pages()
            self.logger.info(f'Successfully verified reseller price is not empty')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "reseller_price_not_empty_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_reseller_price_not_empty_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_reseller_price_not_empty_error.png"
            self.logger.error("Error while verifying  reseller price is not empty")
            self.logger.exception(e)
            return False

    def verify_customer_selection_popup_contents(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.verify_customer_selection_popup_contents()
            self.logger.info(f'Successfully verified customer selection popup contents')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "customer_popup_contents_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_customer_popup_contents_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_customer_popup_contents_error.png"
            self.logger.error("Error while verifying customer selection popup contents")
            self.logger.exception(e)
            return False

    def validate_customer_select_skip_functionality(self, customer, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.verify_customer_selection_skip(customer)
            self.logger.info(f'Successfully verified customer selection popup skip functionality')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "customer_popup_skip_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_customer_popup_skip_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_customer_popup_skip_error.png"
            self.logger.error("Error while verifying customer selection popup skip functionality")
            self.logger.exception(e)
            return False

    def validate_customer_selection(self, customer, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.select_customer(customer)
            self.logger.info(f'Successfully verified customer selection')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "customer_selection_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "verify_customer_selection_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "verify_customer_selection_error.png"
            self.logger.error("Error while verifying customer selection")
            self.logger.exception(e)
            return False

    def go_to_details_page_and_validate_customer(self, sku, customer, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.search(sku)
            x4a_inventory_inquiry.click_on_sku_and_validate_customer(sku, customer)
            self.logger.info(f'Successfully searched and clicked on sku')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "click_searched_sku_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "clicking_on_searched_sku_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "clicking_on_searched_sku_error.png"
            self.logger.error("Error while searching and clicking on sku")
            self.logger.exception(e)
            return False

    def edit_customer_and_validate_data(self, customer, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.verify_edit_customer_selection_skip(customer)
            x4a_inventory_inquiry.verify_edit_customer_selection_save(customer)
            self.logger.info(f'Successfully verified edit customer')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "edit_customer_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "edit_customer_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "edit_customer_error.png"
            self.logger.error("Error while editing customer")
            self.logger.exception(e)
            return False

    def validate_inventory_visibility_data_present(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.verify_inventory_visibility_data_present()
            self.logger.info(f'Successfully verified inventory visibility data is present')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_visibilty_data_present_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_visibility_data_present_verification_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "inventory_visibility_data_present_verification_error.png"
            self.logger.error("Error while checking inventory visibility data present")
            self.logger.exception(e)
            return False

    def validate_inventory_visibility_data_not_present(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.verify_inventory_visibility_data_not_present()
            self.logger.info(f'Successfully verified inventory visibility data is not present')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "no_inventory_visibilty_data_present_verified_successful.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "no_inventory_visibility_data_present_verification_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "no_inventory_visibility_data_present_verification_error.png"
            self.logger.error("Error while checking no inventory visibility data present")
            self.logger.exception(e)
            return False

    def search_and_go_to_sku_details(self, sku, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.search(sku)
            sku_data = x4a_inventory_inquiry.collect_sku_data()
            x4a_inventory_inquiry.click_on_sku(sku)
            self.logger.info(f'Successfully searched and clicked on sku')
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "click_searched_sku_successful.png")
            return True, sku_data
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "clicking_on_searched_sku_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                  "clicking_on_searched_sku_error.png"
            self.logger.error("Error while searching and clicking on sku")
            self.logger.exception(e)
            return False, ''

    def go_to_list_page_from_details_page(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            x4a_inventory_inquiry.go_back_to_listing_page_from_details()
            self.logger.info("Successfully clicked on Inventory Inquiry")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_inquiry_clicked_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_inquiry_clicking_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "inventory_inquiry_clicking_error.png"
            self.logger.error("Error while clicking on inventory inquiry")
            self.logger.exception(e)
            return False

    def validate_inventory_details_headers(self, sku_data, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        ui_details_headers = []
        try:
            details_headers = x4a_inventory_inquiry.get_details_page_headers()
            for ui_header in details_headers:
                ui_details_headers.append(ui_header)
            assert len(self.inventory_details_page_headers) == len(ui_details_headers), 'Number of header fields in inventory details mismatched'
            for header in self.inventory_details_page_headers:
                if header not in ui_details_headers:
                    raise Exception(f'{header} is missing in details page headers')
            assert details_headers['Vendor code'] == sku_data['vendor code'], 'Vendor code field mismatched in details headers'
            assert details_headers['Vendor part'] == sku_data['vpn'], 'Vendor part field mismatched in details header'
            if details_headers['Country'] == '' or details_headers['Country'] == '-':
                raise Exception('Country field is empty in inventory details header')
            if details_headers['Currency'] == '' or details_headers['Currency'] == '-':
                raise Exception('Currency field is empty in inventory details header')
            self.logger.info("Successfully validated inventory details page headers")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "inventory_details_headers_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "inventory_details_headers_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "inventory_details_headers_validation_error.png"
            self.logger.error("Error while validating details page headers")
            self.logger.exception(e)
            return False

    def validate_product_details_fields(self, sku_data, feature_file_name, screen_shot, customer=None):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            product_details_sections_headers, description_section, vendor_details_section, codes_section, product_costs = x4a_inventory_inquiry.get_product_details()
            assert len(self.product_details_sections) == len(product_details_sections_headers), 'Number of section under product details mismatched'
            for section in self.product_details_sections:
                if section not in product_details_sections_headers:
                    raise Exception(f'{section} section is missing in product details tab')
            if customer:
                assert description_section["Description"] == sku_data['description'], "Product details Description mismatched"
                assert vendor_details_section["Vendor"] == sku_data["vendor"], "Product details Vendor mismatched"
                assert codes_section["Classification code"] == sku_data["class"], "Product details Classification code mismatched"
                assert codes_section["Media code"] != "-", "Product details Media code is empty"
                assert codes_section["CPU code"] != "-", "Product details CPU code is empty"
                assert product_costs["Reseller price"] != "-", "Product details Reseller price is empty"
                assert product_costs["IM cost"] != "-", "Product details IM cost is empty"
                assert product_costs["IM retail price"] != "-", "Product details IM retail price is empty"
                assert product_costs["Dealer price"] != "-", "Product details Dealer price is empty"
                assert product_costs["Replacement price"] != "-", "Product details Replacement price is empty"
            else:
                assert description_section["Description"] == sku_data[
                    'description'], "Product details Description mismatched"
                assert vendor_details_section["Vendor"] == sku_data["vendor"], "Product details Vendor mismatched"
                assert codes_section["Classification code"] == sku_data[
                    "class"], "Product details Classification code mismatched"
                assert codes_section["Media code"] != "-", "Product details Media code is empty"
                assert codes_section["CPU code"] != "-", "Product details CPU code is empty"
            self.logger.info("Successfully validated product details fields")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "product_details_fields_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "product_details_fields_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "product_details_fields_validation_error.png"
            self.logger.error("Error while validating product details fields")
            self.logger.exception(e)
            return False

    def validate_additional_inventory_details_fields(self, feature_file_name, screen_shot, customer=None):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            additional_inventory_details_sections_headers, categories_sections, general_information_sections = x4a_inventory_inquiry.get_additional_attributes_details()
            assert len(self.additional_inventory_details_sections) == len(additional_inventory_details_sections_headers), 'Number of sections under additional inventory details mismatched'
            for section in self.additional_inventory_details_sections:
                if section not in additional_inventory_details_sections_headers:
                    raise Exception(f'{section} section is missing in additional inventory details tab')
            if customer:
                assert categories_sections["CAT/SUB"] != "-", "Additional inventory details CAT/SUB is empty"
            else:
                assert categories_sections["CAT/SUB"] == "-", "Additional inventory details CAT/SUB is not empty"
            self.logger.info("Successfully validated Additional inventory details")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "additional_inventory_details_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "additional_inventory_details_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "additional_inventory_details_validation_error.png"
            self.logger.error("Error while validating Additional inventory details")
            self.logger.exception(e)
            return False

    def validate_inventory_visibility_fields(self, feature_file_name, screen_shot):
        x4a_inventory_inquiry = X4AInventoryInquiryPage(self.driver)
        try:
            inventory_visibility_columns = x4a_inventory_inquiry.validate_inventory_visibility_table()
            assert len(inventory_visibility_columns) == len(self.inventory_visibility_table_headers)
            for column in self.inventory_inquiry_table_headers:
                if column not in inventory_visibility_columns:
                    raise Exception(f'{column} column is missing in inventory visibility')
            self.logger.info("Successfully validated Inventory visibility")
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                        + "Inventory_visibility_validated_successfully.png")
            return True
        except Exception as e:
            self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\error\\" + feature_file_name +
                                        "Inventory_visibility_validation_error.png")
            screen_shot["path"] = self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + \
                                                            "Inventory_visibility_validation_error.png"
            self.logger.error("Error while validating Inventory visibility")
            self.logger.exception(e)
            return False
