class SqlConstant:
    X4A_INPUT_ORDER_INSERT_SQL_QUERY = "INSERT INTO x4a_input_order(" \
                                         "feature_file_name, reseller_bcn, im_order_number, order_type, reseller_po, vendor_name, order_status)" \
                                         "VALUES(?, ?, ?, ?, ?, ?, ?)"

    X4A_GET_BCN_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT reseller_bcn FROM x4a_input_order where feature_file_name =?"

    X4A_GET_IM_ORDER_NUMBER_BY_FEATURE_FILE_NAME_SQL_QUERY  = "SELECT im_order_number FROM x4a_input_order where feature_file_name =?"

    X4A_GET_ORDER_TYPE_BY_FEATURE_FILE_NAME_SQL_QUERY  = "SELECT order_type FROM x4a_input_order where feature_file_name =?"

    X4A_GET_VENDOR_NAME_BY_FEATURE_FILE_NAME_SQL_QUERY  = "SELECT vendor_name FROM x4a_input_order where feature_file_name =?"

    X4A_GET_RESELLER_PO_BY_FEATURE_FILE_NAME_SQL_QUERY  = "SELECT reseller_po FROM x4a_input_order where feature_file_name =?"

    X4A_GET_ORDER_STATUS_BY_FEATURE_FILE_NAME_SQL_QUERY  = "SELECT order_status FROM x4a_input_order where feature_file_name =?"

