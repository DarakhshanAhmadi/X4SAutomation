@edi_line_level_data_validation @regression
Feature: EDI Line Level Validation

  Background:
    Given Set the API endpoint and headers

  # OMS-1858
  @line_level_validation_backorder_flag
  Scenario: Line Level Validation Backorder Flag3
    Then Validate order is rejected for order type TC and ctoValidOrderCode