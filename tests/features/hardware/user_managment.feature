@user_management @regression
Feature: user management

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    When Traverse to associate management page
    Then Verify the Associate Header List

  # ADT-4655
  @searchAssociate
  Scenario: Search Associate details from Associate management page
    When Open the associate detail page
    Then Verify that Associate is Active
    And Verify the associates roles
    And Verify associate country

  # ADT-4656, ADT-4667, ADT-4677, ADT-4687
  @manageRole
  Scenario: Manage Associate role from Associate management page
    When A role is deleted
    Then Verify the roles deleted properly
    When A new role is added
    Then Verify the associates roles
    
  # ADT-4659, ADT-4679
  @manageCountry
  Scenario: Manage Associate country from Associate management page
    When A country is deleted
    Then Verify the country deleted properly
    When A new country is added
    Then Verify associate country

  # ADT-4666
  @associateDeactivation
  Scenario: Deactivate Associate from Associate management page
    When Associate is deactivated
    Then Verify the Associate is deactivated
    When Associate is Activated
    Then Verify that Associate is Active


