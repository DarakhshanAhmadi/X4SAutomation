--------------------------------------------------------------- Version 1.0 [01st July 2023] ---------------------------------------------------------------

--------------------------------------------------------------- DDL -----------------------------------------------------------------------

--------------------------------------------------------------- X4A ---------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS x4a_input_order(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
feature_file_name String NOT NULL,
reseller_bcn String,
im_order_number String,
order_type String,
reseller_po String,
vendor_name String,
order_status String,
customer_po String,
total_revenue_min String,
total_revenue_max String,
customer_name String,
order_value String,
reference_numbers String,
billing_to_info String,
ship_to_info String,
end_user_info String,
order_lines_tab String,
serial_numbers  String,
additional_attributes String,
fraud_cancel_order_confirmation_id String,
fraud_reprocess_order_confirmation_id String,
data_errors_resubmit_order_confirmation_id String,
reseller_name String,
end_user_name String,
created_on String,
filter_order_type String,
filter_order_status String,
modify_reference_details_data_errors_order_id String,
modify_shipping_notes_data_errors_order_id String,
modify_vmf_details_data_errors_order_id String,
modify_end_user_details_data_errors_order_id String,
end_user_po String,
edit_order_lines String,
modify_billing_address_data_errors_order_id String,
order_line_data_errors_order_id Sting,
modify_order_line_data_errors_order_id String,
im360_data_errors_order_confirmation_id String
);

CREATE TABLE IF NOT EXISTS x4a_user_data(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
feature_file_name String NOT NULL,
Associate_Name String,
Associate_Email String,
Associate_Roles String,
Associate_countries String
);

CREATE TABLE IF NOT EXISTS x4a_bulk_order_data(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
feature_file_name String NOT NULL,
Scenario  String,
Operator_ID  String,
Country_Code String,
Customer_Branch_and_Number String,
Reseller_PO  String,
Carrier_Code  String,
Order_Type    String,
Header_Comment_1 String,
Header_Comment_2 String,
Ingram_SKU String,
Qty String
);


CREATE TABLE IF NOT EXISTS x4a_sales_order_details(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
feature_file_name String NOT NULL,
order_entry_channel String,
im_order_number String,
order_type String,
reseller_po String,
end_user_po String,
order_status String,
order_value TEXT,
currency_code String,
terms_code String,
ship_from_warehouse_id String,
warehouse_name String,
carrier_code String,
ship_to_suffix TEXT,
ship_to_name String,
ship_to_address String,
ship_to_phone String,
ship_to_contact String,
ship_to_email String,
bill_to_suffix TEXT,
bill_to_name String,
bill_to_address String,
bill_to_phone String,
bill_to_contact String,
bill_to_email String,
end_user_id String,
end_user_address String,
end_user_contact String
);


CREATE TABLE IF NOT EXISTS x4a_sales_order_lines(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
im_order_number String,
line_number TEXT,
line_status String,
im_part_number String,
vpn String,
description String,
is_acop_applied String,
unit_weight String,
unit_price String,
extended_price String,
cost String,
quantity String,
quantity_confirmed String,
quantity_backordered String,
special_bid_number String,
serial_numbers String,
sales_order_details_tbl_id String,
FOREIGN KEY(sales_order_details_tbl_id) REFERENCES x4a_sales_order_details(id)
);


CREATE TABLE IF NOT EXISTS x4a_inventory(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
feature_file_name String NOT NULL,
sku TEXT,
mfn_part_number String,
vendor_business_manager String,
vendor_name String,
country String,
actions String,
comment String
);