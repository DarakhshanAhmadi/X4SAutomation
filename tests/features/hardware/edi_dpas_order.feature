@edi_dpas_order @regression
Feature: EDI Data Validation - DPAS Order

  Background:
    Given Set the API endpoint and headers

  # OMS-2499
  @validate_dpascode_and_dpaspgrmid
  Scenario: DpasCode and DpasprogramID validation
    Then Validate the dpascode and dpasprogramid if not available in input file
    Then Validate the dpascode and dpasprogramid if available in input file
