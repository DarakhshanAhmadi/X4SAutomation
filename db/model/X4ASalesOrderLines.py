class X4ASalesOrderLine:
    def __init__(self, im_order_number, line_number, line_status, im_part_number, vpn, description, is_acop_applied, unit_weight,
                 unit_price, extended_price, extended_cost, quantity, quantity_confirmed, quantity_backordered, special_bid_number,
                 serial_numbers, sales_order_details_tbl_id):
        self.im_order_number = im_order_number
        self.line_number = line_number
        self.line_status = line_status
        self.im_part_number = im_part_number
        self.vpn = vpn
        self.description = description
        self.is_acop_applied = is_acop_applied
        self.unit_weight = unit_weight
        self.unit_price = unit_price
        self.extended_price = extended_price
        self.extended_cost = extended_cost
        self.quantity = quantity
        self.quantity_confirmed = quantity_confirmed
        self.quantity_backordered = quantity_backordered
        self.special_bid_number = special_bid_number
        self.serial_numbers = serial_numbers
        self.sales_order_details_tbl_id = sales_order_details_tbl_id




