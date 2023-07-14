from sqlite3 import Error
from db.util.SqlConstant import SqlConstant

from tests.test_base_x4a import BaseTest


class X4AUserDataDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, x4a_user_data_list):
        # This method is responsible to insert multiple records into x4a_user_data table
        try:
            self.logger.info("Inserting the input data into x4a_user_data table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for x4a_user_data in x4a_user_data_list:
                cursor.execute(SqlConstant.X4A_USER_DATA_INSERT_SQL_QUERY,
                               (x4a_user_data.feature_file_name, x4a_user_data.Associate_Name, x4a_user_data.Associate_Email,
                                x4a_user_data.Associate_Roles, x4a_user_data.Associate_Countries))
                connection.commit()
        except Error as e:
            self.logger.error("Exception occurred while trying to insert the Associate details into x4a_user_data table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_user_data table")


    def get_associate_details(self, sql_util):
        # This method is responsible for fetching Associate details from user_data table
        reseller_reconcile_key = None
        try:
            self.logger.info(f"Fetching Associate details for user_management feature from User data Table.")
            self.connection = sql_util.get_connection()
            cursor = self.connection.cursor()
            cursor.execute(SqlConstant.X4A_USER_DATA_BY_FEATURE_FILE_SQL_QUERY)
            user_data = cursor.fetchall()
            # for record in user_data:
            #     user_data = record[0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch Associate details from user_data table " + str(e))
        else:
            self.logger.info('Associate details fetched successfully!')
        finally:
            sql_util.close_connection(self.connection)
        
        return user_data[0]

