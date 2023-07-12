@sales_orders @regression
Feature: Sales Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login

  # EDT-8452
  @all_column_on_sales_orders_page
  Scenario: All columns visible on Sales Orders Page
    When the user traverse to Sales Order menu
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

  @logout
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
