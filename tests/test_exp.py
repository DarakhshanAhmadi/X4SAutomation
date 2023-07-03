from CommonUtilities import readWriteTestData
from CommonUtilities.logGeneration import LogGenerator
from CommonUtilities.readProperties import ReadConfig

test_data_all = readWriteTestData.load_excel_to_dictionary(ReadConfig.get_test_data_file(), "Input_Data")
logger = LogGenerator.logGen()


def test_abc():
    logger.info(test_data_all)
