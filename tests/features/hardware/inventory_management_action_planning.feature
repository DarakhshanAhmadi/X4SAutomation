@inventory_management_action_planning @regression
Feature: Inventory Management Action Planning

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    When provide user ID and Password to login
    Then the user traverse to Action planning under Inventory Management menu

  @verify_column_headers
  Scenario: Verify table columns under top 100 under performing tab
    Given click on top 100 under performing sku
    Then verify the columns in the table are correct