@inventory_inquiry @regression
Feature: Inventory Inquiry

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    When provide user ID and Password to login
    Then the user traverse to Inventory Inquiry menu

    #OMS-455
  @verify_column_headers_and_quick_search_options
  Scenario: Verify table columns and quick search options
     Then verify the columns in the table are correct

    #OMS-456
  @verify_search
  Scenario: Verify search
     When search a sku
     Then Verify search result

   #OMS-471, OMS-461, OMS-1522
  @verify_customer_selection_for_listing_page
  Scenario: Verify customer selection in list page
     Given verify reseller price is empty and no customer present by default
     And verify customer selection popup contents
     And verify customer selection skip functionality
     When verify customer selection
     Then verify reseller price is populated
     Then edit customer and verify
     Then go to details page and validate selected customer is displayed

    #OMS-616
  @verify_customer_selection_for_details_page
  Scenario: Verify customer selection in details page
     Given the user traverse to Inventory Inquiry list page
     And search sku and go to details page
     And verify customer selection popup contents
     And verify customer selection skip functionality
     And verify no data present under inventory visibility
     When verify customer selection
     Then edit customer and verify
     And verify data present under inventory visibility