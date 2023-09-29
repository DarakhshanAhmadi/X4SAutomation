from sqlite3 import Error
from db.util.SqlConstant import SqlConstant

from tests.test_base_x4a import BaseTest


class X4AbulkOrderDataDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, x4a_bulk_order_scenario_list):
        # This method is responsible to insert multiple records into x4a_bulk_order_data table
        try:
            self.logger.info("Inserting the input data into x4a_bulk_order_data table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for x4a_bulk_order_data in x4a_bulk_order_scenario_list:
                cursor.execute(SqlConstant.X4A_BULK_ORDER_SCENARIO_SQL_QUERY,
                               (x4a_bulk_order_data.feature_file_name, x4a_bulk_order_data.Scenario, x4a_bulk_order_data.Operator_ID,
                                x4a_bulk_order_data.Country_Code, x4a_bulk_order_data.Customer_Branch_and_Number,
                                x4a_bulk_order_data.Reseller_PO, x4a_bulk_order_data.Carrier_Code,
                                x4a_bulk_order_data.Order_Type, x4a_bulk_order_data.Header_Comment_1,
                                x4a_bulk_order_data.Header_Comment_2, x4a_bulk_order_data.Ingram_SKU,
                                x4a_bulk_order_data.Qty))
                connection.commit()
        except Error as e:
            self.logger.error("Exception occurred while trying to insert the bulk order details into x4a_bulk_order_data table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_bulk_order_data table")


    def get_scenario_details(self, sql_util, scenario_no):
        # This method is responsible for fetching bulk order details from bulk_order_data table
        try:
            self.logger.info(f"Fetching bulk order details from bulk order data Table.")
            self.connection = sql_util.get_connection()
            cursor = self.connection.cursor()
            cursor.execute(SqlConstant.X4A_BULK_ORDER_DATA_BY_FEATURE_FILE_SQL_QUERY, [scenario_no])
            bulk_order_data = cursor.fetchall()
            # for record in bulk_order_data:
            #     bulk_order_data = record[0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch bulk order details from bulk_order_data table " + str(e))
        else:
            self.logger.info('bulk order details fetched successfully!')
        finally:
            sql_util.close_connection(self.connection)
        
        return bulk_order_data

