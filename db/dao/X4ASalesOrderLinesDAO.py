import sqlite3
from sqlite3 import Error
from db.util.SqlConstant import SqlConstant

from tests.test_base_x4a import BaseTest


class X4ASalesOrderLinesDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, x4a_sales_order_lines_list):
        # This method is responsible to insert multiple records into x4a_sales_order_lines table
        try:
            self.logger.info("Inserting the input data into x4a_sales_order_lines table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for x4a_sales_order_lines in x4a_sales_order_lines_list:
                cursor.execute(SqlConstant.X4A_SALES_ORDER_LINES_INSERT_SQL_QUERY,
                               (x4a_sales_order_lines.im_order_number, x4a_sales_order_lines.line_number,
                                x4a_sales_order_lines.line_status,
                                x4a_sales_order_lines.im_part_number, x4a_sales_order_lines.vpn, x4a_sales_order_lines.description,
                                x4a_sales_order_lines.is_acop_applied, x4a_sales_order_lines.unit_weight, x4a_sales_order_lines.unit_price,
                                x4a_sales_order_lines.extended_price, x4a_sales_order_lines.cost, x4a_sales_order_lines.quantity,
                                x4a_sales_order_lines.quantity_confirmed, x4a_sales_order_lines.quantity_backordered, x4a_sales_order_lines.special_bid_number,
                                x4a_sales_order_lines.serial_numbers, x4a_sales_order_lines.sales_order_details_tbl_id))
                connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to insert the data into x4a_sales_order_lines table "
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_sales_order_lines table")

    def get_x4a_order_lines_by_im_order(self, sql_util, im_order_number):
        # This method is responsible to get given test case records from x4a_sales_order_lines table
        order_lines_json = None
        try:
            self.logger.info("Fetching the records from x4a_sales_order_lines table by im order")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            cursor.execute(SqlConstant.X4A_SALES_ORDER_LINES_DETAILS_FETCH_SQL_QUERY, [str(im_order_number)])
            order_test_case_lines = cursor.fetchall()
            order_lines_json = [dict(ix) for ix in order_test_case_lines]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch test case record from x4a_sales_order_lines table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
            self.logger.info("Records fetched successfully from x4a_sales_order_lines table")
            return order_lines_json



