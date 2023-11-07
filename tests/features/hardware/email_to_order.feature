@email_to_order @regression
Feature: Email To Order

  # OMS-573
  @login @test
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Email to order menu
    Then verify Email to order page

  @eto_order_page @test
  Scenario: ETO order management
    When ETO order selected
    Then verify ETO order page headers

#  OMS-575
  @order_through_mail @test1
  Scenario: Send Order to email
    When mail send with order pdf
    And Search ETO order by order status completed
    Then verify ETO order status

  @search_eto_order @test
  Scenario: Search ETO order
    When Search ETO order by Customer PO Number "2"
    Then verify ETO order status
    When Search ETO order by Customer PO Number "3"
    Then verify ETO order status
    When Search ETO order by Customer PO Number "4"
    Then verify ETO order status
    When Search ETO order by Customer PO Number "5"
    Then verify ETO order status

  @logout
  Scenario: logout X4A
    Given logout the X4A url

