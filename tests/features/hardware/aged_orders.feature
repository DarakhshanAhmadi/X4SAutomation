@aged_orders @regression
Feature: Aged Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login

  @verify_column_headers_and_quick_search_options
  Scenario: Verify table columns and quick search options
     When the user traverse to Aged Order Tab
     Then verify the columns in the table are correct
     And Verify quick search options

  @search_order_number
  Scenario: Verify quick search with IM order number
     When search IM order number
     Then verify the data for searched order is listed

  @search_vendor_name
  Scenario: Verify quick search with vendor name
    When search vendor name
    Then verify the data for searched vendor name is listed

  @search_bcn_account
  Scenario: Verify quick search with BCN account
    When search bcn account
    Then verify the data for searched bcn account is listed

  @search_customer_po
  Scenario: Verify quick search with Customer PO
    When search customer po
    Then verify the data for searched customer po is listed

  @search_order_date
  Scenario: Verify search with order date
    When select order date range
    Then verify the date for searched order date is listed
    And verify reset is working for order date

  @search_last_update_date
  Scenario: Verify search with last update date
    When select last update date range
    Then verify the date for searched last update date is listed
    And verify reset is working for last update date


  @filter_bcn_account
  Scenario: Verify filter with BCN account
    When filter with bcn
    Then verify the data for filtered bcn account is listed

  @filter_vendor
  Scenario: Verify filter with Vendor
    When filter with vendor
    Then verify the data for filtered vendor is listed

  @filter_customer_name
  Scenario: Verify filter with Customer name
    When filter with customer name
    Then verify the data for filtered customer name is listed

  @filter_order_type
  Scenario: Verify filter with Order type
    When filter with order type
    Then verify the data for filtered order type is listed

  @filter_order_status
  Scenario: Verify filter with Order status
    When filter with order status
    Then verify the data for filtered order status is listed

  @filter_total_revenue
  Scenario: Verify filter with Total revenue
    When filter with total revenue
    Then verify the data for filtered total revenue is listed

  @filter_bcn_vendor_order_status
  Scenario: Verify filter with BCN, Vendor and Order status
    When filter with bcn, vendor and order status
    Then verify the data for filtered bcn, vendor and order status is listed

  @logout
  Scenario: logout X4A
    Given logout the X4A url