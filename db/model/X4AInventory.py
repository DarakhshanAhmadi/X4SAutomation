class X4AInventory:
    def __init__(self, feature_file_name, under_performing_sku, under_performing_mfr_part_number, vendor_business_manager, vendor_name, country, actions, comment,
                 aging_sku, aging_mfr_part_number, customer, edit_customer):
        self.feature_file_name = feature_file_name
        self.under_performing_sku = under_performing_sku
        self.under_performing_mfr_part_number = under_performing_mfr_part_number
        self.vendor_business_manager = vendor_business_manager
        self.vendor_name = vendor_name
        self.country = country
        self.actions = actions
        self.comment = comment
        self.aging_sku = aging_sku
        self.aging_mfr_part_number = aging_mfr_part_number
        self.customer = customer
        self.edit_customer = edit_customer
