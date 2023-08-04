class SqlConstant:
    X4A_INPUT_ORDER_INSERT_SQL_QUERY = "INSERT INTO x4a_input_order(" \
                                       "feature_file_name, reseller_bcn, im_order_number, order_type, " \
                                       "reseller_po, vendor_name, order_status, customer_po, total_revenue_min, total_revenue_max, customer_name," \
                                       "order_value, reference_numbers, billing_to_info, ship_to_info, end_user_info, order_lines_tab, serial_numbers, additional_attributes)" \
                                       "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    X4A_GET_IM_ORDER_NUMBER_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT im_order_number FROM x4a_input_order where feature_file_name =?"

    X4A_GET_VENDOR_NAME_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT vendor_name FROM x4a_input_order where feature_file_name =?"

    X4A_GET_BCN_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT reseller_bcn FROM x4a_input_order where feature_file_name =?"

    X4A_INPUT_ORDER_GET_CUSTOMER_PO_NUMBER_BY_FEATURE_FILE_NAME = "SELECT customer_po from x4a_input_order where feature_file_name = ?"

    X4A_INPUT_ORDER_GET_CUSTOMER_NAME_BY_FEATURE_FILE_NAME = "SELECT customer_name from x4a_input_order where feature_file_name = ?"

    X4A_GET_ORDER_VALUE_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT order_value FROM x4a_input_order where feature_file_name =?"

    X4A_GET_ORDER_STATUS_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT order_status FROM x4a_input_order where feature_file_name =?"

    X4A_INPUT_ORDER_GET_MIN_TOTAL_REVENUE_BY_FEATURE_FILE_NAME = "SELECT total_revenue_min from x4a_input_order where feature_file_name = ?"

    X4A_INPUT_ORDER_GET_MAX_TOTAL_REVENUE_BY_FEATURE_FILE_NAME = "SELECT total_revenue_max from x4a_input_order where feature_file_name = ?"

    X4A_GET_RESELLER_PO_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT reseller_po FROM x4a_input_order where feature_file_name =?"

    X4A_USER_DATA_INSERT_SQL_QUERY = "INSERT INTO x4a_user_data(" \
                                     "feature_file_name, Associate_Name, Associate_Email, Associate_Roles, " \
                                     "Associate_countries)" \
                                     "VALUES(?, ?, ?, ?, ?)"

    X4A_USER_DATA_BY_FEATURE_FILE_SQL_QUERY = "SELECT * from x4a_user_data"

    X4A_INPUT_GET_ORDER_TEST_CASE_RECORD_SQL_QUERY = "SELECT * FROM x4a_input_order where feature_file_name=?"

    X4A_GET_ORDER_TYPE_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT order_type FROM x4a_input_order where feature_file_name =?"

