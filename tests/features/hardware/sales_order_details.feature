@sales_order_details @regression @demo_regression
Feature: Sales Order Details

  @fetch_order_details
  Scenario: sales order details check
    Given fetch sales order details via api

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    And the user traverse to Sales Order menu


  @all_tabs-on_order_details_page
  Scenario: All tabs visible on Order Details page
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed
    When Click on searched IM order number
    Then Verify that all tabs should be present


  # EDT-8329
  @same_header_display_for_all_tab
  Scenario: Same header display for all tab
    When Click on Order Details tab on Order Details page
    Then Validate header data contains Order value and Order type
    When Click on Billing tab on Order Details page
    Then Validate header data contains Order value and Order type
    When Click on Order lines tab on Order Details page
    Then Validate header data contains Order value and Order type
    When Click on Additional attributes tab on Order Details page
    Then Validate header data contains Order value and Order type

  # EDT-8332
  @ingram_order_num_and_order_status_title
  Scenario: Ingram order number and Order Status title on Order details page
    Then Verify that title on the header of the order details page contains Ingram order number and Order Status

  # EDT-8332
  @header_data_on_order_details_page
  Scenario: Header data on Order details page
    Then Validate header data contains Order value
    And Validate header data contains Order type

  # EDT-8489
  @reference_number_fields_data
  Scenario: Reference Number fields data validation
    When Click on Order Details tab on Order Details page
    Then Validate fields under reference number section

  # EDT-8489
  @bill_to_info_fields_data
  Scenario: Bill to info fields data validation
    When Click on Billing tab on Order Details page
    Then Validate fields under Bill to info section

  # EDT-8489
  @ship_to_info_fields_data
  Scenario: Ship to info fields data validation
    When Click on Billing tab on Order Details page
    Then Validate fields under Ship to info section

  # EDT-8489
  @end_user_info_fields_data
  Scenario: End user info fields data validation
    When Click on Billing tab on Order Details page
    Then Validate fields under End user info section

  #  # EDT-8489
#  @order_lines_tab_fields_data
#  Scenario: Order lines tab fields data validation
#    When Click on Order lines tab on Order Details page
#    Then Validate fields under Order lines tab
#
#  # EDT-8489
#  @serial_number_header_fields_data
#  Scenario: Serial number header data validation
#    When Click on Order lines tab on Order Details page
#    And Click on Serial numbers view more option
#    Then Validate fields under Serial Numbers header
#
#  # EDT-8489
#  @additional_attributes_header_fields_data
#  Scenario: Additional Attributes header data validation
#    When Click on Order lines tab on Order Details page
#    And Click on Additional attributes view more option
#    Then Validate fields under Additional attributes header
