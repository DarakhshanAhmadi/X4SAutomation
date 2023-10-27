import sqlite3
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
                                x4a_input_order.im_order_number,
                                x4a_input_order.order_type, x4a_input_order.reseller_po, x4a_input_order.vendor_name,
                                x4a_input_order.order_status, x4a_input_order.customer_po,
                                x4a_input_order.total_revenue_min,
                                x4a_input_order.total_revenue_max, x4a_input_order.customer_name,
                                x4a_input_order.order_value,
                                x4a_input_order.reference_numbers, x4a_input_order.billing_to_info,
                                x4a_input_order.ship_to_info,
                                x4a_input_order.end_user_info, x4a_input_order.order_lines_tab,
                                x4a_input_order.serial_numbers,
                                x4a_input_order.additional_attributes,
                                x4a_input_order.fraud_cancel_order_confirmation_id,
                                x4a_input_order.fraud_reprocess_order_confirmation_id,
                                x4a_input_order.data_errors_resubmit_order_confirmation_id,
                                x4a_input_order.reseller_name,
                                x4a_input_order.end_user_name, x4a_input_order.created_on,
                                x4a_input_order.filter_order_type, x4a_input_order.filter_order_status,
                                x4a_input_order.modify_reference_details_data_errors_order_id,
                                x4a_input_order.modify_shipping_notes_data_errors_order_id,
                                x4a_input_order.modify_vmf_details_data_errors_order_id,
                                x4a_input_order.modify_end_user_details_data_errors_order_id,
                                x4a_input_order.end_user_po, x4a_input_order.edit_order_line,
                                x4a_input_order.modify_billing_address_data_errors_order_id,
                                x4a_input_order.order_line_data_errors_order_id,
                                x4a_input_order.modify_order_line_data_errors_order_id,
                                x4a_input_order.im360_data_errors_order_confirmation_id),
                               )
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
                "Exception occurred while trying to fetch reseller bcn from x4a_input_order table by feature file name"
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
                "Exception occurred while trying to fetch IM Order Number from x4a_input_order table by feature file name"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("IM Order Number %s fetched successfully from X4A_input_order table by feature file name",
                             im_order_no)
            return im_order_no

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
                "Exception occurred while trying to fetch Vendor Name from x4a_input_order table by feature file name"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Vendor Name %s fetched successfully from X4A_input_order table by feature file name",
                             vendor_name)
            return vendor_name

    def get_customer_po_number_by_feature_file_name(self, sql_util, feature_file_name):
        # This method is responsible to fetch customer po number from x4a_input_order table
        customer_po = None
        try:
            self.logger.info("Fetching the customer po number from X4A_input_order table by feature file name ID %s",
                             feature_file_name)
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_INPUT_ORDER_GET_CUSTOMER_PO_NUMBER_BY_FEATURE_FILE_NAME,
                           [str(feature_file_name)])
            customer_pos = cursor.fetchall()
            self.logger.info(customer_pos)
            for record in customer_pos:
                customer_po = record[0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch customer po number from x4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data fetched successfully into x4a_input_order table")
        return customer_po

    def get_customer_name_by_feature_file_name(self, sql_util, feature_file_name):
        # This method is responsible to fetch customer po number from x4a_input_order table
        customer_name = None
        try:
            self.logger.info("Fetching the customer name from X4A_input_order table by feature file name ID %s",
                             feature_file_name)
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_INPUT_ORDER_GET_CUSTOMER_NAME_BY_FEATURE_FILE_NAME, [str(feature_file_name)])
            customer_names = cursor.fetchall()
            self.logger.info(customer_names)
            for record in customer_names:
                customer_name = record[0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch customer name from x4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data fetched successfully into x4a_input_order table")
        return customer_name

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
                "Exception occurred while trying to fetch Reseller PO from x4a_input_order table by feature file name"
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
                "Exception occurred while trying to fetch Vendor Name from x4a_input_order table by feature file name"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Order Status %s fetched successfully from X4A_input_order table by feature file name",
                             order_status)
            return order_status

    def get_max_total_revenue_by_feature_file_name(self, sql_util, feature_file_name):
        # This method is responsible to fetch customer po number from x4a_input_order table
        max_total_revenue = None
        try:
            self.logger.info("Fetching the max tax revenue from X4A_input_order table by feature file name ID %s",
                             feature_file_name)
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_INPUT_ORDER_GET_MAX_TOTAL_REVENUE_BY_FEATURE_FILE_NAME,
                           [str(feature_file_name)])
            max_total_revenues = cursor.fetchall()
            for record in max_total_revenues:
                max_total_revenue = record[0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch max total revenue from x4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data fetched successfully into x4a_input_order table")
        return max_total_revenue

    def get_min_total_revenue_by_feature_file_name(self, sql_util, feature_file_name):
        # This method is responsible to fetch customer po number from x4a_input_order table
        min_total_revenue = None
        try:
            self.logger.info("Fetching the min total revenue from X4A_input_order table by feature file name ID %s",
                             feature_file_name)
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            cursor.execute(SqlConstant.X4A_INPUT_ORDER_GET_MIN_TOTAL_REVENUE_BY_FEATURE_FILE_NAME,
                           [str(feature_file_name)])
            min_total_revenues = cursor.fetchall()
            for record in min_total_revenues:
                min_total_revenue = record[0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch min total revenue from x4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
        self.logger.info("data fetched successfully into x4a_input_order table")
        return min_total_revenue

    def get_x4a_input_test_case_order_detail(self, sql_util, feature_file_name):
        # This method is responsible to get given test case records from x4ainput_order table
        order_test_case_details_json = None
        try:
            self.logger.info("Fetching the records from x4a_input_order table by test case ID and marketplace")
            connection = sql_util.get_connection()
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            cursor.execute(SqlConstant.X4A_INPUT_GET_ORDER_TEST_CASE_RECORD_SQL_QUERY, [str(feature_file_name)])
            order_test_case_details = cursor.fetchall()
            order_test_case_details_json = [dict(ix) for ix in order_test_case_details][0]
        except Error as e:
            self.logger.error("Exception occurred while trying to fetch test case record fromx4a_input_order table "
                              + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)
            self.logger.info("Records fetched successfully from x4a_input_order table")
            return order_test_case_details_json

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
                "Exception occurred while trying to fetch Order Type Name from x4a_input_order table by feature file name"
                + str(e))
            raise e
        finally:
            sql_util.close_connection(connection)

            self.logger.info("Order Type %s fetched successfully from X4A_input_order table by feature file name",
                             order_type)
            return order_type

    def save_confirmation_id_in_db(self, sql_util, feature_file_name, data_errors_resubmit_order_confirmation_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating Data errors resubmit order confirmation_id into x4a_input_order table")
            cursor.execute(SqlConstant.X4A_UPDATE_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                           [data_errors_resubmit_order_confirmation_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update Data errors resubmit order confirmation_id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info("Data errors resubmit order confirmation_id updated successfully into x4a_input_order table")

    def save_confirmation_id_for_reference_details_in_db(self, sql_util, feature_file_name,
                                                         modify_reference_details_data_errors_order_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating modify Reference Details data errors order id into x4a_input_order table")
            cursor.execute(
                SqlConstant.X4A_UPDATE_MODIFY_REFERENCE_DETAILS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                [modify_reference_details_data_errors_order_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update modify Reference Details data errors order id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info(
            "Modify Reference Details data errors order id into x4a_input_order table updated successfully into x4a_input_order table")

    def save_confirmation_id_for_shipping_notes_in_db(self, sql_util, feature_file_name,
                                                      modify_shipping_notes_data_errors_order_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating modify Shipping notes data errors order id into x4a_input_order table")
            cursor.execute(
                SqlConstant.X4A_UPDATE_MODIFY_SHIPPING_NOTES_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                [modify_shipping_notes_data_errors_order_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update modify Shipping notes data errors order id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info(
            "Modify Shipping notes data errors order id into x4a_input_order table updated successfully into x4a_input_order table")

    def save_confirmation_id_for_vmf_details_in_db(self, sql_util, feature_file_name,
                                                   modify_vmf_details_data_errors_order_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating modify VMF Details data errors order id into x4a_input_order table")
            cursor.execute(
                SqlConstant.X4A_UPDATE_MODIFY_VMF_DETAILS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                [modify_vmf_details_data_errors_order_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update modify VMF Details data errors order id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info(
            "Modify VMF Details data errors order id into x4a_input_order table updated successfully into x4a_input_order table")

    def save_confirmation_id_for_end_user_details_in_db(self, sql_util, feature_file_name,
                                                        modify_end_user_details_data_errors_order_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating modify VMF Details data errors order id into x4a_input_order table")
            cursor.execute(
                SqlConstant.X4A_UPDATE_MODIFY_END_USER_DETAILS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                [modify_end_user_details_data_errors_order_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update modify End User Details data errors order id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info(
            "Modify End User Details data errors order id into x4a_input_order table updated successfully into x4a_input_order table")

    def save_confirmation_id_for_billing_address_details_in_db(self, sql_util, feature_file_name,
                                                               modify_billing_address_data_errors_order_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating modify Billing Address data errors order id into x4a_input_order table")
            cursor.execute(
                SqlConstant.X4A_UPDATE_MODIFY_BILLING_ADDRESS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                [modify_billing_address_data_errors_order_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update modify Billing Address data errors order id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info(
            "Modify Billing Address data errors order id into x4a_input_order table updated successfully into x4a_input_order table")

    def save_confirmation_id_for_order_line_in_db(self, sql_util, feature_file_name,
                                                  order_line_data_errors_order_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating remove Order Line data errors order id into x4a_input_order table")
            cursor.execute(
                SqlConstant.X4A_UPDATE_REMOVE_ORDER_LINE_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                [order_line_data_errors_order_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update remove Order Line data errors order id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info(
            "Remove Order Line data errors order id into x4a_input_order table updated successfully into x4a_input_order table")

    def save_confirmation_id_for_modify_order_line_in_db(self, sql_util, feature_file_name,
                                                         modify_order_line_data_errors_order_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating Order Line data errors order id into x4a_input_order table")
            cursor.execute(
                SqlConstant.X4A_UPDATE_ORDER_LINE_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                [modify_order_line_data_errors_order_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update Order Line data errors order id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info(
            "Modify Order Line data errors order id into x4a_input_order table updated successfully into x4a_input_order table")

    def save_im360_confirmation_id_in_db(self, sql_util, feature_file_name, im360_data_errors_order_confirmation_id):
        try:
            connection = sql_util.get_connection()
            cursor = connection.cursor()
            self.logger.info("Updating Im260 Data errors order confirmation_id into x4a_input_order table")
            cursor.execute(SqlConstant.X4A_UPDATE_IM360_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY,
                           [im360_data_errors_order_confirmation_id, feature_file_name])
            connection.commit()
        except Error as e:
            self.logger.error(
                "Exception occurred while trying to update Data errors resubmit order confirmation_id into x4a_input_order table " + str(
                    e))
        finally:
            sql_util.close_connection(connection)
        self.logger.info("Data errors resubmit order confirmation_id updated successfully into x4a_input_order table")
