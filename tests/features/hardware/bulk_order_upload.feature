@bulk_order_upload @regression
Feature: Bulk Order Upload

  @login @bulk_order
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Bulk order update menu
    Then verify bulk order update page

#  OMS-178
  @file_upload_option_and_dialog_box
  Scenario: File Upload option & Dialog Box
    When upload file button clicked
    Then verify upload file ready popup

# OMS-175
  @file_upload_error
  Scenario: Upload file error
    When other than excel file was uploaded
    Then verify error message

# OMS-176
  @template_error
  Scenario: Template error
    When different template was uploaded
    Then verify template error message

#  OMS-174, OMS-177
  @file_upload_and_browse_file 
  Scenario: Upload file
    When file was selected "4"
    Then verify select file popup
    When click on delete icon
    Then verify upload file ready popup
    When selected file for review
    Then verify bulk order page

# OMS-185
  @download_template
  Scenario: Download template
    When download template button clicked
    Then verify the downloaded template file name and its data
    When download template button clicked multiple times
    Then verify the all downloaded template file names

# OMS-186, OMS-187, OMS-193, OMS-191, OMS-1262
  @view_review
  Scenario: View Review Option
    When filter status with "Error found"
    Then verify the file upload list for status "Error found"
    When filter status with "Partially complete"
    Then verify the file upload list for status "Partially complete"
    When review icon clicked and downloaded the order list
    Then verify order page and downloaded order list
    When filter status with "Order placed"
    Then verify the file upload list for status "Order placed"
    When view icon clicked and downloaded the order list
    Then verify order page and downloaded order list

# OMS-188
  @cancel_delete
  Scenario: Cancel delete Option
    When filter status with "Upload in progress"
    Then verify the CANCEL icon
    When CANCEL icon clicked
    Then verify the DELETE icon and status upload cancelled
    When DELETE icon clicked
    Then search with the file name is not present

# OMS-186 , OMS-487
  @filter_with_user
  Scenario: filter user Option
    When filter with user
    Then verify the file upload list page filtered with user
    When upload Duplicate file
    Then verify Duplicate file error message

# OMS-179, OMS-180, OMS-195
  @error_in_order
  Scenario: error in order
    When upload file with one field as Null value
    Then verify the error message with one field as Null value
    When clicked on Discard button
    And upload file with two field as Null value
    Then verify the error message with two field as Null value
    When upload file with three field as Null value
    Then verify the error message with three field as Null value
    When clicked Apply button after filling required field
    Then verify Order status is Ready to place

# OMS-182, OMS-192
  @place_order
  Scenario: Place Order Option
    When upload file button clicked
    And selected file for review
    Then verify bulk order page
    And verify status as Ready to place and place order button
    When filter with file name
    Then verify the PLACE ORDERS icon
    When PLACE ORDERS icon clicked
    Then verify that order is placed

# OMS-487
  @duplicate_error 
  Scenario: Duplicate error
    When upload Duplicate file
    Then verify Duplicate file error message

# OMS-184
  @bulk_order_upload_page 
  Scenario: Bulk order upload page
    When upload file button clicked
    And selected file for review
    And filter with file name
    Then verify bulk order upload page

# OMS-183, OMS-488, OMS-489
  @multiple_place_order 
  Scenario: Multiple place order
    When file was selected "5"
    And clicked on review button
    And clicked on place order button
    Then verify multiple bulk order page status

  @logout
  Scenario: logout X4A
    Given logout the X4A url

