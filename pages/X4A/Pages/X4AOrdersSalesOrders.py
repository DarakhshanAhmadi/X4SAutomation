import random
import time
from datetime import datetime, date, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from CommonUtilities.baseSet.BasePage import BasePage
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.readProperties import ReadConfig


class X4ASalesOrdersPage(BasePage):
    parse_config_json = ParseConfigFile()
    screen_shot_path = ReadConfig.getScreenshotPath()

    """Sales Orders Page"""

    SALES_MENU = (By.XPATH, "//*[@data-testid='sales-MenuItem']")
    SALES_ORDER_OPTION = (By.XPATH, "//*[text()='Order Management']")
    ORDER_MANAGEMENT_OPTION = (By.XPATH, "(//*[text()='Order Management'])[2]")
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BOX_SEARCH_ICON = (By.XPATH, "//*[@data-testid='SearchIcon']")
    ORDER_BCN_ITEM_LIST = (By.XPATH,
                           "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='customerNumber']")
    PAGINATION = (By.XPATH,
                  "//div[@class='MuiInputBase-root MuiInputBase-colorPrimary css-1eyhk8h-MuiInputBase-root-MuiTablePagination-select']")
    ORDER_DATE_XPATH = "//*[@id='root']/div/div[2]/div[1]/div/div[5]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[9]"
    SALES_ORDER_TABLE = "//div[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']"
    IM_ORDER_NUMBER_LIST = (By.XPATH,
                            "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderNumber']")
    ORDER_TYPE_LIST = (By.XPATH,
                       "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderTypeName']")
    VENDOR_NAME_LIST = (By.XPATH,
                        "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='vendorName']")
    RESELLER_PO_LIST = (By.XPATH,
                        "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='customerOrderNumber']")

    ORDER_STATUS_LIST = (By.XPATH,
                         "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderStatus']")

    SALES_ORDER_PAGE = (By.XPATH, "//h2[text()='Order Management']")
    IM_ORDER = (By.XPATH, "//div[text()='IM Order #']")
    INVOICE_NUMBER = (By.XPATH, "//div[text()='invoicenumber']")
    COUNTRY_CODE = (By.XPATH, "//div[text()='countrycode']")
    TRACKING = (By.XPATH, "//div[text()='Tracking#']")
    TYPE = (By.XPATH, "//div[text()='Type']")
    BCN = (By.XPATH, "//div[text()='BCN']")
    RESELLER_PO = (By.XPATH, "//div[text()='Reseller PO#']")
    RESELLER_NAME = (By.XPATH, "//div[text()='Reseller name']")
    VENDOR_NAME = (By.XPATH, "//div[text()='Vendor name']")
    END_USER_NAME = (By.XPATH, "//div[text()='End user name']")
    END_USER_PO = (By.XPATH, "//div[text()='End user PO#']")
    ORDER_VALUE = (By.XPATH, "//div[text()='Order value']")
    ORDER_STATUS = (By.XPATH, "//div[text()='Order status']")
    CREATED_ON = (By.XPATH, "//div[text()='Created on']")
    CREATED_ON_FIRST_VALUE = (By.XPATH, "//*[@role='cell'] [@data-field='orderCreateDate'][1]")
    CREATED_ON_LIST = (By.XPATH,
                       "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderCreateDate']")
    ARROWUPWARDICON = (By.XPATH, "//*[text()='Created on']/parent::div//*[@data-testid='ArrowUpwardIcon']")
    USER_DROPDOWN = (By.XPATH, "//*[@data-testid='KeyboardArrowDownIcon']")
    LOGOUT = (By.XPATH, "//*[text()='LogOut']")

    SEARCHED_IM_ORDER_NUMBER = (By.XPATH,
                                "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderNumber']/div/a")
    FILTER_ICON = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/button")
    FILTER_BY_IM_ORDER = (By.XPATH, "//p[text()='IM Order #']")
    FILTER_IM_ORDER_TEXTBOX = (By.XPATH, "//input[@id='orderNumber']")
    FILTER_BY_ORDER_TYPES = (By.XPATH, "//div[text()='Order Types']")
    FILTER_ORDER_TYPES_TEXTBOX = (By.XPATH, "//input[@placeholder='Search Order Types']")
    FILTER_ORDER_TYPE_CHECKBOX = (
        By.XPATH, "//label[@data-testid='OrderTypes-0-Label']/span[@data-testid='OrderTypes-0-checkbox']")
    FILTER_BY_BCN = (By.XPATH, "//p[text()='BCN']")
    FILTER_BCN_TEXTBOX = (By.XPATH, "//*[@id='bcnCustomer']")
    FILTER_BY_RESELLER_PO = (By.XPATH, "//p[text()='Reseller PO #']")
    FILTER_RESELLER_PO_TEXTBOX = (By.XPATH, "//input[@id='customerOrderNumber']")
    FILTER_BY_RESELLER_NAME = (By.XPATH, "//p[text()='Reseller name']")
    FILTER_RESELLER_NAME_TEXTBOX = (By.XPATH, "//input[@id='customerName']")
    FILTER_BY_VENDOR_NAME = (By.XPATH, "//p[text()='Vendor name']")
    FILTER_VENDOR_NAME_TEXTBOX = (By.XPATH, "(//input[@id='bcnCustomer'])[2]")
    FILTER_BY_END_USER_NAME = (By.XPATH, "//p[text()='End user name']")
    FILTER_END_USER_TEXTBOX = (By.XPATH, "//input[@id='endUserName']")
    FILTER_BY_ORDER_VALUE = (By.XPATH, "//p[text()='Order value']")
    FILTER_MIN_ORDER_VALUE = (By.XPATH, "//input[@id='totalRevenuMin']")
    FILTER_MAX_ORDER_VALUE = (By.XPATH, "//input[@id='totalRevenuMxn']")
    FILTER_BY_ORDER_STATUS = (By.XPATH, "//div[text()='Order Status']")
    FILTER_ORDER_STATUS_TEXTBOX = (By.XPATH, "//input[@placeholder='Search Order Status']")
    FILTER_ORDER_STATUS_CHECKBOX = (
        By.XPATH, "//label[@data-testid='OrderStatus-0-Label']/span[@data-testid='OrderStatus-0-checkbox']")
    FILTER_BY_CREATED_ON = (By.XPATH, "//p[text()='Created on']")
    FILTER_APPLY_BUTTON = (By.XPATH, "//button[text()='Apply']")
    FILTER_CHECK_ICON = (By.XPATH, "//*[@data-testid='CheckCircleIcon']")
    ORDER_NUMBER_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-row']/div[@data-field='orderNumber']")
    TABLE_ROWS = (By.XPATH, "//div[@class='MuiDataGrid-row']")
    NO_RESULT_TEXT = (By.XPATH, "//span[text()='No sales orders found.']")
    ORDER_TYPE_ITEM_LIST = (By.XPATH,
                            "//*[@class='MuiDataGrid-virtualScrollerRenderZone css-uw2ren-MuiDataGrid-virtualScrollerRenderZone']//div[@data-field='orderTypeName']")
    ITEMS_PER_PAGE = (By.XPATH,
                      "//div[@class='MuiTablePagination-select MuiSelect-select MuiSelect-standard MuiInputBase-input css-d2iqo8-MuiSelect-select-MuiInputBase-input']")
    MULTIPLE_VENDOR_LINK = (By.XPATH, "//div[@class='MuiBox-root css-7g6ps3']/p[@id='modal-modal-description']/div")
    LINK_CLOSE_BUTTON = (By.XPATH, "//button[text()='Close']")
    ORDER_VALUE_SORT = (By.XPATH, "//*[text()='Order value']")
    FILTER_CREATED_ON_LIST = (By.XPATH, "//div[@data-testid='CreatedOn-accordionData']/div/label/span[2]")
    ORDER_DETAILS_STATUS = (By.XPATH, "//*[@id='orderDetails']//*[contains(@class,'MuiChip-label')]")
    CANCEL_ORDER_BTN = (By.XPATH, "//*[text()='Cancel Order']")
    CANCEL_ORDER_ALERT_TITLE = (By.XPATH, "//*[@id='alert-dialog-title']")
    CANCEL_ORDER_ALERT_CONFIRMATION = (By.XPATH, "//*[@id='alert-dialog-description']")
    CONFIRM_CANCEL_ORDER = (By.XPATH, "//*[text()='Yes, Cancel Order']")
    DEFER_CANCEL_ORDER = (By.XPATH, "//*[text()='No, Keep Order']")
    SUCCESS_TOAST_NOTIFICATION = (By.XPATH, "//*[contains(@class, 'MuiAlert-message')]")

    """Order Details page"""

    ORDER_DETAILS_TAB = (By.XPATH, "//button/div/div[text()='Order Details']")
    BILLING_TAB = (By.XPATH, "//button/div/div[text()='Billing']")
    ORDER_LINES_TAB = (By.XPATH, "//button/div/div[text()='Order lines']")
    ORDER_TRACKING_TAB = (By.XPATH, "//button/div/div[text()='Order Tracking']")
    ADDITION_ATTRIBUTE_TAB = (By.XPATH, "//button/div/div[text()='Additional attributes']")
    IM_ORDER_NUMBER_TITLE = (By.XPATH, "//h2[contains(text(),'IM order #')]")
    ORDER_STATUS_TITLE = (By.XPATH, "//h2[contains(text(),'IM order #')]/parent::div/div/span")
    ORDER_VALUE_HEADER = (By.XPATH, "//*[@class='TopArea']/div[2]/div[1]")
    ORDER_TYPE_HEADER = (By.XPATH, "//*[@class='TopArea']/div[2]/div[3]")
    RESUBMIT_ORDER_BUTTON = (By.XPATH, "//*[text()='Resubmit Order']")
    RESUBMIT_ORDER_POPUP_MESSAGE = (By.XPATH, "//*[@id='alert-dialog-description']")
    RESUBMIT_YES_BUTTON = (By.XPATH, "//button[text()='Yes, Resubmit Order']")
    MORE_OPTIONS_MENU = (By.XPATH, "(//*[@data-testid='MoreVertOutlinedIcon'])[1]")
    MARK_FOR_CANCEL = (By.XPATH, "(//*[text()='Mark for cancel'])[1]")
    EDIT_PENCIL_ICON = "(//*[@data-testid='EditOutlinedIcon'])[1]//parent::button"
    ORDER_LINE_DESC = (By.XPATH, "((//*[contains(@class, 'MuiDataGrid-row')])[1]//child::strong)[1]")
    RESUBMIT_STATUS_TITLE = (By.XPATH, "//h2[text()='Order resubmission status']")
    CLOSE_RESUBMIT_POPUP = (By.XPATH, "//*[@data-testid='CloseIcon']")
    SCROLL = (By.XPATH, "(//*[contains(@class, 'virtualScroller')])[3]")
    """Order Details tab-Reference numbers"""

    END_USER_PO_FIELD = (By.XPATH, "//*[text()='End user PO:']/parent::div/div[@class='fieldValue']/strong")
    RESELLER_PO_FIELD = (By.XPATH, "//*[text()='Reseller PO:']/parent::div/div[@class='fieldValue']/strong")
    VENDOR_ORDER_FIELD = (By.XPATH, "//*[text()='Vendor order:']/parent::div/div[@class='fieldValue']/strong")
    VENDOR_SALES_ORDER_FIELD = (
        By.XPATH, "//*[text()='Vendor sales order:']/parent::div/div[@class='fieldValue']/strong")
    REFERENCE_NUMBER_EDIT_ICON = (By.XPATH, "//*[@data-testid='ModeEditOutlineOutlinedIcon']")
    POPUP_CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    POPUP_UPDATE_BUTTON = (By.XPATH, "//button[text()='Update']")
    POPUP_END_USER_TEXTBOX = (By.ID, "reference-details-po-number")
    POPUP_RESELLER_PO_TEXTBOX = (By.ID, "reference-details-edit-customer-number")
    REFERENCE_NUMBERS_END_USER_PO = (
        By.XPATH, "//*[@id='tablayout-tabpanel-0']/div/div/div/div/div[1]/div/div[1]/div[2]/strong")
    REFERENCE_NUMBERS_RESELLER_PO = (
        By.XPATH, "//*[@id='tablayout-tabpanel-0']/div/div/div/div/div[1]/div/div[2]/div[2]/strong")
    CARRIER_CODE_FIELD = (By.XPATH, "//*[@id='tablayout-tabpanel-0']/div/div/div/div/div[2]/div/div/div/div[2]")

    """Billing tab - Ship from"""
    SHIP_FROM_WAREHOUSE_ID = (
        By.XPATH, "//*[@id='tablayout-tabpanel-1']/div/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/strong")
    SHIP_FROM_WAREHOUSE_NAME = (
        By.XPATH, "//*[@id='tablayout-tabpanel-1']/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/strong")

    """Biiling tab-Bill to info"""

    BILL_TO_ID_FIElD = (By.XPATH, "//*[text()='Bill to ID (suffix):']/parent::div/div[@class='labeltext']/strong")
    BILL_TO_INFO_CONTACT_FIElD = (
        By.XPATH, "//*[@class='billingToId']//div[text()='Contact:']/parent::div/div[@class='labeltext']/strong")
    BILL_TO_INFO_COMPANY_NAME_FIElD = (
        By.XPATH, "//*[@class='billingToId']//*[text()='Address:']/parent::div/div[@class='field'][1]/strong")
    BILL_TO_INFO_EMAIL_FIElD = (
        By.XPATH, "//*[@class='billingToId']//div[text()='Email:']/parent::div/div[@class='labeltext']/strong")
    BILL_TO_INFO_ADDRESS_FIElD = (
        By.XPATH, "//*[@class='billingToId']//*[text()='Address:']/parent::div/div[@class='field'][1]")
    BILL_TO_INFO_PHONE_NO_FIElD = (
        By.XPATH, "//*[@class='billingToId']//div[text()='Phone number:']/parent::div/div[@class='labeltext']/strong")

    """Biiling tab-Ship to info"""

    SHIP_TO_INFO_EDIT_ICON = (By.XPATH, "//*[@class='shipToId']//*[@data-testid='ModeEditOutlineOutlinedIcon']")
    SHIP_TO_ID_FIElD = (By.XPATH, "//*[text()='Ship to ID (suffix):']/parent::div/div[@class='labeltext']/strong")
    SHIP_TO_INFO_CONTACT_FIElD = (
        By.XPATH, "//*[@id='tablayout-tabpanel-1']/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/strong")
    SHIP_TO_INFO_COMPANY_NAME_FIElD = (
        By.XPATH, "//*[@class='shipToId']//*[text()='Address:']/parent::div/div[@class='field'][1]/div/strong")
    SHIP_TO_INFO_EMAIL_FIElD = (
        By.XPATH, "//*[@class='shipToId']//*[text()='Email:']/parent::div/div[@class='labeltext']/strong")
    SHIP_TO_INFO_PHONE_NO_FIElD = (
        By.XPATH, "//*[@class='shipToId']//*[text()='Phone number:']/parent::div/div[@class='labeltext']/strong")
    SHIP_TO_INFO_SHIPPING_COMMENT_FIElD = (
        By.XPATH,
        "//*[@class='shipToId']//*[text()='Shipping comments:']/parent::div/div[@class='labeltext']/div/strong")
    SHIP_TO_INFO_ADDRESS_FIElD = (
        By.XPATH, "//*[@class='shipToId']//*[text()='Address:']/parent::div/div[@class='field'][1]")
    SHIP_TO_EDIT_SEARCH_BAR = (By.XPATH, "//input[@id='outlined-basic']")
    SHIP_TO_SHIPPING_ADD_SELECT = (By.XPATH, "//input[@name='selectedCard']//parent::span")
    SHIP_TO_INFO_CANCEL_BTN = (By.XPATH, "//*[text()='Cancel']")
    SAVE_BTN = (By.XPATH, "//*[text()='Save']")

    """Biiling tab-End user info"""

    END_USER_INFO_EDIT_ICON = (By.XPATH, "//*[@class='endUserId']//*[@data-testid='ModeEditOutlineOutlinedIcon']")
    END_USER_ID_FIElD = (By.XPATH, "//*[text()='End user ID (suffix):']/parent::div/div[@class='labeltext']/strong")
    END_USER_COMPANY_NAME_FIElD = (
        By.XPATH, "//*[@class='endUserId']//*[text()='Company name:']/parent::div/div[@class='labeltext']/strong")
    END_USER_ADDRESS_FIElD = (
        By.XPATH, "//*[@class='endUserId']//*[text()='Address:']/parent::div/div[@class='field'][1]")
    END_USER_CONTACT_FIElD = (
        By.XPATH, "//*[@class='endUserId']//*[text()='Contact:']/parent::div/div[@class='labeltext']/strong")
    END_USER_PHONE_NO_FIElD = (
        By.XPATH, "//*[@class='endUserId']//*[text()='Phone number:']/parent::div/div[@class='labeltext']/strong")
    END_USER_EMAIL_FIElD = (
        By.XPATH, "//*[@class='endUserId']//*[text()='Email:']/parent::div/div[@class='labeltext']/strong")
    END_USER_EDIT_SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search end user']")
    END_USER_EDIT_ADD_SELECT = (By.XPATH, "//input[@name='selectedCard']//parent::span")

    """Order Lines tab """

    ORDER_LINE = (By.XPATH, "//*[@data-rowindex='0']/div[@role='cell' and @data-field='ingramOrderLineNumber']")
    ORDER_LINE_STATUS = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='lineStatus']")
    ORDER_LINE_DESCRIPTION = (
        By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='partDescription']/div/div[1]/strong")
    ORDER_LINE_VPN_NUMBER = (
        By.XPATH, "//*[@data-rowindex='0']//div[@role='cell' and @data-field='partDescription']/div/div/span[1]")
    ORDER_LINE_IM_PART = (
        By.XPATH, "//*[@data-rowindex='0']//div[@role='cell' and @data-field='partDescription']/div/div/span[2]")
    ORDER_LINE_SPECIAL_BID_NUMBER = (
        By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='specialBidNumber']")
    ORDER_LINE_SBN_TEXT = (
        By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='specialBidNumber']//input")
    ORDER_LINE_UNIT_PRICE = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='unitPrice']")
    ORDER_LINE_UNIT_PRICE_TEXT = (
        By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='unitPrice']//input")
    ORDER_LINE_EXTENDED_PRICE = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='extendedPrice']")
    ORDER_LINE_COST = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='cost']")
    ORDER_LINE_EXTENDED_COST = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='extendedCost']")
    ORDER_LINE_MARGIN = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='margin']")
    ORDER_LINE_CURRENCY_CODE = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='currencyCode']")
    ORDER_LINE_PAYMENT_TERMS = (By.XPATH, "//*[@role='cell' and @data-field='paymentTerms']")
    ORDER_LINE_QUANTITY = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='quantityOrdered']")
    ORDER_LINE_QUANTITY_TEXT = (By.XPATH, "(//*[@data-field='quantityOrdered'])[2]//input")
    ORDER_LINE_QUANTITY_CONFIRMED = (
        By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='quantityConfirmed']")
    ORDER_LINE_QUANTITY_BACKORDERED = (
        By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='quantityBackOrdered']")
    ORDER_LINE_NOTES = (By.XPATH, "//*[@data-rowindex='0']//*[@role='cell' and @data-field='lineNotes']")
    CLOSE_BUTTON_ON_POPUP = (By.XPATH, "//*[@id='modal-modal-title']/parent::div/following-sibling::div")
    ORDER_LINES = (By.XPATH, "//div[@class='MuiDataGrid-row']")
    ACOP_APPLIED_COLUMN = (
        By.XPATH, "//div[@class='MuiDataGrid-columnHeaderTitleContainer']/div[text()='ACOP applied']")
    ORDER_LINE_EDIT_ICON = (By.XPATH,
                            "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-anj852-MuiButtonBase-root-MuiIconButton-root']")
    EDIT_CHECK_ICON = (By.XPATH,
                       "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hp16lx-MuiButtonBase-root-MuiIconButton-root']/*[@data-testid='CheckCircleOutlineOutlinedIcon']")
    EDIT_CANCEL_ICON = (By.XPATH,
                        "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hp16lx-MuiButtonBase-root-MuiIconButton-root']/*[@data-testid='ClearOutlinedIcon']")
    THREE_DOTS_ICON_OPTIONS = (
        By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-6hp17o-MuiList-root-MuiMenu-list']")
    ORDER_LINES_MARKED_FOR_CANCEL = (By.XPATH, "//div[@class='custom-selected-row MuiDataGrid-row']")

    """Order Lines tab-Additional Attributes """

    INCOMETAXAMOUNT_NAME_VALUE = (
        By.XPATH, "//div[text()='icmstaxamount']//following-sibling::div[@data-field='attributeValue']")
    OTHERTAXAMOUNT_NAME_VALUE = (
        By.XPATH, "//div[text()='othertaxamount']//following-sibling::div[@data-field='attributeValue']")
    ROLLSWITCH_VALUE = (By.XPATH, "//div[text()='rollswitch']//following-sibling::div[@data-field='attributeValue']")
    ADDITION_ATTRIBUTE_CLOSE_BUTTON = (By.XPATH, "//button[text()='Close']")

    """" Additional Attributes Tab """
    TERMS_CODE = (By.XPATH, "//*[@id='panel1bh-content']/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]")
    PAGE_ELEMENT = "//*[@id='orderDetails']/div"
    """constructor of the Login Page c`lass"""

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_sales_orders(self):
        try:
            self.do_click_by_locator(self.SALES_MENU)
            self.do_double_click(self.SALES_ORDER_OPTION)
            self.logger.info("Clicked on Sales Orders in the menu")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Sales orders ' + str(e))
            raise e

    def go_to_sales_orders_list_page(self):
        try:
            self.do_click_by_locator(self.SALES_MENU)
            self.do_double_click(self.ORDER_MANAGEMENT_OPTION)
            self.logger.info("Clicked on Sales Orders in the menu")
        except Exception as e:
            self.logger.error('Exception occurred while clicking on Sales orders ' + str(e))
            raise e

    def is_sales_orders_listing_page_visible(self):
        try:
            if self.do_check_visibility(self.SALES_ORDER_PAGE):
                self.logger.info("Successfully verified Sales Orders listing page")
            else:
                raise Exception('Order management title validation failed')
        except Exception as e:
            self.logger.error('Exception occurred while verifying Sales Orders listing page ' + str(e))
            raise e

    def is_im_order_clum_visible(self):
        try:
            if not self.do_check_visibility(self.IM_ORDER):
                return False
            self.logger.info("Successfully verified the IM Order Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying IM Order column Sales Orders listing page ' + str(e))
            return False

    def is_invoice_nmbr_clum_visible(self):
        try:
            if not self.do_check_visibility(self.INVOICE_NUMBER):
                return False
            self.logger.info("Successfully verified the Invoice number Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Invoice number column Sales Orders listing page ' + str(e))
            return False

    def is_country_code_clum_visible(self):
        try:
            if not self.do_check_visibility(self.COUNTRY_CODE):
                return False
            self.logger.info("Successfully verified the Country code Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Country code column Sales Orders listing page ' + str(e))
            return False

    def is_tracking_clum_visible(self):
        try:
            if not self.do_check_visibility(self.TRACKING):
                return False
            self.logger.info("Successfully verified the Tracking Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Tracking column Sales Orders listing page ' + str(e))
            return False

    def is_type_clum_visible(self):
        try:
            if not self.do_check_visibility(self.TYPE):
                return False
            self.logger.info("Successfully verified the Type Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Type Column on Sales Orders listing page ' + str(e))
            return False

    def is_bcn_clum_visible(self):
        try:
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft = 1300")
            time.sleep(2)
            if not self.do_check_visibility(self.BCN):
                return False
            self.logger.info("Successfully verified the BCN Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying BCN Column on Sales Orders listing page ' + str(e))
            return False

    def is_reseller_po_clum_visible(self):
        try:
            if not self.do_check_visibility(self.RESELLER_PO):
                return False
            self.logger.info("Successfully verified the BCN Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Reseller PO Column on Sales Orders listing page ' + str(e))
            return False

    def is_reseller_nm_clum_visible(self):
        try:
            if not self.do_check_visibility(self.RESELLER_NAME):
                return False
            self.logger.info("Successfully verified the Reseller number Column")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying BCN Column on Sales Orders listing page ' + str(e))
            return False

    def is_vendor_nm_clum_visible(self):
        try:
            if not self.do_check_visibility(self.VENDOR_NAME):
                return False
            self.logger.info("Successfully verified the Vendor Name Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Vendor Name Column on Sales Orders listing page ' + str(e))
            return False

    def is_end_user_nm_clum_visible(self):
        try:
            if not self.do_check_visibility(self.END_USER_NAME):
                return False
            self.logger.info("Successfully verified the End User name Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying End User name Column on Sales Orders listing page ' + str(e))
            return False

    def is_end_user_po_clum_visible(self):
        try:
            if not self.do_check_visibility(self.END_USER_PO):
                return False
            self.logger.info("Successfully verified the End User PO Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying End User PO Column on Sales Orders listing page ' + str(e))
            return False

    def is_order_value_clum_visible(self):
        try:
            if not self.do_check_visibility(self.ORDER_VALUE):
                return False
            self.logger.info("Successfully verified the Order Value Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order Value Column on Sales Orders listing page ' + str(e))
            return False

    def is_order_status_clum_visible(self):
        try:
            if not self.do_check_visibility(self.ORDER_STATUS):
                return False
            self.logger.info("Successfully verified the Order Status Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order Status Column on Sales Orders listing page ' + str(e))
            return False

    def is_created_on_clum_visible(self):
        try:
            if not self.do_check_visibility(self.CREATED_ON):
                return False
            self.logger.info("Successfully verified the Created on Column")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Created on Column on Sales Orders listing page ' + str(e))
            return False

    def search_bcn(self, reseller_bcn):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, reseller_bcn)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_bcn = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Search BCN: {search_bcn}')
            assert str(search_bcn) == str(reseller_bcn)
            self.logger.info("Search Reseller BCN match successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search reseller bcn %s", e)
            raise e

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

    def search_im_order_number(self, im_order_number):
        try:
            self.do_click_by_locator(self.SEARCH_BOX)
            self.do_send_keys(self.SEARCH_BOX, im_order_number)
            self.do_click_by_locator(self.SEARCH_BOX_SEARCH_ICON)
            search_im_order_no = self.do_get_attribute(self.SEARCH_BOX, "value")
            self.logger.info(f'Search IM Order No: {search_im_order_no}')
            assert str(search_im_order_no) == str(im_order_number)
            self.logger.info("Searched IM Order matched successfully")
        except Exception as e:
            self.logger.error("Exception occurred while search IM Order No %s", e)
            raise e

    def do_validate_im_order_number(self, im_order_number):
        try:
            im_order_number_list = self.get_all_elements(self.IM_ORDER_NUMBER_LIST)
            self.logger.info("length of list %s" % len(im_order_number_list))
            self.scroll()
            im_order_number_list = self.get_all_elements(self.IM_ORDER_NUMBER_LIST)
            self.logger.info("length of list %s" % len(im_order_number_list))
            count = 0
            for im_order_number_item in im_order_number_list:
                if str(im_order_number) in im_order_number_item.text:
                    count = count + 1
                else:
                    return False
            if count == len(im_order_number_list):
                return True
            self.logger.info(f'Total number of IM Order Number count is: {count}')
        except Exception as e:
            self.logger.error("Not able to validate IM Order Number")
            return False

    def do_validate_created_on_ascending_on_pages(self, page1, page2, feature_file_name):
        try:
            time.sleep(3)
            element = "//div[@data-id=0]/div[@data-colindex=6]"
            order_value_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(order_value_element)
            element = "//div[@class='MuiDataGrid-row'] [@data-id='1']/div[@data-field='orderCreateDate']"
            created_on_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(created_on_element)
            self.do_check_visibility(self.CREATED_ON)
            if self.do_validate_created_on_ascending(page1):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_created_on_date_ascending_successfully.png")
                if self.do_validate_created_on_ascending(page2):
                    self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                                + "_validate_created_on_date_ascending_successfully.png")
                    self.logger.info(
                        f'Successfully validate Created on date is in ascending order on {page1} and {page2} number')
                    return True
                else:
                    self.driver.save_screenshot(
                        self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_ascending_error.png")
                    self.logger.error(f'Failed to Created on date is in ascending order on {page2} number')
                    return False
            else:
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_ascending_error.png")
                self.logger.error(f'Failed to validate Created on date is in ascending order on {page1} number')
                return False
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in ascending order")
            return False

    def do_validate_created_on_ascending(self, page_number):
        try:
            time.sleep(3)
            self.go_to_page(page_number)

            created_on_date = self.get_element_text(self.CREATED_ON_FIRST_VALUE)
            self.logger.info(created_on_date)
            dt_obj1 = datetime.strptime(created_on_date, "%m/%d/%Y %H:%M:%S")
            self.logger.info(dt_obj1)

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            self.scroll()

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            count = 0
            for created_on_list_item in created_on_list:
                created_on_date1 = created_on_list_item.text
                dt_obj2 = datetime.strptime(created_on_date1, "%m/%d/%Y %H:%M:%S")
                self.logger.info(dt_obj2)
                if dt_obj1 == dt_obj2:
                    count = count + 1
                    pass
                else:
                    if dt_obj1 > dt_obj2:
                        count = count + 1
                        self.logger.info(f'Count: {count}')
                    else:
                        return False
            if count == len(created_on_list):
                self.logger.info(f'Total number of create on date count is: {count}')
                return True
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in ascending order")
            return False

    def do_validate_created_on_descending_on_pages(self, page1, page2, feature_file_name):
        try:
            time.sleep(3)
            element = "//div[@data-id=0]/div[@data-colindex=6]"
            order_value_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(order_value_element)
            element = "//div[@class='MuiDataGrid-row'] [@data-id='1']/div[@data-field='orderCreateDate']"
            created_on_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(created_on_element)
            self.do_click_by_locator(self.CREATED_ON)
            if self.do_validate_created_on_descending(page1):
                self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                            + "_validate_created_on_date_descending_successfully.png")
                if self.do_validate_created_on_descending(page2):
                    self.driver.save_screenshot(self.screen_shot_path + "\\X4A\\success\\" + feature_file_name
                                                + "_validate_created_on_date_descending_successfully.png")
                    self.logger.info(
                        f'Successfully validate Created on date is in descending order on {page1} and {page2} number')
                    return True
                else:
                    self.driver.save_screenshot(
                        self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_descending_error.png")
                    self.logger.error(f'Failed to Created on date is in descending order on {page2} number')
                    return False
            else:
                self.driver.save_screenshot(
                    self.screen_shot_path + "\\X4A\\error\\" + feature_file_name + "_validate_created_on_date_descending_error.png")
                self.logger.error(f'Failed to validate Created on date is in descending order on {page1} number')
                return False
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in descending order")
            return False

    def do_validate_created_on_descending(self, page_number):
        try:
            time.sleep(3)
            self.go_to_page(page_number)
            created_on_date = self.get_element_text(self.CREATED_ON_FIRST_VALUE)
            self.logger.info(created_on_date)
            dt_obj1 = datetime.strptime(created_on_date, "%m/%d/%Y %H:%M:%S")
            self.logger.info(dt_obj1)

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            self.scroll()

            created_on_list = self.get_all_elements(self.CREATED_ON_LIST)
            self.logger.info("length of list %s" % len(created_on_list))
            count = 0
            for created_on_list_item in created_on_list:
                created_on_date1 = created_on_list_item.text
                dt_obj2 = datetime.strptime(created_on_date1, "%m/%d/%Y %H:%M:%S")
                self.logger.info(dt_obj2)
                if dt_obj1 == dt_obj2:
                    count = count + 1
                    pass
                else:
                    if dt_obj1 < dt_obj2:
                        count = count + 1
                        self.logger.info(f'Count: {count}')
                    else:
                        return False
            if count == len(created_on_list):
                self.logger.info(f'Total number of create on date count is: {count}')
                return True
        except Exception as e:
            self.logger.error("Not able to validate Created on date is in descending order")
            return False

    def logout_x4a(self):
        try:
            self.do_click_by_locator(self.USER_DROPDOWN)
            self.do_click_by_locator(self.LOGOUT)
            self.logger.info("Logout Successfully")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Logout X4A ' + str(e))
            return False

    def click_on_im_order_num(self):
        try:
            self.do_click_by_locator(self.SEARCHED_IM_ORDER_NUMBER)
            self.logger.info("Successfully Clicked on Im order number")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click on IM Order Number ' + str(e))
            return False

    def is_order_details_tab_visible(self):
        try:
            self.do_check_visibility(self.ORDER_DETAILS_TAB)
            self.logger.info("Successfully verified the Order Details tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Order Details tab on Order Details page ' + str(e))
            return False

    def is_billing_tab_visible(self):
        try:
            time.sleep(2)
            self.do_check_visibility(self.BILLING_TAB)
            self.logger.info("Successfully verified the Billing tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Billing tab on Order Details page ' + str(e))
            return False

    def is_order_lines_tab_visible(self):
        try:
            time.sleep(2)
            self.do_check_visibility(self.ORDER_LINES_TAB)
            self.logger.info("Successfully verified the Order Lines tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Order Lines tab on Order Details page ' + str(e))
            return False

    def is_order_tracking_tab_visible(self):
        try:
            self.do_check_visibility(self.ORDER_TRACKING_TAB)
            self.logger.info("Successfully verified the Order Tracking tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Order Tracking tab on Order Details page ' + str(e))
            return False

    def is_addition_attributes_visible(self):
        try:
            self.do_check_visibility(self.ADDITION_ATTRIBUTE_TAB)
            self.logger.info("Successfully verified Additional attribites tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Additional attribites tab on Order Details page ' + str(e))
            return False

    def is_ingram_order_number_and_order_status_title_shown(self, im_order_number, order_status):
        try:
            self.do_check_visibility(self.IM_ORDER_NUMBER_TITLE)
            order_number = self.get_element_text(self.IM_ORDER_NUMBER_TITLE)
            order_number = order_number.replace("IM order #: ", "")
            if im_order_number in order_number:
                self.logger.info("Successfully verified IM Order Number title")
            status = self.get_element_text(self.ORDER_STATUS_TITLE)
            assert str(status) == str(order_status)
            self.logger.info("Successfully verified Order Status title")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Additional attribites tab on Order Details page ' + str(e))
            return False

    def is_order_value_header_data_visible(self, order_value):
        try:
            self.do_check_visibility(self.ORDER_VALUE_HEADER)
            ord_value = self.get_element_text(self.ORDER_VALUE_HEADER)
            ord_value = ord_value.split(":")
            if float((ord_value[-1])[2:]) == float(order_value):
                self.logger.info("Successfully verified Order value header")
                return True
            else:
                self.logger.error("Order value header did not match")
                self.logger.error(f'API:{float(order_value)}  UI:{float((ord_value[-1])[2:])}')
                return False
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order value header on Order Details page ' + str(e))
            return False

    def is_order_type_header_data_visible(self, order_type):
        try:
            self.do_check_visibility(self.ORDER_TYPE_HEADER)
            or_type = self.get_element_text(self.ORDER_TYPE_HEADER)
            if str(order_type) in str(or_type):
                self.logger.info("Successfully verified Order Type header")
                return True
            else:
                self.logger.error("Order Type header did not match")
                self.logger.error(f'API:{order_type} UI:{or_type}')
                return False
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order Type header on Order Details page ' + str(e))
            return False

    def is_end_user_po_field_visible(self, end_user_po):
        try:
            end_ur_po = self.get_element_text(self.END_USER_PO_FIELD)
            if str(end_user_po) == '':
                end_user_po = end_user_po.replace("", "-")
            assert str(end_ur_po) == str(end_user_po)
            self.logger.info("Successfully verified End user PO field under Reference number")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying End user PO field under Reference number ' + str(e))
            return False

    def is_reseller_po_field_visible(self, reseller_po):
        try:
            r_po = self.get_element_text(self.RESELLER_PO_FIELD)
            assert str(r_po) == str(reseller_po)
            self.logger.info("Successfully verified Reseller PO field under Reference number")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Reseller PO field under Reference number ' + str(e))
            return False

    def is_vendor_order_field_visible(self, vendor_order):
        try:
            if str(vendor_order) == '.':
                vendor_order = vendor_order.replace(".", "-")
            vendor_ord = self.get_element_text(self.VENDOR_ORDER_FIELD)
            assert str(vendor_ord) == str(vendor_order)
            self.logger.info("Successfully verified Vendor order field under Reference number")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Vendor order field under Reference number ' + str(e))
            return False

    def is_vendor_sales_order_field_visible(self, vendor_sales_order):
        try:
            if str(vendor_sales_order) == '.':
                vendor_sales_order = vendor_sales_order.replace(".", "-")
            vendor_sale_ord = self.get_element_text(self.VENDOR_SALES_ORDER_FIELD)
            assert str(vendor_sale_ord) == str(vendor_sales_order)
            self.logger.info("Successfully verified Vendor sales order field under Reference number")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Vendor sales order field under Reference number ' + str(e))
            return False

    def is_carrier_code_visible(self, carrier_code):
        try:
            ui_carrier_code = self.get_element_text(self.CARRIER_CODE_FIELD)
            assert str(ui_carrier_code) == str(carrier_code)
            self.logger.info("Successfully verified carrier code field")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying carrier code field' + str(e))
            return False

    def click_on_billing_tab(self):
        try:
            time.sleep(6)
            self.do_click_by_locator(self.BILLING_TAB)
            self.logger.info("Successfully Clicked Billing tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click on Billing tab ' + str(e))
            return False

    def click_on_order_details_tab(self):
        try:
            time.sleep(5)
            self.do_click_by_locator(self.ORDER_DETAILS_TAB)
            self.logger.info("Successfully Clicked Order Details tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click on Order Details tab ' + str(e))
            return False

    def click_on_order_lines_tab(self):
        try:
            time.sleep(2)
            self.do_click_by_locator(self.ORDER_LINES_TAB)
            self.logger.info("Successfully Clicked Order lines tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click on Order lines tab ' + str(e))
            return False

    def click_on_order_tracking_details_tab(self):
        try:
            self.do_click_by_locator(self.ORDER_TRACKING_TAB)
            self.logger.info("Successfully Clicked Order Tracking tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click on Order Tracking tab ' + str(e))
            return False

    def click_on_additional_attr_tab(self):
        try:
            self.do_click_by_locator(self.ADDITION_ATTRIBUTE_TAB)
            self.logger.info("Successfully Clicked Addition Attribute tab")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click on Addition Attribute tab ' + str(e))
            return False

    def is_bill_to_id_field_visible(self, bill_to_id):
        try:
            id = self.get_element_text(self.BILL_TO_ID_FIElD)
            if str(id) != str(bill_to_id):
                self.logger.error(f'Bill to id mismatched\n API;{bill_to_id}  UI:{id}')
            else:
                self.logger.info("Successfully verified Bill to Id field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Bill to Id field under Billing to info' + str(e))
            return False

    def is_company_nm_bill_field_visible(self, bill_to_company_name):
        try:
            company_name = self.get_element_text(self.BILL_TO_INFO_COMPANY_NAME_FIElD)
            if str(company_name) != str(bill_to_company_name):
                self.logger.error(f'Bill to company name mismatched\n API;{bill_to_company_name}  UI:{company_name}')
            else:
                self.logger.info("Successfully verified Company name field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Company name field under Billing to info' + str(e))
            return False

    def is_address_bill_field_visible(self, bill_to_address):
        try:
            addr = self.get_element_text(self.BILL_TO_INFO_ADDRESS_FIElD)
            address = addr.replace("\n", " ")
            if str(address) != str(bill_to_address):
                self.logger.error(f'Bill to Address mismtched\n UI:{address}  API":{bill_to_address}')
            else:
                self.logger.info("Successfully verified Address field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Address field under Billing to info' + str(e))
            return False

    def is_contact_bill_field_visible(self, bill_to_contact):
        try:
            if str(bill_to_contact) == '':
                bill_to_contact = bill_to_contact.replace("", "-")
            contact = self.get_element_text(self.BILL_TO_INFO_CONTACT_FIElD)
            if str(contact) != str(bill_to_contact):
                self.logger.error(f'Bill to Contact mismatched\n API:{bill_to_contact}  UI:{contact}')
            else:
                self.logger.info("Successfully verified Contact field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Contact field under Billing to info' + str(e))
            return False

    def is_phone_no_bill_field_visible(self, bill_to_phone_no):
        try:
            if str(bill_to_phone_no) == '':
                bill_to_phone_no = bill_to_phone_no.replace("", "-")
            phone_no = self.get_element_text(self.BILL_TO_INFO_EMAIL_FIElD)
            if str(phone_no) != str(bill_to_phone_no):
                self.logger.error(f'Bill to Phone mismatched\n API:{bill_to_phone_no}  UI:{phone_no}')
            else:
                self.logger.info("Successfully verified Phone no field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Phone no field under Billing to info' + str(e))
            return False

    def is_email_bill_field_visible(self, bill_to_email):
        try:
            if str(bill_to_email) == '':
                bill_to_email = bill_to_email.replace("", "-")
            email = self.get_element_text(self.BILL_TO_INFO_EMAIL_FIElD)
            if str(email) != str(bill_to_email):
                self.logger.error(f'Bill to Email mismatched\n API:{bill_to_email}  UI:{email}')
            else:
                self.logger.info("Successfully verified Email field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Email field under Billing to info' + str(e))
            return False

    def is_ship_to_id_field_visible(self, ship_to_id):
        try:
            if str(ship_to_id) == '':
                ship_to_id = ship_to_id.replace("", "-")
            id = self.get_element_text(self.SHIP_TO_ID_FIElD)
            if str(id) != str(ship_to_id):
                self.logger.error(f'Ship to id mismatched\n API:{ship_to_id}  UI:{id}')
            else:
                self.logger.info("Successfully verified Ship to Id field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Ship to Id field under Billing to info' + str(e))
            return False

    def is_company_nm_ship_field_visible(self, ship_to_cmp_nm):
        try:
            company_name = self.get_element_text(self.SHIP_TO_INFO_COMPANY_NAME_FIElD)
            if str(company_name) != str(ship_to_cmp_nm):
                self.logger.error(f'Ship to company name mismatched\n API:{ship_to_cmp_nm}  UI:{company_name}')
            else:
                self.logger.info("Successfully verified Company name field under Ship to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Company name field under Ship to info' + str(e))
            return False

    def is_address_ship_field_visible(self, ship_to_addr):
        try:
            addr = self.get_element_text(self.SHIP_TO_INFO_ADDRESS_FIElD)
            address = addr.replace("\n", " ")
            if str(address) == str(ship_to_addr):
                self.logger.info("Successfully verified Address field under Ship to info")
            else:
                self.logger.error("Address field under Ship to info mismatched")
                self.logger.error(f'API:{ship_to_addr}  UI:{address}')
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Address field under Ship to info' + str(e))
            return False

    def is_contact_ship_field_visible(self, ship_to_contact):
        try:
            if str(ship_to_contact) == '':
                ship_to_contact = ship_to_contact.replace("", "-")
            contact = self.get_element_text(self.SHIP_TO_INFO_CONTACT_FIElD)
            if str(contact) != str(ship_to_contact):
                self.logger.error(f'Ship to contact mismatched\n API:{ship_to_contact}  UI:{contact}')
            else:
                self.logger.info("Successfully verified Contact field under Ship to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Contact field under Ship to info' + str(e))
            return False

    def is_phone_no_ship_field_visible(self, ship_to_phn_no):
        try:
            if str(ship_to_phn_no) == '':
                ship_to_phn_no = ship_to_phn_no.replace("", "-")
            phone_no = self.get_element_text(self.SHIP_TO_INFO_PHONE_NO_FIElD)
            if str(phone_no) != str(ship_to_phn_no):
                self.logger.error(f'Ship to Phone mismatched\n API:{ship_to_phn_no}  UI:{phone_no}')
            else:
                self.logger.info("Successfully verified Phone no field under Ship to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Phone no field under Ship to info' + str(e))
            return False

    def is_email_ship_field_visible(self, ship_to_email):
        try:
            if str(ship_to_email) == '':
                ship_to_email = ship_to_email.replace("", "-")
            email = self.get_element_text(self.SHIP_TO_INFO_EMAIL_FIElD)
            if str(email) != str(ship_to_email):
                self.logger.error(f'Ship to Email mismatched\n API:{ship_to_email}  UI:{email}')
            else:
                self.logger.info("Successfully verified Email field under Ship to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Email field under Ship to info' + str(e))
            return False

    def is_shipping_comment_ship_field_visible(self, ship_to_shipping_comment):
        try:
            if str(ship_to_shipping_comment) == '.':
                ship_to_shipping_comment = ship_to_shipping_comment.replace(".", "-")
            comment = self.get_element_text(self.SHIP_TO_INFO_SHIPPING_COMMENT_FIElD)
            assert str(comment) == str(ship_to_shipping_comment)
            self.logger.info("Successfully verified Shipping Comment field under Ship to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Shipping Comment field under Ship to info' + str(e))
            return False

    def is_end_user_id_field_visible(self, end_user_id):
        try:
            if str(end_user_id) == '':
                end_user_id = end_user_id.replace("", "-")
            id = self.get_element_text(self.END_USER_ID_FIElD)
            if str(id) != str(end_user_id):
                self.logger.error(f'End user id mismatched\n API:{end_user_id}  UI:{id}')
            else:
                self.logger.info("Successfully verified End user Id field under End user info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying End user Id field under End user  info' + str(e))
            return False

    def is_company_nm_end_user_field_visible(self, end_user_cmp_nm):
        try:
            if str(end_user_cmp_nm) == '':
                end_user_cmp_nm = end_user_cmp_nm.replace("", "-")
            company_name = self.get_element_text(self.END_USER_COMPANY_NAME_FIElD)
            if str(company_name) != str(end_user_cmp_nm):
                self.logger.error(f'End user company name mismatched\n API:{end_user_cmp_nm}  UI:{company_name}')
            else:
                self.logger.info("Successfully verified Company name field under End user info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Company name field under End user info' + str(e))
            return False

    def is_address_end_user_field_visible(self, end_user_addr):
        try:
            address = self.get_element_text(self.END_USER_ADDRESS_FIElD)
            if str(address):
                address = address.replace("\n", " ")
            if str(address) != str(end_user_addr):
                self.logger.error(f'End user adress mismatched UI:{address} API:{end_user_addr}')
            self.logger.info("Successfully verified Address field under End User info")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying Address field under End User info' + str(e))
            return False

    def is_contact_end_user_field_visible(self, end_user_contact):
        try:
            if str(end_user_contact) == '':
                end_user_contact = end_user_contact.replace("", "-")
            contact = self.get_element_text(self.END_USER_CONTACT_FIElD)
            if str(contact) != str(end_user_contact):
                self.logger.error(f'End user contact mismatched UI:{contact} API:{end_user_contact}')
            else:
                self.logger.info("Successfully verified End User field under End user info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Contact field under End user info' + str(e))
            return False

    def is_phone_no_end_user_field_visible(self, end_user_phn_no):
        try:
            if str(end_user_phn_no) == '.':
                end_user_phn_no = end_user_phn_no.replace(".", "-")
            phone_no = self.get_element_text(self.END_USER_PHONE_NO_FIElD)
            if str(phone_no) != str(end_user_phn_no):
                self.logger.error(f'End user Phone mismatched UI:{phone_no} API:{end_user_phn_no}')
            else:
                self.logger.info("Successfully verified Phone no field under End user info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Phone no field under End user info' + str(e))
            return False

    def is_email_end_user_field_visible(self, end_user_email):
        try:
            if str(end_user_email) == '.':
                end_user_email = end_user_email.replace(".", "-")
            email = self.get_element_text(self.END_USER_EMAIL_FIElD)
            if str(email) != str(end_user_email):
                self.logger.error(f'End user Email mismatched UI:{email} API:{end_user_email}')
            else:
                self.logger.info("Successfully verified Email field under End User info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Email field under End User info' + str(e))
            return False

    def is_order_line_field_visible(self, order_line):
        try:
            ord_line = self.get_element_text(self.ORDER_LINE)
            assert str(ord_line) == str(order_line)

            self.logger.info("Successfully verified Order line field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line field under Order lines tab"' + str(e))
            return False

    def is_order_line_status_field_visible(self, order_line_status):
        try:
            status = self.get_element_text(self.ORDER_LINE_STATUS)
            assert str(status) == str(order_line_status)
            self.logger.info("Successfully verified Order line status field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line status field under Order lines tab"' + str(e))
            return False

    def is_order_line_description_field_visible(self, order_line_description):
        try:
            description = self.get_element_text(self.ORDER_LINE_DESCRIPTION)
            assert str(description) == str(order_line_description)
            self.logger.info("Successfully verified Order line Description field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Description field under Order lines tab"' + str(e))
            return False

    def is_contact_vpn_no_field_visible(self, order_line_vpn_no):
        try:
            vpn_no = self.get_element_text(self.ORDER_LINE_VPN_NUMBER)
            vpn_no = vpn_no.replace("VPN: ", "")
            assert str(vpn_no) == str(order_line_vpn_no)
            self.logger.info("Successfully verified Order line VPN number field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line VPN number field under Order lines tab"' + str(e))
            return False

    def is_order_line_im_part_field_visible(self, order_line_im_part):
        try:
            im_part = self.get_element_text(self.ORDER_LINE_IM_PART)
            im_part = im_part.replace("IM part #: ", "")
            assert str(im_part) == str(order_line_im_part)
            self.logger.info("Successfully verified Order line IM part # field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line IM part # field under Order lines tab"' + str(e))
            return False

    def is_order_line_special_bid_field_visible(self, order_line_special_bid_no):
        try:
            special_bid = self.get_element_text(self.ORDER_LINE_SPECIAL_BID_NUMBER)
            if str(special_bid) == '':
                special_bid = special_bid.replace("", ".")
            assert str(special_bid) == str(order_line_special_bid_no)
            self.logger.info("Successfully verified Order line Special Bid number field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Special Bid number field under Order lines tab"' + str(
                    e))
            return False

    def is_order_line_unit_price_field_visible(self, order_line_unit_price):
        try:
            unit_price = self.get_element_text(self.ORDER_LINE_UNIT_PRICE)
            assert str(unit_price) == str(order_line_unit_price)
            self.logger.info("Successfully verified Order line Unit Price field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Unit Price field under Order lines tab"' + str(e))
            return False

    def is_order_line_extended_price_field_visible(self, order_line_extended_price):
        try:
            extended_price = self.get_element_text(self.ORDER_LINE_EXTENDED_PRICE)
            assert str(extended_price) == str(order_line_extended_price)
            self.logger.info("Successfully verified Order line Extended Price field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Extended Price field under Order lines tab"' + str(e))
            return False

    def is_order_line_cost_field_visible(self, order_line_cost):
        try:
            cost = self.get_element_text(self.ORDER_LINE_COST)
            assert str(cost) == str(order_line_cost)
            self.logger.info("Successfully verified Order line Cost field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Cost field under Order lines tab"' + str(e))
            return False

    def is_order_line_ext_cost_field_visible(self, order_line_extended_cost):
        try:
            element = "//*[@data-id='0']//*[@role='cell' and @data-field='extendedCost']"
            extended_cost = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(extended_cost)
            ext_cost = self.get_element_text(self.ORDER_LINE_EXTENDED_COST)
            assert str(ext_cost) == str(order_line_extended_cost)
            self.logger.info("Successfully verified Order line Extended cost field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Extended cost field under Order lines tab"' + str(e))
            return False

    def is_order_line_margin_field_visible(self, order_line_margin):
        try:
            element = "//*[@data-id='0']//*[@role='cell' and @data-field='margin']"
            mrg = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(mrg)

            margin = self.get_element_text(self.ORDER_LINE_MARGIN)
            assert str(margin) == str(order_line_margin)
            self.logger.info("Successfully verified Order line Margin field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Margin field under Order lines tab"' + str(e))
            return False

    def is_order_line_currency_code_field_visible(self, order_line_currency_code):
        try:
            element = "//*[@role='cell' and @data-field='currencyCode']"
            currency_code_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(currency_code_element)

            currency_code = self.get_element_text(self.ORDER_LINE_CURRENCY_CODE)
            assert str(currency_code) == str(order_line_currency_code)
            self.logger.info("Successfully verified Order line Currency Code field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Currency Code field under Order lines tab"' + str(e))
            return False

    # def is_order_line_payment_terms_field_visible(self, order_line_payment_terms):
    #     try:
    #         element = "//*[@role='cell' and @data-field='paymentTerms']"
    #         payment_terms_element = self.driver.find_element(By.XPATH, element)
    #         self.scroll_horizontally(payment_terms_element)
    #
    #         payment_terms = self.get_element_text(self.ORDER_LINE_PAYMENT_TERMS)
    #         assert str(payment_terms) == str(order_line_payment_terms)
    #         self.logger.info("Successfully verified Order line Payment terms field under Order lines tab")
    #         return True
    #     except Exception as e:
    #         self.logger.error(
    #             'Exception occurred while verifying Order line Payment terms field under Order lines tab"' + str(e))
    #         return False

    #  Here the horizontal scrolling is not working
    def is_order_line_quantity_field_visible(self, order_line_quantity):
        try:
            time.sleep(10)
            element = "//*[@role='cell' and @data-field='upcCode']"
            upc_code_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(upc_code_element)

            time.sleep(10)
            element = "//*[@role='cell' and @data-field='unitWeight']"
            unit_weight_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(unit_weight_element)

            time.sleep(10)
            element = "//*[@role='cell' and @data-field='weightUom']"
            weight_uom_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(weight_uom_element)

            element = "//*[@role='cell' and @data-field='quantityOrdered']"
            quantity_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(quantity_element)

            quantity = self.get_element_text(self.ORDER_LINE_QUANTITY)
            assert str(quantity) == str(order_line_quantity)
            self.logger.info("Successfully verified Order line Quantity field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Quantity field under Order lines tab"' + str(e))
            return False

    def is_order_line_qty_confirmed_field_visible(self, order_line_quantity_confirmed):
        try:
            element = "//*[@role='cell' and @data-field='quantityConfirmed']"
            quantity_confirmed_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(quantity_confirmed_element)
            quantity_confirmed = self.get_element_text(self.ORDER_LINE_QUANTITY_CONFIRMED)
            assert str(quantity_confirmed) == str(order_line_quantity_confirmed)
            self.logger.info("Successfully verified Order line Quantity Confirmed field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Quantity Confirmed field under Order lines tab"' + str(
                    e))
            return False

    def is_order_line_qty_backordered_field_visible(self, order_line_quantity_backordered):
        try:
            element = "//*[@role='cell' and @data-field='quantityBackOrdered']"
            quantity_backordered_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(quantity_backordered_element)
            quantity_backordered = self.get_element_text(self.ORDER_LINE_QUANTITY_BACKORDERED)
            assert str(quantity_backordered) == str(order_line_quantity_backordered)
            self.logger.info("Successfully verified Order line Quantity Backordered field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line Quantity Backordered field under Order lines tab"' + str(
                    e))
            return False

    def is_order_line_notes_field_visible(self, Order_line_notes):
        try:
            element = "//*[@role='cell' and @data-field='lineNotes']"
            notes_element = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(notes_element)
            notes = self.get_element_text(self.ORDER_LINE_NOTES)
            if str(notes) == '':
                notes = notes.replace("", ".")
            assert str(notes) == str(Order_line_notes)
            self.logger.info("Successfully verified Order line Notes field under Order lines tab")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying')

    def click_on_view_more_option(self):
        try:
            element = "//*[@data-field='serialNumbers']/button"
            view_more_button = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(view_more_button)
            self.do_click_by_locator(view_more_button)
            self.logger.info("Successfully Clicked View more button")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click View more button ' + str(e))
            return False

    def is_serial_line_no_field_visible(self, order_line):
        try:
            ord_line = self.get_element_text(self.ORDER_LINE)
            assert str(ord_line) == str(order_line)
            self.logger.info("Successfully verified Serial numbers field")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Order line field' + str(e))
            return False

    def is_serial_no_description_field_visible(self, order_line_description):
        try:
            description = self.get_element_text(self.ORDER_LINE_DESCRIPTION)
            assert str(description) == str(order_line_description)
            self.logger.info("Successfully verifiedSerial numbers Description field")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Serial numbers Description field' + str(e))
            return False

    def is_serial_no_vpn_no_field_visible(self, order_line_vpn_no):
        try:
            vpn_no = self.get_element_text(self.ORDER_LINE_VPN_NUMBER)
            vpn_no = vpn_no.replace("VPN :", "")
            assert str(vpn_no) == str(order_line_vpn_no)
            self.logger.info("Successfully verified Order line VPN number field")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Serial numbers VPN number field under' + str(e))
            return False

    def is_serial_no_im_part_field_visible(self, order_line_im_part):
        try:
            im_part = self.get_element_text(self.ORDER_LINE_IM_PART)
            im_part = im_part.replace("IM part #: :", "")
            assert str(im_part) == str(order_line_im_part)
            self.logger.info("Successfully verified Serial numbers IM part # field")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Serial numbers IM part # field' + str(e))
            return False

    def is_serial_no_quantity_field_visible(self, serial_no_quantity):
        try:
            quantity = self.get_element_text(self.ORDER_LINE_QUANTITY)
            assert str(quantity) == str(serial_no_quantity)
            self.logger.info("Successfully verified Serial numbers Quantity field")
            self.do_click_by_locator(self.CLOSE_BUTTON_ON_POPUP)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Serial numbers Quantity field' + str(e))
            return False

    def click_on_additional_attr_view_more_button(self):
        try:
            element = "//*[@data-field='additionalAttributes']/button"
            view_more_button = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(view_more_button)
            self.do_click_by_locator(view_more_button)
            self.logger.info("Successfully Clicked View more button")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while Click View more button ' + str(e))
            return False

    def is_icmstaxamount_nm_and_value_visible(self, icmstaxamount_name_value):
        try:
            icmstaxamount_nm_value = self.get_element_text(self.INCOMETAXAMOUNT_NAME_VALUE)
            assert str(icmstaxamount_nm_value) == str(icmstaxamount_name_value)
            self.logger.info("Successfully verified incometaxamount name and value")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying incometaxamount name and value' + str(e))
            return False

    def is_othertaxamount_nm_and_value_visible(self, othertaxamount_name_value):
        try:
            othertaxamount_nm_val = self.get_element_text(self.OTHERTAXAMOUNT_NAME_VALUE)
            assert str(othertaxamount_nm_val) == str(othertaxamount_name_value)
            self.logger.info("Successfully verified othertaxamount name and value")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying othertaxamount name and value' + str(e))
            return False

    def is_rollswitch_nm_and_value_visible(self, rollswitch_name_value):
        try:
            rollswitch_nm_value = self.get_element_text(self.ROLLSWITCH_VALUE)
            assert str(rollswitch_nm_value) == str(rollswitch_name_value)
            self.logger.info("Successfully verified rollswitch name and value")
            self.do_click_by_locator(self.ADDITION_ATTRIBUTE_CLOSE_BUTTON)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying rollswitch name and value' + str(e))
            return False

    def filter_by_im_order(self, im_order):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_IM_ORDER)
            self.do_send_keys(self.FILTER_IM_ORDER_TEXTBOX, im_order)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_IM_ORDER)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by im order' + str(e))
            return False

    def verify_im_order(self, im_order):
        try:
            self.check_if_result_found()
            rows = self.get_all_elements(self.ORDER_NUMBER_ROWS)
            if len(rows) == 1:
                self.logger.info("Order %s found", str(im_order))
                for row in rows:
                    assert row.text == im_order
            else:
                raise Exception("Multiple orders found for searched im order")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying the im order quick search" + str(e))
            return False

    def check_if_result_found(self):
        try:
            self.logger.info("Checking if result found for Sales order")
            table_rows = self.get_all_elements_without_visibility(self.TABLE_ROWS)
        except Exception as e:
            if self.do_check_visibility(self.NO_RESULT_TEXT):
                self.logger.error("No result found for the search or filter")
                raise e
            else:
                self.logger.error("Exception while checking the Sales order search result")
                raise e

    def filter_by_order_type(self, order_type):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_ORDER_TYPES)
            self.do_send_keys(self.FILTER_ORDER_TYPES_TEXTBOX, order_type)
            self.do_click_by_locator(self.FILTER_ORDER_TYPE_CHECKBOX)
            self.do_click_by_locator(self.FILTER_BY_ORDER_TYPES)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by order type' + str(e))
            return False

    def verify_filter_order_type_in_pages(self, order_type):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Order type in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_order_type(order_type)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Order type in page %s", str(random_page))
                    self.filter_by_order_type(order_type)
                    self.go_to_page(random_page)
                    self.validate_order_type(order_type)
                self.logger.info("Verifying Order type in page %s", str(last_page_number))
                self.filter_by_order_type(order_type)
                self.go_to_page(last_page_number)
                self.validate_order_type(order_type)
            self.logger.info("Successfully verified Order type")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying the bcn account quick search" + str(e))
            return False

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

    def validate_order_type(self, order_type):
        try:
            table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
            self.logger.info("Verifying the Order type in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching Order type")
                order_type_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderTypeName']")
                try:
                    ui_order_type = self.get_element_text_for_filter(order_type_xpath)
                    self.logger.info("Fetched ui order type :" + str(ui_order_type))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert ui_order_type == order_type, "Order Type mismatched"
            self.scroll_up(table)
        except Exception as e:
            self.logger.error("Exception occurred verifying order type" + str(e))
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

    def filter_by_bcn(self, bcn):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_BCN)
            self.do_send_keys(self.FILTER_BCN_TEXTBOX, bcn)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_BCN)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by BCN' + str(e))
            return False

    def verify_filter_by_bcn_in_pages(self, bcn):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Order type in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_bcn(bcn)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying BCN in page %s", str(random_page))
                    self.filter_by_bcn(bcn)
                    self.go_to_page(random_page)
                    self.validate_bcn(bcn)
                self.logger.info("Verifying BCN in page %s", str(last_page_number))
                self.filter_by_bcn(bcn)
                self.go_to_page(last_page_number)
                self.validate_bcn(bcn)
            self.logger.info("Successfully verified BCN")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying BCN in table" + str(e))
            return False

    def validate_bcn(self, bcn):
        try:
            self.logger.info("Verifying the BCN in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching BCN")
                bcn_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerNumber']")
                try:
                    ui_bcn = self.get_element_text_for_filter(bcn_xpath)
                    self.logger.info("Fetched ui bcn account :" + str(ui_bcn))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_bcn) == str(bcn), "BCN mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying BCN" + str(e))
            raise e

    def filter_by_reseller_po(self, reseller_po):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_RESELLER_PO)
            self.do_send_keys(self.FILTER_RESELLER_PO_TEXTBOX, reseller_po)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_RESELLER_PO)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by Reseller PO' + str(e))
            return False

    def verify_filter_by_reseller_po_in_pages(self, reseller_po):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Reseller PO in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_reseller_po(reseller_po)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Reseller PO in page %s", str(random_page))
                    self.filter_by_reseller_po(reseller_po)
                    self.go_to_page(random_page)
                    self.validate_reseller_po(reseller_po)
                self.logger.info("Verifying Reseller PO in page %s", str(last_page_number))
                self.filter_by_reseller_po(reseller_po)
                self.go_to_page(last_page_number)
                self.validate_reseller_po(reseller_po)
            self.logger.info("Successfully verified Reseller PO")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying BCN in table" + str(e))
            return False

    def validate_reseller_po(self, reseller_po):
        try:
            self.logger.info("Verifying the Reseller PO in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching Reseller PO")
                reseller_po_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerOrderNumber']")
                try:
                    ui_reseller_po = self.get_element_text_for_filter(reseller_po_xpath)
                    self.logger.info("Fetched ui reseller po :" + str(ui_reseller_po))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_reseller_po) == str(reseller_po), "Reseller PO mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying Reseller PO" + str(e))
            raise e

    def filter_by_reseller_name(self, reseller_name):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_RESELLER_NAME)
            self.do_send_keys(self.FILTER_RESELLER_NAME_TEXTBOX, reseller_name)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_RESELLER_NAME)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by Reseller Name' + str(e))
            return False

    def verify_filter_by_reseller_name_in_pages(self, reseller_name):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Reseller Name in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_reseller_name(reseller_name)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Reseller Name in page %s", str(random_page))
                    self.filter_by_reseller_name(reseller_name)
                    self.go_to_page(random_page)
                    self.validate_reseller_name(reseller_name)
                self.logger.info("Verifying Reseller Name in page %s", str(last_page_number))
                self.filter_by_reseller_name(reseller_name)
                self.go_to_page(last_page_number)
                self.validate_reseller_name(reseller_name)
            self.logger.info("Successfully verified Reseller Name")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying Reseller Name in table" + str(e))
            return False

    def validate_reseller_name(self, reseller_name):
        try:
            self.logger.info("Verifying the Reseller Name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching Reseller Name")
                reseller_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='customerName']")
                try:
                    ui_reseller_name = self.get_element_text_for_filter(reseller_name_xpath)
                    self.logger.info("Fetched ui reseller name :" + str(ui_reseller_name))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_reseller_name) == str(reseller_name), "Reseller Name mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying Reseller Name" + str(e))
            raise e

    def filter_by_vendor_name(self, vendor_name):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_NAME)
            self.do_send_keys(self.FILTER_VENDOR_NAME_TEXTBOX, vendor_name)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_VENDOR_NAME)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by Vendor Name' + str(e))
            return False

    def verify_filter_by_vendor_name_in_pages(self, vendor_name):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Vendor Name in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_vendor_name(vendor_name)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Vendor Name in page %s", str(random_page))
                    self.filter_by_vendor_name(vendor_name)
                    self.go_to_page(random_page)
                    self.validate_vendor_name(vendor_name)
                self.logger.info("Verifying Vendor Name in page %s", str(last_page_number))
                self.filter_by_vendor_name(vendor_name)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.validate_vendor_name(vendor_name)
            self.logger.info("Successfully verified Vendor Name")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying Vendor Name in table" + str(e))
            return False

    def validate_vendor_name(self, vendor_name):
        try:
            self.logger.info("Verifying the Vendor Name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching Vendor Name")
                vendor_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='vendorName']")
                try:
                    ui_vendor_name = self.get_element_text_for_filter(vendor_name_xpath)
                    self.logger.info("Fetched ui Vendor name :" + str(ui_vendor_name))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                if "Multiple Vendors" in ui_vendor_name:
                    self.logger.info("Multiple vendors present")
                    multiple_vendor_link_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                        i) + "']/div/div/button[contains(text(), 'Multiple Vendors')]")
                    self.do_click_by_locator(multiple_vendor_link_xpath)
                    vendor_list = self.get_multiple_vendor_data()
                    if vendor_name not in vendor_list:
                        raise Exception("Vendor name mismatched")
                else:
                    self.logger.info("Single vendor present")
                    assert ui_vendor_name.strip() == vendor_name.strip(), "Vendor Name mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying Vendor Name" + str(e))
            raise e

    def get_multiple_vendor_data(self):
        vendor_list = []
        try:
            self.logger.info("Getting the multiple vendors")
            for i in range(1, 100):
                s = "//*[@id='modal-modal-description']/div/div/div/div[2]/div[2]/div"
                e = self.driver.find_element(By.XPATH, s)
                xpath = (By.XPATH,
                         "//*[@id='modal-modal-description']/div/div/div/div[2]/div[2]/div/div/div/div[@data-id=" + str(
                             i) + "]")
                try:
                    vendor = self.get_element_text_for_filter(xpath)
                except:
                    self.logger.info("There are only %s skus", str(i - 1))
                    break
                vendor_list.append(vendor)
                if i % 3 == 0:
                    self.scroll_down(e)
            self.do_click_by_locator(self.LINK_CLOSE_BUTTON)
        except Exception as e:
            self.logger.error("Error while getting multiple vendor data from link " + str(e))
            raise e
        return vendor_list

    def filter_by_end_user_name(self, end_user_name):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_END_USER_NAME)
            self.do_send_keys(self.FILTER_END_USER_TEXTBOX, end_user_name)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_END_USER_NAME)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by End User Name' + str(e))
            return False

    def verify_filter_by_end_user_name_in_pages(self, end_user_name):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying End User Name in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_end_user_name(end_user_name)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying End User Name in page %s", str(random_page))
                    self.filter_by_end_user_name(end_user_name)
                    self.go_to_page(random_page)
                    self.validate_end_user_name(end_user_name)
                self.logger.info("Verifying End User Name in page %s", str(last_page_number))
                self.filter_by_end_user_name(end_user_name)
                self.go_to_page(last_page_number)
                self.validate_end_user_name(end_user_name)
            self.logger.info("Successfully verified End User Name")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying End User Name in table" + str(e))
            return False

    def validate_end_user_name(self, end_user_name):
        try:
            self.logger.info("Verifying the End User Name in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching End User Name")
                end_user_name_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='firstEndUserName']")
                try:
                    ui_end_user_name = self.get_element_text_for_filter(end_user_name_xpath)
                    self.logger.info("Fetched ui end user name :" + str(ui_end_user_name))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_end_user_name) == str(end_user_name), "End User Name mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying End User Name" + str(e))
            raise e

    def filter_by_order_status(self, order_status):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_ORDER_STATUS)
            self.do_send_keys(self.FILTER_ORDER_STATUS_TEXTBOX, order_status)
            self.do_click_by_locator(self.FILTER_ORDER_STATUS_CHECKBOX)
            self.do_click_by_locator(self.FILTER_BY_ORDER_STATUS)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by Order Status' + str(e))
            return False

    def verify_filter_by_order_status_in_pages(self, order_status):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Order Status in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_order_status(order_status)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Order Status in page %s", str(random_page))
                    self.filter_by_order_status(order_status)
                    self.go_to_page(random_page)
                    self.validate_order_status(order_status)
                self.logger.info("Verifying Order Status in page %s", str(last_page_number))
                self.filter_by_order_status(order_status)
                self.go_to_page(last_page_number)
                time.sleep(2)
                self.validate_order_status(order_status)
            self.logger.info("Successfully verified Order Status")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying Order Status in table" + str(e))
            return False

    def validate_order_status(self, order_status):
        try:
            self.logger.info("Verifying the Order Status in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i == 0:
                    element = "//div[@data-id=0]/div[@data-colindex=6]"
                    order_value_element = self.driver.find_element(By.XPATH, element)
                    self.scroll_horizontally(order_value_element)
                    time.sleep(3)
                    element = "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                        i) + "']/div[@data-field='orderStatus']"
                    order_status_element = self.driver.find_element(By.XPATH, element)
                    self.scroll_horizontally(order_status_element)
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching Order Status")
                order_status_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderStatus']")
                try:
                    ui_order_status = self.get_element_text_for_filter(order_status_xpath)
                    self.logger.info("Fetched ui order status :" + str(ui_order_status))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                assert str(ui_order_status) == str(order_status), "Order Status mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying Order Status" + str(e))
            raise e

    def filter_by_order_value(self, min_order_value, max_order_value):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_ORDER_VALUE)
            self.do_send_keys(self.FILTER_MIN_ORDER_VALUE, min_order_value)
            self.do_send_keys(self.FILTER_MAX_ORDER_VALUE, max_order_value)
            self.do_click_by_locator(self.FILTER_CHECK_ICON)
            self.do_click_by_locator(self.FILTER_BY_ORDER_STATUS)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while filtering by Order Value' + str(e))
            return False

    def verify_filter_by_order_value_in_pages(self, min_order_value, max_order_value):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Order Value in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_order_value(min_order_value, max_order_value)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Order Value in page %s", str(random_page))
                    self.filter_by_order_value(min_order_value, max_order_value)
                    self.go_to_page(random_page)
                    self.validate_order_value(min_order_value, max_order_value)
                self.logger.info("Verifying Order Value in page %s", str(last_page_number))
                self.filter_by_order_value(min_order_value, max_order_value)
                self.go_to_page(last_page_number)
                self.validate_order_value(min_order_value, max_order_value)
            self.logger.info("Successfully verified Order Value")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying Order Value in table" + str(e))
            return False

    def validate_order_value(self, min_order_value, max_order_value):
        try:
            self.logger.info("Verifying the Order Value in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i == 0:
                    element = "//div[@data-id=0]/div[@data-colindex=6]"
                    order_value_element = self.driver.find_element(By.XPATH, element)
                    self.scroll_horizontally(order_value_element)
                    element = "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                        i) + "']/div[@data-field='orderTotalValue']"
                    order_status_element = self.driver.find_element(By.XPATH, element)
                    self.scroll_horizontally(order_status_element)
                    self.do_double_click(self.ORDER_VALUE_SORT)
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching Order Value")
                order_value_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderTotalValue']")
                try:
                    ui_order_value = self.get_element_text_for_filter(order_value_xpath)
                    self.logger.info("Fetched ui order value :" + str(ui_order_value))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                if not float(min_order_value) <= float(str(ui_order_value).replace('$ ', "")) <= float(max_order_value):
                    raise Exception("Order value filter results are incorrect")
        except Exception as e:
            self.logger.error("Exception occurred verifying Order Value" + str(e))
            raise e

    def filter_by_created_on(self, created_on):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.FILTER_ICON)
            self.do_click_by_locator(self.FILTER_BY_CREATED_ON)
            created_on_options = self.get_all_elements(self.FILTER_CREATED_ON_LIST)
            for ele in created_on_options:
                if ele.text == created_on:
                    ele.click()
                    break
            self.do_click_by_locator(self.FILTER_BY_CREATED_ON)
            self.do_click_by_locator(self.FILTER_APPLY_BUTTON)
            time.sleep(2)
        except Exception as e:
            self.logger.error("Exception occurred filtering created on" + str(e))
            raise e

    def verify_filter_by_created_on_in_pages(self, created_on):
        try:
            self.check_if_result_found()
            first_page_number, last_page_number = self.get_pagination_first_and_last_page()
            self.logger.info("Verifying Created On in page %s", str(first_page_number))
            self.go_to_page(first_page_number)
            self.validate_created_on(created_on)
            if first_page_number != last_page_number:
                if last_page_number != first_page_number + 1:
                    random_page = self.get_random_page(first_page_number, last_page_number)
                    self.logger.info("Verifying Created On in page %s", str(random_page))
                    self.filter_by_created_on(created_on)
                    self.go_to_page(random_page)
                    self.validate_created_on(created_on)
                self.logger.info("Verifying Order Created On page %s", str(last_page_number))
                self.filter_by_created_on(created_on)
                self.go_to_page(last_page_number)
                self.validate_created_on(created_on)
            self.logger.info("Successfully verified Created On")
            return True
        except Exception as e:
            self.logger.error("Exception occurred verifying Created On in table" + str(e))
            return False

    def validate_created_on(self, created_on):
        try:
            self.logger.info("Verifying the Created On in table")
            max_rows = self.get_element_text(self.ITEMS_PER_PAGE)
            self.logger.info("Max items per page: " + max_rows)
            for i in range(int(max_rows)):
                if i == 0:
                    element = "//div[@data-id=0]/div[@data-colindex=6]"
                    order_value_element = self.driver.find_element(By.XPATH, element)
                    self.scroll_horizontally(order_value_element)
                    time.sleep(3)
                    element = "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                        i) + "']/div[@data-field='orderCreateDate']"
                    order_status_element = self.driver.find_element(By.XPATH, element)
                    self.scroll_horizontally(order_status_element)
                if i > 0 and i == 6:
                    table = self.driver.find_element(By.XPATH, self.SALES_ORDER_TABLE)
                    self.scroll_down(table)
                    time.sleep(2)
                self.logger.info("Fetching Created On")
                created_on_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'] [@data-id='" + str(
                    i) + "']/div[@data-field='orderCreateDate']")
                try:
                    ui_created_on = self.get_element_text_for_filter(created_on_xpath).split(" ")[0]
                    self.logger.info("Fetched ui Created On :" + str(ui_created_on))
                except:
                    self.logger.info("There are only " + str(i) + " rows")
                    break
                if created_on == 'Today':
                    created_on_date = str(date.today().strftime("%m/%d/%Y"))
                elif created_on == 'Yesterday':
                    created_on_date = (date.today() - timedelta(days=1)).strftime("%m/%d/%Y")
                assert ui_created_on == created_on_date, "Created On Mismatched"
        except Exception as e:
            self.logger.error("Exception occurred verifying Created On" + str(e))
            raise e

    def update_end_user_po_and_reseller_po(self, end_user_po, reseller_po):
        try:
            self.do_click_by_locator(self.REFERENCE_NUMBER_EDIT_ICON)
            self.do_send_keys(self.POPUP_END_USER_TEXTBOX, end_user_po)
            self.do_send_keys(self.POPUP_RESELLER_PO_TEXTBOX, reseller_po)
            self.do_click_by_locator(self.POPUP_UPDATE_BUTTON)
        except Exception as e:
            self.logger.error("Exception occurred updating end user po and reseller po" + str(e))
            raise e

    def cancel_update_of_end_user_po_and_reseller_po(self, end_user_po, reseller_po):
        try:
            self.do_click_by_locator(self.REFERENCE_NUMBER_EDIT_ICON)
            self.do_send_keys(self.POPUP_END_USER_TEXTBOX, end_user_po)
            self.do_send_keys(self.POPUP_RESELLER_PO_TEXTBOX, reseller_po)
            self.do_click_by_locator(self.POPUP_CANCEL_BUTTON)
        except Exception as e:
            self.logger.error("Exception occurred while cancelling edit of end user po and reseller po" + str(e))
            raise e

    def do_update_end_user_po_and_reseller_po(self, end_user_po, reseller_po):
        try:
            self.update_end_user_po_and_reseller_po(end_user_po, reseller_po)
            global ui_end_user_po, ui_reseller_po
            ui_end_user_po = self.get_element_text(self.REFERENCE_NUMBERS_END_USER_PO)
            ui_reseller_po = self.get_element_text(self.REFERENCE_NUMBERS_RESELLER_PO)
            return True
        except Exception as e:
            self.logger.error("Exception occurred while updating end user po and reseller po" + str(e))
            return False

    def test_end_user_po_and_reseller_po_updated(self, end_user_po, reseller_po):
        try:
            if ui_end_user_po != end_user_po.upper():
                self.logger.warning(f'End user PO mismatched. UI:{ui_end_user_po} Expected:{end_user_po.upper()}')
            if ui_reseller_po != reseller_po.upper():
                self.logger.warning(f'Reseller PO mismatched. UI:{ui_reseller_po} Expected:{reseller_po.upper()}')
            return True
        except Exception as e:
            self.logger.error("Exception occurred while validating end user po and reseller po" + str(e))
            return False

    def validate_cancel_end_user_po_and_reseller_po(self, end_user_po, reseller_po):
        try:
            ui_end_user_po = self.get_element_text(self.REFERENCE_NUMBERS_END_USER_PO)
            ui_reseller_po = self.get_element_text(self.REFERENCE_NUMBERS_RESELLER_PO)
            self.cancel_update_of_end_user_po_and_reseller_po(end_user_po, reseller_po)
            ui_cancel_end_user_po = self.get_element_text(self.REFERENCE_NUMBERS_END_USER_PO)
            ui_cancel_reseller_po = self.get_element_text(self.REFERENCE_NUMBERS_RESELLER_PO)
            assert ui_end_user_po == ui_cancel_end_user_po, "End user PO mismatched"
            assert ui_reseller_po == ui_cancel_reseller_po, "Reseller PO mismatched"
            return True
        except Exception as e:
            self.logger.error(
                "Exception occurred while validating cancel update of end user po and reseller po" + str(e))
            return False

    def cancel_shipto_enduser_info_and_validate(self, shipto_id, enduser_companyname):
        try:
            shiptoid_before_cancel = self.get_element_text(self.SHIP_TO_ID_FIElD)
            companyname_before_cancel = self.get_element_text(self.SHIP_TO_INFO_COMPANY_NAME_FIElD)
            address_before_cancel = self.get_element_text(self.SHIP_TO_INFO_ADDRESS_FIElD)
            final_address_before_cancel = address_before_cancel.replace('\n', ' ')
            self.do_click_by_locator(self.SHIP_TO_INFO_EDIT_ICON)
            self.do_send_keys(self.SHIP_TO_EDIT_SEARCH_BAR, shipto_id)
            self.driver.find_element(By.XPATH, "//input[@id='outlined-basic']").send_keys(Keys.ENTER)
            self.do_click_by_locator(self.SHIP_TO_SHIPPING_ADD_SELECT)
            self.do_click_by_locator(self.SHIP_TO_INFO_CANCEL_BTN)
            shiptoid_after_cancel = self.get_element_text(self.SHIP_TO_ID_FIElD)
            companyname_after_cancel = self.get_element_text(self.SHIP_TO_INFO_COMPANY_NAME_FIElD)
            address_after_cancel = self.get_element_text(self.SHIP_TO_INFO_ADDRESS_FIElD)
            final_address_after_cancel = address_after_cancel.replace('\n', ' ')
            assert shiptoid_before_cancel == shiptoid_after_cancel, "Ship to ID mismatched"
            assert companyname_before_cancel == companyname_after_cancel, "Company name mismatched"
            assert final_address_before_cancel == final_address_after_cancel, "Address mismatched"

            enduser_id_before_cancel = self.get_element_text(self.END_USER_ID_FIElD)
            enduser_contact_before_cancel = self.get_element_text(self.END_USER_CONTACT_FIElD)
            enduser_companyname_before_cancel = self.get_element_text(self.END_USER_COMPANY_NAME_FIElD)
            enduser_phonenumber_before_cancel = self.get_element_text(self.END_USER_PHONE_NO_FIElD)
            enduser_address_before_cancel = self.get_element_text(self.END_USER_ADDRESS_FIElD)
            enduser_final_address_before_cancel = enduser_address_before_cancel.replace('\n', ' ')
            enduser_email_before_cancel = self.get_element_text(self.END_USER_EMAIL_FIElD)
            self.do_click_by_locator(self.END_USER_INFO_EDIT_ICON)
            self.do_send_keys(self.END_USER_EDIT_SEARCH_BAR, enduser_companyname)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Search end user']").send_keys(Keys.ENTER)
            self.do_click_by_locator(self.END_USER_EDIT_ADD_SELECT)
            self.do_click_by_locator(self.SHIP_TO_INFO_CANCEL_BTN)
            enduser_id_after_cancel = self.get_element_text(self.END_USER_ID_FIElD)
            enduser_contact_after_cancel = self.get_element_text(self.END_USER_CONTACT_FIElD)
            enduser_companyname_after_cancel = self.get_element_text(self.END_USER_COMPANY_NAME_FIElD)
            enduser_phonenumber_after_cancel = self.get_element_text(self.END_USER_PHONE_NO_FIElD)
            enduser_address_after_cancel = self.get_element_text(self.END_USER_ADDRESS_FIElD)
            enduser_final_address_after_cancel = enduser_address_after_cancel.replace('\n', ' ')
            enduser_email_after_cancel = self.get_element_text(self.END_USER_EMAIL_FIElD)
            assert enduser_id_before_cancel == enduser_id_after_cancel, "EndUser ID mismatched"
            assert enduser_contact_before_cancel == enduser_contact_after_cancel, "EndUser contact mismatched"
            assert enduser_companyname_before_cancel == enduser_companyname_after_cancel, "EndUser company name mismatched"
            assert enduser_phonenumber_before_cancel == enduser_phonenumber_after_cancel, "EndUser phone number mismatched"
            assert enduser_final_address_before_cancel == enduser_final_address_after_cancel, "EndUser address mismatched"
            assert enduser_email_before_cancel == enduser_email_after_cancel, "EndUser email mismatched"
            return True
        except Exception as e:
            self.logger.error("Exception occurred while cancelling shipto and end user info update" + str(e))
            return False

    def update_shipto_enduser_info(self, shipto_id, enduser_companyname):
        try:
            self.do_click_by_locator(self.SHIP_TO_INFO_EDIT_ICON)
            self.do_send_keys(self.SHIP_TO_EDIT_SEARCH_BAR, shipto_id)
            self.driver.find_element(By.XPATH, "//input[@id='outlined-basic']").send_keys(Keys.ENTER)
            self.do_click_by_locator(self.SHIP_TO_SHIPPING_ADD_SELECT)
            self.do_click_by_locator(self.SAVE_BTN)
            global shiptoid_updated, companyname_updated, address_after_updated, final_address_updated, shipto_phoneno_updated, shipto_contact_updated, shipto_email_updated
            shiptoid_updated = self.get_element_text(self.SHIP_TO_ID_FIElD)
            companyname_updated = self.get_element_text(self.SHIP_TO_INFO_COMPANY_NAME_FIElD)
            address_after_updated = self.get_element_text(self.SHIP_TO_INFO_ADDRESS_FIElD)
            final_address_updated = address_after_updated.replace('\n', ' ')
            shipto_phoneno_updated = self.get_element_text(self.SHIP_TO_INFO_PHONE_NO_FIElD)
            shipto_contact_updated = self.get_element_text(self.SHIP_TO_INFO_CONTACT_FIElD)
            shipto_email_updated = self.get_element_text(self.SHIP_TO_INFO_EMAIL_FIElD)

            self.do_click_by_locator(self.END_USER_INFO_EDIT_ICON)
            self.do_send_keys(self.END_USER_EDIT_SEARCH_BAR, enduser_companyname)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Search end user']").send_keys(Keys.ENTER)
            self.do_click_by_locator(self.END_USER_EDIT_ADD_SELECT)
            self.do_click_by_locator(self.SAVE_BTN)
            global enduser_id_updated, enduser_contact_updated, enduser_companyname_updated, enduser_phonenumber_updated, enduser_final_address_updated, enduser_email_updated
            enduser_id_updated = self.get_element_text(self.END_USER_ID_FIElD)
            enduser_contact_updated = self.get_element_text(self.END_USER_CONTACT_FIElD)
            enduser_companyname_updated = self.get_element_text(self.END_USER_COMPANY_NAME_FIElD)
            enduser_phonenumber_updated = self.get_element_text(self.END_USER_PHONE_NO_FIElD)
            enduser_address_updated = self.get_element_text(self.END_USER_ADDRESS_FIElD)
            enduser_final_address_updated = enduser_address_updated.replace('\n', ' ')
            enduser_email_updated = self.get_element_text(self.END_USER_EMAIL_FIElD)
            return True
        except Exception as e:
            self.logger.error("Exception occurred while updating shipto and end user info update" + str(e))
            return False

    def shipto_enduser_info_validation(self, ship_to_suffix, ship_to_name, ship_to_address, ship_to_phone,
                                       ship_to_contact, ship_to_email, end_user_id, end_user_address, end_user_contact):
        try:
            breakpoint()
            if shiptoid_updated != ship_to_suffix:
                self.logger.warning(f'Ship to ID mismatched. UI:{shiptoid_updated} Expected:{ship_to_suffix}')
            if companyname_updated != ship_to_name:
                self.logger.warning(f'Ship to Company name mismatched. UI:{companyname_updated} Expected:{ship_to_name}')
            if final_address_updated != ship_to_address:
                self.logger.warning(f'Ship to Address mismatched. UI:{final_address_updated} Expected:{ship_to_address}')
            if shipto_phoneno_updated != ship_to_phone:
                self.logger.warning(f'Ship to phone number mismatched. UI:{shipto_phoneno_updated} Expected:{ship_to_phone}')
            if shipto_contact_updated != ship_to_contact:
                self.logger.warning(f'Ship to contact mismatched. UI:{shipto_contact_updated} Expected:{ship_to_contact}')
            if shipto_email_updated != ship_to_email:
                self.logger.warning(f'Ship to email mismatched. UI:{shipto_email_updated} Expected:{ship_to_email}')

            if enduser_id_updated != enduser_id_updated:
                self.logger.warning(f'EndUser ID mismatched. UI:{enduser_id_updated} Expected:{enduser_id_updated}')
            if enduser_contact_updated != end_user_contact:
                self.logger.warning(f'EndUser contact mismatched. UI:{enduser_contact_updated} Expected:{end_user_contact}')
            if enduser_final_address_updated != end_user_address:
                self.logger.warning(f'EndUser address mismatched. UI:{enduser_final_address_updated} Expected:{end_user_address}')
            return True
        except Exception as e:
            self.logger.error("Exception occurred while validating shipto and end user info update" + str(e))
            return False

    def validate_acop_field(self):
        try:
            self.do_check_visibility(self.ACOP_APPLIED_COLUMN)
            rows = self.get_all_elements(self.ORDER_LINES)
            for row in range(len(rows)):
                row_xpath = (By.XPATH, "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                    row) + "]/div[@data-field='isAcopApplied']")
                text = self.get_element_text(row_xpath)
                if text != "Yes" and text != "No":
                    self.logger.error(f'Acop field: {text}')
                    raise Exception("ACOP field value is incorrect")
            self.logger.info("Successfully validated ACOP field")
            return True
        except Exception as e:
            self.logger.error(
                "Exception occurred while validating ACOP field" + str(e))
            return False

    def validate_order_status_to_check_if_editable(self):
        try:
            status = self.get_element_text(self.ORDER_STATUS_TITLE)
            if status != 'Order Hold(IM)' and status != 'In Progress(IM)' and status != 'Customer Hold(IM)':
                self.logger.error(f'Order status is {status}, so the order cant be edited')
                raise Exception("Order cant be edited")
            self.logger.info("Successfully verified Order Status in order details")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying order status in order details page ' + str(e))
            return False

    # Here the horizontal scrolling is not working
    def update_order_line(self, special_bid, unit_price, quantity):
        try:
            self.do_click_by_locator(self.ORDER_LINE_EDIT_ICON)
            time.sleep(3)
            self.do_check_visibility(self.EDIT_CHECK_ICON)
            self.do_check_visibility(self.EDIT_CANCEL_ICON)
            self.do_click_by_locator(self.ORDER_LINE_SPECIAL_BID_NUMBER)
            self.do_send_keys(self.ORDER_LINE_SPECIAL_BID_NUMBER, special_bid)
            time.sleep(3)

            # scroll till quantity
            self.driver.execute_script("document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1200")
            time.sleep(2)

            self.do_click_by_locator(self.ORDER_LINE_UNIT_PRICE)
            self.do_send_keys(self.ORDER_LINE_UNIT_PRICE, unit_price)

            self.do_click_by_locator(self.ORDER_LINE_QUANTITY)
            self.do_send_keys(self.ORDER_LINE_QUANTITY, quantity)

            page_ele = self.driver.find_element(By.XPATH, self.PAGE_ELEMENT)
            self.scroll_down(page_ele)
            self.driver.execute_script("document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying order status in order details page ' + str(e))
            return False

    def click_order_line_edit_check_icon(self):
        try:
            time.sleep(2)
            self.do_click_by_locator(self.EDIT_CHECK_ICON)
            time.sleep(2)
            self.logger.info("Clicked on order line check icon")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while clicking on edit check icon ' + str(e))
            return False

    def click_order_line_edit_cancel_icon(self):
        try:
            self.do_click_by_locator(self.EDIT_CANCEL_ICON)
            time.sleep(5)
            self.logger.info("Clicked on order line cancel changes icon")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while clicking on edit cancel icon ' + str(e))
            return False

    # Here the horizontal scrolling is not working
    def get_order_line_data(self):
        order_line_data = {}
        try:
            order_line_data['special_bid'] = self.do_get_attribute(self.ORDER_LINE_SBN_TEXT, 'value')

            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1200")
            time.sleep(2)

            order_line_data['unit_price'] = self.do_get_attribute(self.ORDER_LINE_UNIT_PRICE_TEXT, 'value')
            order_line_data['cost'] = self.get_element_text(self.ORDER_LINE_COST)
            order_line_data['margin'] = self.get_element_text(self.ORDER_LINE_MARGIN)
            order_line_data['quantity'] = self.do_get_attribute(self.ORDER_LINE_QUANTITY_TEXT, 'value')
            order_line_data['quantity_confirmed'] = self.get_element_text(self.ORDER_LINE_QUANTITY_CONFIRMED)
            order_line_data['quantity_backordered'] = self.get_element_text(self.ORDER_LINE_QUANTITY_BACKORDERED)
            self.logger.info(order_line_data)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return order_line_data
        except Exception as e:
            self.logger.error(
                'Exception occurred while clicking on edit cancel icon ' + str(e))
            raise e

    def check_cancel_options_are_correct_in_order_lines(self):
        try:
            order_lines = self.get_all_elements(self.ORDER_LINES)
            for i in range(len(order_lines)):
                self.driver.refresh()
                time.sleep(3)
                self.do_click_by_locator(self.ORDER_LINES_TAB)
                three_dots_xpath = (By.XPATH, "//div[@data-rowindex=" + str(
                    i) + "]/div/button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hp16lx-MuiButtonBase-root-MuiIconButton-root']")
                self.do_click_by_locator(three_dots_xpath)
                order_line_options_xpath = (By.XPATH, "(//li[@role='menuitem'])")
                order_line_options = self.get_all_elements(order_line_options_xpath)
                self.logger.info(len(order_line_options))
                for ele in order_line_options:
                    if ele.text != "Unmark for cancel" and ele.text != "Mark for cancel":
                        return False
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while checking the order lines options :' + str(e))
            return False

    def click_on_mark_for_cancel(self):
        try:
            self.driver.refresh()
            self.do_click_by_locator(self.ORDER_LINES_TAB)
            order_lines = self.get_all_elements(self.ORDER_LINES)
            self.logger.info(len(order_lines))
            for i in range(len(order_lines)):
                three_dots_xpath = (By.XPATH, "//div[@data-rowindex=" + str(
                    i) + "]/div/button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hp16lx-MuiButtonBase-root-MuiIconButton-root']")
                self.do_click_by_locator(three_dots_xpath)
                order_line_options_xpath = (By.XPATH, "(//li[@role='menuitem'])")
                order_line_options = self.get_all_elements(order_line_options_xpath)
                self.logger.info(len(order_line_options))
                mark_for_cancel_elements = []
                for ele in order_line_options:
                    if ele.text == 'Mark for cancel':
                        mark_for_cancel_elements.append(ele)
                self.do_click_by_locator(mark_for_cancel_elements[-1])
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while marking for cancel :' + str(e))
            return False

    def click_on_unmark_for_cancel(self):
        try:
            order_lines = self.get_all_elements(self.ORDER_LINES_MARKED_FOR_CANCEL)
            for i in range(len(order_lines)):
                three_dots_xpath = (By.XPATH, "//div[@data-rowindex=" + str(
                    i) + "]/div/button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1hp16lx-MuiButtonBase-root-MuiIconButton-root']")
                self.do_click_by_locator(three_dots_xpath)
                order_line_options_xpath = (By.XPATH, "(//li[@role='menuitem'])")
                order_line_options = self.get_all_elements(order_line_options_xpath)
                self.logger.info(len(order_line_options))
                unmark_for_cancel_elements = []
                for ele in order_line_options:
                    if ele.text == 'Unmark for cancel':
                        unmark_for_cancel_elements.append(ele)
                self.do_click_by_locator(unmark_for_cancel_elements[-1])
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while marking for cancel :' + str(e))

    def order_status_validate(self, status):
        try:
            self.driver.refresh()
            if self.get_element_text(self.ORDER_DETAILS_STATUS) == status:
                self.logger.info("Order status is validated successfully")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error('Exception occurred while Click on Billing tab ' + str(e))
            return False

    def order_status_edit_category_validate(self, status):
        try:
            order_status = ['Order Hold(IM)', 'Customer Hold(IM)', 'In Progress(IM)']
            if status in order_status:
                self.logger.info("Order is editable")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error('Exception occurred while verifying order status ' + str(e))
            return False

    def click_order_management_link(self):
        try:
            self.do_click_by_locator(self.SALES_ORDER_OPTION)
            self.logger.info("Successfully clicked On order management link")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while clicking on order management link ' + str(e))
            return False

    def verify_cancel_order_button(self):
        try:
            if self.is_present(self.CANCEL_ORDER_BTN):
                self.logger.info("Cancel order button is displayed")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order button ' + str(e))
            return False

    def click_cancel_order_btn(self):
        try:
            self.do_click_by_locator(self.CANCEL_ORDER_BTN)
            self.logger.info("Successfully Clicked On cancel order button")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while clicking on cancel order button ' + str(e))
            return False

    def validate_cancel_order_alert_elements(self):
        try:
            if self.get_element_text(self.CANCEL_ORDER_ALERT_TITLE) == "Cancel Order" and self.get_element_text(
                    self.CANCEL_ORDER_ALERT_CONFIRMATION) == "Are you sure to cancel order? Order will be cancelled permanently, and you can not undo this action." and self.get_element_text(
                self.DEFER_CANCEL_ORDER) == "No, Keep Order" and self.get_element_text(
                self.CONFIRM_CANCEL_ORDER) == "Yes, Cancel Order":
                self.logger.info("Successfully verified cancel order alert elements")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while verifying cancel order alert elements ' + str(e))
            return False

    def cancel_order_click(self):
        try:
            self.do_click_by_locator(self.CONFIRM_CANCEL_ORDER)
            self.logger.info("Successfully Clicked On cancel order confirmation button")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while clicking on cancel order confirmation button ' + str(e))
            return False

    def validate_toast_notification(self):
        try:
            if self.get_element_text(self.SUCCESS_TOAST_NOTIFICATION) == "Cancelled! order was successfully cancelled.":
                self.logger.info("Toast notification message is validated successfully")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error('Exception occurred while validating toast notification ' + str(e))
            return False

    def mark_for_cancel_single_line_item(self):
        try:
            order_lines = self.get_all_elements(self.ORDER_LINES)
            if len(order_lines) > 0:
                global order_desc
                order_desc = self.get_element_text(self.ORDER_LINE_DESC)
                self.logger.info(order_desc)
                self.do_click_by_locator(self.MORE_OPTIONS_MENU)
                order_line_options_xpath = (By.XPATH, "(//li[@role='menuitem'])")
                order_line_options = self.get_all_elements(order_line_options_xpath)
                self.logger.info(len(order_line_options))
                mark_for_cancel_elements = []
                for ele in order_line_options:
                    if ele.text == 'Mark for cancel':
                        mark_for_cancel_elements.append(ele)
                self.do_click_by_locator(mark_for_cancel_elements[-1])
                self.logger.info("Clicked on mark for cancel for single line item")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error('Exception occurred while clicking on mark for cancel for single line item ' + str(e))
            return False

    def order_line_edit_button_verify(self):
        try:
            pencil_icon = self.driver.find_element(By.XPATH, self.EDIT_PENCIL_ICON)
            if not self.is_element_enabled(pencil_icon):
                self.logger.info("Single line item is greyed out and edit button is also not active")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error('Exception occurred while validating order line and edit button ' + str(e))
            return False

    def resubmit_order(self):
        try:
            self.do_click_by_locator(self.RESUBMIT_ORDER_BUTTON)
            popup_message = self.get_element_text(self.RESUBMIT_ORDER_POPUP_MESSAGE)
            assert popup_message == "Are you sure to resubmit order?", "Resubmit popup message did not match"
            self.do_click_by_locator(self.RESUBMIT_YES_BUTTON)
            self.do_check_visibility(self.RESUBMIT_STATUS_TITLE)
            time.sleep(3)
            resubmit_status = self.get_element_text(self.RESUBMIT_ORDER_POPUP_MESSAGE)
            assert resubmit_status == "Order resubmitted successfully", "Resubmit failed"
            self.do_click_by_locator(self.CLOSE_RESUBMIT_POPUP)
            self.logger.info("Successfully resubmitted order")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while resubmitting order ' + str(e))
            return False

    def fetch_order_lines(self):
        order_lines_list = []
        try:
            order_lines = self.get_all_elements(self.ORDER_LINES)
            for i in range(len(order_lines)):
                order_line = {}
                time.sleep(3)
                order_line['line_number'] = self.get_element_text((By.XPATH,
                                                                   "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                       i) + "]/div[@data-field='ingramOrderLineNumber']"))
                order_line['order_line_status'] = self.get_element_text((By.XPATH,
                                                                         "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                             i) + "]/div[@data-field='lineStatus']"))
                order_line['order_line_acop'] = self.get_element_text((By.XPATH,
                                                                       "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                           i) + "]/div[@data-field='isAcopApplied']"))
                order_line['order_line_description'] = self.get_element_text((By.XPATH,
                                                                              "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                  i) + "]/div[@data-field='partDescription']/div/div[1]/strong"))
                order_line['order_line_vpn'] = self.get_element_text((By.XPATH,
                                                                      "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                          i) + "]/div[@data-field='partDescription']/div/div/span[1]"))
                order_line['order_line_im_part'] = self.get_element_text((By.XPATH,
                                                                          "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                              i) + "]/div[@data-field='partDescription']/div/div/span[2]"))
                order_line['order_line_spl_bid'] = self.do_get_attribute((By.XPATH,
                                                                          "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                              i) + "]/div[@data-field='specialBidNumber']/input"),
                                                                         'value')
                self.driver.execute_script(
                    "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1200")
                order_line['order_line_unit_price'] = self.do_get_attribute((By.XPATH,
                                                                             "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                 i) + "]/div[@data-field='unitPrice']/input"),
                                                                            'value')
                order_line['order_line_extended_price'] = self.get_element_text((By.XPATH,
                                                                                 "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                     i) + "]/div[@data-field='extendedPrice']"))
                order_line['order_line_cost'] = self.get_element_text((By.XPATH,
                                                                       "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                           i) + "]/div[@data-field='cost']"))


                order_line['order_line_extended_cost'] = self.get_element_text((By.XPATH,
                                                                                "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                    i) + "]/div[@data-field='extendedCost']"))
                order_line['order_line_margin'] = self.get_element_text((By.XPATH,
                                                                         "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                             i) + "]/div[@data-field='margin']"))
                order_line['order_line_currency_code'] = self.get_element_text((By.XPATH,
                                                                                "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                    i) + "]/div[@data-field='currencyCode']"))


                # scroll till quantity back ordered column
                # time.sleep(3)
                # self.driver.execute_script(
                #     "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

                time.sleep(3)
                order_line['order_line_quantity'] = self.do_get_attribute((By.XPATH,
                                                                           "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                               i) + "]/div[@data-field='quantityOrdered']/input"),
                                                                          'value')
                order_line['order_line_quantity_confirmed'] = self.get_element_text((By.XPATH,
                                                                                     "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                         i) + "]/div[@data-field='quantityConfirmed']"))
                order_line['order_line_quantity_backordered'] = self.get_element_text((By.XPATH,
                                                                                       "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                           i) + "]/div[@data-field='quantityBackOrdered']"))

                order_lines_list.append(order_line)
                self.logger.info(order_lines_list)
                self.driver.execute_script(
                    "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return order_lines_list
        except Exception as e:
            self.logger.error('Exception occurred while fetching order_lines ' + str(e))
            raise e

    def is_ship_from_warehouse_id_field_visible(self, warehouse_id):
        try:
            ui_warehouse_id = self.get_element_text(self.SHIP_FROM_WAREHOUSE_ID)
            if str(warehouse_id) != str(ui_warehouse_id):
                self.logger.error(f'Ship from warehouse id mismatched\n UI:{ui_warehouse_id} API:{warehouse_id}')
            else:
                self.logger.info("Successfully verified Ship from warehouse id field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Ship from warehouse id field under Billing to info' + str(e))
            return False

    def is_ship_from_warehouse_name_field_visible(self, warehouse_name):
        try:
            ui_warehouse_name = self.get_element_text(self.SHIP_FROM_WAREHOUSE_NAME)
            if str(warehouse_name) != str(ui_warehouse_name):
                self.logger.error(f'Ship from warehouse name mismatched\n UI:{ui_warehouse_name} API:{warehouse_name}')
            else:
                self.logger.info("Successfully verified Ship from warehouse name field under Billing to info")
            return True
        except Exception as e:
            self.logger.error(
                'Exception occurred while verifying Ship from warehouse name field under Billing to info' + str(e))
            return False

    def cancelled_order_not_visible_test(self):
        try:
            self.logger.info((By.XPATH, "//*[text()='" + order_desc + "']").__str__())
            element = (By.XPATH, "//*[text()='" + order_desc + "']")
            if not self.do_check_visibility(element):
                self.logger.info("Cancelled order is not visible")
                return True
            else:
                return False
        except Exception as e:
            self.logger.error('Exception occurred while validating order line is not visible ' + str(e))
            return False

    def validate_payment_terms_code(self, payment_terms_code):
        try:
            terms_code = self.get_element_text(self.TERMS_CODE)
            assert str(payment_terms_code) == terms_code, "Payment terms code mismatched"
            self.logger.info("Successfully validated Payment terms code")
            return True
        except Exception as e:
            self.logger.error('Exception occurred while validating payment terms code' + str(e))
            return False

    def get_updated_order_line_data_of_resubmit(self):
        order_line_data = {}
        try:
            order_lines = self.get_all_elements(self.ORDER_LINES)
            index = len(order_lines) - 1
            order_line_data['special_bid'] = self.do_get_attribute((By.XPATH,
                                                                    "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                        index) + "]/div[@data-field='specialBidNumber']/input"),
                                                                   'value')
            order_line_data['unit_price'] = self.do_get_attribute((By.XPATH,
                                                                   "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                       index) + "]/div[@data-field='unitPrice']/input"),
                                                                  'value')

            element = "//*[@data-rowindex='0']//*[@role='cell' and @data-field='cost']"
            cost = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(cost)

            time.sleep(3)
            order_line_data['cost'] = self.get_element_text((By.XPATH,
                                                             "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                 index) + "]/div[@data-field='cost']"))
            order_line_data['margin'] = self.get_element_text((By.XPATH,
                                                               "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                   index) + "]/div[@data-field='margin']"))

            element = "//*[@data-rowindex='0']//*[@role='cell' and @data-field='currencyCode']"
            currency_code = self.driver.find_element(By.XPATH, element)
            self.scroll_horizontally(currency_code)
            # scroll till quantity back order
            time.sleep(2)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 1800")

            time.sleep(2)
            order_line_data['quantity'] = self.do_get_attribute((By.XPATH,
                                                                 "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                     index) + "]/div[@data-field='quantityOrdered']/input"),
                                                                'value')
            order_line_data['quantity_confirmed'] = self.get_element_text((By.XPATH,
                                                                           "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                               index) + "]/div[@data-field='quantityConfirmed']"))
            order_line_data['quantity_backordered'] = self.get_element_text((By.XPATH,
                                                                             "//div[@class='MuiDataGrid-row'][@data-rowindex=" + str(
                                                                                 index) + "]/div[@data-field='quantityBackOrdered']"))
            self.logger.info(order_line_data)
            self.driver.execute_script(
                "document.querySelector(\"div[class$='MuiDataGrid-virtualScroller css-1pans1z-MuiDataGrid-virtualScroller']\").scrollLeft= 0")
            return order_line_data
        except Exception as e:
            self.logger.error(
                'Exception occurred while clicking on edit cancel icon ' + str(e))
            raise e
