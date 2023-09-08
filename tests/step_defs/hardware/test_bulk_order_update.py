# from pytest_bdd import scenario, parsers, when, then, given
# from CommonUtilities import readWriteTestData
# from CommonUtilities.parse_config import ParseConfigFile
# from CommonUtilities.file_operations import logger
# from CommonUtilities.readProperties import ReadConfig
# from db.service.X4AInputOrderDbManagementService import X4AInputOrderDbManagementService
# from pages.X4A.Facade.PrepareObject import PrepareObject
# from pages.X4A.TestSteps.validateBulkOrderUploadData import ValidateBulkOrderUploadData
#
# parse_config_json = ParseConfigFile()
# screen_shot = {"path": " "}
# x4a_status_list = []
# x4a_input_order_list = []
# db_file_path = ReadConfig.get_db_file_path()
#
# @scenario("features/hardware/bulk_order_upload.feature", "Login to X4A portal")
# def test_login_the_x4a_portal():
#     pass
#
# @scenario("features/hardware/bulk_order_upload.feature", "File Upload option & Dialog Box")
# def test_upload_option():
#     pass
# #
# @scenario("features/hardware/bulk_order_upload.feature", "Upload file error")
# def test_upload_file_error():
#     pass
#
# @scenario("features/hardware/bulk_order_upload.feature", "Template error")
# def test_template_error():
#     pass
#
# @scenario("features/hardware/bulk_order_upload.feature", "Upload file")
# def test_upload_file():
#     pass
#
#
# @scenario("features/hardware/bulk_order_upload.feature", "logout X4A")
# def test_logout_x4a():
#     pass
#
#
# @given(parsers.parse('launch chrome browser and open the X4A url'))
# def launch_browser(init_driver):
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     order_management_srv_obj = X4AInputOrderDbManagementService()
#     prepare_obj = PrepareObject(init_driver)
#     feature_file_name = "bulk_order_upload"
#     try:
#         test_data_order = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
#         filtered_order_data = bulk_order_upload_steps.filtered_orders_by_feature_file(test_data_order, feature_file_name)
#         logger.info(filtered_order_data)
#         for order_index, test_data_order in filtered_order_data.iterrows():
#             x4a_input_order_list.clear()
#             logger.info(test_data_order)
#             x4a_input_order_data = prepare_obj.prepare_x4a_inp_ord_data_obj(test_data_order)
#             x4a_input_order_list.append(x4a_input_order_data)
#             order_management_srv_obj.save_x4a_input_order(db_file_path, x4a_input_order_list)
#         environment = parse_config_json.get_data_from_config_json("environment", "environment_type", "config.json")
#         logger.info(environment)
#         if environment == 'Stage':
#             url = parse_config_json.get_data_from_config_json("x4aStageCredentials", "x4aBaseUrl", "config.json")
#         else:
#             url = parse_config_json.get_data_from_config_json("x4aBetaCredentials", "x4aBaseUrl", "config.json")
#         init_driver.get(url)
#     except Exception as e:
#         logger.error("Not able to Launch the browser and login x4a %s", e)
#         raise e
#
#
# @then(parsers.parse('provide user ID and Password to login'))
# def login(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         bulk_order_upload_steps.login(feature_file_name, screen_shot)
#         logger.info("Launched the browser and login to X4A is successfully.")
#     except Exception as e:
#         logger.error("Not able to Launch the browser and login x4a %s", e)
#         raise e
#
#
# @when(parsers.parse('the user traverse to Bulk order update menu'))
# def click_on_bulk_order_upload_menu(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.click_on_bulk_order_upload_menu(feature_file_name, screen_shot):
#             raise Exception("Failed to click on bulk order upload menu")
#     except Exception as e:
#         logger.error("Error while clicking on bulk order upload menu %s", e)
#         raise e
#
#
# @then(parsers.parse('verify bulk order update page'))
# def verify_bulk_order_upload_page(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.verify_bulk_order_upload_page(feature_file_name, screen_shot):
#             raise Exception("Failed to verify bulk order upload page")
#     except Exception as e:
#         logger.error("Error while verifying bulk order upload page %s", e)
#         raise e
#
# @when(parsers.parse('upload file button clicked'))
# def click_upload_file(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.click_upload_file(feature_file_name, screen_shot):
#             raise Exception("Failed to click upload file button")
#     except Exception as e:
#         logger.error("Error while clicking upload file button %s", e)
#         raise e
#
# @then(parsers.parse('verify upload file popup'))
# def verify_upload_file_popup(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.verify_upload_file_popup(feature_file_name, screen_shot):
#             raise Exception("Failed to verify upload file popup")
#     except Exception as e:
#         logger.error("Error while verifying upload file popup %s", e)
#         raise e
#
#
# @when(parsers.parse('other than excel file was uploaded'))
# def do_upload_error_file(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.do_upload_error_file(feature_file_name, screen_shot):
#             raise Exception("Failed to select error file")
#     except Exception as e:
#         logger.error("Error while selecting file %s", e)
#         raise e
#
# @then(parsers.parse('verify error message'))
# def verify_error_popup(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.verify_error_popup(feature_file_name, screen_shot):
#             raise Exception("Failed to verify file error popup")
#     except Exception as e:
#         logger.error("Error while verifying file error popup %s", e)
#         raise e
#
#
# @when(parsers.parse('different template was uploaded'))
# def do_upload_template_error_file(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.do_upload_template_error_file(feature_file_name, screen_shot):
#             raise Exception("Failed to select error file")
#     except Exception as e:
#         logger.error("Error while selecting file %s", e)
#         raise e
#
# @then(parsers.parse('verify template error message'))
# def verify_template_error_message(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.verify_template_error_message(feature_file_name, screen_shot):
#             raise Exception("Failed to verify template error message")
#     except Exception as e:
#         logger.error("Error while verifying template error message %s", e)
#         raise e
#
# @when(parsers.parse('file was uploaded'))
# def do_upload_file(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.do_select_file(feature_file_name, screen_shot):
#             raise Exception("Failed to select file")
#     except Exception as e:
#         logger.error("Error while selecting file %s", e)
#         raise e
#
# @then(parsers.parse('verify upload file ready popup'))
# def verify_selected_file_popup(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.verify_selected_file_popup(feature_file_name, screen_shot):
#             raise Exception("Failed to verify selected file popup")
#     except Exception as e:
#         logger.error("Error while verifying selecting file popup %s", e)
#         raise e
#
# @when(parsers.parse('click on delete icon'))
# def do_delete_file(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         if not bulk_order_upload_steps.do_delete_file(feature_file_name, screen_shot):
#             raise Exception("Failed to delete file")
#     except Exception as e:
#         logger.error("Error while deleting file %s", e)
#         raise e
#
#
# @given(parsers.parse('logout the X4A url'))
# def logout_x4a_url(init_driver):
#     feature_file_name = "bulk_order_upload"
#     bulk_order_upload_steps = ValidateBulkOrderUploadData(init_driver)
#     try:
#         bulk_order_upload_steps.logout_x4a_url(feature_file_name)
#         logger.info("Logout X4A url is successfully.")
#     except Exception as e:
#         logger.error("Not able to logout x4a url %s", e)
#         raise e
