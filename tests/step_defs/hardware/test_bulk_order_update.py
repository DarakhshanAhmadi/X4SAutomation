# import datetime
import os

from pytest_bdd import scenario, parsers, when, then, given
from CommonUtilities import readWriteTestData
from CommonUtilities.parse_config import ParseConfigFile
from CommonUtilities.file_operations import logger
from CommonUtilities.readProperties import ReadConfig
from db.service.X4ABulkOrderDataDbManagementService import X4ABulkOrderDataDbManagementService
from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
from pages.X4A.Facade.PrepareObject import PrepareObject
from pages.X4A.TestSteps.validateBulkOrderUploadData import ValidateBulkOrderUploadData

parse_config_json = ParseConfigFile()
screen_shot = {"path": " "}
x4a_status_list = []
x4a_bulk_order_list = []
db_file_path = ReadConfig.get_db_file_path()
bulk_order_management_srv_obj = X4ABulkOrderDataDbManagementService()
latest_downloaded_file = ""
latest_downloaded_files = ""


@scenario("features/hardware/bulk_order_upload.feature", "Login to X4A portal")
def test_login_the_x4a_portal():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "File Upload option & Dialog Box")
def test_upload_option():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Upload file error")
def test_upload_file_error():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Template error")
def test_template_error():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Upload file")
def test_upload_file():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Download template")
def test_template_file():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "View Review Option")
def test_view_review():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Cancel delete Option")
def test_cancel_delete():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Place Order Option")
def test_place_order():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "filter user Option")
def test_user_option():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "error in order")
def test_error_in_order():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Duplicate error")
def test_duplicate_error():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Bulk order upload page")
def test_bulk_order_upload_page():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Multiple place order")
def test_multiple_place_order():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "Order with vendor part number")
def test_orderwith_vendor_part_number():
    pass


@scenario("features/hardware/bulk_order_upload.feature", "logout X4A")
def test_logout_x4a():
    pass


@given(parsers.parse('launch chrome browser and open the X4A url'))
def launch_browser(init_driver):
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    bulk_order_management_srv_obj = X4ABulkOrderDataDbManagementService()
    prepare_obj = PrepareObject(init_driver)
    feature_file_name = "bulk_order_upload"
    try:
        #
        test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
        filtered_order_data = bulk_order_upload_steps.filtered_orders_by_feature_file(test_data_order,
                                                                                      feature_file_name)
        logger.info("the value of filtered data", filtered_order_data)
        for order_index, test_data_order in filtered_order_data.iterrows():
            x4a_bulk_order_list.clear()
            logger.info("the value of test data", test_data_order)
            x4a_bulk_order_data = prepare_obj.prepare_x4a_bulk_order_data_obj(test_data_order)
            x4a_bulk_order_list.append(x4a_bulk_order_data)
            bulk_order_management_srv_obj.save_scenario_details(db_file_path, x4a_bulk_order_list)
        environment = parse_config_json.get_data_from_config_json("environment", "environment_type", "config.json")
        logger.info(environment)
        if environment == 'Stage':
            url = parse_config_json.get_data_from_config_json("x4aStageCredentials", "x4aBaseUrl", "config.json")
        else:
            url = parse_config_json.get_data_from_config_json("x4aBetaCredentials", "x4aBaseUrl", "config.json")
        init_driver.get(url)
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a " + str(e))
        raise e


