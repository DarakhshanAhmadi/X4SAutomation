@aged_orders @regression
Feature: Aged Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login

  @verify
  Scenario: Verify table columns and quick search options
#     When the user traverse to Aged Order Tab
     Then verify the columns in the table are correct
     And Verify quick search options

  @searchOrderNumber
  Scenario: Verify quick search with IM order number
     When search IM order number
     Then verify the data for searched order is listed

  @searchVendorName
  Scenario: Verify quick search with vendor name
    When search vendor name
    Then verify the data for searched vendor name is listed

  @searchBCNAccount
  Scenario: Verify quick search with BCN account
    When search bcn account
    Then verify the data for searched bcn account is listed

  @searchCustomerPO
  Scenario: Verify quick search with Customer PO
    When search customer po
    Then verify the data for searched customer po is listed

  @searchOrderDate
  Scenario: Verify search with order date
    When select order date range
    Then verify the date for searched order date is listed
    And verify reset is working for order date

  @searchLastUpdateDate
  Scenario: Verify search with last update date
    When select last update date range
    Then verify the date for searched last update date is listed
    And verify reset is working for last update date


  @filterBCNAccount
  Scenario: Verify filter with BCN account
    When filter with bcn
    Then verify the data for filtered bcn account is listed

  @filterVendor
  Scenario: Verify filter with Vendor
    When filter with vendor
    Then verify the data for filtered vendor is listed

  @filterCustomerName
  Scenario: Verify filter with Customer name
    When filter with customer name
    Then verify the data for filtered customer name is listed

  @filterOrderType
  Scenario: Verify filter with Order type
    When filter with order type
    Then verify the data for filtered order type is listed

  @filterOrderStatus
  Scenario: Verify filter with Order status
    When filter with order status
    Then verify the data for filtered order status is listed

  @filterTotalRevenue
  Scenario: Verify filter with Total revenue
    When filter with total revenue
    Then verify the data for filtered total revenue is listed

  @filterBCNVendorOrderStatus
  Scenario: Verify filter with BCN, Vendor and Order status
    When filter with bcn, vendor and order status
    Then verify the data for filtered bcn, vendor and order status is listed

  @logout
  Scenario: logout X4A
    Given logout the X4A url