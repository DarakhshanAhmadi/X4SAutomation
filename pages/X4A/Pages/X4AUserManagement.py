import time

from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AUserDataDbManagementService import X4AUserDataDbManagementService

db_file_path = ReadConfig.get_db_file_path()
class X4AUserManagementPage(BasePage):
    # Define the required locators
    ADMINISTRATION_MENU = (By.XPATH, "//*[@data-testid='administration-MenuItem']")
    ASSOCIATE_MANAGEMENT_OPTION = (By.XPATH, "//*[text()='Associates Management']")
    SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search associate by name or email']")
    SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    COLUMN_HEADER_ITEM_LIST = (By.XPATH, "//div[@role='columnheader']")
    ACTIVE_USER_STATUS = (By.XPATH, "//span[status()='Activated']")
    DEACTIVE_USER_STATUS = (By.XPATH, "//span[status()='Deactivated']")
    ASSOCIATE_ROLES = (By.XPATH, "//*[text()='Associate roles']/parent::div/following-sibling::div/div/span")
    ASSOCIATE_COUNTRIES = (By.XPATH, "//*[text()='Countries']/parent::div/following-sibling::div/div/span")
    ROLES_MANAGE_BUTTON = (By.XPATH, "//*[text()='Associate roles']/following-sibling::button")
    ROLE_DELETE_BUTTON = (By.XPATH,
                          "//*[text()='Sales Associate']/parent::div/parent::div/following-sibling::div/div/div/following-sibling::div")
    ROLES_ADD_BUTTON = (By.XPATH, "//*[text()='+ Add']")
    ASSOCIATE_PERSONA_BOX = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div")
    ASSOCIATE_ROLES_BOX = (By.XPATH, "/html/body/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[1]")

    COUNTRIES_MANAGE_BUTTON = (By.XPATH, "//*[text()='Countries']/following-sibling::button")
    IM_SERVICE_TICKET_NO = (By.XPATH, "//*[@placeholder='Enter # related to this change']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    DROPDOWN_BUTTON = (By.XPATH, "//*[@data-testid='ArrowDropDownIcon']")

    USER_DETAILS = (By.XPATH, "//p[text()='User details']")
    COUNTRY_SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search']")
    COUNTRY_ASSIGN_BUTTON = (By.XPATH, "//button[text()='Assign']")

    ACTIVATE_BUTTON = (By.XPATH, "//button[text()='Activate']")
    ACTIVATION_BUTTON = (By.XPATH, "//div[@class='MuiBox-root css-13787cw']//button[text()='Activate']")

    DEACTIVATE_BUTTON = (By.XPATH, "//button[text()='De-activate']")
    DEACTIVATION_BUTTON = (By.XPATH, "//button[text()='Deactivate']")

    USER_NAME_TEXT = (By.XPATH, "//div[@class='MuiBox-root css-z2wu8w']/h3")
    USER_EMAIL_TEXT = (By.XPATH, "//div[@class='MuiBox-root css-z2wu8w']/p")
    USER_STATUS_TEXT = (By.XPATH, "//div[@class='MuiBox-root css-0']/span")
    COUNTRY_DELETE_BUTTON = (By.XPATH, "//*[@data-testid='DeleteOutlineIcon']")

    Exp_column_header_list = ["Name", "Email", "Status", "Designation", "Country", "Phone", "Date added", "Action"]

    user_data_management_srv_obj = X4AUserDataDbManagementService()
    associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
    user_email = associate_detail_list[3]
    user_name = associate_detail_list[2]
    role_db_list = associate_detail_list[4].split(",")
    role_list = role_db_list[1].split(" - ")
    associate_role = role_list[1]

    country_db_list = associate_detail_list[5].split(",")

    def go_to_associate_management(self):
        try:
            self.do_click_by_locator(self.ADMINISTRATION_MENU)
            self.do_double_click(self.ASSOCIATE_MANAGEMENT_OPTION)
            self.logger.info("Successfully open Associate management page")
        except Exception as e:
            self.logger.error('Exception occured while clicking on Associate management ' + str(e))
            raise e

    def do_validate_coloumn_header(self):
        try:
            # validate Associate management page's coloumn headers
            self.logger.info("Validating coloumn header in associate details page")
            column_header_list = self.get_all_elements(self.COLUMN_HEADER_ITEM_LIST)
            self.logger.info("length of list %s" % len(column_header_list))
            flag = True
            for i in range(len(column_header_list)):
                if self.Exp_column_header_list[i] in column_header_list[i].text:
                    self.logger.info("validated column header %s is passed" % column_header_list[i].text)
                else:
                    flag = False
                    self.logger.info("validated column header %s is failed" % column_header_list[i].text)
            if flag == False:
                raise Exception("Validation failed for Column Header")

            else:
                self.logger.info("Validation passed for Column Header")
            return True
        except Exception as e:
            self.logger.error("Not able to check column header")
            return False

    def do_search_associate(self):
        try:
            # Get user data like name ,email from Input
            USER_ICON = (By.XPATH, "//span[text()='" + str(self.user_email) + "']/parent::div/preceding-sibling::div/a/span")
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, self.user_name)
            self.logger.info("Enter the Associate name need to be searched")
            # click USER ICON
            self.do_click_by_locator(USER_ICON)
            self.logger.info("successfully searched the associate name from the list")
        except Exception as e:
            self.logger.error('Exception occured while searching associate name' + str(e))
            raise e

    def do_validate_associate_page(self,user_status):
        try:
            # validate Associate details page
            assert self.do_check_visibility(self.USER_DETAILS),"user details page not opened"
            assert self.user_name == self.get_element_text(self.USER_NAME_TEXT),"User name validation failed"
            assert self.user_email == self.get_element_text(self.USER_EMAIL_TEXT),"User email validation failed"
            assert user_status == self.get_element_text(self.USER_STATUS_TEXT),"User status failed"

            self.logger.info("Successfully validated Associate details page")
            return True
        except Exception as e:
            self.logger.error("Not able to validate associate details")
            return False

    def do_validate_associate_role(self):
        try:
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            self.logger.info("validate the roles from database")
            for i in associate_role_list:
                if i.text not in self.role_db_list:
                    raise Exception(" Validation Associate role failed for %s" % i.text)
                else:
                    self.logger.info("Validated Associate roles %s is passed" % i.text)
 
            return True
        except Exception as e:
            self.logger.error("Not able to validate roles")
            return False

    def do_manage_associate_role(self):
        try:
            # Manage Associate role and delete the last role assigned.
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            flag = False
            self.do_click_by_locator(self.ROLES_MANAGE_BUTTON)
            for i in associate_role_list:
                if self.associate_role in i.text:
                    self.do_click_by_locator(self.ROLE_DELETE_BUTTON)
                    self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
                    self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
                    self.do_click_by_locator(self.SAVE_BUTTON)

                    self.logger.info("Deleted Associate role %s is passed" % associate_role_list[i].text)
                    flag = True

            return flag
        except Exception as e:
            self.logger.error("Not able to delete role")
            return False

    def do_validate_associate_role_after_deletion(self):
        try:
            # validate associate after role deletion
            # get the role deleted for associate
            deleted_role = self.role_db_list[1]
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            flag = False
            # check deleted associate role does not available in role list
            for i in associate_role_list:
                if deleted_role not in i.text:
                    flag = True
            if flag:
                self.logger.info("Successfully validated the deleted role not exist in role list.")
            else:
                self.logger.error("Deleted role exist in role list.")

            return flag
        except Exception as e:
            self.logger.error("Not able to validate roles")
            return False

    def do_add_associate_role(self):
        # ASSOCIATE_PERSONA_BOX = (By.XPATH, "//span[text()='Associate persona ']/following-sibling::div/div/span")
        try:
            associate_persona = self.role_list[0]
            associate_role = self.role_list[1]

            # Get iterator for associate persona and role to be added
            ASSOCIATE_PERSONA_VALUE = (By.XPATH, "//li[@data-value='" + str(associate_persona) + "']")
            ASSOCIATE_ROLE_VALUE = (By.XPATH, "//li[@data-value='" + str(associate_role) + "']")
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            self.logger.info("click on Manage button for Associate Roles")
            self.do_click_by_locator(self.ROLES_MANAGE_BUTTON)
            self.logger.info("click on Add button for Associate Roles")
            self.do_click_by_locator(self.ROLES_ADD_BUTTON)
            self.logger.info("click on persona box for Associate Roles")
            self.do_click_by_locator(self.ASSOCIATE_PERSONA_BOX)
            self.logger.info("click on desired for Associate Roles")
            self.do_click_by_locator(ASSOCIATE_PERSONA_VALUE)

            self.logger.info("click on Role box for Associate Roles")
            self.do_click_by_locator(self.ASSOCIATE_ROLES_BOX)
            self.logger.info("click on desired for Associate Roles")
            self.do_click_by_locator(ASSOCIATE_ROLE_VALUE)
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            self.do_click_by_locator(self.SAVE_BUTTON)
            self.logger.info("Associate role has been added")
            return True
        except Exception as e:
            self.logger.error("Not able to add country")
            return False

    def do_validate_associate_country(self):
        try:
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            if 'All countries(Global)' in associate_country_list[0].text:
                self.logger.info("Validated Associate country %s is passed" % associate_country_list[0].text)
                return True
            else:
                for i in associate_country_list:
                    if i.text not in self.country_db_list:
                        raise Exception("Validated Associate country %s is failed" % i.text)
                    else:
                        self.logger.info("Validated Associate country %s is passed" % i.text)


                return True
        except Exception as e:
            self.logger.error("Not able to validate country")
            return False

    def do_manage_associate_country(self):
        try:
            # Manage Associate country and delete a country.
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            self.do_click_by_locator(self.COUNTRIES_MANAGE_BUTTON)
            self.do_click_by_locator(self.COUNTRY_SEARCH_BOX)
            deleted_country = self.country_db_list[len(associate_country_list)-1]
            self.do_send_keys(self.COUNTRY_SEARCH_BOX, deleted_country)
            self.do_click_by_locator(self.COUNTRY_DELETE_BUTTON)
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            self.do_click_by_locator(self.SAVE_BUTTON)
            self.logger.info("Deletion of Associate country %s is passed" % associate_country_list[len(associate_country_list)-1].text)

            return True
        except Exception as e:
            self.logger.error("Not able to delete country")
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            self.do_click_by_locator(self.CANCEL_BUTTON)

            return False

    def do_validate_associate_country_after_deletion(self):
        try:
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            deleted_country = self.country_db_list[len(associate_country_list)-1]
            flag = False
            for i in associate_country_list:
                if deleted_country not in i.text:
                    flag = True

            return flag
        except Exception as e:
            self.logger.error("Not able to validate country")
            return False

    def do_add_associate_country(self):
        try:
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            self.do_click_by_locator(self.COUNTRIES_MANAGE_BUTTON)
            self.do_click_by_locator(self.COUNTRY_SEARCH_BOX)
            self.logger.info("get the country to be added")
            deleted_country = self.country_db_list[len(associate_country_list) - 1]
            self.logger.info("Search the country to be added")
            self.do_send_keys(self.COUNTRY_SEARCH_BOX, deleted_country)
            self.logger.info("Click on assign button for respective country")
            self.do_click_by_locator(self.COUNTRY_ASSIGN_BUTTON)
            self.logger.info("Click on IM service ticket no")
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            self.logger.info("get the country to be added")
            self.do_click_by_locator(self.SAVE_BUTTON)

            return True
        except Exception as e:
            self.logger.error("Not able to add country")
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            self.do_click_by_locator(self.CANCEL_BUTTON)
            return False

    def do_deactivate_account(self):
        try:
            # Traverse to user management page
            self.go_to_associate_management()
            # Open the associated details page
            self.do_search_associate()
            # click on De-Activate button
            self.do_click_by_locator(self.DEACTIVATE_BUTTON)
            # Enter IM Service Ticket No
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            # click on Deactivate button
            self.do_click_by_locator(self.DEACTIVATION_BUTTON)
            self.logger.info("The associate account has been deactivated")

            return True
        except Exception as e:
            self.logger.error("Not able to deactivate account")
            return False

    def do_activate_account(self):
        try:
            # Traverse to user management page
            self.go_to_associate_management()
            # Open the associated details page
            self.do_search_associate()
            # click on Activate button
            self.do_click_by_locator(self.ACTIVATE_BUTTON)
            # Enter IM Service Ticket No
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            # click on Activate button
            self.do_click_by_locator(self.ACTIVATION_BUTTON)
            self.logger.info("The associate account has been activated")

            return True
        except Exception as e:
            self.logger.error("Not able to activate account")
            return False

