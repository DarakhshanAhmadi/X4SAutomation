class X4AInputOrder:
    def __init__(self, feature_file_name, reseller_bcn, im_order_number, order_type, reseller_po, vendor_name, order_status, customer_po, total_revenue_min, total_revenue_max, customer_name,
                 order_value, reference_numbers, billing_to_info, ship_to_info, end_user_info, order_lines_tab, serial_numbers, additional_attributes, reseller_name):
        self.feature_file_name = feature_file_name
        self.reseller_bcn = reseller_bcn
        self.im_order_number = im_order_number
        self.order_type = order_type
        self.reseller_po = reseller_po
        self.vendor_name = vendor_name
        self.order_status = order_status
        self.customer_po = customer_po
        self.total_revenue_min = total_revenue_min
        self.total_revenue_max = total_revenue_max
        self.customer_name = customer_name
        self.order_value = order_value
        self.reference_numbers = reference_numbers
        self.billing_to_info = billing_to_info
        self.ship_to_info = ship_to_info
        self.end_user_info = end_user_info
        self.order_lines_tab = order_lines_tab
        self.serial_numbers = serial_numbers
        self.additional_attributes = additional_attributes
        self.reseller_name = reseller_name

