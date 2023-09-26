@sales_orders @regression @demo_regression
Feature: Sales Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    And the user traverse to Sales Order menu

  # EDT-8452/OMS-877
  @all_column_on_sales_orders_page
  Scenario: All columns visible on Sales Orders Page
    Then verify that Sales Orders listing page visible
    And verify that all column should be present

  #EDT-8452/OMS-877
  @search_im_order_no
  Scenario: Search order by IM Order from Sales Order
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed

  # EDT-8470/OMS-878
  @created_on_ascending
  Scenario: validation of created on date ascending
    When search a order with specific BCN
    Then Validate All orders created on date should be ascending

  # EDT-8470/OMS-878
  @created_on_descending
  Scenario: validation of created on date descending
    When search a order with specific BCN
    Then Validate All orders created on date should be descending


  # EDT-8472/OMS-880
  @filter_im_order
  Scenario: Verify filter with IM order
    When Filter by IM order
    Then Verify the data for filtered IM order is listed

  # EDT-8472/OMS-880
  @filter_order_type
  Scenario: Verify filter by Order type
    When Filter by Order type
    Then Validate the order Type is listed

  # EDT-8472/OMS-880
  @filter_reseller_po
  Scenario: Verify filter by Reseller PO
    When Filter by Reseller PO
    Then Validate the Reseller PO is listed

  # EDT-8472/OMS-880
  @filter_bcn
  Scenario: Verify filter by BCN
    When Filter by BCN
    Then Validate the BCN is listed

  # EDT-8472/OMS-880
  @filter_reseller_name
  Scenario: Verify filter by Reseller Name
    When Filter by Reseller Name
    Then Validate the Reseller Name is listed


   # EDT-8472
  @filter_vendor_name
  Scenario: Verify filter by Vendor Name
    When Filter by Vendor Name
    Then Validate the Vendor Name is listed

  # EDT-8472/OMS-880
  @filter_end_user_name
  Scenario: Verify filter by End User Name
    When Filter by End User Name
    Then Validate the End User Name is listed

  # EDT-8472/OMS-880
  @filter_order_status
  Scenario: Verify filter by Order Status
    When Filter by Order Status
    Then Validate the Order Status is listed

  # EDT-8472/OMS-880
  @filter_order_value
  Scenario: Verify filter by Order Value
    When Filter by Order Value
    Then Validate the Order Value is listed

  # EDT-8472/OMS-880
  @filter_created_on
  Scenario: Verify filter by Created On
    When Filter by Created On
    Then Validate the Created On is listed
  
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


  @logout
  Scenario: logout X4A
    Given logout the X4A url

#  # EDT-8470/OMS-878
#  @search_bcn
#  Scenario: Search order by BCN from Sales Order
#    When search a order with specific BCN
#    Then Validate the searched BCN is listed
#
#  #EDT-8452/OMS-877
#  @search_order_type
#  Scenario: Search order by Type from Sales Order
#    When search a order with specific order Type
#    Then Validate the order Type is listed
#
#  #EDT-8452/OMS-877
#  @search_reseller_po
#  Scenario: Search order by Reseller PO from Sales Order
#    When search a order with specific Reseller PO
#    Then Validate the Reseller PO is listed
#
#  #EDT-8452/OMS-877
#  @search_vendor_name
#  Scenario: Search order by Vendor name from Sales Order
#    When search a order with specific Vendor name
#    Then Validate the Vendor name is listed
#
#  #EDT-8452/OMS-877
#  @search_order_status
#  Scenario: Search order by Order status from Sales Order
#    When search a order with specific Order status
#    Then Validate the Order status is listed
#
