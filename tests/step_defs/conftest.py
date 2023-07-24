import os
import time
import pytest
from selenium import webdriver
from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.readProperties import ReadConfig
from CommonUtilities.file_operations import logger
from db.database_operations import DataOperations


@pytest.fixture(scope="module")
def init_driver():
    screen_shot_path = ReadConfig.getScreenshotPath()
    module_screen_shot_path = screen_shot_path + "\\X4A\\"
    pass_screen_shot_path = screen_shot_path + "\\X4A\\success\\"
    fail_screen_shot_path = screen_shot_path + "\\X4A\\error\\"
    os.makedirs(screen_shot_path, exist_ok=True)
    os.makedirs(module_screen_shot_path, exist_ok=True)
    os.makedirs(pass_screen_shot_path, exist_ok=True)
    os.makedirs(fail_screen_shot_path, exist_ok=True)
    create_database()
    browser = ReadConfig.get_browser()
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_argument("--incognito")
        web_driver = webdriver.Chrome(executable_path=ReadConfig.get_chrome_executable_path(), options=options)
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
        options.add_argument("inprivate")
        web_driver = webdriver.Edge(executable_path=ReadConfig.get_edge_executable_path(), options=options)
    web_driver.maximize_window()
    yield web_driver
    time.sleep(5)
    web_driver.quit()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    os.environ['IS_FEATURE_FAILED'] = str("True")
    logger.error(f"Scenario: {scenario.name} is failed of feature: {feature.tags} => {feature.name} .")
    logger.error(f"Failed Step: {step.name}.")


def pytest_configure(config):
    config._metadata["Project Name"] = "Automatic Data Creator (ACDC)"
    config._metadata["Designed By"] = "XVS QA Team"
    config._metadata["Tester"] = "XVS QA Team "
    config._metadata["version"] = "2.0"


def create_database():
    logger = LogGenerator.logGen()
    data_operations = DataOperations()
    try:
        data_operations.create_database_data()
    except Exception as e:
        logger.error("Failed to create database: %s", e)
        raise e