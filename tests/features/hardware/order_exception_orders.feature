@order_exception_orders @regression @demo_regression
Feature: Order Exception Orders


  @login
  Scenario: Login to X4A portal
    Given Launch chrome browser and open the X4A url
    Then Provide user ID and Password to login
    When The user traverse to Order Exception menu

  # EDT-9280/OMS-784
  @resubmit_order_popup
  Scenario: Verify resubmit order popup
    Given The order exception is created via api
    When Search and Select the Data Errors Order
    Then Verify that Resubmit Order button should display
    And Update the correct Reseller PO
    And Update the correct End customer order
    When Resubmit Order Button clicked
    Then Verify contents of Resubmit Order Confirmation popup
    When Click on Review button
    Then Verify Order Details page opened

  # EDT-9280/OMS-784
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
    Given The order exception is created via api for Reference Details
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
    Given The order exception is created via api for Shipping notes
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

  # OMS-48
  @filter_panel_options
  Scenario: Verify filter panel options
    When Click on Filter icon
    Then Verify filter panel options

  # OMS-48
  @order_entry_method_and_country_options_list
  Scenario: Verify Order entry method and Country options list
    When Verify Order entry method options list
    Then Verify Country options list
    And After selected any option clear all button should display
    And Selected multiple order entry method options should get display in header


  # OMS-48
  @country_and_order_entry_method_clear_all_value
  Scenario: Selected values get cleared from filter header
    When Click on Filter icon
    And Select any option from Order Entry Method and Country dropdown list
    And Click on Clear all button
    Then Selected values should get cleared from filter header and all data should get loaded in grid

  # OMS-48
  @order_entry_method_and_country_options_list
  Scenario: Verify Data in grid should get updated as per selected filter
    When Click on Filter icon
    And Select any option from Order Entry Method dropdown list
    Then Data in grid should get updated as per selected Order Entry Method filter if no data found for selected value No orders found message should display
    When Select any option from Country dropdown list
    Then Data in grid should get updated as per selected country filter if no data found for selected value No orders found message should display

  # OMS-2471
  @filter_panel_last_order_attempt_on_section
  Scenario: Last order attempt on section should display inside filter panel
    When Click on Filter icon
    Then Verify that Last order attempt on section should display inside filter panel
    And Verify that contents of Last order attempt on section
    And Verify that Last order attempt on section Calendar should open and it should allow date selection
    And Select the Last order attempt on section From and To date and Verify that Data should get filtered on selected date ranges
    And Select last 30 days checkbox from Last order attempt on section and Verify that data should get filtered on selected date ranges


  # OMS-2471
  @filter_panel_created_on_section
  Scenario: Created on section should display inside filter panel
    When Click on Filter icon
    Then Verify that Created on section should display inside filter panel
    And Verify that contents of Created On section
    And Verify that Created On section Calendar should open and it should allow date selection
    And Select the Created On section From and To date and Verify that Data should get filtered on selected date ranges
    And Select last 30 days checkbox from Created on section and Verify that data should get filtered on selected date ranges

  # OMS-43
  @vmf_details_edit_popup
  Scenario: Verify VMF Details Edit popup content
    Given The order exception is created via api for VMF Details
    When Search and Select the Data Errors Order for VMF Details
    Then Verify that Edit icon should display beside VMF Details
    And Verify contents of Edit VMF Details popup


  # OMS-43
  @vmf_details_edit_popup
  Scenario: Updated VMF data should get display on Order Details page
    When Verify that Attribute value should allow special characters
    Then Enter valid data for Attribute value fields save it then Verify Saved data should get display in order details page
    And Verify that VMF entered data should not get saved after click on X icon
    And Verify that modified VMF data should not get updated on order details page after click on Cancel button

  # OMS-782
  @end_user_details_edit_popup
  Scenario: Verify End User Details Edit popup content
    Given The order exception is created via api for End User Details
    When Search and Select the Data Errors Order for End User Details
    Then Verify that Edit icon should display beside End User Details
    And Verify contents of Edit End User Details popup

  # OMS-782
  @search_end_user
  Scenario: Searching End User
    Then Verify that all address matching with entered text should get displayed
    And Select the end user with suffix and verify that Edit icon should display for user and Save button should get enabled
    And Verify contents of selected end user with suffix edit popup
    When Remove the data from Name, Phone Number, Email and Click on Add button then Validation required message should display
    Then Click on Save Button and Verify that selected end user information should get displayed on order details page
    And Modify Name, Phone Number, Email and Click on Add button then Verify that updated end user information should display on order details page

  # OMS-782/OMS-3068
  @add_new_end_user_edit_popup
  Scenario: Verify Add New End User Edit popup content
    Then Verify contents of Edit Add New End User popup
    And Verify that Customer type options list
    And Verify that added new end user should display and user should able to select it and checkbox is disable

  # OMS-33
  @billing_address_edit_popup
  Scenario: Verify Billing Address Edit popup content
    Given The order exception is created via api for Billing Address
    When Search and Select the Data Errors Order for Billing Address
    Then Verify contents of Edit Billing Address popup
    When Click on X icon on popup and Verify that Order Details page should display
    And Click on Cancel button on popup and Verify that Order Details page should display

  # OMS-33
  @search_billing_address
  Scenario: Verify billing address search with suffix
    When Search with special characters then No records found matching your search criteria should display
    And Search with valid Suffix and then Billing address details should get loaded in popup
    And Select the searched address and then Save button should get enabled on selecting address
    Then Verify that selected billing address should get displayed on Order details page

  # OMS-29
  @order_line_remove_icon
  Scenario: Verify that order resubmitted successfully after click on Mark for Cancel option
    Given The order exception is created via api for Order Line
    When Search and Select the Data Errors Order for Order Line
    Then Verify that remove icon should display for order line
    When Click on Mark for Cancel option and Verify line should grey out and should not allow further edit operations
    And Click on Unmark for Cancel option and Verify line should become enable and it should allow edit operations
    Then Verify that Order should get resubmitted succesfully after cancel the Order line

  # OMS-29
  @order_line_mark_for_dropdown
  Scenario: Verify that At least one order line is required to resubmit the order message
    When Click on Mark for Cancel option from dropdown and Verify line should grey out
    And Click on Unmark for Cancel option from dropdown and Verify line should get enable
    Then Verify that At least one order line is required to resubmit the order message


  # OMS-46
  @update_existing_order_line
  Scenario: Modify existing Order line
    Given The order exception is created via api for modify Order Line
    When Search and Select the Data Errors Order for modify Order Line
    Then Verify that Edit Icon should display for each lines
    When Click on edit icon and Verify that Update and Cancel Icon should display
    Then Verify that Quantity, Reseller price, End user price and End user po# fields become editable
    When Click on X icon and Verify that Updated data should get discarded
    Then Verify that Quantity, Reseller price, End user price and End user po# fields not allow non numeric content

  # OMS-46
  @resubmit_updated_existing_order_line
  Scenario: Update Quantity, Reseller price and End User PO value and resubmit the order
    When Update the Order line Quantity, Reseller price and End User PO value
    And Update PO and End customer order number with valid data then validate updated data on order details page
    And Resubmit Order Button clicked
    And Click on Resubmit Order Yes button
    Then Verify that Order has been successfully resubmitted message should display

  # OMS-3073/OMS-3059
  @operator_id
  Scenario: Operator Id on Order Details Page
    Given The order exception is created via api
    When Search and Select the Data Errors Order
    Then Verify that Operator ID should be display on the Order details page
    And Verify that Channel label should get displayed on Order details page

  # OMS-3059
  @order_channel
  Scenario: Order Channel on Order Details Page
    Given The order exception is created via api using IM360 payload
    Then Verify that Order channel should match with the channel showing on list page

