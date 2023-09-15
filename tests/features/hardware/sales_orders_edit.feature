@sales_orders_edit @regression @demo_regression
Feature: Sales Orders Edit

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    #And the user traverse to Sales Order menu

  # EDT-10681 # EDT-10685
  @validate_updated_order_details
  Scenario: Validate Updated Order Details
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed
    When Click on searched IM order number
    When Verify order status is "Customer Hold(IM)"
    And Check if the order is editable
    Then Validate Cancel update of end user po and reseller po
    Then Update end user po and reseller po
    When Click on Order lines tab on Order Details page
    Then Cancel order line changes and validate it
    Then Update order line special bid unit price and quantity
    Then Click on resubmit order
    Then Validate end user po and reseller po updated
    Then Validate order line changes are updated

  # EDT-10977
  @unmark_for_cancel_order_line
  Scenario: Validate unmark cancel order line
    When Verify order status is "Customer Hold(IM)"
    And Click on Order lines tab on Order Details page
    And Click on three dots and check that the options are correct
    Then Click on mark for cancel for order lines
    And Click on Unmark for cancel order line

  # EDT-10730
  @void_entire_order
  Scenario: Verify customer hold cancel order
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed
    When Click on searched IM order number
    When Verify order status is "Customer Hold(IM)"
    Then Validate cancel order button is displayed
    Then Click on cancel order button
    Then Verify the elements displayed on cancel order alert
    Then Cancel the order
    Then Verify success toast notification is displayed
    When Verify order status is "VOIDED"

  # EDT-10971
  @cancel_single_line_item
  Scenario: Validate Mark a single line item for cancel
    When search a order with specific IM Order number
    Then Validate the IM Order number is listed
    When Click on searched IM order number
    When Verify order status is "Customer Hold(IM)"
    And Click on Order lines tab on Order Details page
    Then Click on mark for cancel for single line item
    Then Verify order line and edit button will not be active
    Then Click on resubmit order
    When Click on Order lines tab on Order Details page
    Then Verify cancelled order line is not visible

  @logout
  Scenario: logout X4A
    Given logout the X4A url