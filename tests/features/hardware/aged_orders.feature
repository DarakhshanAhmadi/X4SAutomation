@aged_orders @regression
Feature: Aged Orders

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login

  @searchOrder
  Scenario: Search order by BCN from Aged Order
     When the user traverse to Aged Order Tab
#     Then verify the columns in the table are correct

