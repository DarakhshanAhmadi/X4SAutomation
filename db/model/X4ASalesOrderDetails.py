class X4ASalesOrderDetails:
    def __init__(self, feature_file_name, order_entry_channel, im_order_number, order_type, reseller_po, end_user_po, order_status,
                 order_value, currency_code, terms_code, ship_from_warehouse_id, warehouse_name, carrier_code, ship_to_suffix, ship_to_name,
                 ship_to_address, ship_to_phone, ship_to_contact, ship_to_email, bill_to_suffix, bill_to_name,
                 bill_to_address, bill_to_phone, bill_to_contact, bill_to_email, end_user_id, end_user_address, end_user_contact):
        self.feature_file_name = feature_file_name
        self.order_entry_channel = order_entry_channel
        self.im_order_number = im_order_number
        self.order_type = order_type
        self.reseller_po = reseller_po
        self.end_user_po = end_user_po
        self.order_status = order_status
        self.order_value = order_value
        self.currency_code = currency_code
        self.terms_code = terms_code
        self.ship_from_warehouse_id = ship_from_warehouse_id
        self.warehouse_name = warehouse_name
        self.carrier_code = carrier_code
        self.ship_to_suffix = ship_to_suffix
        self.ship_to_name = ship_to_name
        self.ship_to_address = ship_to_address
        self.ship_to_phone = ship_to_phone
        self.ship_to_contact = ship_to_contact
        self.ship_to_email = ship_to_email
        self.bill_to_suffix = bill_to_suffix
        self.bill_to_name = bill_to_name
        self.bill_to_address = bill_to_address
        self.bill_to_phone = bill_to_phone
        self.bill_to_contact = bill_to_contact
        self.bill_to_email = bill_to_email
        self.end_user_id = end_user_id
        self.end_user_address = end_user_address
        self.end_user_contact = end_user_contact
