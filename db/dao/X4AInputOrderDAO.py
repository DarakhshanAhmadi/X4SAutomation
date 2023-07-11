from sqlite3 import Error
from db.util.SqlConstant import SqlConstant
from tests.test_base_x4a import BaseTest
import sqlite3


class X4AInputOrderDAO(BaseTest):

    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_records(self, sql_util, x4a_input_order_list):
        # This method is responsible to insert multiple records into x4a_input_order table
        try:
            self.logger.info("Inserting the input data into x4a_input_order table")
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            for x4a_input_order in x4a_input_order_list:
                cursor.execute(SqlConstant.X4A_INPUT_ORDER_INSERT_SQL_QUERY,
                               (x4a_input_order.feature_file_name, x4a_input_order.reseller_bcn,
                                x4a_input_order.im_order_number, x4a_input_order.order_type, x4a_input_order.reseller_po,
                                x4a_input_order.vendor_name,x4a_input_order.order_status))
                connection.commit()
        except Error as e:
            self.logger.error("Exception occurred while trying to insert the input data into x4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data inserted successfully into x4a_input_order table")

    def get_bcn_by_feature_file_name(self, sql_util, feature_file_name):
        reseller_bcn = None
        try:
            self.logger.info("Fetching the reseller bcn from x4a_input_order table by feature file name")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_GET_BCN_BY_FEATURE_FILE_NAME_SQL_QUERY, [str(feature_file_name)])
            x4a_input_order = cursor.fetchall()
            for record in x4a_input_order:
                reseller_bcn = record[0]
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to fetch reseller bcn from IM360_input_order table by test "
                "case ID"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Reseller BCN %s fetched successfully from X4A_input_order table by feature file name",
                             reseller_bcn)
            return reseller_bcn

    def get_im_order_number_by_feature_file_name(self, sql_util, feature_file_name):
        im_order_no = None
        try:
            self.logger.info("Fetching the IM Order Number from x4a_input_order table by feature file name")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_GET_IM_ORDER_NUMBER_BY_FEATURE_FILE_NAME_SQL_QUERY, [str(feature_file_name)])
            x4a_input_order = cursor.fetchall()
            for record in x4a_input_order:
                im_order_no = record[0]
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to fetch IM Order Number from IM360_input_order table by test "
                "case ID"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("IM Order Number %s fetched successfully from X4A_input_order table by feature file name",
                             im_order_no)
            return im_order_no

    def get_order_type_by_feature_file_name(self, sql_util, feature_file_name):
        order_type = None
        try:
            self.logger.info("Fetching the Order Type from x4a_input_order table by feature file name")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_GET_ORDER_TYPE_BY_FEATURE_FILE_NAME_SQL_QUERY, [str(feature_file_name)])
            x4a_input_order = cursor.fetchall()
            for record in x4a_input_order:
                order_type = record[0]
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to fetch Order Type from IM360_input_order table by test "
                "case ID"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Order Type %s fetched successfully from X4A_input_order table by feature file name",
                             order_type)
            return order_type

    def get_vendor_name_by_feature_file_name(self, sql_util, feature_file_name):
        vendor_name = None
        try:
            self.logger.info("Fetching the Vendor Name from x4a_input_order table by feature file name")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_GET_VENDOR_NAME_BY_FEATURE_FILE_NAME_SQL_QUERY, [str(feature_file_name)])
            x4a_input_order = cursor.fetchall()
            for record in x4a_input_order:
                vendor_name = record[0]
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to fetch Vendor Name from IM360_input_order table by test "
                "case ID"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Vendor Name %s fetched successfully from X4A_input_order table by feature file name",
                             vendor_name)
            return vendor_name

    def get_reseller_po_by_feature_file_name(self, sql_util, feature_file_name):
        reseller_po = None
        try:
            self.logger.info("Fetching the Reseller PO from x4a_input_order table by feature file name")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_GET_RESELLER_PO_BY_FEATURE_FILE_NAME_SQL_QUERY, [str(feature_file_name)])
            x4a_input_order = cursor.fetchall()
            for record in x4a_input_order:
                reseller_po = record[0]
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to fetch Reseller PO from IM360_input_order table by test "
                "case ID"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Reseller PO %s fetched successfully from X4A_input_order table by feature file name",
                             reseller_po)
            return reseller_po

    def get_order_status_by_feature_file_name(self, sql_util, feature_file_name):
        order_status = None
        try:
            self.logger.info("Fetching the Order Status from x4a_input_order table by feature file name")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_GET_ORDER_STATUS_BY_FEATURE_FILE_NAME_SQL_QUERY, [str(feature_file_name)])
            x4a_input_order = cursor.fetchall()
            for record in x4a_input_order:
                order_status = record[0]
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to fetch Vendor Name from IM360_input_order table by test "
                "case ID"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Order Status %s fetched successfully from X4A_input_order table by feature file name",
                             order_status)
            return order_status

