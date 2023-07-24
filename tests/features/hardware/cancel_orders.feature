@cancel_orders @regression
Feature: Cancel Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Error Order menu

#  EDT-9815
  @Verify_Cancel_order_button_for_more_than_one_record
  Scenario: Verify Cancel order button for more than one record
    When Selected more than one record from System Error list
    Then Cancel button should remain disable
#
#  EDT-9815
  @Verify_cancel_order_button_for_one_record
  Scenario: Verify Cancel order button for one record
    When Selected only one record from System Error list
    Then Cancel button should get enable
    When Cancel button clicked
    Then verify the cancel order popup
    When click to No keep order button
    Then verify error detail page opened

#  EDT-9815
  @Verify_on_click_Yes_Cancel_order_button
  Scenario: Verify on click Yes, Cancel order button
    When Click on the YES button
    Then verify the cancel order popup after yes button
    When Click on the Back button
    Then verify redirect back to "Cancel Order" popup
#
#  EDT-9815
  @Verify_on_Cancel_order_button_without_reason
  Scenario: Verify on click cancel order button without giving reason
    When Click Cancel Order button without giving reason
    Then verify cancel order message

#  EDT-9815
  @Verify_on_Cancel_order_button_with_proper_reason
  Scenario: Verify on click cancel order button with proper reason
    When Order cancel with proper reason
    Then verify successfully cancel order message

  @logout
  Scenario: logout X4A
    Given logout the X4A url

