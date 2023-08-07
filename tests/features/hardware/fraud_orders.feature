@fraud_orders @regression
Feature: Fraud Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Error Order menu

#  EDT 10312
  @Fraud_orders_tab
  Scenario: Verify Fraud Orders tab
    Then Verify that Fraud Orders tab shown on Error orders page

#  EDT-10356
  @reprocess_order_button
  Scenario: Verify Reprocess Order Button
    When Search and Select the Order
    Then Verify that Reprocess Order button should display
    When Reprocess Order Button button clicked
    Then Verify the Reprocess Order popup
    When Click to Review button
    Then Verify Order Details page opened

#  EDT-10356
  @after_reprocess_order_not_present
  Scenario: Verify Order in list after successful reprocess
    When Reprocess Order Button button clicked
    Then Verify the Reprocess Order popup
    When Click on Reprocess Order Yes button
    Then Verify that Reprocessed! Order was successfully resubmitted message should display
    And Verify that Order should not be there in list

#  EDT-10355
  @Cancel_order_button
  Scenario:  Verify fraud Cancel Order Button
    When Search and Select the Order for Cancel
    Then Verify that Cancel Order button should display
    When Cancel Order Button button clicked
    Then Verify the Fraud Cancel Order popup
    When Click to No keep order button
    Then Verify Order Details page opened

#  EDT-10355
  @Verify_on_click_Yes_Cancel_order_button
  Scenario: Verify Cancel order popup after click on Yes, Cancel order button
    When Click on the Yes Cancel Order button
    Then Verify the cancel order popup after yes button
    When Click on the Back button
    Then Verify redirect back to Cancel Order popup

#  EDT-10355
  @Verify_on_Cancel_order_button_without_reason
  Scenario: Verify to click on Cancel order button without giving reason
    When Click on Cancel Order button without giving reason
    Then Verify Cancel order message

#  EDT-10355
  @Verify_on_Cancel_order_button_with_proper_reason
  Scenario: Verify on click Cancel order button with proper reason
    When Order cancel with proper reason
    Then Verify successfully cancel order message
    And Verify that Cancel Order should not be there in list

  @logout
  Scenario: logout X4A
    Given logout the X4A url
