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

  @logout
  Scenario: logout X4A
    Given logout the X4A url