@then(parsers.parse('provide user ID and Password to login'))
def login(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        bulk_order_upload_steps.login(feature_file_name, screen_shot)
        logger.info("Launched the browser and login to X4A is successfully.")
    except Exception as e:
        logger.error("Not able to Launch the browser and login x4a " + str(e))
        raise e


@when(parsers.parse('the user traverse to Bulk order update menu'))
def click_on_bulk_order_upload_menu(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.click_on_bulk_order_upload_menu(feature_file_name, screen_shot):
            raise Exception("Failed to click on bulk order upload menu")
    except Exception as e:
        logger.error("Error while clicking on bulk order upload menu " + str(e))
        raise e


@then(parsers.parse('verify bulk order update page'))
def verify_bulk_order_update_page(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_bulk_order_update_page(feature_file_name, screen_shot):
            raise Exception("Failed to verify bulk order upload page")
    except Exception as e:
        logger.error("Error while verifying bulk order upload page " + str(e))
        raise e


@when(parsers.parse('upload file button clicked'))
def click_upload_file(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.click_upload_file(feature_file_name, screen_shot):
            raise Exception("Failed to click upload file button")
    except Exception as e:
        logger.error("Error while clicking upload file button " + str(e))
        raise e


@then(parsers.parse('verify upload file ready popup'))
def verify_upload_file_popup(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_upload_file_popup(feature_file_name, screen_shot):
            raise Exception("Failed to verify upload file popup")
    except Exception as e:
        logger.error("Error while verifying upload file popup " + str(e))
        raise e


@when(parsers.parse('other than excel file was uploaded'))
def do_upload_error_file(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_upload_error_file(feature_file_name, screen_shot):
            raise Exception("Failed to select error file")
    except Exception as e:
        logger.error("Error while selecting file " + str(e))
        raise e


@then(parsers.parse('verify error message'))
def verify_error_popup(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_error_popup(feature_file_name, screen_shot):
            raise Exception("Failed to verify file error popup")
    except Exception as e:
        logger.error("Error while verifying file error popup " + str(e))
        raise e


@when(parsers.parse('different template was uploaded'))
def do_upload_template_error_file(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_upload_template_error_file(feature_file_name, screen_shot):
            raise Exception("Failed to select error file")
    except Exception as e:
        logger.error("Error while selecting file " + str(e))
        raise e


@then(parsers.parse('verify template error message'))
def verify_template_error_message(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_template_error_message(feature_file_name, screen_shot):
            raise Exception("Failed to verify template error message")
    except Exception as e:
        logger.error("Error while verifying template error message " + str(e))
        raise e


@when(parsers.parse('file was selected "{scenario_no}"'))
def do_upload_file(init_driver, scenario_no):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_select_file(feature_file_name, screen_shot, scenario_no):
            raise Exception("Failed to select file")
    except Exception as e:
        logger.error("Error while selecting file " + str(e))
        raise e


@then(parsers.parse('verify select file popup'))
def verify_selected_file_popup(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_selected_file_popup(feature_file_name, screen_shot):
            raise Exception("Failed to verify selected file popup")
    except Exception as e:
        logger.error("Error while verifying selecting file popup " + str(e))
        raise e


@when(parsers.parse('click on delete icon'))
def do_delete_file(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_delete_file(feature_file_name, screen_shot):
            raise Exception("Failed to delete file")
    except Exception as e:
        logger.error("Error while deleting file " + str(e))
        raise e


@when(parsers.parse('selected file for review'))
def do_select_review(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_select_review(feature_file_name, screen_shot):
            raise Exception("Failed to select review button")
    except Exception as e:
        logger.error("Error while select review button " + str(e))
        raise e


@then(parsers.parse('verify status as Ready to place and place order button'))
def verify_place_order_button(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_place_order_button(feature_file_name, screen_shot):
            raise Exception("Failed to verify place order button")
    except Exception as e:
        logger.error("Error while verifying place order button " + str(e))
        raise e


@then(parsers.parse('verify bulk order page'))
def verify_bulk_order_page(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_bulk_order_page(feature_file_name, screen_shot):
            raise Exception("Failed to verify bulk order page")
    except Exception as e:
        logger.error("Error while verifying bulk order page " + str(e))
        raise e



@when(parsers.parse('download template button clicked'))
def do_download_template(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_download_template(feature_file_name, screen_shot, "single"):
            raise Exception("Failed to download file")
    except Exception as e:
        logger.error("Error while downloading file " + str(e))
        raise e


@then(parsers.parse('verify the downloaded template file name and its data'))
def verify_template_file_downloaded(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        global latest_downloaded_file

        latest_downloaded_file = bulk_order_upload_steps.validate_file_name_and_data(feature_file_name, screen_shot)
        file = latest_downloaded_file.split("\\")
        file_name = file[-1]
        file_str = "Ingram_BulkUpload_Template"
        required_file_name = file_str

        logger.info(required_file_name)
        logger.info(file_name)
        if required_file_name not in file_name:
            raise Exception("File name validation failed")
        logger.info("File verified successfully")
    except Exception as e:
        logger.error("Failed to validate file name: " + str(e))
        raise e


@when(parsers.parse('download template button clicked multiple times'))
def do_download_multiple_template(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_download_template(feature_file_name, screen_shot, "multiple"):
            raise Exception("Failed to download file")
    except Exception as e:
        logger.error("Error while downloading file " + str(e))
        raise e


@then(parsers.parse('verify the all downloaded template file names'))
def verify_multiple_template_file_downloaded(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        count = 1
        global latest_downloaded_files

        latest_downloaded_files = bulk_order_upload_steps.validate_multiple_file_name(feature_file_name, screen_shot)

        for i in latest_downloaded_files:
            file = i.split("\\")
            file_name = file[-1]
            file_str = "Ingram_BulkUpload_Template"
            if count == len(latest_downloaded_files):
                required_file_name = file_str
            else:
                required_file_name = file_str + ' (' + str(count) + ')'
                count = count + 1
            logger.info(required_file_name)
            logger.info(file_name)
            if required_file_name not in file_name:
                raise Exception("File name validation failed")
            logger.info("File verified successfully")
        for i in latest_downloaded_files:
            os.remove(i)
    except Exception as e:
        logger.error("Failed to validate file name " + str(e))
        raise e



@when(parsers.parse('filter status with "{status}"'))
def do_select_partially_complete_status(init_driver, status):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_select_status(feature_file_name, screen_shot, status):
            raise Exception("Failed to select "+ status + " status")
    except Exception as e:
        logger.error("Error while selecting "+ status + " status " + str(e))
        raise e


# @when(parsers.parse('filter status with Error found'))
# def do_select_error_found_status(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#
#         if not bulk_order_upload_steps.do_select_status(feature_file_name, screen_shot, 'Error found'):
#             raise Exception("Failed to select Error found status")
#     except Exception as e:
#         logger.error("Error while selecting Error found status " + str(e))
#         raise e
#
#
# @when(parsers.parse('filter status with Order placed'))
# def do_select_order_placed_status(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#
#         if not bulk_order_upload_steps.do_select_status(feature_file_name, screen_shot, 'Order placed'):
#             raise Exception("Failed to select Order placed status")
#     except Exception as e:
#         logger.error("Error while selecting Order placed status " + str(e))
#         raise e
#

@when(parsers.parse('filter with file name'))
def do_select_file_name_search(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_select_file_name_search(feature_file_name, screen_shot):
            raise Exception("Failed to select file name")
    except Exception as e:
        logger.error("Error while selecting file name " + str(e))
        raise e


@then(parsers.parse('verify the file upload list for status "{status}"'))
def verify_view_review_icon(init_driver, status):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_view_review_icon(feature_file_name, screen_shot, status):
            raise Exception("Failed to verify review icon for status " + status)
    except Exception as e:
        logger.error("Error while verifying review icon " + str(e))
        raise e


# @then(parsers.parse('verify the file upload list for status "{status}"'))
# def verify_view_icon(init_driver, status):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.verify_view_icon(feature_file_name, screen_shot, status):
#             raise Exception("Failed to verify file upload list for status " + status)
#     except Exception as e:
#         logger.error("Error while verifying file upload list and view icon " + str(e))
#         raise e
#

@when(parsers.parse('review icon clicked'))
def do_click_review_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_review_icon(feature_file_name, screen_shot):
            raise Exception("Failed to click review icon")
    except Exception as e:
        logger.error("Error while clicking review icon " + str(e))
        raise e


@when(parsers.parse('view icon clicked'))
def do_click_review_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_view_icon(feature_file_name, screen_shot):
            raise Exception("Failed to click review icon")
    except Exception as e:
        logger.error("Error while clicking review icon " + str(e))
        raise e


@then(parsers.parse('verify Download order list button for status "{status}"'))
def verify_download_order_list(init_driver, status):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_download_order_list(feature_file_name, screen_shot, status):
            raise Exception("Failed to verify download order list button")
    except Exception as e:
        logger.error("Error while verifying download order list button " + str(e))
        raise e


@when(parsers.parse('clicked on review button'))
def do_click_review_button(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_review_button(feature_file_name, screen_shot):
            raise Exception("Failed to click review button")
    except Exception as e:
        logger.error("Error while clicking review button " + str(e))
        raise e


@when(parsers.parse('clicked on place order button'))
def do_click_place_order_button(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_place_order_button(feature_file_name, screen_shot):
            raise Exception("Failed to click place order button")
    except Exception as e:
        logger.error("Error while clicking place order button" + str(e))
        raise e


@then(parsers.parse('verify order page and downloaded order list'))
def verify_downloaded_order_list(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_downloaded_order_list(feature_file_name, screen_shot):
            raise Exception("Failed to verify downloaded order list")
    except Exception as e:
        logger.error("Error while verifying downloaded order list " + str(e))
        raise e


# @when(parsers.parse('filter status with Upload in progress'))
# def do_select_upload_in_progress_status(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#
#         if not bulk_order_upload_steps.do_select_status(feature_file_name, screen_shot, 'Upload in progress'):
#             raise Exception("Failed to select Upload in progress status")
#     except Exception as e:
#         logger.error("Error while selecting Upload in progress status " + str(e))
#         raise e
#
#
# @when(parsers.parse('filter status with ready to place'))
# def do_select_ready_to_place_status(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#
#         if not bulk_order_upload_steps.do_select_status(feature_file_name, screen_shot, 'Ready to place'):
#             raise Exception("Failed to select Ready to place status")
#     except Exception as e:
#         logger.error("Error while selecting Ready to place status " + str(e))
#         raise e
#

@then(parsers.parse('verify the CANCEL icon'))
def verify_cancel_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_cancel_icon(feature_file_name, screen_shot):
            raise Exception("Failed to verify cancel icon")
    except Exception as e:
        logger.error("Error while verifying cancel icon " + str(e))
        raise e


@when(parsers.parse('CANCEL icon clicked'))
def do_click_cancel_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_cancel_icon(feature_file_name, screen_shot):
            raise Exception("Failed to click cancel icon")
    except Exception as e:
        logger.error("Error while clicking cancel icon " + str(e))
        raise e


@then(parsers.parse('verify the PLACE ORDERS icon'))
def verify_place_order_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_place_orders_icon(feature_file_name, screen_shot):
            raise Exception("Failed to verify place order icon")
    except Exception as e:
        logger.error("Error while verifying place order icon " + str(e))
        raise e


@then(parsers.parse('verify the DELETE icon and status upload cancelled'))
def verify_delete_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_delete_icon(feature_file_name, screen_shot):
            raise Exception("Failed to verify delete icon")
    except Exception as e:
        logger.error("Error while verifying delete icon " + str(e))
        raise e


@when(parsers.parse('DELETE icon clicked'))
def do_click_delete_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_delete_icon(feature_file_name, screen_shot):
            raise Exception("Failed to click DELETE icon")
    except Exception as e:
        logger.error("Error while clicking DELETE icon " + str(e))
        raise e


@then(parsers.parse('search with the file name is not present'))
def verify_deleted_record(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_deleted_record(feature_file_name, screen_shot):
            raise Exception("Failed to verify delete file")
    except Exception as e:
        logger.error("Error while verifying delete file " + str(e))
        raise e


@then(parsers.parse('verify the PLACE ORDERS icon'))
def verify_place_orders_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_place_orders_icon(feature_file_name, screen_shot):
            raise Exception("Failed to verify place orders icon")
    except Exception as e:
        logger.error("Error while verifying place orders icon " + str(e))
        raise e


@when(parsers.parse('PLACE ORDERS icon clicked'))
def do_click_place_orders_icon(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.do_click_place_orders_icon(feature_file_name, screen_shot):
            raise Exception("Failed to click place orders icon")
    except Exception as e:
        logger.error("Error while clicking place orders icon " + str(e))
        raise e


@then(parsers.parse('verify that order is placed'))
def verify_order_placed(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_order_placed(feature_file_name, screen_shot):
            raise Exception("Failed to verify delete file")
    except Exception as e:
        logger.error("Error while verifying delete file " + str(e))
        raise e


@when(parsers.parse('filter with user'))
def do_select_uploaded_by_option(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_select_uploaded_by_option(feature_file_name, screen_shot, 'Shyam Tiwari'):
            raise Exception("Failed to select Ready to place status")
    except Exception as e:
        logger.error("Error while selecting Ready to place status " + str(e))
        raise e


@then(parsers.parse('verify the file upload list page filtered with user'))
def verify_user_name(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_user_name(feature_file_name, screen_shot, 'Shyam Tiwari'):
            raise Exception("Failed to verify user name")
    except Exception as e:
        logger.error("Error while verifying user name " + str(e))
        raise e


@when(parsers.parse('upload Duplicate file'))
def do_upload_duplicate_file(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_upload_duplicate_file(feature_file_name, screen_shot):
            raise Exception("Failed to select duplicate file")
    except Exception as e:
        logger.error("Error while selecting Ready to place status " + str(e))
        raise e


@then(parsers.parse('verify Duplicate file error message'))
def verify_duplicate_file_error_message(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_duplicate_file_error_message(feature_file_name, screen_shot):
            raise Exception("Failed to verify duplicate error message")
    except Exception as e:
        logger.error("Error while verifying duplicate error message" + str(e))
        raise e


@when(parsers.parse('upload file with one field as Null value'))
def do_uploaded_file_with_one_null_values(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_uploaded_file(feature_file_name, screen_shot, 'One_Null_Value'):
            raise Exception("Failed to upload file with one null value")
    except Exception as e:
        logger.error("Error while uploading file " + str(e))
        raise e


@then(parsers.parse('verify the error message with one field as Null value'))
def verify_error_message_with_one_null_values(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_error_message(feature_file_name, screen_shot, 'One_Null_Value'):
            raise Exception("Failed to verify error message")
    except Exception as e:
        logger.error("Error while verifying error message " + str(e))
        raise e


@when(parsers.parse('clicked on Discard button'))
def do_click_discard_button(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_click_discard_button(feature_file_name, screen_shot):
            raise Exception("Failed to click discard button")
    except Exception as e:
        logger.error("Error while uploading file " + str(e))
        raise e


@when(parsers.parse('upload file with two field as Null value'))
def do_uploaded_file_with_two_null_values(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_uploaded_file(feature_file_name, screen_shot, 'Two_Null_Value'):
            raise Exception("Failed to upload file with two null values")
    except Exception as e:
        logger.error("Error while uploading file " + str(e))
        raise e


@then(parsers.parse('verify the error message with two field as Null value'))
def verify_error_message_with_two_null_values(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_error_message(feature_file_name, screen_shot, 'Two_Null_Value'):
            raise Exception("Failed to verify error message")
    except Exception as e:
        logger.error("Error while verifying error message " + str(e))
        raise e


@when(parsers.parse('clicked Apply button after filling required field'))
def do_click_apply_button(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_click_apply_button(feature_file_name, screen_shot):
            raise Exception("Failed to click Apply button")
    except Exception as e:
        logger.error("Error while clicking button " + str(e))
        raise e


@then(parsers.parse('verify Order status is Ready to place'))
def verify_order_status_ready_to_place(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_order_status(feature_file_name, screen_shot, 'Ready to place'):
            raise Exception("Failed to verify order status as Ready to place")
    except Exception as e:
        logger.error("Error while verifying order status " + str(e))
        raise e


@when(parsers.parse('upload file with three field as Null value'))
def do_uploaded_file_with_three_null_values(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_uploaded_file(feature_file_name, screen_shot, 'Three_Null_Value'):
            raise Exception("Failed to upload file with 3 null values")
    except Exception as e:
        logger.error("Error while uploading file " + str(e))
        raise e


@then(parsers.parse('verify the error message with three field as Null value'))
def verify_error_message_with_three_null_values(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_error_message(feature_file_name, screen_shot, 'Three_Null_Value'):
            raise Exception("Failed to verify error message")
    except Exception as e:
        logger.error("Error while verifying error message " + str(e))
        raise e


@then(parsers.parse('verify bulk order upload page'))
def verify_bulk_order_upload_page(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_bulk_order_upload_page(feature_file_name, screen_shot):
            raise Exception("Failed to verify bulk order upload page")
    except Exception as e:
        logger.error("Error while verifying bulk order upload page " + str(e))
        raise e


@then(parsers.parse('verify multiple bulk order page status'))
def verify_multiple_bulk_order_upload_page(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        if not bulk_order_upload_steps.verify_multiple_bulk_order_upload_page(feature_file_name, screen_shot):
            raise Exception("Failed to verify multiple bulk order page status")
    except Exception as e:
        logger.error("Error while verifying bulk order upload page " + str(e))
        raise e


@when(parsers.parse('upload file with valid Ingram sku and vendor part number value'))
def do_uploaded_file_with_sku_and_vendor_part_no(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_uploaded_file(feature_file_name, screen_shot, 'Sku_And_Vendor_Part_No'):
            raise Exception("Failed to upload file with sku and vendor part no")
    except Exception as e:
        logger.error("Error while uploading file " + str(e))
        raise e


@when(parsers.parse('upload file with only valid vendor part number value'))
def do_upload_file_with_sku_null_and_vendor_part_no(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_uploaded_file(feature_file_name, screen_shot, 'Null_Sku_and_Vendor_Part_No'):
            raise Exception("Failed to upload file with Null sku and vendor part no")
    except Exception as e:
        logger.error("Error while uploading file " + str(e))
        raise e


@when(parsers.parse('upload file with vendor part number and Ingram SKU mismatch'))
def do_upload_file_with_sku_and_vendor_part_no_mismatch(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_uploaded_file(feature_file_name, screen_shot, 'Sku_And_Vendor_Part_No_Mismatch'):
            raise Exception("Failed to upload file with sku and vendor part no")
    except Exception as e:
        logger.error("Error while uploading file " + str(e))
        raise e


@when(parsers.parse('clicked Apply button after updating ingram sku field'))
def do_click_apply_button_for_ingram_sku(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:

        if not bulk_order_upload_steps.do_click_apply_button_for_ingram_sku(feature_file_name, screen_shot):
            raise Exception("Failed to click Apply button")
    except Exception as e:
        logger.error("Error while clicking button " + str(e))
        raise e


@given(parsers.parse('logout the X4A url'))
def logout_x4a_url(init_driver):
    feature_file_name = "bulk_order_upload"
    bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
    try:
        bulk_order_upload_steps.logout_x4a_url(feature_file_name)
        logger.info("Logout X4A url is successfully.")
    except Exception as e:
        logger.error("Not able to logout x4a url " + str(e))
        raise e
