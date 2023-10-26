from pytest_bdd import scenario, given, parsers, then

from RestApi.Operations.edi_data_validation import EDIDataValidation


@scenario("features/hardware/edi_api_header_level_data_validation.feature", "Header Level Validation - Prefix")
def test_edi_header_level_validation_prefix():
    pass


@scenario("features/hardware/edi_api_header_level_data_validation.feature",
          "Header Level Validation - Process Reference Numbers")
def test_edi_header_level_validation_process_reference_no():
    pass


@scenario("features/hardware/edi_api_header_level_data_validation.feature",
          "Header Level Validation - Process header level pass-thru fields")
def test_edi_header_level_validation_process_pass_thru_fields():
    pass


@scenario("features/hardware/edi_api_header_level_data_validation.feature", "Header Level Validation - Back Order Flag")
def test_edi_header_level_validation_back_order_flag():
    pass


@scenario("features/hardware/edi_api_header_level_data_validation.feature",
          "Header Level Validation - Process Buyer Information")
def test_edi_header_level_validation_process_buyer_information():
    pass


@scenario("features/hardware/edi_api_header_level_data_validation.feature",
          "Header Level Validation - Freight Out Code, Third Party Freight account and Carrier Code")
def test_edi_header_level_validation_frieght_code():
    pass


@scenario("features/hardware/edi_api_header_level_data_validation.feature",
          "Header Level Validation - Special Shipping Information-H16")
def test_edi_header_level_validation_special_shipping_info_h16():
    pass


@scenario("features/hardware/edi_line_level_data_validation.feature",
          "Line Level Validation Backorder Flag3")
def test_edi_line_level_validation_back_order_flag():
    pass


@scenario("features/hardware/edi_bill_to_ship_to_suffix_validation.feature",
          "Bill To Ship To Address and Suffix Validation")
def test_edi_bill_to_ship_to_add_and_suffix_validation():
    pass


@scenario("features/hardware/edi_bill_to_ship_to_suffix_validation.feature",
          "Bill to information")
def test_edi_bill_to_information():
    pass


@scenario("features/hardware/edi_bill_to_ship_to_suffix_validation.feature",
          "Bill to information - Validate billToFaxNbr, billToLotusId and billToEmail")
def test_edi_bill_to_faxnbr_lotus_id_email_information():
    pass


@given(parsers.parse('Set the API endpoint and headers'))
def set_api_endpoint_headers():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.set_api_endpoint_headers()


@then(parsers.parse('Validate the currency code if not available in input file'))
def validate_currency_code_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.currency_code_not_available_validate()


@then(parsers.parse('Validate the currency code if available in input file'))
def validate_currency_code_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.currency_code_available_validate()


@then(parsers.parse('Validate the terms9 if not available in input file'))
def validate_terms9_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.terms9_not_available_validate()


@then(parsers.parse('Validate the terms9 if available in input file'))
def validate_terms9_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.terms9_available_validate()


@then(parsers.parse('Validate the poDate if not available in input file'))
def validate_po_date_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.po_date_not_available_validate()


@then(parsers.parse('Validate the poDate if available in input file'))
def validate_po_date_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.po_date_available_validate()


@then(parsers.parse('Validate the etaDate if not available in input file'))
def validate_eta_date_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.eta_date_not_available_validate()


@then(parsers.parse('Validate the etaDate if available in input file'))
def validate_eta_date_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.eta_date_available_validate()


@then(parsers.parse('Validate the cancelDate if not available in input file'))
def validate_cancel_date_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.cancel_date_not_available_validate()


@then(parsers.parse('Validate the cancelDate if available in input file'))
def validate_cancel_date_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.cancel_date_available_validate()


@then(parsers.parse('Validate the requiredShipDate if not available in input file'))
def validate_required_ship_date_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.required_ship_date_not_available_validate()


@then(parsers.parse('Validate the requiredShipDate if available in input file'))
def validate_required_ship_date_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.required_ship_date_available_validate()


@then(parsers.parse('Validate the departmentNumber if not available in input file'))
def validate_department_no_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.department_no_not_available_validate()


@then(parsers.parse('Validate the departmentNumber if available in input file'))
def validate_department_no_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.department_no_available_validate()


@then(parsers.parse('Validate the sellerSalesNumber if not available in input file'))
def validate_seller_sales_no_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.seller_sales_no_not_available_validate()


@then(parsers.parse('Validate the sellerSalesNumber if available in input file'))
def validate_seller_sales_no_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.seller_sales_no_available_validate()


@then(parsers.parse('Validate the endUserPoNumber if not available in input file'))
def validate_end_user_po_no_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.enduser_po_no_not_available_validate()


@then(parsers.parse('Validate the endUserPoNumber if available in input file'))
def validate_end_user_po_no_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.enduser_po_no_available_validate()


@then(parsers.parse('Validate the customerOrderNumber if not available in input file'))
def validate_customer_order_no_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.customer_order_no_not_available_validate()


@then(parsers.parse('Validate the customerOrderNumber if available in input file'))
def validate_customer_order_no_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.customer_order_no_available_validate()


