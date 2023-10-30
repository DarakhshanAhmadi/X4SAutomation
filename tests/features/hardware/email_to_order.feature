@email_to_order @regression
Feature: Email To Order

  # OMS-573
  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Email to order menu
    Then verify Email to order page

#  OMS-575
  @eto_order_page
  Scenario: ETO order management
    When ETO order selected
    Then verify ETO order page headers

  @logout
  Scenario: logout X4A
    Given logout the X4A url

