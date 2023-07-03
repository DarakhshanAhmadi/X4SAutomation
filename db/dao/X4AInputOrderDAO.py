from sqlite3 import Error
from db.util.SqlConstant import SqlConstant

from tests.test_base_x4a import BaseTest


class X4AInputOrderDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, im360_input_order_list):
        # This method is responsible to insert multiple records into x4a_input_order table
        try:
            self.logger.info("Inserting the input data into x4a_input_order table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for im360_input_order in im360_input_order_list:
                cursor.execute(SqlConstant.X4A_INPUT_ORDER_INSERT_SQL_QUERY,
                               (im360_input_order.feature_file_name, im360_input_order.reseller_bcn,
                                im360_input_order.reseller_po))
                connection.commit()
        except Error as e:
            self.logger.error("Exception occurred while trying to insert the input data into x4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_input_order table")