@then(parsers.parse('Validate the customerVendorNumber if not available in input file'))
def validate_customer_vendor_no_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.customer_vendor_no_not_available_validate()


@then(parsers.parse('Validate the customerVendorNumber if available in input file'))
def validate_customer_vendor_no_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.customer_vendor_no_available_validate()


@then(parsers.parse('Validate the contractNumber for order type RL or KD'))
def validate_contract_no_for_order_type_rl_kd():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.contract_no_for_order_type_rl_kd_validate()


@then(parsers.parse('Validate the premiumService if not available in input file'))
def validate_premium_service_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.premium_service_not_available_validate()


@then(parsers.parse('Validate the premiumService if available in input file'))
def validate_premium_service_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.premium_service_available_validate()


@then(parsers.parse('Validate the fixedDeliveryDate if not available in input file'))
def validate_fixed_delivery_date_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.fixed_delivery_date_not_available_validate()


@then(parsers.parse('Validate the fixedDeliveryDate if available in input file'))
def validate_fixed_deliver_date_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.fixed_delivery_date_available_validate()


@then(parsers.parse('Validate the warehouseActionCode if not available in input file'))
def validate_warehouse_action_code_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.warehouse_action_code_not_available_validate()


@then(parsers.parse('Validate the warehouseActionCode if available in input file'))
def validate_warehouse_action_code_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.warehouse_action_code_available_validate()


@then(parsers.parse('Validate the backOrderFlag if not available in input file'))
def validate_back_order_flag_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.back_order_flag_not_available_validate()


@then(parsers.parse('Validate the backOrderFlag if available in input file'))
def validate_back_order_flag_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.back_order_flag_available_validate()


@then(parsers.parse('Validate the buyer information if not available in input file'))
def validate_buyer_information_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.buyer_information_not_available_validate()


@then(parsers.parse('Validate the buyer information if available in input file'))
def validate_buyer_information_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.buyer_information_available_validate()


@then(parsers.parse('Validate the frieghtcode if not available in input file'))
def validate_frieght_code_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.frieght_code_not_available_validate()


@then(parsers.parse('Validate the frieghtcode if available in input file'))
def validate_frieght_code_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.frieght_code_available_validate()


@then(parsers.parse('Validate the thirdpartyfrieghtaccount if not available in input file'))
def validate_third_party_frieght_account_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.third_party_frieght_account_not_available_validate()


@then(parsers.parse('Validate the thirdpartyfrieghtaccount if available in input file'))
def validate_third_party_frieght_account_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.third_party_frieght_account_available_validate()


@then(parsers.parse('Validate the IM carrier field and IMI ship via field for order type SO'))
def validate_im_carrier_field_and_imi_ship_via_field_for_order_type_so():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.im_carrier_field_and_imi_ship_via_field_validate()


@then(parsers.parse('Validate the carrier code if not available in input file'))
def validate_carrier_code_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.carrier_code_not_available_validate()


@then(parsers.parse('Validate the carrier code if available in input file'))
def validate_carrier_code_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.carrier_code_available_validate()


@then(parsers.parse('Validate the header16FormCode if not available in input file'))
def validate_header16_form_code_if_not_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.header16_form_code_not_available_validate()


@then(parsers.parse('Validate the header16FormCode if available in input file'))
def validate_header16_form_code_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.header16_form_code_available_validate()


@then(parsers.parse('Validate order is rejected for order type TC and ctoValidOrderCode'))
def validate_order_is_rejected_cto_valid_order_code():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.rejected_cto_valid_order_code_validate()


@then(parsers.parse('Validate the billToAddress if available in input file'))
def validate_bill_to_address_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_address_available_validate()


@then(parsers.parse('Validate the shipToAddress if available in input file'))
def validate_ship_to_address_if_available():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.ship_to_address_available_validate()


@then(parsers.parse('Validate the billToRefPlu if not empty in input file'))
def validate_bill_to_refplu_if_not_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_refplu_not_empty_validate()


@then(parsers.parse('Validate the customer number if billToRefNumber is not empty'))
def validate_the_customer_number_if_billtorefnumber_is_not_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.customer_no_validate()


@then(parsers.parse('Validate the billToFaxNbr if empty in input file'))
def validate_bill_to_refplu_if_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_faxnbr_empty_validate()


@then(parsers.parse('Validate the billToFaxNbr if not empty in input file'))
def validate_bill_to_refplu_if_not_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_faxnbr_not_empty_validate()


@then(parsers.parse('Validate the billToLotusId if empty in input file'))
def validate_bill_to_lotus_id_if_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_lotus_id_empty_validate()


@then(parsers.parse('Validate the billToLotusId if not empty in input file'))
def validate_bill_to_lotus_id_if_not_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_lotus_id_not_empty_validate()


@then(parsers.parse('Validate the billToEmail if empty in input file'))
def validate_bill_to_email_if_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_email_empty_validate()


@then(parsers.parse('Validate the billToEmail if not empty in input file'))
def validate_bill_to_email_if_not_empty():
    edi_data_obj = EDIDataValidation()
    edi_data_obj.bill_to_email_not_empty_validate()
