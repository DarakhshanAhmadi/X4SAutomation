import sqlite3
from sqlite3 import Error
from db.util.SqlConstant import SqlConstant
from tests.test_base_x4a import BaseTest
import sqlite3


class X4AInventoryDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, x4a_inventory_list):
        # This method is responsible to insert multiple records into x4a_inventory table
        try:
            self.logger.info("Inserting the input data into x4a_inventory table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for x4a_inventory in x4a_inventory_list:
                cursor.execute(SqlConstant.X4A_INVENTORY_INSERT_SQL_QUERY,
                               (x4a_inventory.feature_file_name, x4a_inventory.under_performing_sku,
                                x4a_inventory.under_performing_mfn_part_number,
                                x4a_inventory.vendor_business_manager, x4a_inventory.vendor_name, x4a_inventory.country,
                                x4a_inventory.actions, x4a_inventory.comment, x4a_inventory.aging_sku, x4a_inventory.aging_mfn_part_number))
                connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to insert the data into x4a_inventory table "
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_inventory table")

    def get_x4a_inventory_test_case_detail(self, sql_util, feature_file_name):
        # This method is responsible to get given test case records from x4a_inventory table
        inventory_test_case_details_json = None
        try:
            self.logger.info("Fetching the records from x4a_inventory table")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            cursor.execute(SqlConstant.X4A_INVENTORY_GET_TEST_CASE_RECORD_SQL_QUERY, [str(feature_file_name)])
            inventory_test_case_details = cursor.fetchall()
            inventory_test_case_details_json = [dict(ix) for ix in inventory_test_case_details][0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch test case record from x4a_inventoryx4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
            self.logger.info("Records fetched successfully from x4a_inventory table")
            return inventory_test_case_details_json