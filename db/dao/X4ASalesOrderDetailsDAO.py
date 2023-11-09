import sqlite3
from sqlite3 import Error
from db.util.SqlConstant import SqlConstant

from tests.test_base_x4a import BaseTest


class X4ASalesOrderDetailsDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, x4a_sales_order_details_list):
        # This method is responsible to insert multiple records into x4a_sales_order_details table
        try:
            self.logger.info("Inserting the input data into x4a_sales_order_details table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for x4a_sales_order_details in x4a_sales_order_details_list:
                cursor.execute(SqlConstant.X4A_SALES_ORDER_DETAILS_INSERT_SQL_QUERY,
                               (x4a_sales_order_details.feature_file_name, x4a_sales_order_details.order_entry_channel,
                                x4a_sales_order_details.im_order_number,
                                x4a_sales_order_details.order_type, x4a_sales_order_details.reseller_po, x4a_sales_order_details.end_user_po,
                                x4a_sales_order_details.order_status, x4a_sales_order_details.order_value, x4a_sales_order_details.currency_code,
                                x4a_sales_order_details.terms_code, x4a_sales_order_details.ship_from_warehouse_id, x4a_sales_order_details.warehouse_name,
                                x4a_sales_order_details.carrier_code, x4a_sales_order_details.ship_to_suffix, x4a_sales_order_details.ship_to_name,
                                x4a_sales_order_details.ship_to_address, x4a_sales_order_details.ship_to_phone, x4a_sales_order_details.ship_to_contact, x4a_sales_order_details.ship_to_email,
                                x4a_sales_order_details.bill_to_suffix, x4a_sales_order_details.bill_to_name,
                                x4a_sales_order_details.bill_to_address, x4a_sales_order_details.bill_to_phone, x4a_sales_order_details.bill_to_contact,
                                x4a_sales_order_details.bill_to_email,  x4a_sales_order_details.end_user_id, x4a_sales_order_details.end_user_address,
                                x4a_sales_order_details.end_user_contact, x4a_sales_order_details.special_bid, x4a_sales_order_details.unit_price, x4a_sales_order_details.quantity))
                connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to insert the data into x4a_sales_order_details table "
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_sales_order_details table")

    def get_id_from_im_order_number(self, sql_util, im_order_number):
        # This method is responsible to fetch id from x4a_sales_order_details table
        id = None
        try:
            self.logger.info("Fetching the id from x4a_sales_order_details table by im order")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_SALES_ORDER_DETAILS_GET_ID_SQL_QUERY, [str(im_order_number)])
            x4a_sales_order_details = cursor.fetchall()
            for record in x4a_sales_order_details:
                id = record[-1]
        except Error as e:
            self.logger.error(
                "Exception occurred while fetching the id from x4a_sales_order_details table by im order"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
            self.logger.info("Fetched id successfully from x4a_sales_order_details table")
            return id

    def get_x4a_order_detail(self, sql_util, im_order_number):
        # This method is responsible to get given test case records from x4a_sales_order_details table
        order_details_json = None
        try:
            self.logger.info("Fetching the records from x4a_sales_order_details table by test case ID and marketplace")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            cursor.execute(SqlConstant.X4A_SALES_ORDER_DETAILS_GET_ORDER_DETAILS_SQL_QUERY, [str(im_order_number)])
            order_test_case_details = cursor.fetchall()
            order_details_json = [dict(ix) for ix in order_test_case_details][0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch test case record from x4a_sales_order_details table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
            self.logger.info("Records fetched successfully from x4a_sales_order_details table")
            return order_details_json

