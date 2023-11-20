import time
import random
import string
import time
import pandas
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig
from datetime import date, timedelta
from CommonUtilities.parse_json_common import common_json_ops


class X4AOrderExceptionPage(BasePage):
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()
    common_json = common_json_ops()

    SALES_ICON = (By.XPATH, "//*[@data-testid='SalesIcon']")
    SALES_MENU = (By.XPATH, "//*[@data-testid='sales-MenuItem']")
    ORDER_EXCEPTION_OPTION = (By.XPATH, "//*[text()='Order Exception']")
    ORDER_EXCEPTION_TEXT = (By.XPATH, "//*[text()='Order Exception']")
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
    ORDER_EXCEPTION_PAGE = (By.XPATH, "//*[text()='Order Exception']")
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
    YES_RESUBMIT_ORDER_BUTTON = (By.XPATH, "//button[text()='Yes, resubmit order']")
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
    LAST_ORDER_ATTEMPT_SECTION_FILTER_PANEL = (By.XPATH, "//*[text()='Last Order Attempt On']")
    CREATED_ON_SECTION_FILTER_PANEL = (By.XPATH, "//*[text()='Created On']")
    LAST_ORDER_ATTEMPT_SECTION_FROM_LABEL_WITH_DATE_RANGE_FILTER = (By.XPATH,
                                                                    "//*[text()='Last Order Attempt On']/../../following-sibling::div//*[text()='From']/parent::div/div/div/div/input[@name='rangePicker']")
    LAST_ORDER_ATTEMPT_SECTION_TO_LABEL_WITH_DATE_RANGE_FILTER = (By.XPATH,
                                                                  "//*[text()='Last Order Attempt On']/../../following-sibling::div//*[text()='To']/parent::div/div/div/div/input[@name='rangePicker']")
    LAST_ORDER_ATTEMPT_SECTION_SELECTED_EXPAND_MORE_BUTTON = (
        By.XPATH,
        "//*[text()='Last Order Attempt On']/parent::div/following-sibling::div/*[@data-testid='ExpandMoreIcon']")
    LAST_ORDER_ATTEMPT_SECTION_SELECTED_ALL_DATES_CHECKBOX = (By.XPATH,
                                                              "//*[text()='Last Order Attempt On']/parent::div/../following-sibling::div//div/label/span[text()='Select all dates']")
    LAST_ORDER_ATTEMPT_SECTION_TODAY_CHECKBOX = (By.XPATH,
                                                 "//*[text()='Last Order Attempt On']/parent::div/../following-sibling::div//div/label/span[text()='Today']")
    LAST_ORDER_ATTEMPT_SECTION_YESTERDAY_CHECKBOX = (By.XPATH,
                                                     "//*[text()='Last Order Attempt On']/parent::div/../following-sibling::div//div/label/span[text()='Yesterday']")
    LAST_ORDER_ATTEMPT_SECTION_SEE_MORE_LESS_BUTTON = (By.XPATH,
                                                       "//*[text()='Last Order Attempt On']/parent::div/../following-sibling::div//div/button[@data-testid='LastOrderAttempt-SeeMoreLess']")
    LAST_ORDER_ATTEMPT_SECTION_LAST_WEEK_CHECKBOX = (By.XPATH,
                                                     "//*[text()='Last Order Attempt On']/parent::div/../following-sibling::div//div/label/span[text()='Last week']")
    LAST_ORDER_ATTEMPT_SECTION_LAST_30_DAYS_CHECKBOX = (By.XPATH,
                                                        "//*[text()='Last Order Attempt On']/parent::div/../following-sibling::div//div/label/span[text()='Last 30 days']")
    CREATED_ON_SECTION_FROM_LABEL_WITH_DATE_RANGE_FILTER = (By.XPATH,
                                                            "//*[text()='Created On']/../../following-sibling::div//*[text()='From']/parent::div/div/div/div/input[@name='rangePicker']")
    CREATED_ON_SECTION_SELECTED_EXPAND_MORE_BUTTON = (
        By.XPATH, "//*[text()='Created On']/parent::div/following-sibling::div/*[@data-testid='ExpandMoreIcon']")
    CREATED_ON_SECTION_TO_LABEL_WITH_DATE_RANGE_FILTER = (By.XPATH,
                                                          "//*[text()='Created On']/../../following-sibling::div//*[text()='To']/parent::div/div/div/div/input[@name='rangePicker']")
    CREATED_ON_SECTION_SELECTED_ALL_DATES_CHECKBOX = (By.XPATH,
                                                      "//*[text()='Created On']/parent::div/../following-sibling::div//div/label/span[text()='Select all dates']")
    CREATED_ON_SECTION_TODAY_CHECKBOX = (
        By.XPATH, "//*[text()='Created On']/parent::div/../following-sibling::div//div/label/span[text()='Today']")
    CREATED_ON_SECTION_YESTERDAY_CHECKBOX = (
        By.XPATH, "//*[text()='Created On']/parent::div/../following-sibling::div//div/label/span[text()='Yesterday']")
    CREATED_ON_SECTION_SEE_MORE_LESS_BUTTON = (By.XPATH,
                                               "//*[text()='Created On']/parent::div/../following-sibling::div//div/button[@data-testid='createdOn-SeeMoreLess']")
    CREATED_ON_SECTION_LAST_WEEK_CHECKBOX = (
        By.XPATH, "//*[text()='Created On']/parent::div/../following-sibling::div//div/label/span[text()='Last week']")
    CREATED_ON_SECTION_LAST_30_DAYS_CHECKBOX = (
        By.XPATH,
        "//*[text()='Created On']/parent::div/../following-sibling::div//div/label/span[text()='Last 30 days']")
    LAST_ORDER_ATTEMPT_SECTION_FROM_CALENDER_ICON = (By.XPATH,
                                                     "//*[text()='Last Order Attempt On']/../../following-sibling::div//*[text()='From']/parent::div/div/div/div/div/button[@aria-label='calendar icon button']")
    LAST_ORDER_ATTEMPT_SECTION_TO_CALENDER_ICON = (By.XPATH,
                                                   "//*[text()='Last Order Attempt On']/../../following-sibling::div//*[text()='To']/parent::div/div/div/div/div/button[@aria-label='calendar icon button']")
    LAST_ORDER_ATTEMPT_SECTION_FROM_CURRENT_DATE = (By.XPATH, "//button[@aria-current='date']")
    LAST_ORDER_ATTEMPT_SECTION_TO_CURRENT_DATE = (By.XPATH, "//button[@aria-current='date']")
    CREATED_ON_SECTION_FROM_CALENDER_ICON = (By.XPATH,
                                             "//*[text()='Created On']/../../following-sibling::div//*[text()='From']/parent::div/div/div/div/div/button[@aria-label='calendar icon button']")
    CREATED_ON_SECTION_TO_CALENDER_ICON = (By.XPATH,
                                           "//*[text()='Created On']/../../following-sibling::div//*[text()='To']/parent::div/div/div/div/div/button[@aria-label='calendar icon button']")
    CREATED_ON_SECTION_FROM_CURRENT_DATE = (By.XPATH, "//button[@aria-current='date']")
    CREATED_ON_SECTION_TO_CURRENT_DATE = (By.XPATH, "//button[@aria-current='date']")
    LAST_ORDER_ATTEMPT_SECTION_FROM_YESTERDAY_DATE = (
        By.XPATH, "//button[@aria-current='date']/preceding::button[@role='gridcell'][1]")
    LAST_ORDER_ATTEMPT_SECTION_FROM_SELECTED_DATE_VALUE = (By.XPATH,
                                                           "//*[text()='Last Order Attempt On']/../../following-sibling::div//*[text()='From']/parent::div/div/div/div/input[@name='rangePicker']")
    LAST_ORDER_ATTEMPT_SECTION_TO_SELECTED_DATE_VALUE = (By.XPATH,
                                                         "//*[text()='Last Order Attempt On']/../../following-sibling::div//*[text()='To']/parent::div/div/div/div/input[@name='rangePicker']")
    LAST_ORDER_ATTEMPT_DATE_ITEM_ITEM_LIST = (By.XPATH,
                                              "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='lastOrderAttemptDate']")
    CREATED_ON_ITEM_LIST = (By.XPATH,
                            "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='createdOn']")
    CREATED_ON_SECTION_FROM_YESTERDAY_DATE = (
        By.XPATH, "//button[@aria-current='date']/preceding::button[@role='gridcell'][1]")
    CREATED_ON_SECTION_FROM_SELECTED_DATE_VALUE = (By.XPATH,
                                                   "//*[text()='Created On']/../../following-sibling::div//*[text()='From']/parent::div/div/div/div/input[@name='rangePicker']")
    CREATED_ON_SECTION_TO_SELECTED_DATE_VALUE = (By.XPATH,
                                                 "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[5]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div/input")
    TABLE_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-row']")

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

    """End User Details"""

    END_USER_DETAILS_EDIT_BUTTON = (
        By.XPATH, "//*[text()='End user details']/*[@data-testid='ModeEditOutlineOutlinedIcon']")
    EDIT_END_USER_DETAILS_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/H2")
    END_USER_DETAILS_CANCEL_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../../div[3]/button[1]")
    END_USER_DETAILS_SAVE_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/../../div[3]/button[2]")
    END_USER_DETAILS_ClOSE_ICON_BUTTON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    END_USER_SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search Company']")
    ADD_NEW_END_USER_LINK = (By.XPATH, "//*[text()='Add New End User']/button")
    SEARCHED_END_USER_TITLE_LIST = (
        By.XPATH, "//*[@aria-labelledby='Selected-card-group-label']/div/div/div/div/div[2]/div/h3")
    SAVE_BUTTON_DISABLE = (By.XPATH,
                           "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root Mui-disabled  css-1i25qo9-MuiButtonBase-root-MuiButton-root'']")
    SELECTED_END_USER_EDIT_BUTTON = (By.XPATH, "//*[@data-testid='EditOutlinedIcon']")
    SAVE_BUTTON_ENABLE = (By.XPATH,
                          "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root  css-1i25qo9-MuiButtonBase-root-MuiButton-root']")
    READ_ONLY_END_USER_ID_SUFFIX = (By.XPATH,
                                    "//*[@id='end-user-id']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")
    READY_ONLY_COMPANY_NAME = (By.XPATH,
                               "//*[@id='company-name']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")
    READ_ONLY_ADDRESS_LINE_1 = (By.XPATH,
                                "//*[@id='address-line-1']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")
    READ_ONLY_ADDRESS_LINE_2 = (By.XPATH,
                                "//*[@id='address-line-2']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")
    READ_ONLY_CITY = (By.XPATH,
                      "//*[@id='city']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")
    READ_ONLY_STATE = (By.XPATH,
                       "//*[@id='state']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")
    READ_ONLY_ZIP_CODE = (By.XPATH,
                          "//*[@id='zip-code']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")
    READ_ONLY_COUNTRY = (By.XPATH,
                         "//*[@id='country']/parent::div[@class='MuiInputBase-root MuiInputBase-colorPrimary Mui-disabled MuiInputBase-formControl css-zzmosa-MuiInputBase-root']")

    DEFAULT_SELECTED_THE_CHECKBOX_BILLING_AND_TECHNICAL_CONTACT = (By.XPATH,
                                                                   "//*[text()='The billing & technical contact is the same as the primary contact']/parent::label/span/input[@checked]")
    PHONE_NUMBER_TEXTBOX = (By.XPATH, "//*[@id='phone-number' and @aria-invalid='false']")
    NAME_TEXTBOX = (By.XPATH, "//*[@id='ContactName' and @aria-invalid='false']")
    EMAIL_TEXTBOX = (By.XPATH, "//*[@id='email' and @aria-invalid='false']")
    SELECTED_END_USER_COMPANY_NAME = (By.XPATH, "//*[@data-testid='EditOutlinedIcon']/parent::button/../h3")
    SELECTED_END_USER_CONTACT_NAME = (By.XPATH, "//*[@data-testid='EditOutlinedIcon']/parent::button/parent::div/../h6")
    SELECTED_END_USER_PHONE_NUMBER = (
        By.XPATH, "//*[@data-testid='EditOutlinedIcon']/parent::button/parent::div/../p[1]")
    SELECTED_END_USER_EMAIL = (By.XPATH, "//*[@data-testid='EditOutlinedIcon']/parent::button/parent::div/../p[2]")
    SELECTED_END_USER_ADDRESS_1 = (By.XPATH, "//*[@data-testid='EditOutlinedIcon']/parent::button/parent::div/../p[3]")
    SELECTED_END_USER_ADDRESS_2 = (By.XPATH, "//*[@data-testid='EditOutlinedIcon']/parent::button/parent::div/../p[7]")
    SELECTED_END_USER_ID = (By.XPATH, "//*[@data-testid='EditOutlinedIcon']/parent::button/parent::div/../p[9]")
    END_USER_COMPANY_NAME = (By.XPATH, "//*[text()='Company name:']/parent::div/div[@class='fieldValue']/strong")
    END_USER_CONTACT_NAME = (By.XPATH, "//*[text()='Contact:']/parent::div/div[@class='fieldValue']/strong")
    END_USER_EMAIL = (By.XPATH, "//*[text()='Email:']/parent::div/div[@class='fieldValue']/strong")
    END_USER_PHONE_NUMBER = (By.XPATH, "//*[text()='Phone Number:']/parent::div/div[@class='fieldValue']/strong")
    END_USER_ADDRESS_1 = (By.XPATH, "//*[text()='Address:']/parent::div/div/p[1]")
    END_USER_ADDRESS_2 = (By.XPATH, "//*[text()='Address:']/parent::div/div/p[5]")
    END_USER_ID = (By.XPATH, "//*[text()='End User ID(Suffix):']/parent::div/following-sibling::div/strong")
    EDIT_END_USER_CANCEL_BUTTON = (By.XPATH, "//*[text()='Add']/preceding::button[1][text()='Cancel']")
    ADDITIONAL_INFO_EDIT_BUTTON = (
        By.XPATH, "//*[text()='Additional info']/parent::div/*[@data-testid='ModeEditOutlineOutlinedIcon']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    EDIT_END_USER_CONTACT_NAME_REQUIRED_MESSAGE = (By.XPATH, "//*[text()='Name']/following-sibling::span")
    EDIT_END_USER_PHONE_NUMBER_REQUIRED_MESSAGE = (By.XPATH, "//*[text()='Phone Number']/following-sibling::span")
    EDIT_END_USER_EMAIL_REQUIRED_MESSAGE = (By.XPATH, "//*[text()='Email']/following-sibling::span")

    """Add New End User"""

    EDIT_ADD_NEW_END_USER_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseOutlinedIcon']/parent::button/../p")
    ADD_NEW_END_USER_ClOSE_ICON_BUTTON = (By.XPATH, "//*[@data-testid='CloseOutlinedIcon']")
    ADD_NEW_END_USER_CANCEL_BUTTON = (By.XPATH, "//*[@data-testid='CloseOutlinedIcon']/../../../div[3]/button[1]")
    ADD_NEW_END_USER_COMPANY_NAME_LABEL = (By.XPATH, "//*[text()='Company Name']")
    ADD_NEW_END_USER_COMPANY_NAME_TEXTBOX = (
        By.XPATH, "//*[text()='Company Name']/following-sibling::div/input[@placeholder='Enter company name']")
    ADD_NEW_END_USER_CUSTOMER_TYPE_LABEL = (By.XPATH, "//*[text()='Customer type']")
    ADD_NEW_END_USER_CUSTOMER_TYPE_DROPDOWN = (
        By.XPATH, "//*[text()='Customer type']/following-sibling::div/div[@id='customerType']")
    ADD_NEW_END_USER_CUSTOMER_TYPE_LIST = (By.XPATH, "//div[@role='presentation']/div/ul[@role='listbox']/li")
    ADD_NEW_END_USER_SELECT_COMMERCIAL_TYPE = (
        By.XPATH, "//div[@role='presentation']/div/ul[@role='listbox']/li[text()='COMMERCIAL']")
    ADD_NEW_END_USER_CONTACT_NAME_LABEL = (By.XPATH, "//*[text()='Contact Name']")
    ADD_NEW_END_USER_CONTACT_NAME_TEXTBOX = (
        By.XPATH, "//*[text()='Contact Name']/following-sibling::div/input[@placeholder='Enter contact name']")
    ADD_NEW_END_USER_EMAIL_LABEL = (By.XPATH, "//*[text()='Email']")
    ADD_NEW_END_USER_EMAIL_TEXTBOX = (
        By.XPATH, "//*[text()='Email']/following-sibling::div/input[@placeholder='Enter email']")
    ADD_NEW_END_USER_PHONE_NUMBER_LABEL = (By.XPATH, "//*[text()='Phone Number']")
    ADD_NEW_END_USER_PHONE_NUMBER_TEXTBOX = (
        By.XPATH, "//*[text()='Phone Number']/following-sibling::div/input[@placeholder='Enter  phone number']")
    ADD_NEW_END_USER_ADDRESS_LINE_1_LABEL = (By.XPATH, "//*[text()='Address Line 1']")
    ADD_NEW_END_USER_ADDRESS_LINE_1_TEXTBOX = (
        By.XPATH, "//*[text()='Address Line 1']/following-sibling::div/input[@placeholder='Enter adress line 1']")
    ADD_NEW_END_USER_ADDRESS_LINE_2_LABEL = (By.XPATH, "//*[text()='Address Line 2']")
    ADD_NEW_END_USER_ADDRESS_LINE_2_TEXTBOX = (
        By.XPATH, "//*[text()='Address Line 2']/following-sibling::div/input[@placeholder='Enter adress line 2']")
    ADD_NEW_END_USER_CITY_LABEL = (By.XPATH, "//*[text()='City']")
    ADD_NEW_END_USER_CITY_TEXTBOX = (
        By.XPATH, "//*[text()='City']/following-sibling::div/input[@placeholder='Enter city']")
    ADD_NEW_END_USER_STATE_LABEL = (By.XPATH, "//*[text()='State']")
    ADD_NEW_END_USER_STATE_DROPDOWN = (
        By.XPATH, "//*[text()='State']/following-sibling::div/div[text()='Select state']")
    ADD_NEW_END_USER_COUNTRY_LABEL = (By.XPATH, "//*[text()='Country']")
    ADD_NEW_END_USER_COUNTRY_DROPDOWN = (
        By.XPATH, "//*[text()='Country']/following-sibling::div/div[text()='Select country']")
    ADD_NEW_END_USER_ZIP_CODE_LABEL = (By.XPATH, "//*[text()='Zip Code']")
    ADD_NEW_END_USER_ZIP_CODE_TEXTBOX = (
        By.XPATH, "//*[text()='Zip Code']/following-sibling::div/input[@placeholder='Enter zip code']")
    SELECT_UNITED_STATE = (By.XPATH, "//*[text()='United States']")
    SELECT_STATE_CALIFORNIA = (By.XPATH, "//*[text()='California']")
    ADD_NEW_END_USER_ADD_BUTTON = (By.XPATH, "//*[@data-testid='CloseOutlinedIcon']/../../../div[3]/button[2]")
    USER_ADDED_SUCCESSFUL_MESSAGE = (
        By.XPATH, "//*[@data-testid='SuccessOutlinedIcon']/parent::div/following-sibling::div[1]")
    BILLING_AND_TECHNICAL_CONTACT_CHECKED_AND_DISABLED = (By.XPATH,
                                                          "//*[text()='The billing & technical contact is the same as the primary contact']/parent::label/span/input[@checked and @disabled]")
    BILLING_AND_TECHNICAL_CONTACT_CHECKBOX = (
        By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div[2]/div/label/span[1]/input")
    BILLING_AND_TECHNICAL_CONTACT_UNCHECK_CHECKBOX = (By.XPATH, "//*[@data-testid='CheckBoxOutlineBlankIcon']")

    """Billing Address"""

    BILLING_ADDRESS_EDIT_BUTTON = (
        By.XPATH, "//*[text()='Billing address']/parent::div/*[@data-testid='ModeEditOutlineOutlinedIcon']")
    EDIT_BILLING_ADDRESS_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/h2")
    EDIT_BILLING_ADDRESS_SEARCH_AREA_WITH_PLACEHOLDER = (By.XPATH, "//*[@placeholder='Search Suffix']")
    EDIT_BILLING_ADDRESS_POPUP_CLOSE_ICON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    EDIT_BILLING_ADDRESS_POPUP_DISABLED_SAVE_BUTTON = (By.XPATH, "//*[text()='Save' and @disabled]")
    EDIT_BILLING_ADDRESS_POPUP_CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    BILLING_ADDRESS_NO_RECORDS_FOUND_MESSAGE = (
        By.XPATH, "//*[text()='No records found matching your search criteria']")
    BILLING_ADDRESS_SUFFIX = (By.XPATH, "//*[@aria-labelledby='Selected-card-group-label']//div/div/div[5]/p")
    EDIT_BILLING_ADDRESS_POPUP_ENABLED_SAVE_BUTTON = (By.XPATH, "//*[text()='Save']")
    SELECTED_BILLING_ADDRESS_NAME = (
        By.XPATH, "//*[@aria-labelledby='Selected-card-group-label']//div/div/div/div/div[1]/h3")
    SELECTED_BILLING_ADDRESS = (By.XPATH, "//*[@aria-labelledby='Selected-card-group-label']//div/div/div/div/div[2]/p")
    SELECTED_BILLING_ADDRESS_COUNTRY = (
        By.XPATH, "//*[@aria-labelledby='Selected-card-group-label']//div/div/div/div/div[3]/p")
    SELECTED_BILLING_ADDRESS_PHONE_NUMBER = (
        By.XPATH, "//*[@aria-labelledby='Selected-card-group-label']//div/div/div/div/div[4]/p")
    SELECTED_BILLING_ADDRESS_SUFFIX = (
        By.XPATH, "//*[text()='Billing address']/parent::div/following-sibling::div/div[1]/div[2]")
    BILLING_ADDRESS_NAME = (
        By.XPATH, "//*[text()='Billing address']/parent::div/following-sibling::div/div[2]/div[1]/strong")
    BILLING_ADDRESS = (By.XPATH, "//*[text()='Billing address']/parent::div/following-sibling::div/div[2]/div[5]")

    """Order Lines Tab"""

    ORDER_LINE_TAB = (By.XPATH, "//div[text()='Order lines']")
    ORDER_LINE_REMOVE_ICON = (By.XPATH, "//div[@data-id='1']/div[2]/button/*[@data-testid='MoreVertOutlinedIcon']")
    ORDER_LINE_MARK_FOR_CANCEL_OPTION = (By.XPATH, "//*[text()='Mark for cancel']")
    GRAY_OUT_ORDER_LINE = (By.XPATH, "//*[@class='custom-selected-row MuiDataGrid-row']")
    ORDER_LINE_UNMARK_FOR_CANCEL_OPTION = (By.XPATH, "//*[text()='Unmark for cancel']")
    ORDER_LINE_ENABLE = (By.XPATH, "//*[@class='MuiDataGrid-row']")
    RESUBMIITED_ORDER_SUCCESSFULLY = (By.XPATH, "//div[text()='Order has been successfully resubmitted.']")
    MARK_FOR_DROPDOWN = (By.XPATH, "//*[@id='newOptions']")
    ORDER_LINE_ENABLED = (By.XPATH, "//*[@class='MuiDataGrid-row Mui-selected']")
    AT_LEAST_ONE_ORDER_LINE_REQUIRED_MESSAGE = (
        By.XPATH, "//div[text()='At least one order line is required to resubmit the order']")
    ORDER_LINE_EDIT_ICON = (By.XPATH, "//div[@data-id='1']/div[2]/button/*[@data-testid='EditOutlinedIcon']")
    ORDER_LINE_UPDATE_ICON = (By.XPATH, "//*[@data-testid='CheckCircleOutlineOutlinedIcon']")
    ORDER_LINE_CANCEL_ICON = (By.XPATH, "//*[@data-testid='ClearOutlinedIcon']")
    ORDER_LINE_EDIT_QUANTITY_FIELD = (By.XPATH, "//*[@data-field='quantity']/div/div/input")
    ORDER_LINE_EDIT_RESELLER_PRICE_FIELD = (By.XPATH, "//*[@data-field='resellerPrice']/div/div/input")
    ORDER_LINE_EDIT_END_USER_PRICE_FIELD = (By.XPATH, "//*[@data-field='endUserPrice']/div/div/input")
    ORDER_LINE_EDIT_END_USER_PO_FIELD = (By.XPATH, "//*[@data-field='endUserPoNumber']/div/div/input")
    ORDER_LINE_QUANTITY_FIELD_TEXT = (By.XPATH, "//div[@data-id='1']//*[@data-field='quantity']/div")
    ORDER_LINE_RESELLER_PRICE_FIELD_TEXT = (By.XPATH, "//div[@data-id='1']//*[@data-field='resellerPrice']/div")
    ORDER_LINE_END_USER_PRICE_FIELD_TEXT = (By.XPATH, "//div[@data-id='1']//*[@data-field='endUserPrice']/div")
    ORDER_LINE_END_USER_PO_FIELD_TEXT = (By.XPATH, "//div[@data-id='1']//*[@data-field='endUserPoNumber']/div")
    ORDER_DETAILS_TAB = (By.XPATH, "//div[text()='Order details']")
    OPERATOR_ID = (By.XPATH, "//*[text()='Operator ID']/parent::div")
    CHANNEL_LABEL = (By.XPATH, "//div[text()='Channel']")
    LISTING_PAGE_CHANNEL_NAME = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='channel']")
    ORDER_DEATILS_PAGE_CHANNEL_NAME = (By.XPATH, "//*[text()='Channel']/parent::div")

    """Shipping Details"""

    SHIPPING_DETAILS_SECTION = (By.XPATH, "//div[text()='Shipping Details']")
    SHIPPING_DETAILS_CARRIER_CODE_LABEL = (By.XPATH, "//div[text()='Carrier code:']")
    SHIPPING_DETAILS_FREIGHT_ACCOUNT_NUMBER_LABEL = (By.XPATH, "//div[text()='Freight account number:']")
    SHIPPING_DETAILS_SHIPMENT_COMPLETE_LABEL = (By.XPATH, "//div[text()='Shipment complete:']")
    SHIPPING_DETAILS_REQUESTED_DELIVER_YDATE_LABEL = (By.XPATH, "//div[text()='Requested delivery date:']")
    SHIPPING_DETAILS_SIGNATURE_REQUIRED_LABEL = (By.XPATH, "//div[text()='Signature required:']")
    SHIPPING_DETAILS_CARRIER_SERVICE_LABEL = (By.XPATH, "//div[text()='Carrier service:']")

    """Shipping Address"""

    SHIPPING_ADDRESS_EDIT_BUTTON = (
        By.XPATH, "//*[text()='Shipping address']/parent::div/*[@data-testid='ModeEditOutlineOutlinedIcon']")
    EDIT_SHIPPING_ADDRESS_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseIcon']/parent::div/h2")
    EDIT_SHIPPING_ADDRESS_SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search Company']")
    EDIT_SHIPPING_ADDRESS_POPUP_CLOSE_ICON = (By.XPATH, "//*[@data-testid='CloseIcon']")
    EDIT_SHIPPING_ADDRESS_POPUP_DISABLED_SAVE_BUTTON = (By.XPATH, "//*[text()='Save' and @disabled]")
    EDIT_SHIPPING_ADDRESS_POPUP_CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    SEARCHED_SHIPPING_ADDRESS_TITLE_LIST = (
        By.XPATH, "//*[@aria-labelledby='Selected-card-group-label']/div/div/div/div/div[2]/h6")
    ADD_NEW_SHIPPING_ADDRESS_BUTTON = (By.XPATH, "//*[text() ='Add new Shipping address']")
    ADD_NEW_SHIPPING_ADDRESS_POPUP_TITLE = (By.XPATH, "//*[@data-testid='CloseOutlinedIcon']/parent::button/../p")
    ADD_NEW_SHIPPING_ADDRESS_COMPANY_NAME_TEXTBOX = (
        By.XPATH, "//*[text()='Company Name']/following-sibling::div/input[@placeholder='Enter company name']")
    ADD_NEW_SHIPPING_ADDRESS_CONTACT_NAME = (
        By.XPATH, "//*[text()='Contact Name ']/following-sibling::div/input[@placeholder='Enter contact name']")
    ADD_NEW_SHIPPING_ADDRESS_EMAIL = (
        By.XPATH, "//*[text()='Email']/following-sibling::div/input[@placeholder='Enter email']")
    ADD_NEW_SHIPPING_ADDRESS_PHONE_NUMBER = (
        By.XPATH, "//*[text()='Phone Number']/following-sibling::div/input[@placeholder='Enter phone number']")
    ADD_NEW_SHIPPING_ADDRESS_LINE_1 = (
        By.XPATH, "//*[text()='Address Line 1']/following-sibling::div/input[@placeholder='Enter adress line 1']")
    ADD_NEW_SHIPPING_ADDRESS_LINE_2 = (
        By.XPATH, "//*[text()='Address Line 2']/following-sibling::div/input[@placeholder='Enter adress line 2']")
    ADD_NEW_SHIPPING_ADDRESS_CITY = (
        By.XPATH, "//*[text()='City']/following-sibling::div/input[@placeholder='Enter city']")
    ADD_NEW_SHIPPING_ADDRESS_STATE_DROPDOWN = (
        By.XPATH, "//*[text()='State']/following-sibling::div/div[text()='Select state']")
    ADD_NEW_SHIPPING_ADDRESS_COUNTRY_DROPDOWN = (By.XPATH, "//*[text()='Country']/following-sibling::div/div")
    ADD_NEW_SHIPPING_ADDRESS_ZIP_CODE = (
        By.XPATH, "//*[text()='Zip Code']/following-sibling::div/input[@placeholder='Enter zip code']")
    ADD_NEW_SHIPPING_ADDRESS_ADD_ENABLED_BUTTON = (By.XPATH, "//button[text()='Add']")
    ADD_NEW_SHIPPING_ADDRESS_CANCEL_BUTTON = (By.XPATH, "/html/body/div[3]/div[3]/div[3]/button[text()='Cancel']")
    ADD_NEW_SHIPPING_ADDRESS_CLOSE_BUTTON = (
        By.XPATH, "//*[text()='Add New Shipping Address']/parent::div/button/*[@data-testid='CloseOutlinedIcon']")
    SHIPPING_ADDRESS_COMPANY_NAME = (By.XPATH, "//*[@class='shippingAddress']/div/div[2]/div[1]/strong")
    SHIPPING_ADDRESS_CONTACT_NAME = (By.XPATH, "//*[@class='shippingAddress']/div/div[2]/div[2]/strong")
    SHIPPING_ADDRESS_PHONE_NUMBER = (By.XPATH, "//*[@class='shippingAddress']/div/div[2]/div[3]")
    SHIPPING_ADDRESS_LINE_1 = (By.XPATH, "//*[@class='shippingAddress']/div/div[2]/div[5]")
    SHIPPING_ADDRESS_LINE_2 = (By.XPATH, "//*[@class='shippingAddress']/div/div[2]/div[6]")
    RESUBMIT_ORDER_MSG = (By.XPATH, "//*[text()='Resubmit Order']/parent::div/following-sibling::div[2]")
    RESUBMIT_ORDER_CANCEL_ORDER_BUTTON = (
        By.XPATH, "//*[text()='Resubmit Order']/parent::div/following-sibling::div//*[text()='Cancel Order']")
    RESUBMIT_ORDER_PROCEED_BUTTON = (
        By.XPATH, "//*[text()='Resubmit Order']/parent::div/following-sibling::div//*[text()='Proceed']")
    RESUBMIT_ORDER_HEADER_MSG = (By.XPATH, "//*[text()='Resubmit Order']/parent::div/following-sibling::div[1]/div/div")

    """Add Order Line"""

    ADD_ORDER_LINE_BUTTON = (
        By.XPATH, "//*[@id='OrderDetails']/div/div[1]/div[1]/div[2]/button[text()='Add order line']")
    NEW_ORDER_LINE_POPUP = (By.XPATH, "//*[text()='New order line']")
    NEW_ORDER_LINE_IM_PART_NO_TEXTBOX = (By.XPATH, "//input[@placeholder='Add IMP']")
    NEW_ORDER_LINE_QTY_TEXTBOX = (By.XPATH, "//input[@placeholder='Add Qty']")
    NEW_ORDER_LINE_PRICE_TEXTBOX = (By.XPATH, "//input[@placeholder='Add price']")
    NEW_ORDER_LINE_VALIDATE_BUTTON = (By.XPATH, "//button[text()='Validate']")
    NEW_ORDER_LINE_CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    ADD_NEW_LINE_ADD_BUTTON = (By.XPATH, "//button[text()='Add']")

    def go_to_order_exception(self):
        try:
            self.do_click_by_locator(self.SALES_MENU)
            self.logger.info("Clicked on Order in the menu")
            self.do_double_click(self.ORDER_EXCEPTION_OPTION)
            self.logger.info("Clicked on Order Exception option")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Order Exception ' + str(e))
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
            self.go_to_order_exception()
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
            self.logger.error('Exception occurred while clicking on cancel button ' + str(e))
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
            assert 'Order Exception' in self.get_element_text(
                self.ORDER_EXCEPTION_TEXT), "Cancel Order Title not present"
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
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
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
            self.logger.error('Exception occurred while clicking on Reprocess Order button ' + str(e))
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
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
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
            self.logger.error('Exception occurred while clicking on Cancel Order button ' + str(e))
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
            for retry in range(3):
                self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
                time.sleep(5)
                if self.do_check_visibility(self.FRAUD_FIRST_RECORD):
                    break
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
            self.logger.error('Exception occurred while clicking on Resubmit Order button ' + str(e))
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
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            self.logger.info("Order reprocessed successfully")
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
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
            time.sleep(5)
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
            if "End Customer order number is invalid" in end_customer_order_invalid_message:
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
                self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
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
            # self.do_check_visibility(self.HEADER_CLEAR_ALL_BUTTON)
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
            self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
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
            is_visible = self.do_check_visibility(self.NO_FAILED_ORDER_FOUND_MESSAGE)
            if is_visible:
                self.logger.info("Successfully verify updated grid as per country")
            else:
                self.driver.execute_script(
                    "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

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
                self.logger.info(f'Total number of Country  count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate country")
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
                self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_end_user_details_edit_icon(self):
        try:
            time.sleep(3)
            self.do_check_availability(self.END_USER_DETAILS_EDIT_BUTTON)
            self.do_check_availability(self.ADDITIONAL_INFO_EDIT_BUTTON)
            self.do_check_visibility(self.END_USER_DETAILS_EDIT_BUTTON)
            return True
        except Exception as e:
            return False

    def verify_contents_of_edit_end_user_details(self):
        try:
            self.do_click_by_locator(self.END_USER_DETAILS_EDIT_BUTTON)
            edit_end_user_details_title = 'Edit end user details'
            edit_end_user_details_cancel_button = 'Cancel'
            edit_end_user_details_save_button = 'Save'

            assert edit_end_user_details_title in self.get_element_text(
                self.EDIT_END_USER_DETAILS_POPUP_TITLE), "Edit End User Details Title not present"

            cancel = self.get_element_text(self.END_USER_DETAILS_CANCEL_BUTTON)
            assert edit_end_user_details_cancel_button in self.get_element_text(
                self.END_USER_DETAILS_CANCEL_BUTTON), "End User CANCEL button is not present"

            assert edit_end_user_details_save_button in self.get_element_text(
                self.END_USER_DETAILS_SAVE_BUTTON), "End User SAVE button is not present"

            self.do_check_visibility(self.END_USER_DETAILS_ClOSE_ICON_BUTTON)
            self.do_check_visibility(self.END_USER_SEARCH_BOX)
            self.do_check_visibility(self.ADD_NEW_END_USER_LINK)
            self.logger.info(
                "Successfully verified Edit END User Details Popup title, CANCEL, SAVE button, X icon, Search box, Add new end user link on popup")
            return True
        except Exception as e:
            return False

    def do_verify_all_addr_matching_with_entered_text(self):
        try:
            time.sleep(3)
            count = 0
            search_text = "test"
            self.do_clear_textfield(self.END_USER_SEARCH_BOX)
            self.do_send_keys(self.END_USER_SEARCH_BOX, search_text)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            end_user_title_list = self.get_all_elements(self.SEARCHED_END_USER_TITLE_LIST)
            for element in range(len(end_user_title_list)):
                end_user_title = end_user_title_list[element].text
                print(end_user_title.lower())
                title = end_user_title.lower()
                if search_text in title:
                    self.logger.info(f'Searching End User {title} match with search text')
                    count = count + 1
                if count == len(end_user_title_list):
                    return True
        except Exception as e:
            return False

    def do_verify_edit_button_and_save_button_enable(self, end_user_with_suffix):
        try:
            self.do_clear_textfield(self.END_USER_SEARCH_BOX)
            self.do_send_keys(self.END_USER_SEARCH_BOX, end_user_with_suffix)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(5)
            element = "/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div/div/div[1]/span/input"
            search_end_user_with_suffix = self.driver.find_element(By.XPATH, element)
            search_end_user_with_suffix.click()
            self.do_check_visibility(self.SELECTED_END_USER_EDIT_BUTTON)
            self.do_check_visibility(self.SAVE_BUTTON_ENABLE)
            return True
        except Exception as e:
            return False

    def do_verify_selected_end_user_info_on_order_details_page(self):
        try:
            selected_end_user_company_name = self.get_element_text(self.SELECTED_END_USER_COMPANY_NAME)
            selected_end_user_contact = self.get_element_text(self.SELECTED_END_USER_CONTACT_NAME)
            selected_end_user_email = self.get_element_text(self.SELECTED_END_USER_EMAIL)
            selected_end_user_phone_no = self.get_element_text(self.SELECTED_END_USER_PHONE_NUMBER)
            selected_end_user_addr1 = self.get_element_text(self.SELECTED_END_USER_ADDRESS_1)
            selected_end_user_addr2 = self.get_element_text(self.SELECTED_END_USER_ADDRESS_2)
            selected_end_user_id = self.get_element_text(self.SELECTED_END_USER_ID)
            selected_end_ur_id = selected_end_user_id.replace("Suffix : ", "")

            self.do_click_by_locator(self.SAVE_BUTTON_ENABLE)

            end_user_company_name = self.get_element_text(self.END_USER_COMPANY_NAME)
            end_user_contact = self.get_element_text(self.END_USER_CONTACT_NAME)
            end_user_email = self.get_element_text(self.END_USER_EMAIL)
            end_user_phone_no = self.get_element_text(self.END_USER_PHONE_NUMBER)
            end_user_addr1 = self.get_element_text(self.END_USER_ADDRESS_1)
            end_user_addr2 = self.get_element_text(self.END_USER_ADDRESS_2)
            end_user_id = self.get_element_text(self.END_USER_ID)

            if ((selected_end_user_company_name == end_user_company_name) & (
                    selected_end_user_contact == end_user_contact) &
                    (selected_end_user_email == end_user_email) & (selected_end_user_phone_no == end_user_phone_no) &
                    (selected_end_user_addr1 == end_user_addr1) & (selected_end_user_addr2 == end_user_addr2) &
                    (selected_end_ur_id == end_user_id)):
                self.logger.info(
                    "Successfully Verified selected end user information should get displayed on order details page")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_contents_of_selected_end_user_with_suffix_edit_popup(self):
        try:
            self.do_click_by_locator(self.SELECTED_END_USER_EDIT_BUTTON)
            self.do_check_visibility(self.READ_ONLY_END_USER_ID_SUFFIX)
            self.do_check_visibility(self.READY_ONLY_COMPANY_NAME)
            self.do_check_visibility(self.NAME_TEXTBOX)
            self.do_check_visibility(self.PHONE_NUMBER_TEXTBOX)
            self.do_check_visibility(self.EMAIL_TEXTBOX)
            self.do_check_visibility(self.READ_ONLY_ADDRESS_LINE_1)
            self.do_check_visibility(self.READ_ONLY_ADDRESS_LINE_2)
            self.do_check_visibility(self.READ_ONLY_CITY)
            self.do_check_visibility(self.READ_ONLY_STATE)
            self.do_check_visibility(self.READ_ONLY_ZIP_CODE)
            self.do_check_visibility(self.READ_ONLY_COUNTRY)
            self.do_check_availability(self.DEFAULT_SELECTED_THE_CHECKBOX_BILLING_AND_TECHNICAL_CONTACT)
            return True
        except Exception as e:
            return False

    def do_validate_message_for_mandatory_fields(self):
        try:
            self.do_clear_textfield(self.NAME_TEXTBOX)
            self.do_send_keys(self.NAME_TEXTBOX, '')

            self.do_clear_textfield(self.PHONE_NUMBER_TEXTBOX)
            self.do_send_keys(self.PHONE_NUMBER_TEXTBOX, '')

            self.do_clear_textfield(self.EMAIL_TEXTBOX)
            self.do_send_keys(self.EMAIL_TEXTBOX, '')

            time.sleep(3)
            self.do_click_by_locator(self.ADD_BUTTON)

            contact_name_required_message = "Please enter a Contact name"
            phone_number_required_message = "Please enter a Phone Number"
            email_required_message = "Please enter a Valid Email Address"

            assert contact_name_required_message in self.get_element_text(
                self.EDIT_END_USER_CONTACT_NAME_REQUIRED_MESSAGE), "Please enter a Contact name message not present"

            assert phone_number_required_message in self.get_element_text(
                self.EDIT_END_USER_PHONE_NUMBER_REQUIRED_MESSAGE), "Please enter a Phone Number message not present"

            assert email_required_message in self.get_element_text(
                self.EDIT_END_USER_EMAIL_REQUIRED_MESSAGE), "Please enter a Valid Email Address message not present"

            self.do_click_by_locator(self.EDIT_END_USER_CANCEL_BUTTON)
            return True
        except Exception as e:
            return False

    def do_verify_modified_end_user_info_on_order_details_page(self, end_user):
        try:
            self.do_click_by_locator(self.END_USER_DETAILS_EDIT_BUTTON)
            self.do_clear_textfield(self.END_USER_SEARCH_BOX)
            self.do_send_keys(self.END_USER_SEARCH_BOX, end_user)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(5)
            element = "/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div/div/div[1]/span/input"
            search_end_user = self.driver.find_element(By.XPATH, element)
            search_end_user.click()
            self.do_click_by_locator(self.SELECTED_END_USER_EDIT_BUTTON)

            char_count = 3
            modified_name = "Testing" + ''.join(random.choices(string.ascii_lowercase, k=char_count))
            print("The randomly generated string is : " + str(modified_name))  # print the random data
            self.do_send_keys(self.NAME_TEXTBOX, modified_name)

            num_count = 10
            modified_phone_number = ''.join(random.choices(string.digits, k=num_count))
            print("The randomly generated number is : " + str(modified_phone_number))  # print the random data
            self.do_send_keys(self.PHONE_NUMBER_TEXTBOX, modified_phone_number)

            alphabet_count = 5
            modified_email = "test." + ''.join(
                random.choices(string.ascii_lowercase, k=alphabet_count)) + "@ingrammicro.com"
            print("The randomly generated String is : " + str(modified_email))  # print the random data
            self.do_send_keys(self.EMAIL_TEXTBOX, modified_email)

            self.do_click_by_locator(self.ADD_BUTTON)

            self.do_click_by_locator(self.SAVE_BUTTON_ENABLE)

            end_user_contact = self.get_element_text(self.END_USER_CONTACT_NAME)
            end_user_email = self.get_element_text(self.END_USER_EMAIL)
            end_user_phone_no = self.get_element_text(self.END_USER_PHONE_NUMBER)

            if ((modified_name == end_user_contact) &
                    (modified_email == end_user_email) & (modified_phone_number == end_user_phone_no)):
                self.logger.info(
                    "Successfully Verified Modified end user information should get displayed on order details page")
                return True
            else:
                return False
        except Exception as e:
            return False

    def verify_contents_of_edit_add_new_end_user(self):
        try:
            self.do_click_by_locator(self.END_USER_DETAILS_EDIT_BUTTON)
            self.do_click_by_locator(self.ADD_NEW_END_USER_LINK)
            edit_add_new_end_user_title = 'Add New End User'
            edit_add_new_end_user_cancel_button = 'Cancel'
            edit_add_new_end_user_add_button = 'Add'

            assert edit_add_new_end_user_title in self.get_element_text(
                self.EDIT_ADD_NEW_END_USER_POPUP_TITLE), "Edit Add New End User Title not present"

            assert edit_add_new_end_user_cancel_button in self.get_element_text(
                self.ADD_NEW_END_USER_CANCEL_BUTTON), "Add New End User CANCEL button is not present"

            assert edit_add_new_end_user_add_button in self.get_element_text(
                self.ADD_BUTTON), "Add New End User Add button is not present"

            self.do_check_visibility(self.ADD_NEW_END_USER_ClOSE_ICON_BUTTON)

            self.do_check_visibility(self.ADD_NEW_END_USER_COMPANY_NAME_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_COMPANY_NAME_TEXTBOX)

            self.do_check_visibility(self.ADD_NEW_END_USER_CUSTOMER_TYPE_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_CUSTOMER_TYPE_DROPDOWN)

            self.do_check_visibility(self.ADD_NEW_END_USER_CONTACT_NAME_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_CONTACT_NAME_TEXTBOX)

            self.do_check_visibility(self.ADD_NEW_END_USER_EMAIL_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_EMAIL_TEXTBOX)

            self.do_check_visibility(self.ADD_NEW_END_USER_PHONE_NUMBER_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_PHONE_NUMBER_TEXTBOX)

            self.do_check_visibility(self.ADD_NEW_END_USER_ADDRESS_LINE_1_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_ADDRESS_LINE_1_TEXTBOX)

            self.do_check_visibility(self.ADD_NEW_END_USER_ADDRESS_LINE_2_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_ADDRESS_LINE_2_TEXTBOX)

            self.do_check_visibility(self.ADD_NEW_END_USER_CITY_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_CITY_TEXTBOX)

            self.do_check_visibility(self.ADD_NEW_END_USER_STATE_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_STATE_DROPDOWN)

            self.do_check_visibility(self.ADD_NEW_END_USER_COUNTRY_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_COUNTRY_DROPDOWN)

            self.do_check_visibility(self.ADD_NEW_END_USER_ZIP_CODE_LABEL)
            self.do_check_visibility(self.ADD_NEW_END_USER_ZIP_CODE_TEXTBOX)

            self.logger.info(
                "Successfully verified Edit Add New End User Details Popup content")
            return True
        except Exception as e:
            return False

    def verify_customer_type_option_list(self):
        try:
            self.do_click_by_locator(self.ADD_NEW_END_USER_CUSTOMER_TYPE_DROPDOWN)
            customer_type_list = ['COMMERCIAL', 'LOCAL', 'FEDERAL', 'HIGHER EDUCATION', 'INTERNET SERVICE PROVIDER',
                                  'K - 12', 'STATE', 'TELECOM', 'TEACHING HOSPITALS',
                                  'DOCTOR’S OFFICES', 'PUBLIC HOSPITALS', 'NON-PROFIT', 'PRIVATE HOSPITALS']
            customer_type_option_list = self.get_all_elements_without_visibility(
                self.ADD_NEW_END_USER_CUSTOMER_TYPE_LIST)
            option_list = []
            for element in customer_type_option_list:
                self.logger.info(element.text)
                text = element.text
                option_list.append(text)
            option_list.pop(0)
            self.logger.info(option_list)
            result = all(elem in customer_type_list for elem in option_list)
            if result:
                self.logger.info("Successfully verified Customer Type options list")
                self.do_click_by_locator(self.ADD_NEW_END_USER_SELECT_COMMERCIAL_TYPE)
                return True
            else:
                self.logger.info("Failed to verify Customer Type options list")
                return False
        except Exception as e:
            return False

    def do_verify_add_new_user_with_valid_data(self):
        try:
            company_name = "Automation " + ''.join(random.choices(string.ascii_lowercase, k=3))
            print("The randomly generated string is : " + str(company_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_END_USER_COMPANY_NAME_TEXTBOX, company_name)

            contact_name = "Test " + ''.join(random.choices(string.ascii_lowercase, k=2))
            print("The randomly generated number is : " + str(contact_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_END_USER_CONTACT_NAME_TEXTBOX, contact_name)

            modified_email = "test." + ''.join(random.choices(string.ascii_lowercase, k=5)) + "@ingrammicro.com"
            print("The randomly generated String is : " + str(modified_email))  # print the random data
            self.do_send_keys(self.ADD_NEW_END_USER_EMAIL_TEXTBOX, modified_email)

            phone_number = ''.join(random.choices(string.digits, k=10))
            print("The randomly generated number is : " + str(phone_number))  # print the random data
            self.do_send_keys(self.ADD_NEW_END_USER_PHONE_NUMBER_TEXTBOX, phone_number)

            self.do_send_keys(self.ADD_NEW_END_USER_ADDRESS_LINE_1_TEXTBOX, "A-202 4th floor")

            self.do_send_keys(self.ADD_NEW_END_USER_ADDRESS_LINE_2_TEXTBOX, "Wisconsin State Highways 29")

            self.do_send_keys(self.ADD_NEW_END_USER_CITY_TEXTBOX, "Slab City")

            self.do_click_by_locator(self.ADD_NEW_END_USER_COUNTRY_DROPDOWN)
            self.do_click_by_locator(self.SELECT_UNITED_STATE)

            self.do_click_by_locator(self.ADD_NEW_END_USER_STATE_DROPDOWN)
            time.sleep(2)
            self.do_click_by_locator(self.SELECT_STATE_CALIFORNIA)

            self.do_send_keys(self.ADD_NEW_END_USER_ZIP_CODE_TEXTBOX, "92233")

            self.do_click_by_locator(self.ADD_NEW_END_USER_ADD_BUTTON)

            successful_msg = "User has been added successfully!"
            assert successful_msg in self.get_element_text(
                self.USER_ADDED_SUCCESSFUL_MESSAGE), "User has been added successfully! message not present"

            self.do_send_keys(self.END_USER_SEARCH_BOX, company_name)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(5)
            element = "/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div/div/div[1]/span/input"
            search_end_user = self.driver.find_element(By.XPATH, element)
            search_end_user.click()
            self.logger.info("Successfully User able to select end user")
            self.do_click_by_locator(self.SELECTED_END_USER_EDIT_BUTTON)
            self.do_check_availability(self.BILLING_AND_TECHNICAL_CONTACT_CHECKED_AND_DISABLED)
            self.logger.info(
                "Successfully Verified that the end user ERP type is I and The billing & technical contact is the same as the primary contact checkbox is Checked and Disabled")
            self.do_click_by_locator(self.EDIT_END_USER_CANCEL_BUTTON)
            self.do_click_by_locator(self.END_USER_DETAILS_ClOSE_ICON_BUTTON)
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            return True
        except Exception as e:
            return False

    def verify_contents_of_edit_billing_address(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.BILLING_SHIPPING_TAB)
            self.do_click_by_locator(self.BILLING_ADDRESS_EDIT_BUTTON)
            edit_billing_address_title = 'Edit Billing Address'

            assert edit_billing_address_title in self.get_element_text(
                self.EDIT_BILLING_ADDRESS_POPUP_TITLE), "Edit Billing Address Title not present"

            self.do_check_visibility(self.EDIT_BILLING_ADDRESS_SEARCH_AREA_WITH_PLACEHOLDER)
            self.do_check_visibility(self.EDIT_BILLING_ADDRESS_POPUP_CANCEL_BUTTON)
            self.do_check_visibility(self.EDIT_BILLING_ADDRESS_POPUP_CLOSE_ICON)
            self.do_check_visibility(self.EDIT_BILLING_ADDRESS_POPUP_DISABLED_SAVE_BUTTON)
            self.logger.info(
                "Successfully verified Edit Billing Address Popup title, Search Area with Placeholder, X icon, Cancel and Save Disabled button on popup")
            return True
        except Exception as e:
            return False

    def do_verify_order_details_page_after_click_on_x_icon(self):
        try:
            self.do_click_by_locator(self.EDIT_BILLING_ADDRESS_POPUP_CLOSE_ICON)
            self.do_check_visibility(self.ORDER_DETAILS_PAGE)
            return True
        except Exception as e:
            return False

    def do_verify_order_details_page_after_click_on_cancel_button(self):
        try:
            self.do_click_by_locator(self.BILLING_ADDRESS_EDIT_BUTTON)
            self.do_click_by_locator(self.EDIT_BILLING_ADDRESS_POPUP_CANCEL_BUTTON)
            self.do_check_visibility(self.ORDER_DETAILS_PAGE)
            return True
        except Exception as e:
            return False

    def do_search_with_special_character(self):
        try:
            self.do_click_by_locator(self.BILLING_ADDRESS_EDIT_BUTTON)
            self.do_click_by_locator(self.EDIT_BILLING_ADDRESS_SEARCH_AREA_WITH_PLACEHOLDER)
            self.do_send_keys(self.EDIT_BILLING_ADDRESS_SEARCH_AREA_WITH_PLACEHOLDER, '^%^&')
            self.do_check_visibility(self.BILLING_ADDRESS_NO_RECORDS_FOUND_MESSAGE)
            return True
        except Exception as e:
            return False

    def do_search_with_valid_suffix(self):
        try:
            suffix = '117'
            self.do_clear_textfield(self.EDIT_BILLING_ADDRESS_SEARCH_AREA_WITH_PLACEHOLDER)
            self.do_send_keys(self.EDIT_BILLING_ADDRESS_SEARCH_AREA_WITH_PLACEHOLDER, suffix)
            billing_add_suffix = self.get_element_text(self.BILLING_ADDRESS_SUFFIX)
            bill_addr_suffix = billing_add_suffix.replace("Suffix:\n", "")
            if suffix == bill_addr_suffix:
                self.logger.info("Successfully Billing Address Details get loaded in popup")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_select_searched_addr_and_save_button_enabled(self):
        try:
            time.sleep(5)
            element = "/html/body/div[2]/div[3]/div/div/div[3]/div/div/div/div/div/div/span/input"
            search_billing_address = self.driver.find_element(By.XPATH, element)
            search_billing_address.click()
            self.do_check_visibility(self.EDIT_BILLING_ADDRESS_POPUP_ENABLED_SAVE_BUTTON)
            return True
        except Exception as e:
            return False

    def do_verify_selected_billing_addr_on_order_details_page(self):
        try:
            selected_billing_addr_name = self.get_element_text(self.SELECTED_BILLING_ADDRESS_NAME)
            selected_address = self.get_element_text(self.SELECTED_BILLING_ADDRESS)
            selected_address_country = self.get_element_text(self.SELECTED_BILLING_ADDRESS_COUNTRY)
            selected_address_phone = self.get_element_text(self.SELECTED_BILLING_ADDRESS_PHONE_NUMBER)
            selected_suffix = self.get_element_text(self.BILLING_ADDRESS_SUFFIX)
            selected_bill_addr_suffix = selected_suffix.replace("Suffix:\n", "")

            self.do_click_by_locator(self.EDIT_BILLING_ADDRESS_POPUP_ENABLED_SAVE_BUTTON)

            selected_billing_address = selected_address + ' ' + selected_address_country
            self.logger.info(f'Billing Address: {selected_billing_address}')

            billing_address_suffix = self.get_element_text(self.SELECTED_BILLING_ADDRESS_SUFFIX)
            billing_address_name = self.get_element_text(self.BILLING_ADDRESS_NAME)
            billing_address = self.get_element_text(self.BILLING_ADDRESS)

            if (selected_bill_addr_suffix == billing_address_suffix) & (
                    selected_billing_addr_name == billing_address_name) & (
                    selected_billing_address in billing_address) & (selected_address_phone in billing_address):
                self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_order_line_remove_icon(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_LINE_TAB)
            self.do_check_visibility(self.ORDER_LINE_REMOVE_ICON)
            return True
        except Exception as e:
            return False

    def do_click_on_mark_for_cancel_and_line_not_editable(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_LINE_REMOVE_ICON)
            self.do_click_by_locator(self.ORDER_LINE_MARK_FOR_CANCEL_OPTION)
            self.do_check_visibility(self.GRAY_OUT_ORDER_LINE)
            return True
        except Exception as e:
            return False

    def do_click_on_unmark_for_cancel_and_line_is_editable(self):
        try:
            time.sleep(2)
            self.do_click_by_locator(self.ORDER_LINE_REMOVE_ICON)
            self.do_click_by_locator(self.ORDER_LINE_UNMARK_FOR_CANCEL_OPTION)
            self.do_check_visibility(self.ORDER_LINE_ENABLE)
            return True
        except Exception as e:
            return False

    def do_verify_order_resubmitted_successfully(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_LINE_REMOVE_ICON)
            self.do_click_by_locator(self.ORDER_LINE_MARK_FOR_CANCEL_OPTION)
            self.do_click_by_locator(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            self.do_click_by_locator(self.YES_RESUBMIT_ORDER_BUTTON)
            self.do_check_visibility(self.RESUBMIITED_ORDER_SUCCESSFULLY)
            return True
        except Exception as e:
            return False

    def do_click_on_mark_for_cancel_from_dropdown_and_line_grey_out(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_LINE_TAB)
            element = "//*[@id='tablayout-tabpanel-2']/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/span/input"
            order_line_checkbox = self.driver.find_element(By.XPATH, element)
            order_line_checkbox.click()
            self.do_click_by_locator(self.MARK_FOR_DROPDOWN)
            self.do_click_by_locator(self.ORDER_LINE_MARK_FOR_CANCEL_OPTION)
            self.do_check_visibility(self.GRAY_OUT_ORDER_LINE)
            return True
        except Exception as e:
            return False

    def do_click_on_unmark_for_cancel_from_dropdownn_and_line_get_unable(self):
        try:
            self.do_click_by_locator(self.MARK_FOR_DROPDOWN)
            self.do_click_by_locator(self.ORDER_LINE_UNMARK_FOR_CANCEL_OPTION)
            self.do_check_visibility(self.ORDER_LINE_ENABLE)
            return True
        except Exception as e:
            return False

    def do_verify_atleast_one_order_line_required_message(self):
        try:
            self.do_click_by_locator(self.MARK_FOR_DROPDOWN)
            self.do_click_by_locator(self.ORDER_LINE_MARK_FOR_CANCEL_OPTION)
            self.do_click_by_locator(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            self.do_click_by_locator(self.YES_RESUBMIT_ORDER_BUTTON)
            self.do_check_visibility(self.AT_LEAST_ONE_ORDER_LINE_REQUIRED_MESSAGE)
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            return True
        except Exception as e:
            return False

    def do_verify_last_order_attempt_on_section(self):
        try:
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_FILTER_PANEL)
            self.logger.info("Last order attempt on section visible successfully")
            return True
        except Exception as e:
            return False

    def do_verify_created_on_section(self):
        try:
            self.do_check_visibility(self.CREATED_ON_SECTION_FILTER_PANEL)
            self.logger.info("Created on section visible successfully")
            return True
        except Exception as e:
            return False

    def do_verify_contents_of_last_order_attempt_on_section(self):
        try:
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_SELECTED_EXPAND_MORE_BUTTON)
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_FROM_LABEL_WITH_DATE_RANGE_FILTER)
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_TO_LABEL_WITH_DATE_RANGE_FILTER)
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_SELECTED_ALL_DATES_CHECKBOX)
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_TODAY_CHECKBOX)
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_YESTERDAY_CHECKBOX)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_SEE_MORE_LESS_BUTTON)
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_LAST_WEEK_CHECKBOX)
            self.do_check_visibility(self.LAST_ORDER_ATTEMPT_SECTION_LAST_30_DAYS_CHECKBOX)
            self.logger.info("Contents of Last Order Attempt On section visible successfully")
            return True
        except Exception as e:
            return False

    def do_verify_contents_of_created_on_section(self):
        try:
            self.do_click_by_locator(self.CREATED_ON_SECTION_SELECTED_EXPAND_MORE_BUTTON)
            self.do_check_visibility(self.CREATED_ON_SECTION_FROM_LABEL_WITH_DATE_RANGE_FILTER)
            self.do_check_visibility(self.CREATED_ON_SECTION_TO_LABEL_WITH_DATE_RANGE_FILTER)
            self.do_check_visibility(self.CREATED_ON_SECTION_SELECTED_ALL_DATES_CHECKBOX)
            self.do_check_visibility(self.CREATED_ON_SECTION_TODAY_CHECKBOX)
            self.do_check_visibility(self.CREATED_ON_SECTION_YESTERDAY_CHECKBOX)
            self.do_click_by_locator(self.CREATED_ON_SECTION_SEE_MORE_LESS_BUTTON)
            self.do_check_visibility(self.CREATED_ON_SECTION_LAST_WEEK_CHECKBOX)
            self.do_check_visibility(self.CREATED_ON_SECTION_LAST_30_DAYS_CHECKBOX)
            self.logger.info("Contents of Created On section visible successfully")
            return True
        except Exception as e:
            return False

    def do_verify_last_ord_attempt_on_sec_calender_open_and_able_to_select_date(self):
        try:
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_FROM_CALENDER_ICON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_FROM_CURRENT_DATE)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_TO_CALENDER_ICON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_TO_CURRENT_DATE)
            self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
            self.logger.info("Successfully able to select the Last Order Attempt on section date from calender")
            return True
        except Exception as e:
            return False

    def do_verify_created_on_sec_calender_open_and_able_to_select_date(self):
        try:
            self.do_click_by_locator(self.CREATED_ON_SECTION_FROM_CALENDER_ICON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_FROM_CURRENT_DATE)
            self.do_click_by_locator(self.CREATED_ON_SECTION_TO_CALENDER_ICON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_TO_CURRENT_DATE)
            self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
            self.logger.info("Successfully able to select the Created on section date from calender")
            return True
        except Exception as e:
            return False

    def do_verify_last_ord_attempt_on_data_get_filter_as_per_selected_date_range_in_pages(self):
        try:
            from_date, to_date = self.filter_by_last_ord_attempt_on_data_to_and_from_as_per_selected_date_range()
            is_visible = self.do_check_visibility(self.NO_FAILED_ORDER_FOUND_MESSAGE)
            if is_visible:
                self.logger.info(
                    "Successfully verify updated grid as per Last order attempt date/time filtered date range")
                return True
            else:
                first_page_number, last_page_number = self.get_pagination_first_and_last_page()
                self.logger.info("Verifying updated grid as per Last order attempt date/time filtered date in page %s",
                                 str(first_page_number))
                self.go_to_page(first_page_number)
                self.validate_last_ord_attempt_on_data_as_per_selected_date_range(from_date, to_date)
                if first_page_number != last_page_number:
                    if last_page_number != first_page_number + 1:
                        random_page = self.get_random_page(first_page_number, last_page_number)
                        self.logger.info(
                            "Verifying updated grid as perLast order attempt date/time filtered date in page %s",
                            str(random_page))
                        from_date, to_date = self.filter_by_last_ord_attempt_on_data_to_and_from_as_per_selected_date_range()
                        self.go_to_page(random_page)
                        self.validate_last_ord_attempt_on_data_as_per_selected_date_range(from_date, to_date)
                    self.logger.info(
                        "Verifying updated grid as per Last order attempt date/time filtered date in page %s",
                        str(last_page_number))
                    from_date, to_date = self.filter_by_last_ord_attempt_on_data_to_and_from_as_per_selected_date_range()
                    self.go_to_page(last_page_number)
                    self.validate_last_ord_attempt_on_data_as_per_selected_date_range(from_date, to_date)
                self.logger.info(
                    "Successfully verified updated grid as per Last order attempt date/time filtered date range")
                return True
        except Exception as e:
            return False

    def filter_by_last_ord_attempt_on_data_to_and_from_as_per_selected_date_range(self):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_SELECTED_EXPAND_MORE_BUTTON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_FROM_CALENDER_ICON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_FROM_YESTERDAY_DATE)

            from_date = self.do_get_attribute(self.LAST_ORDER_ATTEMPT_SECTION_FROM_SELECTED_DATE_VALUE, "value")
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_TO_CALENDER_ICON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_TO_CURRENT_DATE)
            to_date = self.do_get_attribute(self.LAST_ORDER_ATTEMPT_SECTION_TO_SELECTED_DATE_VALUE, "value")
            self.do_click_by_locator(self.APPLY_BUTTON)
            self.logger.info("Filtered  Last order attempt section from and to date")
            time.sleep(2)
            return from_date, to_date
        except Exception as e:
            raise e

    def validate_last_ord_attempt_on_data_as_per_selected_date_range(self, from_date, to_date):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            element = "//*[text()='Last order attempt date/time']"
            last_order_attempt_date_time_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(last_order_attempt_date_time_element)

            last_order_attempt_date_time_list = self.get_all_elements(self.LAST_ORDER_ATTEMPT_DATE_ITEM_ITEM_LIST)
            self.logger.info(
                "length of Last order attempt date/time list %s" % len(last_order_attempt_date_time_list))
            self.scroll()

            last_order_attempt_date_time_list = self.get_all_elements(self.LAST_ORDER_ATTEMPT_DATE_ITEM_ITEM_LIST)
            self.logger.info(
                "length of Last order attempt date/time list %s" % len(last_order_attempt_date_time_list))
            count = 0

            for last_order_attempt_date_time_item in last_order_attempt_date_time_list:
                if (str(from_date) in last_order_attempt_date_time_item.text) | (
                        str(to_date) in last_order_attempt_date_time_item.text):
                    count = count + 1
                if count == len(last_order_attempt_date_time_list):
                    self.logger.info(
                        "Successfully Verified that Last order attempt date Data should get filtered on selected date ranges")
                    break
        except Exception as e:
            raise e

    def do_verify_created_on_data_get_filter_as_per_selected_date_range_in_pages(self):
        try:
            from_date, to_date = self.filter_by_created_on_data_to_and_from_as_per_selected_date_range()
            is_visible = self.do_check_visibility(self.NO_FAILED_ORDER_FOUND_MESSAGE)
            if is_visible:
                self.logger.info("Successfully verify updated grid as per Created on filtered date")
                return True
            else:
                first_page_number, last_page_number = self.get_pagination_first_and_last_page()
                self.logger.info("Verifying updated grid as per Created on filtered date in page %s",
                                 str(first_page_number))
                self.go_to_page(first_page_number)
                self.validate_created_on_data_as_per_selected_date_range(from_date, to_date)
                if first_page_number != last_page_number:
                    if last_page_number != first_page_number + 1:
                        random_page = self.get_random_page(first_page_number, last_page_number)
                        self.logger.info("Verifying updated grid as per Created on filtered date in page %s",
                                         str(random_page))
                        from_date, to_date = self.filter_by_created_on_data_to_and_from_as_per_selected_date_range()
                        self.go_to_page(random_page)
                        self.validate_created_on_data_as_per_selected_date_range(from_date, to_date)
                    self.logger.info("Verifying updated grid as per Created on filtered date in page %s",
                                     str(last_page_number))
                    from_date, to_date = self.filter_by_created_on_data_to_and_from_as_per_selected_date_range()
                    self.go_to_page(last_page_number)
                self.validate_created_on_data_as_per_selected_date_range(from_date, to_date)
                self.logger.info("Successfully verified updated grid as per Created on filtered date")
                return True
        except Exception as e:
            return False

    def filter_by_created_on_data_to_and_from_as_per_selected_date_range(self):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_SELECTED_EXPAND_MORE_BUTTON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_FROM_CALENDER_ICON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_FROM_YESTERDAY_DATE)

            from_date = self.do_get_attribute(self.CREATED_ON_SECTION_FROM_SELECTED_DATE_VALUE, "value")
            self.do_click_by_locator(self.CREATED_ON_SECTION_TO_CALENDER_ICON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_TO_CURRENT_DATE)
            to_date = self.do_get_attribute(self.CREATED_ON_SECTION_TO_SELECTED_DATE_VALUE, "value")
            self.logger.info("Filtered Created on section from and to date")
            time.sleep(3)
            self.do_click_by_locator(self.APPLY_BUTTON)
            return from_date, to_date
        except Exception as e:
            raise e

    def validate_created_on_data_as_per_selected_date_range(self, from_date, to_date):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            element = "//*[text()='Created on']"
            created_on_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(created_on_element)

            created_on_list = self.get_all_elements(self.CREATED_ON_ITEM_LIST)
            self.logger.info("length of Created On list %s" % len(created_on_list))
            self.scroll()

            created_on_list = self.get_all_elements(self.CREATED_ON_ITEM_LIST)
            self.logger.info("length of Created On list %s" % len(created_on_list))
            count = 0

            for created_on_item in created_on_list:
                if (str(from_date) in created_on_item.text) | (str(to_date) in created_on_item.text):
                    count = count + 1
                if count == len(created_on_list):
                    self.logger.info(
                        "Successfully Verified that Created On Data should get filtered on selected date ranges")
                    break
        except Exception as e:
            raise e

    def verify_filter_by_last_ord_attempt_on_data_by_selecting_30_days_in_pages(self):
        try:
            is_visible = self.do_check_visibility(self.NO_FAILED_ORDER_FOUND_MESSAGE)
            if is_visible:
                self.logger.info("Successfully verify updated grid as per Last order attempt filtered date")
                return True
            else:
                first_page_number, last_page_number = self.get_pagination_first_and_last_page()
                self.logger.info("Verifying Last order attempt date/time data in page %s", str(first_page_number))
                self.filter_by_last_ord_attempt_on_data_by_selecting_30_days()
                self.go_to_page(first_page_number)
                self.validate_last_ord_attempt_on_data()
                if first_page_number != last_page_number:
                    if last_page_number != first_page_number + 1:
                        random_page = self.get_random_page(first_page_number, last_page_number)
                        self.logger.info("Verifying Last order attempt date/time data in page %s", str(random_page))
                        self.filter_by_last_ord_attempt_on_data_by_selecting_30_days()
                        self.go_to_page(random_page)
                        self.validate_last_ord_attempt_on_data()
                    self.logger.info("Verifying Last order attempt date/time data in page %s", str(last_page_number))
                    self.filter_by_last_ord_attempt_on_data_by_selecting_30_days()
                    self.go_to_page(last_page_number)
                    self.validate_last_ord_attempt_on_data()
                self.logger.info("Successfully verified Last order attempt date/time data")
                return True
        except Exception as e:
            self.logger.error("Exception occurred verifying Last order attempt date/time data in table" + str(e))
            return False

    def filter_by_last_ord_attempt_on_data_by_selecting_30_days(self):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_SELECTED_EXPAND_MORE_BUTTON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_SEE_MORE_LESS_BUTTON)
            self.do_click_by_locator(self.LAST_ORDER_ATTEMPT_SECTION_LAST_30_DAYS_CHECKBOX)
            self.do_click_by_locator(self.APPLY_BUTTON)
            self.logger.info("Filtered Last order attempt section date with Last 30 days")
            time.sleep(2)
            return True
        except Exception as e:
            return False

    def validate_last_ord_attempt_on_data(self):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            element = "//*[text()='Last order attempt date/time']"
            last_order_attempt_date_time_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(last_order_attempt_date_time_element)

            last_order_attempt_date_time_list = self.get_all_elements(self.LAST_ORDER_ATTEMPT_DATE_ITEM_ITEM_LIST)
            self.logger.info(
                "length of Last order attempt date/time list %s" % len(last_order_attempt_date_time_list))
            self.scroll()

            last_order_attempt_date_time_list = self.get_all_elements(self.LAST_ORDER_ATTEMPT_DATE_ITEM_ITEM_LIST)
            self.logger.info(
                "length of Last order attempt date/time list %s" % len(last_order_attempt_date_time_list))
            count = 0
            start_date = date.today() - timedelta(days=30)
            end_date = date.today()
            date_list = pandas.date_range(start_date, end_date + timedelta(days=0), freq='d').strftime(
                "%m/%d/%Y").tolist()
            for last_order_attempt_date_time_item in last_order_attempt_date_time_list:
                dt = last_order_attempt_date_time_item.text
                last_order_attempt_date_time_item_dt = dt.split(", ")

                if last_order_attempt_date_time_item_dt[0] in date_list:
                    count = count + 1
                if count == len(last_order_attempt_date_time_list):
                    self.logger.info(
                        "Successfully Verified that Last order attempt date Data should get filtered on selected date ranges")
                    break
        except Exception as e:
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

    def get_random_page(self, first, last):
        try:
            if last > 10:
                return random.randint(2, 10)
            elif last <= 10:
                return random.randint(first + 1, last - 1)
        except Exception as e:
            self.logger.error("Exception while generating random number" + str(e))
            raise e

    def verify_filter_by_created_on_data_by_selecting_30_days_in_pages(self):
        try:
            self.filter_by_created_on_data_by_selecting_30_days()
            is_visible = self.do_check_visibility(self.NO_FAILED_ORDER_FOUND_MESSAGE)
            if is_visible:
                self.logger.info("Successfully verify updated grid as per Created on filtered date")
                return True
            else:
                first_page_number, last_page_number = self.get_pagination_first_and_last_page()
                self.logger.info("Verifying updated grid as per Created on filtered date in page %s",
                                 str(first_page_number))
                self.go_to_page(first_page_number)
                self.validate_created_on_data()
                if first_page_number != last_page_number:
                    if last_page_number != first_page_number + 1:
                        random_page = self.get_random_page(first_page_number, last_page_number)
                        self.logger.info("Verifying updated grid as per Created on filtered date in page %s",
                                         str(random_page))
                        self.filter_by_created_on_data_by_selecting_30_days()
                        self.go_to_page(random_page)
                        self.validate_created_on_data()
                    self.logger.info("Verifying updated grid as per Created on filtered date in page %s",
                                     str(last_page_number))
                    self.filter_by_created_on_data_by_selecting_30_days()
                    self.go_to_page(last_page_number)
                    self.validate_created_on_data()
                self.logger.info("Successfully verified updated grid as per Created on filtered date")
                self.driver.execute_script(
                    "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
                return True
        except Exception as e:
            return False

    def filter_by_created_on_data_by_selecting_30_days(self):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.BITTOM_CLEAR_ALL_BUTTON)
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_SELECTED_EXPAND_MORE_BUTTON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_SEE_MORE_LESS_BUTTON)
            self.do_click_by_locator(self.CREATED_ON_SECTION_LAST_30_DAYS_CHECKBOX)
            self.do_click_by_locator(self.APPLY_BUTTON)
            self.logger.info("Filtered Created on section date with Last 30 days")
            time.sleep(2)
            return True
        except Exception as e:
            return False

    def validate_created_on_data(self):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            element = "//*[text()='Created on']"
            created_on_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(created_on_element)

            created_on_list = self.get_all_elements(self.CREATED_ON_ITEM_LIST)
            self.logger.info(
                "length of Created on list %s" % len(created_on_list))
            self.scroll()

            created_on_list = self.get_all_elements(self.CREATED_ON_ITEM_LIST)
            self.logger.info(
                "length of Created on list %s" % len(created_on_list))
            count = 0
            start_date = date.today() - timedelta(days=30)
            end_date = date.today()
            date_list = pandas.date_range(start_date, end_date + timedelta(days=0), freq='d').strftime(
                "%m/%d/%Y").tolist()
            for created_on_item in created_on_list:
                dt = created_on_item.text
                created_on_item_dt = dt.split(", ")

                if created_on_item_dt[0] in date_list:
                    count = count + 1
                if count == len(created_on_list):
                    self.logger.info(
                        "Successfully Verified that Created on date Data should get filtered on selected date ranges")
                    break
        except Exception as e:
            raise e

    def do_verify_order_line_edit_icon(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_LINE_TAB)
            self.do_check_visibility(self.ORDER_LINE_EDIT_ICON)
            self.logger.info(
                "Successfully Verified order line Edit icon")
            return True
        except Exception as e:
            return False

    def do_verify_update_and_cancel_icon(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_LINE_EDIT_ICON)
            self.do_check_visibility(self.ORDER_LINE_UPDATE_ICON)
            self.do_check_visibility(self.ORDER_LINE_CANCEL_ICON)
            self.logger.info(
                "Successfully Verified Update and Cancel Button")
            return True
        except Exception as e:
            return False

    def do_verify_editable_order_line_fields(self):
        try:
            time.sleep(3)
            self.do_check_visibility(self.ORDER_LINE_EDIT_QUANTITY_FIELD)
            self.do_check_visibility(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD)
            self.do_check_visibility(self.ORDER_LINE_EDIT_END_USER_PRICE_FIELD)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            self.do_check_visibility(self.ORDER_LINE_EDIT_END_USER_PO_FIELD)
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            self.logger.info(
                "Successfully able to edit Quantity, Reseller price, End user price and End user po# fields")
            return True
        except Exception as e:
            return False

    def do_verify_order_line_updated_data_discarded(self):
        try:
            order_line_quantity = "2"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_QUANTITY_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_QUANTITY_FIELD, order_line_quantity)

            order_line_reseller_price = "4"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD, order_line_reseller_price)

            order_line_end_user_price = "6"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_END_USER_PRICE_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_END_USER_PRICE_FIELD, order_line_end_user_price)

            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            order_line_end_user_po = "END_USER_PO"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_END_USER_PO_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_END_USER_PO_FIELD, order_line_end_user_po)

            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")

            self.do_click_by_locator(self.ORDER_LINE_CANCEL_ICON)
            self.do_check_visibility(self.ORDER_LINE_EDIT_ICON)

            quantity = self.get_element_text(self.ORDER_LINE_QUANTITY_FIELD_TEXT)
            reseller_price = self.get_element_text(self.ORDER_LINE_RESELLER_PRICE_FIELD_TEXT)
            end_user_price = self.get_element_text(self.ORDER_LINE_END_USER_PRICE_FIELD_TEXT)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")
            end_user_po = self.get_element_text(self.ORDER_LINE_END_USER_PO_FIELD_TEXT)

            if (order_line_quantity != quantity) & (order_line_reseller_price != reseller_price) & (
                    order_line_end_user_price != end_user_price) & (order_line_end_user_po != end_user_po):
                self.driver.execute_script(
                    "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
                self.logger.info(
                    "Verified that Quantity, Reseller price, End user price and End user po# fields discarded successfully")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_order_line_fields_not_allow_non_numberic_content(self):
        try:
            self.do_click_by_locator(self.ORDER_LINE_EDIT_ICON)

            order_line_quantity = "Test_123"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_QUANTITY_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_QUANTITY_FIELD, order_line_quantity)

            order_line_reseller_price = "Test_456"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD, order_line_reseller_price)

            order_line_end_user_price = "Test_567"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_END_USER_PRICE_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_END_USER_PRICE_FIELD, order_line_end_user_price)

            quantity = self.do_get_attribute(self.ORDER_LINE_EDIT_QUANTITY_FIELD, "value")
            reseller_price = self.do_get_attribute(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD, "value")
            end_user_price = self.do_get_attribute(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD, "value")

            if (order_line_quantity != quantity) & (order_line_reseller_price != reseller_price) & (
                    order_line_end_user_price != end_user_price):
                self.logger.info(
                    "Verified that Quantity, Reseller price, End user price and End user po# fields not allowed non numberic contents")
                return True
            else:
                self.logger.error(
                    "Quantity, Reseller price, End user price and End user po# fields allowed non numberic contents")
                return False
        except Exception as e:
            return False

    def do_update_order_line_field_value(self):
        try:
            order_line_quantity = "2"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_QUANTITY_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_QUANTITY_FIELD, order_line_quantity)

            order_line_reseller_price = "4"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_RESELLER_PRICE_FIELD, order_line_reseller_price)

            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            order_line_end_user_po = "END_USER_PO"
            self.do_clear_textfield(self.ORDER_LINE_EDIT_END_USER_PO_FIELD)
            self.do_send_keys(self.ORDER_LINE_EDIT_END_USER_PO_FIELD, order_line_end_user_po)

            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")

            self.do_click_by_locator(self.ORDER_LINE_UPDATE_ICON)
            self.do_click_by_locator(self.ORDER_DETAILS_TAB)
            self.logger.info("Successfully Updated the order line fields value")
            return True
        except Exception as e:
            return False

    def do_verify_operator_id(self):
        try:
            attr_list = []
            operator_id = None
            path = ".\\RestApi\\Resources\\data_error_order_payload.json"
            data = self.common_json.read_json_file(path)
            self.logger.info(data)
            attr_list = data['additionalAttributes']
            print(attr_list)
            for some_dict in range(len(attr_list)):
                attr_item = attr_list[some_dict]
                print(attr_item)
                if attr_item['attributeName'] == 'operatorid':
                    operator_id = attr_item['attributeValue']
                    print(operator_id)
                    break
            operator_id_value = self.get_element_text(self.OPERATOR_ID).replace("Operator ID:\n", "")
            self.logger.info(f'Operator_id value: {operator_id_value}')
            if operator_id == operator_id_value:
                self.logger.info("Successfully Verified Operator Id")
                self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_channel_label(self):
        try:
            self.do_check_visibility(self.CHANNEL_LABEL)
            self.logger.info("Channel label visible")
            return True
        except Exception as e:
            return False

    def do_verify_order_channel_matched(self, confirmation_id):
        global channel
        try:
            time.sleep(5)
            self.do_click_by_locator(self.DATA_ERROR_OPTION)
            self.do_click_by_locator(self.SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.CONFRIMATION_ID_OPTION)
            self.do_send_keys(self.DATA_ERRORS_SEARCH_BOX, confirmation_id)
            for i in range(3):
                self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
                time.sleep(5)
                if self.do_check_visibility(self.FRAUD_FIRST_RECORD):
                    channel = self.get_element_text(self.LISTING_PAGE_CHANNEL_NAME)
                    self.logger.info(f'Listing Page Channel Name: {channel}')
                    break
            self.do_click_by_locator(self.FRAUD_FIRST_RECORD)
            time.sleep(3)
            order_details_channel_value = self.get_element_text(self.ORDER_DEATILS_PAGE_CHANNEL_NAME).replace(
                "Channel:\n", "")
            self.logger.info(f'Operator_id value: {order_details_channel_value}')
            if channel == order_details_channel_value:
                self.logger.info("Successfully Verified Operator Id")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_shipping_details(self, confirmation_id):
        try:
            time.sleep(5)
            self.do_click_by_locator(self.DATA_ERROR_OPTION)
            self.do_click_by_locator(self.SEARCH_DROP_DOWN)
            self.do_click_by_locator(self.CONFRIMATION_ID_OPTION)
            self.do_send_keys(self.DATA_ERRORS_SEARCH_BOX, confirmation_id)
            for i in range(3):
                self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
                time.sleep(2)
                if self.do_check_visibility(self.FRAUD_FIRST_RECORD):
                    self.do_click_by_locator(self.FRAUD_FIRST_RECORD)
                    self.logger.info(f'Successfully Clicked on {confirmation_id} order')
                    break
            self.do_click_by_locator(self.BILLING_SHIPPING_TAB)
            self.do_check_visibility(self.SHIPPING_DETAILS_SECTION)
            self.do_check_visibility(self.SHIPPING_DETAILS_CARRIER_CODE_LABEL)
            self.do_check_visibility(self.SHIPPING_DETAILS_FREIGHT_ACCOUNT_NUMBER_LABEL)
            self.do_check_visibility(self.SHIPPING_DETAILS_SHIPMENT_COMPLETE_LABEL)
            self.do_check_visibility(self.SHIPPING_DETAILS_REQUESTED_DELIVER_YDATE_LABEL)
            self.do_check_visibility(self.SHIPPING_DETAILS_SIGNATURE_REQUIRED_LABEL)
            self.do_check_visibility(self.SHIPPING_DETAILS_CARRIER_SERVICE_LABEL)
            self.logger.info("Successfully verified the Shipping Details Section Fields")
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            return True
        except Exception as e:
            return False

    def verify_contents_of_edit_shipping_address(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.BILLING_SHIPPING_TAB)
            self.do_click_by_locator(self.SHIPPING_ADDRESS_EDIT_BUTTON)
            edit_shipping_address_title = 'Edit Shipping Address'

            assert edit_shipping_address_title in self.get_element_text(
                self.EDIT_SHIPPING_ADDRESS_POPUP_TITLE), "Edit Shipping Address Title not present"

            self.do_check_visibility(self.EDIT_SHIPPING_ADDRESS_SEARCH_BOX)
            self.do_check_visibility(self.EDIT_SHIPPING_ADDRESS_POPUP_CANCEL_BUTTON)
            self.do_check_visibility(self.EDIT_SHIPPING_ADDRESS_POPUP_CLOSE_ICON)
            self.do_check_visibility(self.EDIT_SHIPPING_ADDRESS_POPUP_DISABLED_SAVE_BUTTON)
            self.logger.info(
                "Successfully verified Edit Shipping Address Popup title, Search box, X icon, Cancel and Save Disabled button on popup")
            return True
        except Exception as e:
            return False

    def do_verify_order_details_page_after_click_on_x_icon_shipping_addr_popup(self):
        try:
            self.do_click_by_locator(self.EDIT_SHIPPING_ADDRESS_POPUP_CLOSE_ICON)
            self.do_check_visibility(self.ORDER_DETAILS_PAGE)
            self.logger.info("Successfully verified Order Details Page")
            return True
        except Exception as e:
            return False

    def do_verify_order_details_page_after_click_on_cancel_button_shipping_addr_popup(self):
        try:
            self.do_click_by_locator(self.SHIPPING_ADDRESS_EDIT_BUTTON)
            self.do_click_by_locator(self.EDIT_SHIPPING_ADDRESS_POPUP_CANCEL_BUTTON)
            self.do_check_visibility(self.ORDER_DETAILS_PAGE)
            self.logger.info("Successfully verified Order Details Page")
            return True
        except Exception as e:
            return False

    def do_verify_contents_of_add_new_shipping_address_popup(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_BUTTON)
            add_new_shipping_address_title = 'Add New Shipping Address'

            assert add_new_shipping_address_title in self.get_element_text(
                self.ADD_NEW_SHIPPING_ADDRESS_POPUP_TITLE), "Add New Shipping Address Title not present"

            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_COMPANY_NAME_TEXTBOX)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_CONTACT_NAME)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_EMAIL)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_PHONE_NUMBER)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_LINE_1)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_LINE_2)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_CITY)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_STATE_DROPDOWN)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_COUNTRY_DROPDOWN)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_ZIP_CODE)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_CANCEL_BUTTON)
            self.do_check_visibility(self.ADD_NEW_SHIPPING_ADDRESS_ADD_ENABLED_BUTTON)

            self.logger.info("Successfully verified the Add new Shipping address popup content")
            return True
        except Exception as e:
            return False

    def do_verify_all_shipping_addr_matching_with_entered_text(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.SHIPPING_ADDRESS_EDIT_BUTTON)
            count = 0
            search_text = "INGRAM"
            self.do_clear_textfield(self.EDIT_SHIPPING_ADDRESS_SEARCH_BOX)
            self.do_send_keys(self.EDIT_SHIPPING_ADDRESS_SEARCH_BOX, search_text)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            shipping_title_list = self.get_all_elements(self.SEARCHED_SHIPPING_ADDRESS_TITLE_LIST)
            for element in range(len(shipping_title_list)):
                shipping_addr_title = shipping_title_list[element].text
                if search_text in shipping_addr_title:
                    self.logger.info(f'Searching Shiping address {shipping_addr_title} match with search text')
                    count = count + 1
                if count == len(shipping_title_list):
                    self.logger.info("All the shipping addresses matched with search text")
                    return True
        except Exception as e:
            return False

    def do_verify_added_new_shipping_addr_data(self):
        try:
            company_name = "INGRAM MICRO " + ''.join(random.choices(string.ascii_uppercase, k=3))
            self.logger.info("The randomly generated string is : " + str(company_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_COMPANY_NAME_TEXTBOX, company_name)

            contact_name = "LENDING CLUB CORPORATION " + ''.join(random.choices(string.ascii_uppercase, k=2))
            self.logger.info("The randomly generated number is : " + str(contact_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_CONTACT_NAME, contact_name)

            modified_email = "test." + ''.join(random.choices(string.ascii_uppercase, k=5)) + "@ingrammicro.com"
            self.logger.info("The randomly generated String is : " + str(modified_email))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_EMAIL, modified_email)

            phone_number = ''.join(random.choices(string.digits, k=10))
            self.logger.info("The randomly generated number is : " + str(phone_number))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_PHONE_NUMBER, phone_number)

            address_line_1 = "3196 MILL RD"
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_LINE_1, address_line_1)

            address_line_2 = "Wisconsin State Highways 29"

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_LINE_2, address_line_2)

            city = "SANTA ANA"

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_CITY, city)

            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_STATE_DROPDOWN)
            time.sleep(2)
            self.do_click_by_locator(self.SELECT_STATE_CALIFORNIA)

            # self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_COUNTRY_DROPDOWN)
            # self.do_click_by_locator(self.SELECT_UNITED_STATE)

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_ZIP_CODE, "92233")

            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_ADD_ENABLED_BUTTON)

            added_new_shipping_address_line_2 = address_line_2 + " " + city + " " + "CA"

            shipping_address_company_name = self.get_element_text(self.SHIPPING_ADDRESS_COMPANY_NAME)
            shipping_address_contact_name = self.get_element_text(self.SHIPPING_ADDRESS_CONTACT_NAME)
            shipping_address_phone_number = self.get_element_text(self.SHIPPING_ADDRESS_PHONE_NUMBER)
            shipping_address_line_1 = self.get_element_text(self.SHIPPING_ADDRESS_LINE_1)
            shipping_address_line_2 = self.get_element_text(self.SHIPPING_ADDRESS_LINE_2)

            if (company_name == shipping_address_company_name) & (
                    contact_name == shipping_address_contact_name) & (
                    phone_number == shipping_address_phone_number) & (address_line_1 == shipping_address_line_1) & (
                    added_new_shipping_address_line_2 == shipping_address_line_2):
                self.logger.info("Successfully Verified Added New shipping address display in order details page")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_data_not_save_after_click_on_x_icon_on_popup(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.SHIPPING_ADDRESS_EDIT_BUTTON)
            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_BUTTON)

            company_name = "INGRAM MICRO " + ''.join(random.choices(string.ascii_uppercase, k=3))
            self.logger.info("The randomly generated string is : " + str(company_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_COMPANY_NAME_TEXTBOX, company_name)

            contact_name = "LENDING CLUB CORPORATION " + ''.join(random.choices(string.ascii_uppercase, k=2))
            self.logger.info("The randomly generated number is : " + str(contact_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_CONTACT_NAME, contact_name)

            modified_email = "test." + ''.join(random.choices(string.ascii_uppercase, k=5)) + "@ingrammicro.com"
            self.logger.info("The randomly generated String is : " + str(modified_email))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_EMAIL, modified_email)

            phone_number = ''.join(random.choices(string.digits, k=10))
            self.logger.info("The randomly generated number is : " + str(phone_number))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_PHONE_NUMBER, phone_number)

            address_line_1 = "3196 MILL RD"
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_LINE_1, address_line_1)

            address_line_2 = "Wisconsin State Highways 29"

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_LINE_2, address_line_2)

            city = "SANTA ANA"

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_CITY, city)

            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_STATE_DROPDOWN)
            time.sleep(2)
            self.do_click_by_locator(self.SELECT_STATE_CALIFORNIA)

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_ZIP_CODE, "92233")

            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_CLOSE_BUTTON)

            visible = self.do_check_visibility(self.EDIT_BILLING_ADDRESS_POPUP_TITLE)
            if visible:
                self.logger.info(
                    "Successfully verified Edit Shipping Address Pop Shown, newly Added Shipping address data not saved after click on X Icon")
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_verify_data_not_save_after_click_on_cancel_icon_on_popup(self):
        try:
            time.sleep(3)
            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_BUTTON)

            company_name = "INGRAM MICRO " + ''.join(random.choices(string.ascii_uppercase, k=3))
            self.logger.info("The randomly generated string is : " + str(company_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_COMPANY_NAME_TEXTBOX, company_name)

            contact_name = "LENDING CLUB CORPORATION " + ''.join(random.choices(string.ascii_uppercase, k=2))
            self.logger.info("The randomly generated number is : " + str(contact_name))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_CONTACT_NAME, contact_name)

            modified_email = "test." + ''.join(random.choices(string.ascii_uppercase, k=5)) + "@ingrammicro.com"
            self.logger.info("The randomly generated String is : " + str(modified_email))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_EMAIL, modified_email)

            phone_number = ''.join(random.choices(string.digits, k=10))
            self.logger.info("The randomly generated number is : " + str(phone_number))  # print the random data
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_PHONE_NUMBER, phone_number)

            address_line_1 = "3196 MILL RD"
            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_LINE_1, address_line_1)

            address_line_2 = "Wisconsin State Highways 29"

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_LINE_2, address_line_2)

            city = "SANTA ANA"

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_CITY, city)

            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_STATE_DROPDOWN)
            time.sleep(2)
            self.do_click_by_locator(self.SELECT_STATE_CALIFORNIA)

            self.do_send_keys(self.ADD_NEW_SHIPPING_ADDRESS_ZIP_CODE, "92233")

            self.do_click_by_locator(self.ADD_NEW_SHIPPING_ADDRESS_CANCEL_BUTTON)

            visible = self.do_check_visibility(self.EDIT_BILLING_ADDRESS_POPUP_TITLE)
            if visible:
                self.logger.info(
                    "Successfully verified Edit Shipping Address Pop Shown, newly Added Shipping address data not saved after click on Cancel button")
                self.do_click_by_locator(self.EDIT_SHIPPING_ADDRESS_POPUP_CANCEL_BUTTON)
                self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
                return True
            else:
                return False
        except Exception as e:
            return False

    def do_correct_PO_and_resubmit_order(self):
        try:
            self.do_click_by_locator(self.REFERENCE_DETAILS_EDIT_BUTTON)
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            special_symbols = ['!', '@', '$', '%', '^', '&', '*']
            for x in range(len(special_symbols)):
                symbol = str(special_symbols[x])
                if symbol in reseller_po:
                    reseller_po = reseller_po.replace(symbol, "")
                    break
            self.logger.info(reseller_po)
            self.do_send_keys(self.RESELLER_PO_VALUE, reseller_po)
            self.do_click_by_locator(self.DATA_ERROR_ORDER_UPDATE_BUTTON)
            self.do_click_by_locator(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            self.do_click_by_locator(self.YES_RESUBMIT_ORDER_BUTTON)
            order_resubmit_message = 'Order has been successfully resubmitted.'
            assert order_resubmit_message in self.get_element_text(
                self.RESUBMITTED_ORDER_SUCCESS_MESSAGE), "Successfully Resubmitted Order message not present"
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            self.logger.info("Order reprocessed successfully")
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            return True
        except Exception as e:
            return False

    def do_correct_PO_add_new_line_and_resubmit_order_cancel_proceed_button(self):
        try:
            self.do_click_by_locator(self.REFERENCE_DETAILS_EDIT_BUTTON)
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            special_symbols = ['!', '@', '$', '%', '^', '&', '*']
            for x in range(len(special_symbols)):
                symbol = str(special_symbols[x])
                if symbol in reseller_po:
                    reseller_po = reseller_po.replace(symbol, "")
                    break
            self.logger.info(reseller_po)
            self.do_send_keys(self.RESELLER_PO_VALUE, reseller_po)
            self.do_click_by_locator(self.DATA_ERROR_ORDER_UPDATE_BUTTON)

            self.logger.info("Adding new order line")
            self.do_click_by_locator(self.ORDER_LINE_TAB)

            self.do_click_by_locator(self.ADD_ORDER_LINE_BUTTON)
            self.do_check_visibility(self.NEW_ORDER_LINE_POPUP)

            self.do_click_by_locator(self.NEW_ORDER_LINE_IM_PART_NO_TEXTBOX)
            self.do_send_keys(self.NEW_ORDER_LINE_IM_PART_NO_TEXTBOX, '6QM398')
            self.logger.info("Successfully added IM Part# number")

            self.do_click_by_locator(self.NEW_ORDER_LINE_QTY_TEXTBOX)
            self.do_send_keys(self.NEW_ORDER_LINE_QTY_TEXTBOX, '3')
            self.logger.info("Successfully added Qty")

            self.do_click_by_locator(self.NEW_ORDER_LINE_PRICE_TEXTBOX)
            self.do_send_keys(self.NEW_ORDER_LINE_PRICE_TEXTBOX, '121')
            self.logger.info("Successfully added price")

            self.do_click_by_locator(self.NEW_ORDER_LINE_VALIDATE_BUTTON)

            time.sleep(5)
            self.do_click_by_locator(self.ADD_NEW_LINE_ADD_BUTTON)

            self.logger.info("Successfully added new order line")

            self.do_click_by_locator(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            self.do_click_by_locator(self.YES_RESUBMIT_ORDER_BUTTON)

            resubmit_order_message_msg = 'Are you sure you want to resubmit order? Purchase order resubmitting, ' + reseller_po +  ' already exists in Impulse. Order will be resubmitted, cannot undo this action.'
            header_msg = 'Purchase order ' + reseller_po + ' already exists'

            pop_up_header_message = self.get_element_text(self.RESUBMIT_ORDER_HEADER_MSG).replace("\n", " ")
            message = self.get_element_text(self.RESUBMIT_ORDER_MSG).replace("\n", " ")

            assert resubmit_order_message_msg in message, "Resubmit order popup message not present"
            assert header_msg in pop_up_header_message, "Resubmit order header message not present"

            self.do_check_visibility(self.RESUBMIT_ORDER_CANCEL_ORDER_BUTTON)
            self.do_check_visibility(self.RESUBMIT_ORDER_PROCEED_BUTTON)

            return True
        except Exception as e:
            return False

    def do_click_cancel_button_and_verify_reject_reason_open(self):
        try:
            self.do_click_by_locator(self.RESUBMIT_ORDER_CANCEL_ORDER_BUTTON)
            self.do_click_by_locator(self.CANCEL_YES_BUTTON)
            self.do_check_visibility(self.REASON_TEXTAERA)
            self.logger.info("Successfully popup opened to enter reject reason.")
            self.do_click_by_locator(self.BACK_BUTTON)
            self.do_click_by_locator(self.CANCEL_NO_BUTTON)
            return True
        except Exception as e:
            return False

    def do_click_proceed_button_and_resubmit_the_order(self):
        try:
            self.do_click_by_locator(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            self.do_click_by_locator(self.YES_RESUBMIT_ORDER_BUTTON)
            self.do_click_by_locator(self.RESUBMIT_ORDER_PROCEED_BUTTON)
            order_resubmit_message = 'Order has been successfully resubmitted.'
            assert order_resubmit_message in self.get_element_text(
                self.RESUBMITTED_ORDER_SUCCESS_MESSAGE), "Successfully Resubmitted Order message not present"
            time.sleep(3)
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            return True
        except Exception as e:
            return False

    def do_correct_end_customer_po_and_resubmit_order_cancel_proceed_button(self):
        try:
            self.do_click_by_locator(self.REFERENCE_DETAILS_EDIT_BUTTON)
            reseller_po = self.do_get_attribute(self.RESELLER_PO_VALUE, "value")
            end_customer_order = self.do_get_attribute(self.END_CUSTOMER_ORDER_VALUE, "value")
            special_symbols = ['!', '@', '$', '%', '^', '&', '*']
            for x in range(len(special_symbols)):
                symbol = str(special_symbols[x])
                if symbol in end_customer_order:
                    end_customer_order = end_customer_order.replace(symbol, "")
            self.logger.info(end_customer_order)
            self.do_send_keys(self.END_CUSTOMER_ORDER_VALUE, end_customer_order)
            self.do_click_by_locator(self.DATA_ERROR_ORDER_UPDATE_BUTTON)

            self.do_click_by_locator(self.DATA_ERRORS_RESUBMIT_ORDER_BUTTON)
            self.do_click_by_locator(self.YES_RESUBMIT_ORDER_BUTTON)

            resubmit_order_message_msg = 'Are you sure you want to resubmit order? Purchase order resubmitting, ' + reseller_po +  ' already exists in Impulse. Order will be resubmitted, cannot undo this action.'
            header_msg = 'Purchase order ' + reseller_po + ' already exists'

            pop_up_header_message = self.get_element_text(self.RESUBMIT_ORDER_HEADER_MSG).replace("\n", " ")
            message = self.get_element_text(self.RESUBMIT_ORDER_MSG).replace("\n", " ")

            assert resubmit_order_message_msg in message, "Resubmit order popup message not present"
            assert header_msg in pop_up_header_message, "Resubmit order header message not present"

            self.do_check_visibility(self.RESUBMIT_ORDER_CANCEL_ORDER_BUTTON)
            self.do_check_visibility(self.RESUBMIT_ORDER_PROCEED_BUTTON)
            self.do_click_by_locator(self.RESUBMIT_ORDER_CANCEL_ORDER_BUTTON)
            self.do_click_by_locator(self.CANCEL_YES_BUTTON)
            self.do_check_visibility(self.REASON_TEXTAERA)
            self.logger.info("Successfully popup opened to enter reject reason.")
            self.do_click_by_locator(self.BACK_BUTTON)
            self.do_click_by_locator(self.CANCEL_NO_BUTTON)
            self.do_click_by_locator(self.ORDER_EXCEPTION_PAGE)
            return True
        except Exception as e:
            return False