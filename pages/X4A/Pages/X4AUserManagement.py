import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from db.service.X4AUserDataDbManagementService import X4AUserDataDbManagementService

db_file_path = ReadConfig.get_db_file_path()
class X4AUserManagementPage(BasePage):
    ADMINISTRATION_MENU = (By.XPATH, "//*[@data-testid='administration-MenuItem']")
    ASSOCIATE_MANAGEMENT_OPTION = (By.XPATH, "//*[text()='Associates Management']")
    SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search associate by name or email']")
    SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    COLUMN_HEADER_ITEM_LIST = (By.XPATH, "//div[@role='columnheader']")
    Exp_column_header_list = ["Name", "Email", "Status", "Designation", "Country", "Phone", "Date added", "Action"]
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

    def go_to_associate_management(self):
        try:
            self.do_click_by_locator(self.ADMINISTRATION_MENU)
            self.do_double_click(self.ASSOCIATE_MANAGEMENT_OPTION)
            self.logger.info("Clicked on Associate management in the menu")
        except Exception as e:
            self.logger.error('Exception occured while clicking on Associate management ' + str(e))
            raise e

    def do_search_associate(self):
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            user_email = associate_detail_list[3]
            USER_ICON = (By.XPATH, "//span[text()='" + str(user_email) + "']/parent::div/preceding-sibling::div/a/span")
            self.do_click_by_locator(self.SEARCH_BOX)
            user_name = associate_detail_list[2]
            self.do_send_keys(self.SEARCH_BOX, user_name)
            self.logger.info("Enter the Associate name need to be searched")
            self.do_click_by_locator(USER_ICON)
        except Exception as e:
            self.logger.error('Exception occured while searching associate name' + str(e))
            raise e

    def do_validate_associate_page(self,user_status):
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            user_name = associate_detail_list[2]
            user_email = associate_detail_list[3]
            assert self.do_check_visibility(self.USER_DETAILS),"user details page not opened"
            assert user_name == self.get_element_text(self.USER_NAME_TEXT),"User name validation failed"
            assert user_email == self.get_element_text(self.USER_EMAIL_TEXT),"User email validation failed"
            assert user_status == self.get_element_text(self.USER_STATUS_TEXT),"User status failed"

            self.logger.info("Successfully searched Associate")
            return True
        except Exception as e:
            self.logger.error("Not able to search user details")
            return False

    def do_validate_coloumn_header(self):
        try:
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

    def do_validate_associate_role(self):
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            role_db_list = associate_detail_list[4].split(",")
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            self.logger.info("validate the roles from database")
            for i in associate_role_list:
                if i.text not in role_db_list:
                    raise Exception(" Validation Associate role failed for %s" % i.text)
                else:
                    self.logger.info("Validated Associate roles %s is passed" % i.text)
 
            return True
        except Exception as e:
            self.logger.error("Not able to validate roles")
            return False

    def do_manage_associate_role(self):
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            role_db_list = associate_detail_list[4].split(",")
            role_list = role_db_list[1].split(" - ")
            associate_role = role_list[1]
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            flag = False
            self.do_click_by_locator(self.ROLES_MANAGE_BUTTON)
            for i in associate_role_list:
                if associate_role in i.text:
                    self.do_click_by_locator(self.ROLE_DELETE_BUTTON)
                    self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
                    self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
                    self.do_click_by_locator(self.SAVE_BUTTON)

                    self.logger.info("Deleted Sales Associate role %s is passed" % associate_role_list[i].text)
                    flag = True

            return flag
        except Exception as e:
            self.logger.error("Not able to delete roles")
            return False
    def do_validate_associate_role_after_deletion(self):
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            role_db_list = associate_detail_list[4].split(",")
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            flag = False
            for i in associate_role_list:
                if role_db_list[1] not in i.text:
                    flag = True

            return flag
        except Exception as e:
            self.logger.error("Not able to validate roles")
            return False

    def do_add_associate_role(self):
        # ASSOCIATE_PERSONA_BOX = (By.XPATH, "//span[text()='Associate persona ']/following-sibling::div/div/span")
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            role_db_list = associate_detail_list[4].split(",")
            role_list = role_db_list[1].split(" - ")
            associate_persona = role_list[0]
            associate_role = role_list[1]

            ASSOCIATE_PERSONA_VALUE = (By.XPATH, "//li[@data-value='" + str(associate_persona) + "']")
            ASSOCIATE_ROLE_VALUE = (By.XPATH, "//li[@data-value='" + str(associate_role) + "']")
            associate_role_list = self.get_all_elements(self.ASSOCIATE_ROLES)
            self.logger.info("length of list %s" % len(associate_role_list))
            flag = False
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

            return True
        except Exception as e:
            self.logger.error("Not able to add country")
            return False

    def do_validate_associate_country(self):
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            country_db_list = associate_detail_list[5].split(",")
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            if 'All countries(Global)' in associate_country_list[0].text:
                self.logger.info("Validated Associate country %s is passed" % associate_country_list[0].text)
                return True
            else:
                for i in associate_country_list:
                    if i.text not in country_db_list:
                        raise Exception("Validated Associate country %s is failed" % i.text)
                    else:
                        self.logger.info("Validated Associate country %s is passed" % i.text)


                return True
        except Exception as e:
            self.logger.error("Not able to validate country")
            return False

    def do_manage_associate_country(self):
        try:
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            country_db_list = associate_detail_list[5].split(",")
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            self.do_click_by_locator(self.COUNTRIES_MANAGE_BUTTON)
            self.do_click_by_locator(self.COUNTRY_SEARCH_BOX)
            deleted_country = country_db_list[len(associate_country_list)-1]
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
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)
            country_db_list = associate_detail_list[5].split(",")
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            deleted_country = country_db_list[len(associate_country_list)-1]
            # self.scroll()
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
            user_data_management_srv_obj = X4AUserDataDbManagementService()
            associate_detail_list = user_data_management_srv_obj.get_associate_details(db_file_path)

            country_db_list = associate_detail_list[5].split(",")
            associate_country_list = self.get_all_elements(self.ASSOCIATE_COUNTRIES)
            self.logger.info("length of list %s" % len(associate_country_list))
            self.do_click_by_locator(self.COUNTRIES_MANAGE_BUTTON)
            self.do_click_by_locator(self.COUNTRY_SEARCH_BOX)
            # self.logger.info("get the country to be added")
            deleted_country = country_db_list[len(associate_country_list) - 1]
            # self.logger.info("Search the country to be added")
            self.do_send_keys(self.COUNTRY_SEARCH_BOX, deleted_country)
            # self.logger.info("Click on assign button for respective country")
            self.do_click_by_locator(self.COUNTRY_ASSIGN_BUTTON)
            # self.logger.info("Click on IM service ticket no")
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            # self.logger.info("get the country to be added")
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
            # self.logger.info("click on De-Activate button")
            self.do_click_by_locator(self.DEACTIVATE_BUTTON)
            # self.logger.info("Enter IM Service Ticket No")
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            # self.logger.info("click on Deactivate button")
            self.do_click_by_locator(self.DEACTIVATION_BUTTON)

            return True
        except Exception as e:
            self.logger.error("Not able to deactivate account")
            return False

    def do_activate_account(self):
        try:
            self.do_click_by_locator(self.ACTIVATE_BUTTON)
            # self.logger.info("Enter IM Service Ticket No")
            self.do_click_by_locator(self.IM_SERVICE_TICKET_NO)
            self.do_send_keys(self.IM_SERVICE_TICKET_NO, '123')
            # self.logger.info("click on Activate button")
            self.do_click_by_locator(self.ACTIVATION_BUTTON)

            return True
        except Exception as e:
            self.logger.error("Not able to activate account")
            return False

