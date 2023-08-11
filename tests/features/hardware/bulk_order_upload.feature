@bulk_order_upload @regression
Feature: Bulk Order Upload

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When the user traverse to Bulk order update menu
    Then verify bulk order update page

#  EDT-8751
  @file_upload_option_and_dialog_box
  Scenario: File Upload option & Dialog Box
    When upload file button clicked
    Then verify upload file popup

# EDT-8843
  @file_upload_error
  Scenario: Upload file error
    When other than excel file was uploaded
    Then verify error message

# EDT-8844
  @template_error
  Scenario: Template error
    When different template was uploaded
    Then verify template error message

#  EDT-8842, EDT-8845
  @file_upload_and_browse_file
  Scenario: Upload file
    When file was uploaded
    Then verify upload file ready popup
    When click on delete icon
    Then verify upload file popup
    When selected file for review
    Then verify bulk order page

# EDT-9593
  @download_template
  Scenario: Download template
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When download template button clicked
    Then verify the downloaded template file name
    When download template button clicked multiple times
    Then verify the all downloaded template file names

  @logout
  Scenario: logout X4A
    Given logout the X4A url

