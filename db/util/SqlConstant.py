class SqlConstant:
    X4A_INPUT_ORDER_INSERT_SQL_QUERY = "INSERT INTO x4a_input_order(" \
                                       "feature_file_name, reseller_bcn, im_order_number, order_type, " \
                                       "reseller_po, vendor_name, order_status, customer_po, total_revenue_min, total_revenue_max, customer_name," \
                                       "order_value, reference_numbers, billing_to_info, ship_to_info, end_user_info, order_lines_tab, " \
                                       "serial_numbers, additional_attributes, fraud_cancel_order_confirmation_id, fraud_reprocess_order_confirmation_id," \
                                       " data_errors_resubmit_order_confirmation_id, reseller_name, end_user_name, created_on, filter_order_type, filter_order_status," \
                                       "modify_reference_details_data_errors_order_id, modify_shipping_notes_data_errors_order_id, modify_vmf_details_data_errors_order_id, " \
                                       "modify_end_user_details_data_errors_order_id, end_user_po, edit_order_lines, modify_billing_address_data_errors_order_id, " \
                                       "order_line_data_errors_order_id, modify_order_line_data_errors_order_id, im360_data_errors_order_confirmation_id)" \
                                       "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

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

    X4A_BULK_ORDER_SCENARIO_SQL_QUERY = "INSERT INTO x4a_bulk_order_data(feature_file_name, Scenario, Operator_ID, " \
                                        "Country_Code, Customer_Branch_and_Number, " \
                                        "Reseller_PO, Carrier_Code, Order_Type, Header_Comment_1, " \
                                        "Header_Comment_2, Ingram_SKU, Qty)" \
                                        "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    X4A_BULK_ORDER_DATA_BY_FEATURE_FILE_SQL_QUERY = "SELECT * from x4a_bulk_order_data where Scenario=?"

    X4A_EMAIL_TO_ORDER_SCENARIO_SQL_QUERY = "INSERT INTO x4a_email_to_order_data(feature_file_name, Account, Country, " \
                                            "Country_Code, Customer_Name, Customer_PO, " \
                                            "Sales_Order, Processed, Additional_Information)" \
                                            "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"

    X4A_EMAIL_TO_ORDER_DATA_BY_FEATURE_FILE_SQL_QUERY = "SELECT * from x4a_email_to_order_data where Scenario=?"

    X4A_INPUT_GET_ORDER_TEST_CASE_RECORD_SQL_QUERY = "SELECT * FROM x4a_input_order where feature_file_name=?"

    X4A_GET_ORDER_TYPE_BY_FEATURE_FILE_NAME_SQL_QUERY = "SELECT order_type FROM x4a_input_order where feature_file_name =?"

    X4A_UPDATE_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set data_errors_resubmit_order_confirmation_id = ? where feature_file_name= ?"
    X4A_UPDATE_MODIFY_REFERENCE_DETAILS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set modify_reference_details_data_errors_order_id = ? where feature_file_name= ?"

    X4A_UPDATE_MODIFY_SHIPPING_NOTES_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set modify_shipping_notes_data_errors_order_id = ? where feature_file_name= ?"

    X4A_UPDATE_MODIFY_VMF_DETAILS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set modify_vmf_details_data_errors_order_id = ? where feature_file_name= ?"

    X4A_UPDATE_MODIFY_END_USER_DETAILS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set modify_end_user_details_data_errors_order_id = ? where feature_file_name= ?"

    X4A_SALES_ORDER_DETAILS_INSERT_SQL_QUERY = "INSERT INTO x4a_sales_order_details(" \
                                       "feature_file_name, order_entry_channel, im_order_number, order_type, reseller_po, end_user_po, order_status, order_value, currency_code, terms_code," \
                                       "ship_from_warehouse_id, warehouse_name, carrier_code, ship_to_suffix, ship_to_name, ship_to_address, ship_to_phone, ship_to_contact, ship_to_email, " \
                                       "bill_to_suffix, bill_to_name, bill_to_address, bill_to_phone, bill_to_contact, bill_to_email, end_user_id, end_user_address, end_user_contact)" \
                                       "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?)"

    X4A_SALES_ORDER_LINES_INSERT_SQL_QUERY = "INSERT INTO x4a_sales_order_lines(" \
                                             "im_order_number, line_number, line_status, im_part_number, vpn, description, is_acop_applied, unit_weight, unit_price, extended_price, cost," \
                                             "quantity, quantity_confirmed, quantity_backordered, special_bid_number, serial_numbers, sales_order_details_tbl_id)" \
                                            "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    X4A_SALES_ORDER_DETAILS_GET_ID_SQL_QUERY = "SELECT id from x4a_sales_order_details where im_order_number = ?"

    X4A_SALES_ORDER_DETAILS_GET_ORDER_DETAILS_SQL_QUERY = "SELECT * FROM x4a_sales_order_details where im_order_number=?"

    X4A_SALES_ORDER_LINES_DETAILS_FETCH_SQL_QUERY = "SELECT * from x4a_sales_order_lines where sales_order_details_tbl_id in (select id from x4a_sales_order_details where im_order_number=?)"

    X4A_UPDATE_MODIFY_BILLING_ADDRESS_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set modify_billing_address_data_errors_order_id = ? where feature_file_name= ?"

    X4A_UPDATE_REMOVE_ORDER_LINE_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set order_line_data_errors_order_id = ? where feature_file_name= ?"

    X4A_INVENTORY_INSERT_SQL_QUERY = "INSERT INTO x4a_inventory(" \
                                               "feature_file_name, under_performing_sku, under_performing_mfr_part_number, vendor_business_manager, vendor_name, country, actions, comment, aging_sku, aging_mfr_part_number)" \
                                               "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    X4A_INVENTORY_GET_TEST_CASE_RECORD_SQL_QUERY = "SELECT * FROM x4a_inventory where feature_file_name=?"

    X4A_UPDATE_ORDER_LINE_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set modify_order_line_data_errors_order_id = ? where feature_file_name= ?"

    X4A_UPDATE_IM360_CONFIRMATION_ID_BY_FEATURE_FILE_NAME_SQL_QUERY = "Update x4a_input_order set im360_data_errors_order_confirmation_id = ? where feature_file_name= ?"