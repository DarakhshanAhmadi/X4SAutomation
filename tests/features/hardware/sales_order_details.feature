@sales_order_details @regression @demo_regression
Feature: Sales Order Details

  @login @l1
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    And the user traverse to Sales Order menu

  #EDT - 10799, EDT-8489, EDT-8332, EDT-8329
  @fetch_order_details
  Scenario Outline: sales order details check
    Given fetch sales order details via api for <order_id> of type <order_type> created on <order_date> via <entry_channel>
    Then go to Sales Order menu
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed
    When Click on searched IM order number
    Then Verify that all tabs should be present
    When Click on Order Details tab on Order Details page
    Then Validate header data contains Order value and Order type
    When Click on Billing tab on Order Details page
    Then Validate header data contains Order value and Order type
    When Click on Order lines tab on Order Details page
    Then Validate header data contains Order value and Order type
    When Click on Additional attributes tab on Order Details page
    Then Validate header data contains Order value and Order type
    Then Verify that title on the header of the order details page contains Ingram order number and Order Status
    Then Validate header data contains Order value
    And Validate header data contains Order type
    When Click on Order Details tab on Order Details page
    Then Validate fields under reference number section
    Then Validate carrier code
    When Click on Billing tab on Order Details page
    Then Validate fields under Ship from info section
    Then Validate fields under Bill to info section
    Then Validate fields under Ship to info section
    Then Validate fields under End user info section
    When Click on Order lines tab on Order Details page
    Then Validate fields under Order lines tab
    Then Validate ACOP field is present and has valid value
    When Click on Additional attributes tab on Order Details page
    Then Validate payment terms code
    Examples:
    |order_id   |order_date|entry_channel|order_type|
    |20-VNH2Q-11|2023-09-21|X4C          |Stock     |
    |20-VNH4H-11|2023-09-21|X4C          |Direct    |
    |20-VN9TB-11|2023-09-04|IM360        |Stock     |
    |20-VNDGX-11|2023-09-08|IM360        |Direct    |
    |20-VNDH1-11|2023-09-08|API Simpli   |Stock     |


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
