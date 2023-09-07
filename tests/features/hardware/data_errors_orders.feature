@data_errors_orders @regression @demo_regression
Feature: Data Errors Orders


  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Error Order menu

#  EDT-9280/OMS-784
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

#  EDT-9280/OMS-784
  @after_resubmitted_order_not_present_in_error_data_list
  Scenario: Verify Order not present in list after successfully resubmitted
    When Resubmit Order Button clicked
    Then Verify contents of Resubmit Order Confirmation popup
    When Click on Resubmit Order Yes button
    Then Verify that Order has been successfully resubmitted message should display
    And Verify that Data Error Order should not be there in list

# EDT-9265
  @reference_detail_edit_popup
  Scenario: Verify Reference Details Edit popup content
    Given the error order is created via api for Reference Details
    When Search and Select the Data Errors Order for Reference Details
    Then Verify that Edit icon should display beside Reference Details title
    Then Verify contents of Edit Reference Details popup

# EDT-9265
  @po_and_end-customer_order_number_invalid_message
  Scenario: Verify the PO number and End customer order invalid message
    Then Verify PO textbox should not allow entering more than 18 characters
    And Verify that PO number is invalid once add this ^ special character
    Then Verify End customer order textbox should not allow entering more than 18 characters
    Then Verify that End customer order number is invalid once add this ^ special character

# EDT-9265
  @po_and_end-customer_order_number_max_length
  Scenario: Verify the PO number and End customer order for the max length
    Then Verify PO textbox should not allow entering more than 18 characters
    And Verify that PO number is invalid once add this ^ special character
    Then Verify End customer order textbox should not allow entering more than 18 characters
    And Verify that End customer order number is invalid once add this ^ special character
    When Click on X icon then verify that modified data should not get updated on order details page
    And Click on Cancel button then verify that modified data should not get updated on order details page

# EDT-9265
  @resubmitted_order_successfully_message
  Scenario: Verify resubmitted successful message
    When Update PO and End customer order number with valid data then validate updated data on order details page
    When Resubmit Order Button clicked
    Then Verify contents of Resubmit Order Confirmation popup
    When Click on Resubmit Order Yes button
    Then Verify that Order has been successfully resubmitted message should display


# EDT-9271
  @shipping_notes_edit_popup
  Scenario: Verify Shipping Notes Edit popup content
    Given the error order is created via api for Shipping notes
    When Search and Select the Data Errors Order for Shipping Notes
    Then Verify that Edit icon should display beside Shipping Notes
    And Verify contents of Edit Shipping Notes popup

# EDT-9271
  @updated_data-display_under_shipping_notes
  Scenario: Updated data should get displayed under shipping notes
    When Click on X icon on popup
    Then Verify Order Details page opened
    When Click on Cancel button on popup
    Then Verify Order Details page opened
    When Add the more 100 characters then validate message for maximum limit
    Then Update shipping notes with special characters and validate updated data should get display under shipping notes

#  OMS-48
  @filter_panel_options
  Scenario: Verify filter panel options
    When Click on Filter icon
    Then Verify filter panel options

#  OMS-48
  @order_entry_method_and_country_options_list
  Scenario: Verify Order entry method and Country options list
    When Verify Order entry method options list
    Then Verify Country options list
    And After selected any option clear all button should display
    And Selected multiple order entry method options should get display in header

#  OMS-48
  @country_and_order_entry_method_clear_all_value
  Scenario: Selected values get cleared from filter header
    When Click on Filter icon
    And Select any option from Order Entry Method and Country dropdown list
    And Click on Clear all button
    Then Selected values should get cleared from filter header and all data should get loaded in grid

#  OMS-48
  @order_entry_method_and_country_options_list
  Scenario: Verify Data in grid should get updated as per selected filter
    When Click on Filter icon
    And Select any option from Order Entry Method dropdown list
    Then Data in grid should get updated as per selected Order Entry Method filter if no data found for selected value No orders found message should display
#    When Select any option from Country dropdown list
#    Then Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display

  @logout
  Scenario: logout X4A
    Given logout the X4A url