class X4AInputOrder:
    def __init__(self, feature_file_name, reseller_bcn, im_order_number, order_type, reseller_po, vendor_name, order_status, customer_po, total_revenue_min, total_revenue_max, customer_name,
                 order_value, reference_numbers, billing_to_info, ship_to_info, end_user_info, order_lines_tab, serial_numbers, additional_attributes,
                 fraud_cancel_order_confirmation_id, fraud_reprocess_order_confirmation_id, data_errors_resubmit_order_confirmation_id, reseller_name,
                 end_user_name, created_on, filter_order_type, filter_order_status, end_user_po, edit_order_lines):
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
        self.fraud_cancel_order_confirmation_id = fraud_cancel_order_confirmation_id
        self.fraud_reprocess_order_confirmation_id = fraud_reprocess_order_confirmation_id
        self.data_errors_resubmit_order_confirmation_id = data_errors_resubmit_order_confirmation_id
        self.reseller_name = reseller_name
        self.end_user_name = end_user_name
        self.created_on = created_on
        self.filter_order_type = filter_order_type
        self.filter_order_status = filter_order_status
        self.end_user_po = end_user_po
        self.edit_order_line = edit_order_lines

