@eto_error_order @regression
Feature: Email To Order - Error Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When The user traverse to Order Exception menu
    Then Click on Email to order tab

  # OMS-2538
  @validate_eto_error_order_details
  Scenario: Validate ETO error order details
    Then Click on eto error order
    Then Verify the eto error order details

  # OMS-2539
  @validate_eto_error_order_shipping_tab_details
  Scenario: Validate ETO error order shipping details
    Then Click on eto error order
    Then Click on shipping tab
    Then Verify ship to and end user info

  @logout
  Scenario: logout X4A
    Given logout the X4A url

