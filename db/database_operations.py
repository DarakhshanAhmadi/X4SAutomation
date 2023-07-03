import logging
import os
from CommonUtilities.parse_config import ParseConfigFile
from db.util.SqlUtil import SqlUtil

logger = logging.getLogger(__name__)


class DataOperations:
    parse_config_file = ParseConfigFile()
    db_file_path = parse_config_file.get_data_from_config_json("dbLocation", "db_file_path")
    db_script_file_path = parse_config_file.get_data_from_config_json("dbLocation", "db_script_file_path")
    sql_util = SqlUtil(db_file_path)

    def create_database_data(self):
        if os.path.exists(self.db_file_path):
            logger.info("Start deleting old database and creating Fresh DB...")
            logger.info(f"Deleting database file [{self.db_file_path}]")
            os.remove(self.db_file_path)
        else:
            logger.info(f"Creating new database file [{self.db_file_path}]")
        self.execute_db_script()

    def execute_db_script(self, script_file_path=None):
        if script_file_path is None:
            script_file_path = self.db_script_file_path
        logger.info(f"Writing DB Script file [{script_file_path}] to database file [{self.db_file_path}]")
        with open(script_file_path) as sql_file:
            sql = sql_file.read()
        conn = self.sql_util.get_connection()
        cur = conn.cursor()
        cur.executescript(sql)
        conn.commit()
        self.sql_util.close_connection(conn)
        logger.info(f"Successfully created the database [{self.db_file_path}]")