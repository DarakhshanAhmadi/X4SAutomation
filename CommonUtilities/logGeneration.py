import logging
import os

from CommonUtilities.parse_config import ParseConfigFile


class LogGenerator:

    @staticmethod
    def logGen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        parse_config_json = ParseConfigFile()
        log_path = os.path.join(parse_config_json.get_data_from_config_json("logData", "logDirectoryPath"),
                                parse_config_json.get_data_from_config_json("logData", "logFileName"))
        logging.basicConfig(filename=log_path, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger()
        return logger
#ReadConfig.getLogFileName()