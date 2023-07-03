import sqlite3
from sqlite3 import Error

from tests.test_base_x4a import BaseTest


class SqlUtil(BaseTest):
    def __init__(self, db_path=None):
        self.db_path = db_path

    def get_connection(self):
        # This method provides a connection of DB that can be used for any DB related operation
        # If DB does not exist then this method also creates a DB
        global connection
        try:
            # self.logger.info("Trying to open database connection")
            connection = sqlite3.connect(self.db_path)
            # self.logger.info("Database connection opened successfully")
        except Error as e:
            self.logger.error("Exception occurred while trying to open the database connection " + str(e))

        return connection

    def close_connection(self, connection):
        # This method is responsible to terminate a DB connection
        try:
            # self.logger.info("Trying to close database connection")
            connection.close()
            # self.logger.info("Database connection closed successfully")
        except Error as e:
            self.logger.error("Exception occurred while trying to close the database connection " + str(e))