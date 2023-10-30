@edi_bill_to_suffix_validation_validation @regression
Feature: EDI Data Validation - Bill To And Suffix To Validation

  Background:
    Given Set the API endpoint and headers

  # OMS-82
  @bill_to_ship_to_suffix_validation
  Scenario: Bill To Ship To Address and Suffix Validation
    Then Validate the billToAddress if available in input file
    Then Validate the shipToAddress if available in input file

  # OMS-84
  @bill_to_information
  Scenario: Bill to information
    Then Validate the billToRefPlu if not empty in input file
    Then Validate the customer number if billToRefNumber is not empty

  # OMS-1330
  @bill_to_information
  Scenario: Bill to information - Validate billToFaxNbr, billToLotusId and billToEmail
    Then Validate the billToFaxNbr if empty in input file
    Then Validate the billToFaxNbr if not empty in input file
    Then Validate the billToLotusId if empty in input file
    Then Validate the billToLotusId if not empty in input file
    Then Validate the billToEmail if empty in input file
    Then Validate the billToEmail if not empty in input file