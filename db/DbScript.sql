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
customer_name String
);

CREATE TABLE IF NOT EXISTS x4a_user_data(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
feature_file_name String NOT NULL,
Associate_Name String,
Associate_Email String,
Associate_Roles String,
Associate_countries String
);