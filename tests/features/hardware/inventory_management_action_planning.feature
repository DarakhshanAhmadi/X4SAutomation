@inventory_management_action_planning @regression
Feature: Inventory Management Action Planning

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    When provide user ID and Password to login
    Then the user traverse to Action planning under Inventory Management menu

    #OMS-52
  @verify_under_performing_sku_table_headers
  Scenario: Verify table columns under Top 100 Under performing SKU table
    Given click on top 100 under performing sku
    Then verify the columns in the table are correct
    And verify filter options are correct

    #OMS-53
  @verify_under_performing_sku_table_filter
  Scenario: Verify Filter results for Top 100 Under performing SKU table
    Given filter by country
    Then filter by under performing sku and validate data
    And filter by under performing MFR part number and validate data
    And filter by vendor business manager and validate data
    And filter by vendor name and validate data

  #OMS-53
  @verify_under_performing_sku_table_sort
  Scenario: Verify Sort results for Top 100 Under performing SKU table
    Given validate improvement opportunity is in descending by default
    Then sort inventory values and validate data
    And sort improvement opportunity and validate data
    And sort value on order and validate data
    And sort actual 121 and validate data
    And sort actual 151 and validate data
    And sort actual 181 and validate data

  #OMS-54, OMS-57
  @verify_under_performing_sku_table_action
  Scenario: Verify Action on SKU for Top 100 Under performing SKU table
    Given filter by under performing sku
    When validate popup text and action options are correct
    Then cancel updated the action and comment for sku and validate
    And save updated the action and comment for sku and validate

  #OMS-60
  @verify_aging_sku_table_headers
  Scenario: Verify table columns under Top 100 Aging SKU table
    Given click on top 100 aging sku tab
    Then verify the columns in top 100 aging sku table are correct
    And verify filter options are correct

   #OMS-61
  @verify_aging_sku_table_filter
  Scenario: Verify Filter results for Top 100 Aging SKU table
    Given filter by country
    Then filter by aging sku and validate data
    And filter by aging MFR part number and validate data
    And filter by vendor business manager and validate data
    And filter by vendor name and validate data

  #OMS-61
  @verify_aging_sku_table_sort
  Scenario: Verify Sort results for Top 100 Aging SKU table
    Given validate actual 151 is in descending by default
    Then sort inventory values and validate data
    And sort value on order and validate data
    And sort actual 121 and validate data
    And sort actual 151 and validate data
    And sort actual 181 and validate data

  #OMS-62 #OMS-66
  @verify_aging_sku_table_action
  Scenario: Verify Action on SKU for Top 100 Aging SKU table
    Given filter by aging sku
    When validate popup text and action options are correct for aging sku
    Then cancel updated the action and comment for sku and validate
    And save updated the action and comment for sku and validate
