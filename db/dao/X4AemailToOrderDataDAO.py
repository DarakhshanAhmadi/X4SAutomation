from sqlite3 import Error
from db.util.SqlConstant import SqlConstant

from tests.test_base_x4a import BaseTest


class X4AemailToOrderDataDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, x4a_email_to_order_scenario_list):
        # This method is responsible to insert multiple records into x4a_email_to_order_data table
        try:
            self.logger.info("Inserting the input data into x4a_email_to_order_data table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for x4a_email_to_order_data in x4a_email_to_order_scenario_list:
                cursor.execute(SqlConstant.X4A_EMAIL_TO_ORDER_SCENARIO_SQL_QUERY,
                               (x4a_email_to_order_data.feature_file_name, x4a_email_to_order_data.Account,
                                x4a_email_to_order_data.Country,x4a_email_to_order_data.Order_Status,
                                x4a_email_to_order_data.Customer_Name, x4a_email_to_order_data.Customer_PO,
                                x4a_email_to_order_data.Sales_Order, x4a_email_to_order_data.Processed,
                                x4a_email_to_order_data.Additional_Information))

                connection.commit()
        except Error as e:
            self.logger.error("Exception occurred while trying to insert the email_to order details into x4a_email_to_order_data table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_email_to_order_data table")


    def get_scenario_details(self, sql_util, scenario_no):
        # This method is responsible for fetching email_to order details from email_to_order_data table
        try:
            self.logger.info(f"Fetching email_to order details from email_to order data Table.")
            self.connection = sql_util.get_connection()
            cursor = self.connection.cursor()
            cursor.execute(SqlConstant.X4A_EMAIL_TO_ORDER_DATA_BY_FEATURE_FILE_SQL_QUERY, [scenario_no])
            email_to_order_data = cursor.fetchall()
            # for record in email_to_order_data:
            #     email_to_order_data = record[0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch email_to order details from email_to_order_data table " + str(e))
        else:
            self.logger.info('email_to order details fetched successfully!')
        finally:
            sql_util.close_connection(self.connection)
        
        return email_to_order_data

