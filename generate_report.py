import os
import time

from CommonUtilities.logGeneration import LogGenerator
from HTMLReporter.plugin import HTMLReporter
from CommonUtilities.readProperties import parse_config_file, ReadConfig
from db.service.AutomationReportDataDbManagementService import AutomationReportDataDbManagementService
from db.service.X4AInputOrderDbManagementService import IM360InputOrderDbManagementService
from db.util.artifact_operations import ArtifactOperations


def test_generate_report():
    logger = LogGenerator.logGen()
    try:
        db_file_path = ReadConfig.get_db_file_path()
        reports_dir_path = parse_config_file.get_data_from_config_json("logData", "reportsDirectoryPath")
        report_file_name = parse_config_file.get_data_from_config_json("logData", "reportFileName")
        logo_file = parse_config_file.get_data_from_config_json("logData", "logoFileName")
        automation_report_db_mgmt_service = AutomationReportDataDbManagementService()
        im360_input_order_db_mgmt_service = IM360InputOrderDbManagementService()

        logger.info("Creating AutomationReports Folder if it is not exists...")
        os.makedirs(reports_dir_path, exist_ok=True)
        path = os.path.join(reports_dir_path, report_file_name)
        logger.info("Getting Dashboard data for Report...")
        dashboard_data = automation_report_db_mgmt_service.get_dashboard_data(db_file_path)
        logger.info("Getting Region data for Report...")
        region_data = automation_report_db_mgmt_service.get_region_data(db_file_path)
        logger.info("Getting Marketplace list for Report...")
        marketplace_list = automation_report_db_mgmt_service.get_marketplace_list(db_file_path)
        logger.info("Getting Config Meta Data for Report...")
        config_metadata = automation_report_db_mgmt_service.get_config_meta_data(db_file_path)
        logger.info("Getting Suite data for Report...")
        suite_data = automation_report_db_mgmt_service.get_suite_data(db_file_path)
        logger.info("Getting Test Execution data for Report...")
        test_execution_data = automation_report_db_mgmt_service.get_test_data(db_file_path)
        logger.info("Getting Screenshot data for Report...")
        failed_test_data = automation_report_db_mgmt_service.get_screenshot_data(db_file_path)
        logger.info("Getting Service name for Report...")
        service_name_list = im360_input_order_db_mgmt_service.get_distinct_service_name(db_file_path)
        logger.info("Getting Test data for Report...")
        test_data = automation_report_db_mgmt_service.get_so_po_test_data(db_file_path)

        # generate html report
        logger.info("Start preparing Automation Report...")
        html_report = HTMLReporter()
        report_file = open(path, 'w')
        message = html_report.generate_report(logo_file, service_name_list, dashboard_data, region_data,
                                              marketplace_list, config_metadata, suite_data, test_execution_data,
                                              test_data, failed_test_data)
        report_file.write(message)
        report_file.close()
        logger.info("Automation Report is generated at location: %s", path)

        archive_artifacts()
    except Exception as e:
        logger.error("Failed to generate Automation Report: %s", e)
        raise e


def archive_artifacts():
    try:
        artifact_operations = ArtifactOperations()
        backup_path = parse_config_file.get_data_from_config_json("logData", "backupDirectoryPath") \
                      + time.strftime("%Y%m%d_%H%M%S")
        os.makedirs(backup_path, exist_ok=True)

        artifact_operations.archive_database(backup_path)
        artifact_operations.archive_output_files(backup_path)
        artifact_operations.archive_screenshots(backup_path)
        artifact_operations.archive_reports(backup_path)
        artifact_operations.archive_logs(backup_path)
    except Exception as e:
        raise e
