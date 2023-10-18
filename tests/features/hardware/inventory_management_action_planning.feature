@inventory_management_action_planning @regression
Feature: Inventory Management Action Planning

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    When provide user ID and Password to login
    Then the user traverse to Action planning under Inventory Management menu

    #OMS-52
  @verify_table_headers_and_filter_options
  Scenario: Verify table columns under top 100 under performing tab
    Given click on top 100 under performing sku
    Then verify the columns in the table are correct
    Then verify filter options are correct

    #OMS-53
  @verify_filter_results
  Scenario: Verify Filter results
    Given filter by country
    Then filter by sku and validate data
    And filter by  MFN part number and validate data
    And filter by vendor business manager and validate data
    And filter by vendor name and validate data

  #OMS-53
  @verify_sort_results
  Scenario: Verify Sort results
    Given validate improvement opportunity is in descending by default
    Then sort inventory values and validate data
    And sort improvement opportunity and validate data
    And sort value on order and validate data
    And sort actual 121 and validate data
    And sort actual 151 and validate data

  #OMS-54, OMS-57
  @verify_action_on_sku
  Scenario: Verify Action on SKU
    Given filter by sku
    When validate popup text and action options are correct
    Then update the action and comment for sku
    And validate the updated action and comments are reflecting for sku