@user_management @regression
Feature: user management

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    And go to administration associate management page
    Then Verify that Associate Header List

  @searchAssociate
  Scenario: Search Associate details from Associate management page
    When Click on search bar and enter Associate name
    Then Verify that Associate details page has been opened
    And Verify the associates roles
    And Verify associate country

  @manageRole
  Scenario: Manage Associate role from Associate management page
    When Click on manage from associate role and Delete the role
    Then Verify the associates roles after deletion
    When Add new role
    Then Verify the associates roles

  @manageCountry
  Scenario: Manage Associate country from Associate management page
    When Click on manage from Countries and Delete the country
    Then Verify the associates countries after deletion
    When Add new country
    Then Verify associate country

  @associateDeactivation
  Scenario: Deactivate Associate from Associate management page
    Then go to administration associate management page
    When Click on search bar and enter Associate name
    And De-Activate the account
    Then go to administration associate management page
    When Click on search bar and enter Associate name
    Then Verify the account is deactivated
    When Activate the account
    Then go to administration associate management page
    When Click on search bar and enter Associate name
    Then Verify that Associate details page has been opened


