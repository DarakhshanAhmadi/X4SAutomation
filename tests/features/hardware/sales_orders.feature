@sales_orders @regression
Feature: Sales Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    And the user traverse to Sales Order menu

  # EDT-8452
  @all_column_on_sales_orders_page
  Scenario: All columns visible on Sales Orders Page
    Then verify that Sales Orders listing page visible
    And verify that all column should be present

  #EDT-8452
  @search_im_order_no
  Scenario: Search order by IM Order from Sales Order
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed

  # EDT-8470
  @created_on_ascending
  Scenario: validation of created on date ascending
    When search a order with specific BCN
    Then Validate All orders created on date should be ascending

  # EDT-8470
  @created_on_descending
  Scenario: validation of created on date descending
    When search a order with specific BCN
    Then Validate All orders created on date should be descending

  # EDT-8329
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

  # EDT-8489
  @order_lines_tab_fields_data
  Scenario: Order lines tab fields data validation
    When Click on Order lines tab on Order Details page
    Then Validate fields under Order lines tab

  # EDT-8489
  @serial_number_header_fields_data
  Scenario: Serial number header data validation
    When Click on Order lines tab on Order Details page
    And Click on Serial numbers view more option
    Then Validate fields under Serial Numbers header

  # EDT-8489
  @additional_attributes_header_fields_data
  Scenario: Additional Attributes header data validation
    When Click on Order lines tab on Order Details page
    And Click on Additional attributes view more option
    Then Validate fields under Additional attributes header

  # EDT-8472
  @filter_im_order
  Scenario: Verify filter with IM order
     When Filter by IM order
     Then Verify the data for filtered IM order is listed

  # EDT-8472
  @filter_order_type
  Scenario: Verify filter by Order type
    When Filter by Order type
    Then Validate the order Type is listed

  # EDT-8472
  @filter_reseller_po
  Scenario: Verify filter by Reseller PO
    When Filter by Reseller PO
    Then Validate the Reseller PO is listed

  # EDT-8472
  @filter_bcn
  Scenario: Verify filter by BCN
    When Filter by BCN
    Then Validate the BCN is listed

  # EDT-8472
  @filter_reseller_name
  Scenario: Verify filter by Reseller Name
    When Filter by Reseller Name
    Then Validate the Reseller Name is listed

  # EDT-8472
  @filter_vendor_name
  Scenario: Verify filter by Vendor Name
    When Filter by Vendor Name
    Then Validate the Vendor Name is listed

  # EDT-8472
  @filter_end_user_name
  Scenario: Verify filter by End User Name
    When Filter by End User Name
    Then Validate the End User Name is listed

  # EDT-8472
  @filter_order_status
  Scenario: Verify filter by Order Status
    When Filter by Order Status
    Then Validate the Order Status is listed

  # EDT-8472
  @filter_order_value
  Scenario: Verify filter by Order Value
    When Filter by Order Value
    Then Validate the Order Value is listed

  # EDT-8472
  @filter_created_on
  Scenario: Verify filter by Created On
    When Filter by Created On
    Then Validate the Created On is listed

  # EDT-  10681
  @update_end_user_po_and_reseller_po
  Scenario: Validate Update and cancel for end user po and reseller po
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed
    When Click on searched IM order number
    And Check if the order is editable
    Then Validate Cancel update of end user po and reseller po
    And Validate Update end user po and reseller po

  #EDT - 10799
  @validate_acop_field
  Scenario: Validate ACOP field
#    When search a order with specific IM Order number
#    Then Validate the IM Order number is listed
#    When Click on searched IM order number
    When Click on Order lines tab on Order Details page
    Then Validate ACOP field is present and has valid value

  # EDT - 10685
  @update_order_line
  Scenario: Validate Update and Cancel for edit order line
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed
    When Click on searched IM order number
    And Click on Order lines tab on Order Details page
    Then Cancel order line changes and validate it
    Then Update order line and validate it

  # @logout
  Scenario: logout X4A
    Given logout the X4A url

#  # EDT-8470
#  @search_bcn
#  Scenario: Search order by BCN from Sales Order
#    When search a order with specific BCN
#    Then Validate the searched BCN is listed
#
#  #EDT-8452
#  @search_order_type
#  Scenario: Search order by Type from Sales Order
#    When search a order with specific order Type
#    Then Validate the order Type is listed
#
#  #EDT-8452
#  @search_reseller_po
#  Scenario: Search order by Reseller PO from Sales Order
#    When search a order with specific Reseller PO
#    Then Validate the Reseller PO is listed
#
#  #EDT-8452
#  @search_vendor_name
#  Scenario: Search order by Vendor name from Sales Order
#    When search a order with specific Vendor name
#    Then Validate the Vendor name is listed
#
#  #EDT-8452
#  @search_order_status
#  Scenario: Search order by Order status from Sales Order
#    When search a order with specific Order status
#    Then Validate the Order status is listed
#
