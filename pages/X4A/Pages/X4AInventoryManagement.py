import time
import random

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage


class X4AInventoryManagementPage(BasePage):

    INVENTORY_MENU = (By.XPATH, "//div[@data-testid='inventory-MenuItem']")
    INVENTORY_MANAGEMENT_OPTION = (By.XPATH, "//*[text()='Inventory management']")
    ACTION_PLANNING = (By.XPATH, "//*[text()='Action planning']")

    """Top 100 Underperforming sku"""
    TOP_100_UNDERPERFORMING_SKU_TAB = (By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 css-zac9d4-MuiTypography-root'][text()='Top 100 Underperforming (UP) SKU']")
    FIRST_COLUMN = (By.XPATH, "//div[text()='SKU'][@class='MuiDataGrid-columnHeaderTitle css-t89xny-MuiDataGrid-columnHeaderTitle']")
    PAGINATION_TAB = (By.XPATH, "//div[@data-testid='required-showing']")
    TOP_100_UNDERPERFORMING_TABLE_HEADERS = (By.XPATH, "//div[@class='css-yrdy0g-MuiDataGrid-columnHeaderRow'][@aria-rowindex=2]/div")
    ACTION_PLANING_PAGE_ELEMENT = "//div[@data-testid='required-Content']"
    COUNTRY_DROPDOWN = (By.XPATH, "//div[@data-testid='required-SelectOption']")
    COUNTRY_DROPDOWN_OPTIONS = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-6hp17o-MuiList-root-MuiMenu-list']/li")
    FILTER_DROP_DOWN = (By.XPATH, "//div[@class='MuiBox-root css-puyl27']")
    FILTER_DROPDOWN_OPTIONS = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-6hp17o-MuiList-root-MuiMenu-list']/li")
    FILTER_SEARCH_TEXTBOX = (By.ID, "mui-1")
    FILTER_SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Common.Search']")
    FILTER_BY_SKU_OPTION = (By.XPATH, "//li[text()='SKU']")
    FILTER_BY_MFN_PART_NUMBER_OPTION = (By.XPATH, "//li[text()='MFN Part number']")
    FILTER_BY_VENDOR_BUSINESS_MANAGER_OPTION = (By.XPATH, "//li[text()='Vendor business manager']")
    FILTER_BY_VENDOR_NAME = (By.XPATH, "//li[text()='Vendor name']")
    TABLE_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div")
    NO_RESULT_TEXT = (By.XPATH, "//span[text()='No SKUs found.']")
    FIRST_ROW_SKU_DATA = (By.XPATH, "//div[@data-id=0]/div[@data-field='sku']")
    ITEMS_PER_PAGE = (By.XPATH,
                      "//div[@class='MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-d2iqo8-MuiSelect-select-MuiInputBase-input']")
    TOP_100_SKUS_TABLE = "//div[@class='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']"
    IMPROVEMENT_OPPORTUNITY = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='skuimprovement']")
    INVENTORY_VALUE = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='currentinvrepcost']")
    VALUE_ON_ORDER = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='valueorder']")
    ACTUAL_121 = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='agingvalue_over120']")
    ACTUAL_151 = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='agingvalue_over150']")
    ACTUAL_181 = (By.XPATH,"//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='agingvalue_over180']")
    INVENTORY_VALUE_SORT = (By.XPATH, "(//div[text()='Inventory value'])[2]")
    IMPROVEMENT_OPPORTUNITY_SORT = (By.XPATH, "//div[text()='Improvement opportunity']")
    VALUE_ON_ORDER_SORT = (By.XPATH, "//div[text()='Value on order']")
    ACTUAL_121_SORT = (By.XPATH, "//div[text()='Actual 121']")
    ACTUAL_151_SORT = (By.XPATH, "//div[text()='Actual 151']")
    ACTUAL_181_SORT = (By.XPATH, "//div[text()='Actual 181']")
    CANCEL_SEARCH_ICON = (By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hg1enx-MuiButtonBase-root-MuiIconButton-root']")
    MFN_PART_NUMBER_VALUES_IN_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='mfrpartnbr']")
    VENDOR_BUSINESS_MANAGER_VALUES_IN_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='vendorbusinessmanager']")
    VENDOR_NAME_VALUES_IN_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-s1v7zr-MuiDataGrid-virtualScrollerRenderZone']/div/div[@data-field='vendorname']")
    FIRST_ROW_THREE_DOTS = (By.XPATH, "//div[@data-id=0]/div[@data-field='action']/div/div/div/button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hp16lx-MuiButtonBase-root-MuiIconButton-root']")
    ADD_OR_EDIT_OPTION = (By.XPATH, "//li[text()='Add / Edit action']")
    ACTION_POPUP_DROPDOWN_SECTION_LABEL = (By.XPATH, "(//p[@id='alert-dialog-description'])[1]")
    ACTION_POPUP_COMMENT_SECTION_LABEL = (By.XPATH, "(//p[@id='alert-dialog-description'])[2]")
    ACTION_POPUP_CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    ACTION_POPUP_SAVE_BUTTON = (By.XPATH, "//button[text()='Save']")
    ACTION_POPUP_DOWNDOWN = (By.XPATH, "//div[@class='MuiOutlinedInput-root MuiInputBase-root MuiInputBase-colorPrimary css-pejs30-MuiInputBase-root-MuiOutlinedInput-root']")
    ACTION_DROPDOWN_OPTIONS = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-6hp17o-MuiList-root-MuiMenu-list']/li")
    ACTION_POPUP_COMMENT_TEXT_AREA = (By.XPATH, "//textarea[@id='textarea']")
    ACTION_POPUP_CLOSE_BUTTON = (By.XPATH, "//button[@aria-label='close']")
    ACTION_FOR_SKU = (By.XPATH, "//div[@data-id=0]/div[@data-field='action']/div/div/div/div/span/div/div")
    COMMENT_FOR_SKU = (By.XPATH, "//div[@data-id=0]/div[@data-field='action']/div/div/div[2]/button")
    BLUE_DOT_FOR_COMMENT_FOR_FIRST_ROW = (By.XPATH, "//div[@data-rowindex=0]/div[@data-field='action']/div/div/div[2]/button/span/span")
    ACTION_SAVE_STATUS_POPUP = (By.XPATH, "//div[@class='MuiAlert-message css-acap47-MuiAlert-message']")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//button[@aria-label='close']")
    COMMENT_TEXT = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1c49e4q-MuiTypography-root']")

    """ Top 100 Aging sku tab """
    TOP_100_AGING_SKU_TAB = (By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 css-zac9d4-MuiTypography-root'][text()='Top 100 Aging SKU']")

    def go_to_inventory_management_action_planning(self):
        try:
            self.do_click_by_locator(self.INVENTORY_MENU)
            self.do_double_click(self.INVENTORY_MANAGEMENT_OPTION)
            self.do_double_click(self.ACTION_PLANNING)
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Inventory Inquiry' + str(e))
            raise e

    def click_on_top_100_underperforming_sku(self):
        try:
            self.do_check_availability(self.TOP_100_UNDERPERFORMING_SKU_TAB)
            self.do_click_by_locator(self.TOP_100_UNDERPERFORMING_SKU_TAB)
            page_element = self.driver.find_element(By.XPATH, self.ACTION_PLANING_PAGE_ELEMENT)
            self.scroll_down(page_element)
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Top 100 underperforming sku tab' + str(e))
            raise e

    def get_table_headers(self, selected_country):
        table_headers = []
        try:
            self.filter_by_country(selected_country)
            for i in range(1, 24):
                xpath = (By.XPATH, "//div[@class='css-yrdy0g-MuiDataGrid-columnHeaderRow'][@aria-rowindex=2]/div[@aria-colindex=" + str(i) + "]")
                if i == 7:
                    self.driver.execute_script(
                        "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
                    time.sleep(2)
                elif i == 15:
                    self.driver.execute_script(
                        "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 3000")
                    time.sleep(2)
                header = self.get_element_text(xpath)
                table_headers.append(header)
            self.logger.info(table_headers)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return table_headers
        except Exception as e:
            self.logger.error('Exception occurred while getting Top 100 sku table headers' + str(e))
            raise e

    def get_filters_list(self):
        filter_options = []
        try:
            self.do_click_by_locator(self.FILTER_DROP_DOWN)
            dropdown_options = self.get_all_elements(self.FILTER_DROPDOWN_OPTIONS)
            for option in dropdown_options:
                filter_options.append(option.text)
            self.do_click_by_locator(dropdown_options[0])
            self.logger.info(filter_options)
            return filter_options
        except Exception as e:
            self.logger.error('Exception occurred while getting Filter dropdown options' + str(e))
            raise e

    def filter_by_sku(self, sku):
        try:
            self.do_click_by_locator(self.FILTER_DROP_DOWN)
            self.do_click_by_locator(self.FILTER_BY_SKU_OPTION)
            self.do_send_keys(self.FILTER_SEARCH_TEXTBOX, sku)
            self.do_click_by_locator(self.FILTER_SEARCH_BUTTON)
            time.sleep(2)
            self.logger.info(f'Successfully filtered by SKU: {sku}')
        except Exception as e:
            self.logger.error('Exception occurred while applying filtering by sku' + str(e))
            raise e

    def filter_by_mfn_part_number(self, mfn_part_number):
        try:
            self.do_click_by_locator(self.FILTER_DROP_DOWN)
            self.do_click_by_locator(self.FILTER_BY_MFN_PART_NUMBER_OPTION)
            self.do_send_keys(self.FILTER_SEARCH_TEXTBOX, mfn_part_number)
            self.do_click_by_locator(self.FILTER_SEARCH_BUTTON)
            self.logger.info(f'Successfully filtered by MFN part number: {mfn_part_number}')
        except Exception as e:
            self.logger.error('Exception occurred while applying filtering by MFN part number' + str(e))
            raise e

    def filter_by_vendor_business_manager(self, vendor_business_manager):
        try:
            self.do_click_by_locator(self.FILTER_DROP_DOWN)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_BUSINESS_MANAGER_OPTION)
            self.do_send_keys(self.FILTER_SEARCH_TEXTBOX, vendor_business_manager)
            self.do_click_by_locator(self.FILTER_SEARCH_BUTTON)
            self.logger.info(f'Successfully filtered by Vendor business manager: {vendor_business_manager}')
        except Exception as e:
            self.logger.error('Exception occurred while applying filtering by Vendor business manager' + str(e))
            raise e

    def filter_by_vendor_name(self, vendor_name):
        try:
            self.do_click_by_locator(self.FILTER_DROP_DOWN)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_NAME)
            self.do_send_keys(self.FILTER_SEARCH_TEXTBOX, vendor_name)
            self.do_click_by_locator(self.FILTER_SEARCH_BUTTON)
            self.logger.info(f'Successfully filtered by Vendor name: {vendor_name}')
        except Exception as e:
            self.logger.error('Exception occurred while applying filtering by Vendor name' + str(e))
            raise e

    def verify_filter_by_sku_results(self, sku):
        try:
            time.sleep(5)
            self.check_if_result_found()
            rows = self.get_all_elements(self.TABLE_ROWS)
            assert len(rows) == 1, 'Many search results found for searched sku'
            ui_sku = self.get_element_text(self.FIRST_ROW_SKU_DATA)
            assert str(sku) == ui_sku, 'Filtered SKU mismatched'
            self.logger.info("Successfully verified filter by SKU")
            self.do_click_by_locator(self.CANCEL_SEARCH_ICON)
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying filter by SKU" + str(e))
            return False

    def verify_filter_by_mfn_part_number_in_pages(self, mfn_part_number):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying MFN part number in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_mfn_part_number(mfn_part_number)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying MFN part number in page %s", str(random_page))
                    self.filter_by_mfn_part_number(mfn_part_number)
                    self.go_to_page(random_page)
                    self.validate_mfn_part_number(mfn_part_number)
                self.logger.info("Verifying MFN part number in page %s", str(last_page_number))
                self.filter_by_mfn_part_number(mfn_part_number)
                self.go_to_page(last_page_number)
                self.validate_mfn_part_number(mfn_part_number)
            self.do_click_by_locator(self.CANCEL_SEARCH_ICON)
            self.logger.info("Successfully verified MFN part number")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying the filter by MFN part number" + str(e))
            return False

    def validate_mfn_part_number(self, mfn_part_number):
        try:
            self.logger.info("Verifying the MFN part number in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            row_data = self.get_all_elements(self.MFN_PART_NUMBER_VALUES_IN_ROWS)
            assert len(row_data) <= int(max_rows)
            for i in range(len(row_data)):
                if row_data[i].text != mfn_part_number:
                    self.logger.error(f'Row {i+1} data mismatched for MFN part number')
                    raise Exception('Data mismatched for MFN part number')
            self.logger.info("Successfully validated data for MFN part number")
        except Exception as e:
            self.logger.error("Exception occurred verifying MFN part number" + str(e))
            raise e

    def verify_filter_by_vendor_business_manager_in_pages(self, vendor_business_manager):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Vendor business manager in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_vendor_business_manager(vendor_business_manager)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Vendor business manager in page %s", str(random_page))
                    self.go_to_page(random_page)
                    self.validate_vendor_business_manager(vendor_business_manager)
                self.logger.info("Verifying Vendor business manager  in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.validate_vendor_business_manager(vendor_business_manager)
            self.do_click_by_locator(self.CANCEL_SEARCH_ICON)
            self.logger.info("Successfully verified Vendor business manager")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying the filter by Vendor business manager" + str(e))
            return False

    def validate_vendor_business_manager(self, vendor_business_manager):
        try:
            self.logger.info("Verifying the Vendor business manager in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            row_data = self.get_all_elements(self.VENDOR_BUSINESS_MANAGER_VALUES_IN_ROWS)
            assert len(row_data) <= int(max_rows)
            for i in range(len(row_data)):
                if row_data[i].text != vendor_business_manager:
                    self.logger.error(f'Row {i + 1} data mismatched for Vendor business manager')
                    raise Exception('Data mismatched for Vendor business manager')
            self.logger.info("Successfully validated data Vendor business manager")
        except Exception as e:
            self.logger.error("Exception occurred verifying Vendor business manager" + str(e))
            raise e

    def verify_filter_by_vendor_name_in_pages(self, vendor_name):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Vendor name in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_vendor_name(vendor_name)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Vendor name in page %s", str(random_page))
                    self.go_to_page(random_page)
                    self.validate_vendor_name(vendor_name)
                self.logger.info("Verifying Vendor name in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.validate_vendor_name(vendor_name)
            self.do_click_by_locator(self.CANCEL_SEARCH_ICON)
            self.logger.info("Successfully verified Vendor name")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying the filter by Vendor name" + str(e))
            return False

    def validate_vendor_name(self, vendor_name):
        try:
            self.logger.info("Verifying the Vendor name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            row_data = self.get_all_elements(self.VENDOR_NAME_VALUES_IN_ROWS)
            assert len(row_data) <= int(max_rows)
            for i in range(len(row_data)):
                if row_data[i].text != vendor_name:
                    self.logger.error(f'Row {i + 1} data mismatched for Vendor name')
                    raise Exception('Data mismatched for Vendor name')
            self.logger.info("Successfully validated data Vendor name")
        except Exception as e:
            self.logger.error("Exception occurred verifying Vendor name" + str(e))
            raise e

    def check_if_result_found(self):
        try:
            self.logger.info("Checking if result found for Top 100 under performing sku")
            table_rows = self.get_all_elements_without_visibility(self.TABLE_ROWS)
        except Exception as e:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No result found for the search or filter")
                raise e
            else:
                self.logger.error("Exception while checking the search result for Top 100 underperforming sku")
                raise e

    def get_pagination_first_and_last_page(self):
        try:
            time.sleep(2)
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            return first_page_number, last_page_number
        except Exception as e:
            self.logger.erro("Exception while getting pagination first and last page")
            raise e

    def filter_by_country(self, selected_country):
        try:
            self.do_click_by_locator(self.COUNTRY_DROPDOWN)
            country_dropdown_options = self.get_all_elements(self.COUNTRY_DROPDOWN_OPTIONS)
            self.logger.info(f'searching for {selected_country} in dropdown')
            for country in country_dropdown_options:
                if country.text == selected_country:
                    self.logger.info(f'{selected_country} found in the dropdown')
                    country.click()
                    break
        except Exception as e:
            self.logger.error("Exception while filtering by country")
            raise e

    def get_random_page(self, first, last):
        try:
            if last > 10:
                return random.randint(2, 10)
            elif last <= 10:
                return random.randint(first + 1, last - 1)
        except Exception as e:
            self.logger.error("Exception while generating random number" + str(e))
            raise e

    def validate_improvement_opportunity_in_pages(self):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Improvement opportunity in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_improvement_opportunity_is_descending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Improvement opportunity in page %s", str(random_page))
                    self.is_improvement_opportunity_is_descending_order()
                self.logger.info("Verifying Improvement opportunity in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_improvement_opportunity_is_descending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified Improvement opportunity")
            return True
        except Exception as e:
            self.logger.error("Exception while validating improvement opportunity in pages" + str(e))
            raise e

    def is_improvement_opportunity_is_descending_order(self):
        improvement_opportunity_list = []
        try:
            elements = self.get_all_elements(self.IMPROVEMENT_OPPORTUNITY)
            for e in elements:
                improvement_opportunity_list.append(float((e.text).replace(',', '')))
            for i in range(len(improvement_opportunity_list)-1):
                if improvement_opportunity_list[i] >= improvement_opportunity_list[i+1]:
                    continue
                else:
                    self.logger.error(f'improvementing opportunity is not in descending in row {i+1}')
                    raise Exception('improvementing opportunity is not in descending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while fetching improvement opportunity" + str(e))
            raise e

    def validate_inventory_value_ascending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.INVENTORY_VALUE_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Inventory value is Ascending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_inventory_value_is_ascending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Inventory value is Ascending in page %s", str(random_page))
                    self.is_inventory_value_is_ascending_order()
                self.logger.info("Verifying Inventory value is Ascending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_inventory_value_is_ascending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified Inventory value is Ascending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Inventory value is Ascending in pages" + str(e))
            raise e

    def is_inventory_value_is_ascending_order(self):
        inventory_value_list = []
        try:
            elements = self.get_all_elements(self.INVENTORY_VALUE)
            for e in elements:
                inventory_value_list.append(float((e.text).replace(',', '')))
            for i in range(len(inventory_value_list)-1):
                if inventory_value_list[i] <= inventory_value_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Inventory value is not in ascending in row {i+1}')
                    raise Exception('Inventory value is not in ascending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Inventory value is Ascending" + str(e))
            raise e

    def validate_inventory_value_descending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.INVENTORY_VALUE_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Inventory value is Descending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_inventory_value_is_descending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Inventory value is Descending in page %s", str(random_page))
                    self.is_inventory_value_is_descending_order()
                self.logger.info("Verifying Inventory value is Descending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_inventory_value_is_descending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified Inventory value is Descending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Inventory value is Ascending in pages" + str(e))
            raise e

    def is_inventory_value_is_descending_order(self):
        inventory_value_list = []
        try:
            elements = self.get_all_elements(self.INVENTORY_VALUE)
            for e in elements:
                inventory_value_list.append(float((e.text).replace(',', '')))
            for i in range(len(inventory_value_list)-1):
                if inventory_value_list[i] >= inventory_value_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Inventory value is not in Descending in row {i+1}')
                    raise Exception('Inventory value is not in Descending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Inventory value is Descending" + str(e))
            raise e

    def validate_value_on_order_ascending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.VALUE_ON_ORDER_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Value on order is Ascending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_value_on_order_ascending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Value on order is Ascending in page %s", str(random_page))
                    self.is_value_on_order_ascending_order()
                self.logger.info("Verifying Value on order is Ascending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_value_on_order_ascending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified Value on order is Ascending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Value on order is Ascending in pages" + str(e))
            raise e

    def is_value_on_order_ascending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.VALUE_ON_ORDER)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] <= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Value on order is not in Ascending in row {i+1}')
                    raise Exception('Value on order is not in Ascending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Value on order is Ascending" + str(e))
            raise e

    def validate_value_on_order_descending_in_pages(self):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.VALUE_ON_ORDER_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Value on order is Descending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_value_on_order_descending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Value on order is Descending in page %s", str(random_page))
                    self.is_value_on_order_descending_order()
                self.logger.info("Verifying Value on order is Descending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_value_on_order_descending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified Value on order is Descending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Value on order is Descending in pages" + str(e))
            raise e

    def is_value_on_order_descending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.VALUE_ON_ORDER)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] >= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Value on order is not in Descending in row {i+1}')
                    raise Exception('Value on order is not in Descending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Value on order is Descending" + str(e))
            raise e

    def validate_actual_121_ascending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.ACTUAL_121_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Actual 121 is Ascending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_actual_121_ascending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Actual 121 is Ascending in page %s", str(random_page))
                    self.is_actual_121_ascending_order()
                self.logger.info("Verifying Actual 121 is Ascending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_actual_121_ascending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified VActual 121 is Ascending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Actual 121 is Ascending in pages" + str(e))
            raise e

    def is_actual_121_ascending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.ACTUAL_121)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] <= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Actual 121 is not in Ascending in row {i+1}')
                    raise Exception('Actual 121 is not in Ascending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Actual 121 is Ascending" + str(e))
            raise e

    def validate_actual_121_descending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.ACTUAL_121_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Actual 121 is Descending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_actual_121_descending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Actual 121 is Descending in page %s", str(random_page))
                    self.is_actual_121_descending_order()
                self.logger.info("Verifying Actual 121 is Descending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_actual_121_descending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified VActual 121 is Descending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Actual 121 is Descending in pages" + str(e))
            raise e

    def is_actual_121_descending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.ACTUAL_121)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] >= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Actual 121 is not in Descending in row {i+1}')
                    raise Exception('Actual 121 is not in Descending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Actual 121 is Descending" + str(e))
            raise e

    def validate_actual_151_ascending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.ACTUAL_151_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Actual 151 is Ascending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_actual_151_ascending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Actual 151 is Ascending in page %s", str(random_page))
                    self.is_actual_151_ascending_order()
                self.logger.info("Verifying Actual 151 is Ascending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_actual_151_ascending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified VActual 151 is Ascending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Actual 151 is Ascending in pages" + str(e))
            raise e

    def is_actual_151_ascending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.ACTUAL_151)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] <= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Actual 151 is not in Ascending for row {i+1}')
                    raise Exception('Actual 151 is not in Ascending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Actual 151 is Ascending" + str(e))
            raise e

    def validate_actual_151_descending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.ACTUAL_151_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Actual 151 is Descending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_actual_151_descending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Actual 151 is Descending in page %s", str(random_page))
                    self.is_actual_151_descending_order()
                self.logger.info("Verifying Actual 151 is Descending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_actual_151_descending_order()
            self.go_to_page(first_page_number)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified VActual 151 is Descending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Actual 151 is Descending in pages" + str(e))
            raise e

    def is_actual_151_descending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.ACTUAL_151)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] >= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Actual 151 is not in Descending in row {i+1}')
                    raise Exception('Actual 151 is not in Descending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Actual 151 is Descending" + str(e))
            raise e

    def validate_improvement_opportunity_ascending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.IMPROVEMENT_OPPORTUNITY_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Improvement opportunity in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_improvement_opportunity_is_ascending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Improvement opportunity Ascending in page %s", str(random_page))
                    self.is_improvement_opportunity_is_ascending_order()
                self.logger.info("Verifying Improvement opportunity Ascending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_improvement_opportunity_is_ascending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified Improvement opportunity Ascending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating improvement opportunity Ascending in pages" + str(e))
            raise e

    def is_improvement_opportunity_is_ascending_order(self):
        improvement_opportunity_list = []
        try:
            elements = self.get_all_elements(self.IMPROVEMENT_OPPORTUNITY)
            for e in elements:
                improvement_opportunity_list.append(float((e.text).replace(',', '')))
            for i in range(len(improvement_opportunity_list)-1):
                if improvement_opportunity_list[i] <= improvement_opportunity_list[i+1]:
                    continue
                else:
                    self.logger.error(f'improvementing opportunity is not in Ascending in row {i+1}')
                    raise Exception('improvementing opportunity is not in Ascending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while fetching improvement opportunity Ascending" + str(e))
            raise e

    def validate_action_popup_contents(self):
        action_options = []
        try:
            three_dots = self.get_all_elements(self.FIRST_ROW_THREE_DOTS)
            self.do_click_by_locator(three_dots[-1])
            self.do_click_by_locator(self.ADD_OR_EDIT_OPTION)
            action_popup_dropdown_label = self.get_element_text(self.ACTION_POPUP_DROPDOWN_SECTION_LABEL)
            action_popup_comment_label = self.get_element_text(self.ACTION_POPUP_COMMENT_SECTION_LABEL)
            comment_textbox_text = self.do_get_attribute(self.ACTION_POPUP_COMMENT_TEXT_AREA, "placeholder")
            assert action_popup_dropdown_label == 'Please, select what action will be perform *', 'Action popup dropdown label is incorrect'
            assert action_popup_comment_label == 'What is being done to eliminate underperforming SKUs?', 'Action popup comment label is incorrect'
            assert comment_textbox_text == 'Input comment (200 character limit)', 'Comment textbox placeholder is incorrect'
            self.do_check_availability(self.ACTION_POPUP_SAVE_BUTTON)
            self.do_check_availability(self.ACTION_POPUP_CANCEL_BUTTON)
            self.do_click_by_locator(self.ACTION_POPUP_DOWNDOWN)
            action_dropdown_options = self.get_all_elements(self.ACTION_DROPDOWN_OPTIONS)
            for action in action_dropdown_options:
                action_options.append(action.text)
            self.do_click_by_locator(action_dropdown_options[0])
            self.logger.info(action_options)
            self.do_click_by_locator(self.ACTION_POPUP_CANCEL_BUTTON)
            return action_options
        except Exception as e:
            self.logger.error("Exception while validating Action popup contents" + str(e))
            raise e

    def update_action_and_comment_and_save(self, action, comment):
        try:
            three_dots = self.get_all_elements(self.FIRST_ROW_THREE_DOTS)
            self.do_click_by_locator(three_dots[-1])
            self.do_click_by_locator(self.ADD_OR_EDIT_OPTION)
            self.do_click_by_locator(self.ACTION_POPUP_DOWNDOWN)
            action_dropdown_options = self.get_all_elements(self.ACTION_DROPDOWN_OPTIONS)
            for option in action_dropdown_options:
                if option.text == action:
                    option.click()
                    break
            self.do_click_by_locator(self.ACTION_POPUP_COMMENT_TEXT_AREA)
            self.do_send_keys(self.ACTION_POPUP_COMMENT_TEXT_AREA, comment)
            self.do_click_by_locator(self.ACTION_POPUP_SAVE_BUTTON)
            self.do_check_availability(self.ACTION_SAVE_STATUS_POPUP)
            save_status = self.get_element_text(self.ACTION_SAVE_STATUS_POPUP)
            assert save_status == 'Save Successful', 'Action save status mismatch'
            time.sleep(2)
            self.do_click_by_locator(self.POPUP_CLOSE_BUTTON)
            time.sleep(3)
        except Exception as e:
            self.logger.error("Exception while updating action and comment and save" + str(e))
            raise e

    def update_action_and_comment_and_cancel(self, action, comment):
        try:
            three_dots = self.get_all_elements(self.FIRST_ROW_THREE_DOTS)
            self.do_click_by_locator(three_dots[-1])
            self.do_click_by_locator(self.ADD_OR_EDIT_OPTION)
            self.do_click_by_locator(self.ACTION_POPUP_DOWNDOWN)
            action_dropdown_options = self.get_all_elements(self.ACTION_DROPDOWN_OPTIONS)
            for option in action_dropdown_options:
                if option.text == action:
                    self.do_click_by_locator(option)
                    break
            self.do_send_keys(self.ACTION_POPUP_COMMENT_TEXT_AREA, comment)
            self.do_click_by_locator(self.ACTION_POPUP_CANCEL_BUTTON)
        except Exception as e:
            self.logger.error("Exception while updating action and comment and cancel" + str(e))
            raise e

    def get_action_and_comment(self):
        try:
            action = self.get_element_text(self.ACTION_FOR_SKU)
            if self.do_check_visibility(self.BLUE_DOT_FOR_COMMENT_FOR_FIRST_ROW):
                self.do_click_by_locator(self.COMMENT_FOR_SKU)
                comment = self.get_element_text(self.COMMENT_TEXT)
                self.do_double_click(self.BLUE_DOT_FOR_COMMENT_FOR_FIRST_ROW)
            else:
                comment = ""
            return action, comment
        except Exception as e:
            self.logger.error("Exception while fetching sku action and comment" + str(e))
            raise e

    def click_on_top_100_aging_sku(self):
        try:
            self.driver.refresh()
            time.sleep(3)
            self.do_click_by_locator(self.TOP_100_AGING_SKU_TAB)
            page_element = self.driver.find_element(By.XPATH, self.ACTION_PLANING_PAGE_ELEMENT)
            self.scroll_down(page_element)
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Top 100 Aging sku tab' + str(e))
            raise e

    def get_table_headers_for_top_100_aging_table(self, selected_country):
        table_headers = []
        try:
            self.filter_by_country(selected_country)
            for i in range(1, 23):
                xpath = (By.XPATH, "//div[@class='css-yrdy0g-MuiDataGrid-columnHeaderRow'][@aria-rowindex=2]/div[@aria-colindex=" + str(i) + "]")
                if i == 7:
                    self.driver.execute_script(
                        "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
                    time.sleep(2)
                elif i == 15:
                    self.driver.execute_script(
                        "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 3000")
                    time.sleep(2)
                header = self.get_element_text(xpath)
                table_headers.append(header)
            self.logger.info(table_headers)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return table_headers
        except Exception as e:
            self.logger.error('Exception occurred while getting Top 100 sku table headers' + str(e))
            raise e

    def validate_actual_151_in_pages(self):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Actual 151 in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_actual_151_descending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Actual 151 in page %s", str(random_page))
                    self.is_actual_151_descending_order()
                self.logger.info("Verifying Actual 151 in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_actual_151_descending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified Actual 151 is descending by default")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Actual 151 is descending by default in pages" + str(e))
            raise e

    def validate_actual_181_ascending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.ACTUAL_181_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Actual 181 is Ascending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_actual_181_ascending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Actual 181 is Ascending in page %s", str(random_page))
                    self.is_actual_181_ascending_order()
                self.logger.info("Verifying Actual 181 is Ascending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_actual_181_ascending_order()
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified VActual 181 is Ascending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Actual 181 is Ascending in pages" + str(e))
            raise e

    def is_actual_181_ascending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.ACTUAL_181)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] <= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Actual 181 is not in Ascending for row {i+1}')
                    raise Exception('Actual 181 is not in Ascending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Actual 181 is Ascending" + str(e))
            raise e

    def validate_actual_181_descending_in_pages(self):
        try:
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 1500")
            self.do_click_by_locator(self.ACTUAL_181_SORT)
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Actual 181 is Descending in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.is_actual_181_descending_order()
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.go_to_page(random_page)
                    self.logger.info("Verifying Actual 181 is Descending in page %s", str(random_page))
                    self.is_actual_181_descending_order()
                self.logger.info("Verifying Actual 181 is Descending in page %s", str(last_page_number))
                self.go_to_page(last_page_number)
                self.is_actual_181_descending_order()
            self.go_to_page(first_page_number)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-axafay-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info("Successfully verified VActual 181 is Descending")
            return True
        except Exception as e:
            self.logger.error("Exception while validating Actual 181 is Descending in pages" + str(e))
            raise e

    def is_actual_181_descending_order(self):
        value_on_order_list = []
        try:
            elements = self.get_all_elements(self.ACTUAL_181)
            for e in elements:
                value_on_order_list.append(float((e.text).replace(',', '')))
            for i in range(len(value_on_order_list)-1):
                if value_on_order_list[i] >= value_on_order_list[i+1]:
                    continue
                else:
                    self.logger.error(f'Actual 181 is not in Descending in row {i+1}')
                    raise Exception('Actual 181 is not in Descending')
            self.logger.info(len(elements))
        except Exception as e:
            self.logger.error("Exception while validating Actual 181 is Descending" + str(e))
            raise e

    def validate_action_popup_contents_for_aging_sku_table(self):
        action_options = []
        try:
            three_dots = self.get_all_elements(self.FIRST_ROW_THREE_DOTS)
            self.do_click_by_locator(three_dots[-1])
            self.do_click_by_locator(self.ADD_OR_EDIT_OPTION)
            action_popup_dropdown_label = self.get_element_text(self.ACTION_POPUP_DROPDOWN_SECTION_LABEL)
            action_popup_comment_label = self.get_element_text(self.ACTION_POPUP_COMMENT_SECTION_LABEL)
            comment_textbox_text = self.do_get_attribute(self.ACTION_POPUP_COMMENT_TEXT_AREA, "placeholder")
            assert action_popup_dropdown_label == 'Please, select what action will be perform *', 'Action popup dropdown label is incorrect'
            assert action_popup_comment_label == 'What is being done to eliminate aging SKUs?', 'Action popup comment label is incorrect'
            assert comment_textbox_text == 'Input comment (200 character limit)', 'Comment textbox placeholder is incorrect'
            self.do_check_availability(self.ACTION_POPUP_CANCEL_BUTTON)
            self.do_check_availability(self.ACTION_POPUP_CANCEL_BUTTON)
            self.do_click_by_locator(self.ACTION_POPUP_DOWNDOWN)
            action_dropdown_options = self.get_all_elements(self.ACTION_DROPDOWN_OPTIONS)
            for action in action_dropdown_options:
                action_options.append(action.text)
            self.do_click_by_locator(action_dropdown_options[0])
            self.logger.info(action_options)
            self.do_click_by_locator(self.ACTION_POPUP_CANCEL_BUTTON)
            return action_options
        except Exception as e:
            self.logger.error("Exception while validating Action popup contents" + str(e))
            raise e
