@inventory_inquiry @regression
Feature: Inventory Inquiry

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    When provide user ID and Password to login
    Then the user traverse to Inventory Inquiry menu

  @verify_column_headers_and_quick_search_options
  Scenario: Verify table columns and quick search options
     Then verify the columns in the table are correct
