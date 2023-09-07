@data_errors_orders @regression
Feature: Fraud Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Error Order menu

#  EDT-9280
  @resubmit_order_popup
  Scenario: Verify resubmit order popup
    Given the error order is created via api
    When Search and Select the Data Errors Order
    Then Verify that Resubmit Order button should display
    And Update the correct Reseller PO
    And Update the correct End customer order
    When Resubmit Order Button clicked
    Then Verify contents of Resubmit Order Confirmation popup
    When Click on Review button
    Then Verify Order Details page opened

#  EDT-9280
  @after_resubmitted_order_not_present_in_error_data_list
  Scenario: Verify Order not present in list after successfully resubmitted
    When Resubmit Order Button clicked
    Then Verify contents of Resubmit Order Confirmation popup
    When Click on Resubmit Order Yes button
    Then Verify that Order has been successfully resubmitted message should display
    And Verify that Data Error Order should not be there in list

  @logout
  Scenario: logout X4A
    Given logout the X4A url