#   OMS-3266
  @Shipping_details
  Scenario Outline: Shipping Details on Order Details Page
    Given Create order exception Using X4D payload without <shipingdetails> via api
    Then Verify that Shipping Details option section should display
    Examples:
      | shipingdetails |
      | Yes            |
      | No             |

  # OMS-788
  @shipping_address_edit_popup
  Scenario: Verify Shipping Address Edit popup contents
    Given The order exception is created via api for Shipping Address
    When Search and Select the Data Errors Order for Shipping Address
    Then Verify contents of Edit Shipping Address popup
    When Click on X icon on shipping address popup and Verify that Order Details page should display
    And Click on Cancel button on shipping address popup and Verify that Order Details page should display

  # OMS-788
  @search_shipping_address
  Scenario: Verify Shipping address search
    When Verify that all shipping address matching with search entered text should get displayed
    Then Verify that Add New Shipping Address pop up contents
    And Add the new shipping address and verify that Added data should display
    When Click on X icon on Add new shipping address popup and Verify that entered data should not get saved
    And Click on Cancel button on Add new shipping address popup and Verify that entered data should not get saved

  # OMS-3557
  @data_error_check_for_duplicate_po_for_us
  Scenario Outline: Verify Resubmitting Data error order with duplicate PO# for US marketplace
    Given Create Data Error Order for duplicate <po_number> PO via api for <country> markeplace
    When Search and Select the Data Errors Order for Duplicate PO
    And Correct the PO# and resubmit the order
    Then Verify that Data Error should get removed form data error list
    Given Create Data Error Order for duplicate <po_number> PO via api for <country> markeplace
    When Search and Select the Data Errors Order for Duplicate PO
    And Correct the PO# and Add new line then Verify Resubmit Order message and Cancel and Proceed button
    And Click on Cancel Order button then popup should open to enter reject reason
    And Click on Proceed button and resubmit the order
    Then Verify that Data Error should get removed form data error list
    Examples:
      | po_number | country |
      | POAUTO^   | US      |

  # OMS-3557
  @data_error_check_for_duplicate_po_for_ca
  Scenario Outline: Verify Resubmitting Data error order with duplicate PO# for CA marketplace
    Given Create Data Error Order for duplicate <po_number> PO via api for <country> markeplace
    When Search and Select the Data Errors Order for Duplicate PO
    And Correct the PO# and resubmit the order
    Examples:
      | po_number  | country |
      | POAUTO^    | CA      |
      | NEWPOAUTO^ | CA  `   |

 # OMS-3557
  @data_error_check_for_duplicate_case_sensitive_po_for_ca
  Scenario Outline: Verify Resubmitting Data error order with duplicate case sensitive PO# for CA marketplace
    Given Create Data Error Order for duplicate <po_number> PO via api for <country> markeplace
    When Search and Select the Data Errors Order for Duplicate PO
    And Correct the End Customer order# then Verify Resubmit Order message and Cancel and Proceed button
    Examples:
      | po_number | country |
      | poauto    | CA      |


  @logout
  Scenario: logout X4A
    Given logout the X4A url