import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.parse_config import ParseConfigFile

"""This is the parent of all pages"""
"""It contains all the generic methods and utilities of all the pages"""


class BasePage:
    logger = LogGenerator.logGen()
    parse_config_json = ParseConfigFile()
    TIMEOUT = 60
    TIMEOUT_LESSER = 15

    SEARCH_BOX = (By.CSS_SELECTOR, "input[placeholder='Filter by keyword']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[title='Start search']")
    CREDIT_HOLD_TITLE = (By.XPATH, "//*[text()='Credit Hold']")
    PAGINATION_PAGES = (By.XPATH, "//div[contains(@data-testid,'-page')]")
    PAGINATION_NEXT_PAGE_ARROW = (By.XPATH, "//div[@class='MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-1cl35i1-MuiButtonBase-root-MuiListItemButton-root']/*[@data-testid='NavigateNextIcon']")

    """constructor of the Base page class"""

    def __init__(self, driver):
        self.driver = driver

    """Waits for an element to be clickable and clicks"""

    def do_click_by_locator(self, by_locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(by_locator)).click()

    def do_click_by_locator_without_visibility(self, by_locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located(by_locator)).click()

    """clicks an element"""

    @staticmethod
    def do_click_by_element(element):
        element.click()

    """Waits for an element to be visible and returns boolean"""

    def do_check_visibility(self, by_locator):
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    """Waits for an element to be clickable and returns boolean"""

    def do_check_clickability(self, by_locator):
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(by_locator))
            return True
        except:
            return False

    """Waits for an element to be available and returns boolean"""

    def do_check_availability(self, by_locator):
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located(by_locator))
            return True
        except:
            return False

    """Waits for an element to be visible and clears textfield"""

    def do_clear_textfield(self, by_locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).clear()

    """Waits for an element to be visible and input texts"""

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        element.send_keys(text)

    """double clicks an element and enters text"""

    def do_double_click_and_send_keys_by_element(self, element, text):
        actions = ActionChains(self.driver)
        # self.driver.execute_script('arguments[0].scrollIntoView();', element)
        # actions.move_to_element(element).click().perform()
        actions.double_click(element)
        actions.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        actions.send_keys(text)
        actions.perform()

    """Waits for the element to be visible and perform double click"""

    def do_double_click(self, by_locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.double_click(element)
        actions.perform()

    """Waits for flyout dropdown to appear and then selects first option"""

    def do_send_keys_down_enter(self, by_locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.move_to_element(element)
        actions.send_keys(Keys.RETURN)
        actions.perform()

    """Waits for an element to be visible and returns element text"""

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """Waits for the element to be visible and returns element title attribute"""

    def get_element_title(self, by_locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute("title")

    """Waits for all the element to be visible and return elements in a list"""

    def get_all_elements(self, by_locator):
        elements = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def get_all_elements_without_visibility(self, by_locator):
        elements = WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_all_elements_located(by_locator))
        return elements

    """Waits for all the element to be visible and return all texts in a list"""

    def get_all_elements_text(self, by_locator):
        elements = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_all_elements_located(by_locator))
        return elements.text

    """Waits for the frame to be visible and switches to the  required frame"""

    def do_switch_to_required_frame(self, by_locator):
        reqd_frame = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        self.driver.switch_to.frame(reqd_frame)
        self.logger.info("Successfully switched frame")

    """It switches to the  parent frame"""

    def do_switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()
        self.logger.info("Successfully switched to parent frame")

    """It switches to the Next Browser tab"""

    def do_switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("Successfully switched to next browser tab")

    """It switches to the Previous Browser tab"""

    def do_switch_to_previous_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.logger.info("Successfully switched to previous browser tab")

    """Static wait"""

    def do_sleep(self, sleep_value):
        min_sleep_time = self.parse_config_json.get_data_from_config_json("sleepTime", "min_sleep")
        above_min_sleep_time = self.parse_config_json.get_data_from_config_json("sleepTime", "above_min_sleep")
        above_min_2_sleep_time = self.parse_config_json.get_data_from_config_json("sleepTime", "above_min_2_sleep")
        average_sleep_time = self.parse_config_json.get_data_from_config_json("sleepTime", "average_sleep")
        above_average_sleep_time = self.parse_config_json.get_data_from_config_json("sleepTime", "above_average_sleep")
        max_sleep_time = self.parse_config_json.get_data_from_config_json("sleepTime", "max_sleep")

        if sleep_value == "min":
            sleep_time = int(min_sleep_time)
        elif sleep_value == "above_min":
            sleep_time = int(above_min_sleep_time)
        elif sleep_value == "above_min_2":
            sleep_time = int(above_min_2_sleep_time)
        elif sleep_value == "average":
            sleep_time = int(average_sleep_time)
        elif sleep_value == "above_average":
            sleep_time = int(above_average_sleep_time)
        elif sleep_value == "max":
            sleep_time = int(max_sleep_time)
        else:
            sleep_time = 1  # Default value

        self.logger.info("Sleeping for %s seconds.." % sleep_time)
        time.sleep(sleep_time)

    """get any attribute value"""

    def do_get_attribute(self, by_locator, attribute_name):
        value = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(by_locator)).get_attribute(attribute_name)
        return value

    """This method is used to checks whether the web-element is present or not"""

    def is_present(self, by_locator):
        try:
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def do_refresh(self):
        try:
            self.driver.refresh()
            self.logger.info("Refreshing the browser")
            return True
        except:
            return False

    """This method is used to hover the mouse to an element"""

    def do_mouse_hover_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    """Waits for an element to visible and gets value"""

    def do_get_keys(self, by_locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('value')

    """Accept Alert popup"""

    def do_accept_alert_popup(self):
        alert_popup = self.driver.switch_to.alert
        alert_popup.accept()

    def do_dismiss_alert_popup(self):
        alert_popup = self.driver.switch_to.alert
        alert_popup.dismiss()

    def do_send_backspace_to_clear_field(self, by_locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    def scroll_down(self, element):
        actions = ActionChains(self.driver)
        for s in range(2):
            actions.send_keys_to_element(element, Keys.PAGE_DOWN).perform()

    def scroll_up(self, element):
        actions = ActionChains(self.driver)
        for s in range(2):
            actions.send_keys_to_element(element, Keys.PAGE_UP).perform()

    def scroll_horizontally(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.logger.info("Scrolled horizontally")

    def go_to_page(self, page_number):
        try:
            self.do_check_availability(self.PAGINATION_PAGES)
            pages = self.get_all_elements(self.PAGINATION_PAGES)
            first_page_number = int(pages[0].text)
            last_page_number = int(pages[-1].text)
            self.logger.info("First page :" + str(first_page_number))
            self.logger.info("Last page :" + str(last_page_number))
            if page_number < first_page_number or page_number > last_page_number:
                raise Exception("The page number provided does not exist.")
            if page_number == last_page_number:
                self.logger.info("Clicked on last page " + str(last_page_number))
                pages[-1].click()
            elif page_number == first_page_number:
                time.sleep(1)
                self.logger.info("Clicked on first page " + str(last_page_number))
                pages[0].click()
            else:
                for page in range(first_page_number, last_page_number + 1):
                    page_xpath = (By.XPATH, "//div[@data-testid = '" + str(page) + "-page']")
                    ui_page_number = self.get_element_text(page_xpath)
                    if str(page_number) in ui_page_number:
                        self.logger.info("Clicked on page " + str(page_number))
                        break
                    else:
                        self.logger.info("Page number did not match, checking with next page.")
                        self.do_click_by_locator(self.PAGINATION_NEXT_PAGE_ARROW)
                        time.sleep(1)
        except Exception as e:
            self.logger.error("Exception occurred while switching to page tab " + str(e))
            raise e

    def wait_till_element_is_not_available(self, by_locator):
        while True:
            try:
                element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
            except:
                break

    def get_element_text_for_filter(self, by_locator):
        element = WebDriverWait(self.driver, self.TIMEOUT_LESSER).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """Function to verify whether WebElement is enabled or not"""
    def is_element_enabled(self, element):
        if element.is_enabled():
            return True
        else:
            return False

    def do_check_visibility_for_validation(self, by_locator):
        try:
            WebDriverWait(self.driver, self.TIMEOUT_LESSER).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False
