@edi_header_level_data_validation @regression
Feature: EDI Header Level Data Validation

  Background:
    Given Set the API endpoint and headers

  # OMS-537
  @prefix_data_validation
  Scenario: Header Level Validation - Prefix
    Then Validate the currency code if not available in input file
    Then Validate the currency code if available in input file
    Then Validate the terms9 if not available in input file
    Then Validate the terms9 if available in input file
    Then Validate the poDate if not available in input file
    Then Validate the poDate if available in input file
    Then Validate the etaDate if not available in input file
    Then Validate the etaDate if available in input file
    Then Validate the cancelDate if not available in input file
    Then Validate the cancelDate if available in input file
    Then Validate the requiredShipDate if not available in input file
    Then Validate the requiredShipDate if available in input file

  # OMS-581
  @frieghtcode_data_validation
  Scenario: Header Level Validation - Freight Out Code, Third Party Freight account and Carrier Code
    Then Validate the frieghtcode if not available in input file
    Then Validate the frieghtcode if available in input file
    Then Validate the thirdpartyfrieghtaccount if not available in input file
    Then Validate the thirdpartyfrieghtaccount if available in input file
    Then Validate the IM carrier field and IMI ship via field for order type SO
    Then Validate the carrier code if not available in input file
    Then Validate the carrier code if available in input file

  # OMS-591
  @process_reference_no_data_validation
  Scenario: Header Level Validation - Process Reference Numbers
    Then Validate the departmentNumber if not available in input file
    Then Validate the departmentNumber if available in input file
    Then Validate the sellerSalesNumber if not available in input file
    Then Validate the sellerSalesNumber if available in input file
    Then Validate the endUserPoNumber if not available in input file
    Then Validate the endUserPoNumber if available in input file
    Then Validate the customerOrderNumber if not available in input file
    Then Validate the customerOrderNumber if available in input file
    Then Validate the customerVendorNumber if not available in input file
    Then Validate the customerVendorNumber if available in input file
    Then Validate the contractNumber for order type RL or KD

  # OMS-571
  @process_pass_thru_data_validation
  Scenario: Header Level Validation - Process header level pass-thru fields
    Then Validate the premiumService if not available in input file
    Then Validate the premiumService if available in input file
    Then Validate the fixedDeliveryDate if not available in input file
    Then Validate the fixedDeliveryDate if available in input file
    Then Validate the warehouseActionCode if not available in input file
    Then Validate the warehouseActionCode if available in input file

  # OMS-582
  @back_order_flag_data_validation
  Scenario: Header Level Validation - Back Order Flag
    Then Validate the backOrderFlag if not available in input file
    Then Validate the backOrderFlag if available in input file

  # OMS-481
  @process_buyer_information_data_validation
  Scenario: Header Level Validation - Process Buyer Information
    Then Validate the buyer information if not available in input file
    Then Validate the buyer information if available in input file

  # OMS-1860
  @special_shipping_info_data_validation
  Scenario: Header Level Validation - Special Shipping Information-H16
    Then Validate the header16FormCode if not available in input file
    Then Validate the header16FormCode if available in input file
