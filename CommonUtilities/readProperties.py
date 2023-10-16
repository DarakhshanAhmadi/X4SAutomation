import os

from CommonUtilities.parse_config import ParseConfigFile

parse_config_file = ParseConfigFile()


class ReadConfig:

    @staticmethod
    def get_chrome_executable_path():
        chrome_executable_path = parse_config_file.get_data_from_config_json("browserDriverPaths",
                                                                             "chromeExecutablePath")
        return chrome_executable_path

    @staticmethod
    def get_firefox_executable_path():
        firefox_executable_path = parse_config_file.get_data_from_config_json("browserDriverPaths",
                                                                              "firefoxExecutablePath")
        return firefox_executable_path

    @staticmethod
    def get_im360_base_url():
        im360_URL = parse_config_file.get_data_from_config_json("im360CommonData", "baseUrl")
        return im360_URL

    @staticmethod
    def get_im360_username():
        im360_username = parse_config_file.get_data_from_config_json("im360CommonData", "im360UserName")
        return im360_username

    @staticmethod
    def get_im360_password():
        im360_password = parse_config_file.get_data_from_config_json("im360CommonData", "enc_im360Password")
        return im360_password

    @staticmethod
    def getLogFileName():
        log_path = os.path.join(parse_config_file.get_data_from_config_json("logData", "logDirectoryPath"),
                                parse_config_file.get_data_from_config_json("logData", "logFileName"))
        return log_path

    @staticmethod
    def get_test_data_file():
        test_data_file = parse_config_file.get_data_from_config_json("inputFile", "inputFileName")
        return test_data_file

    @staticmethod
    def get_db_file_path():
        im360_db_file_path = parse_config_file.get_data_from_config_json("dbLocation", "db_file_path")
        return im360_db_file_path

    @staticmethod
    def get_file_path():
        file_path = parse_config_file.get_data_from_config_json("dbLocation", "file_path")
        return file_path

    @staticmethod
    def getScreenshotPath():
        ScreenShot_path = parse_config_file.get_data_from_config_json("logData", "screenshotsDirectoryPath")
        return ScreenShot_path

    @staticmethod
    def getTestType():
        test_type = parse_config_file.get_data_from_config_json("testType", "test_type")
        return test_type

    @staticmethod
    def get_region_data_file():
        test_data_file = parse_config_file.get_data_from_config_json("inputFile", "regionInputFileData")
        return test_data_file

    @staticmethod
    def get_im360_sample_data_file():
        test_data_file = parse_config_file.get_data_from_config_json("X4A", "im360_sample_excel_file")
        return test_data_file

    @staticmethod
    def getExecutionType():
        test_type = parse_config_file.get_data_from_config_json("executionType", "execution_type")
        return test_type

    @staticmethod
    def get_browser():
        browser = parse_config_file.get_data_from_config_json("browserDriverPaths", "browser")
        return browser

    @staticmethod
    def get_edge_executable_path():
        edge_executable_path = parse_config_file.get_data_from_config_json("browserDriverPaths",
                                                                             "edgeExecutablePath")
        return edge_executable_path

    @staticmethod
    def get_controller_test_data_file():
        test_data_file = parse_config_file.get_data_from_config_json("inputFile", "controllerFileName")
        return test_data_file

    @staticmethod
    def get_inventory_test_data_file():
        test_data_file = parse_config_file.get_data_from_config_json("inputFile", "inventoryInputFileName")
        return test_data_file