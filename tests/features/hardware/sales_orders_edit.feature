@sales_orders_edit @regression @demo_regression
Feature: Sales Orders Edit

  @login
  Scenario: Login to X4A portal
    Given launch chrome browser and open the X4A url
    Then provide user ID and Password to login
    And the user traverse to Sales Order menu

  # EDT-10681 # EDT-10685 # EDT-10683 # EDT-106
  @validate_updated_order_details
  Scenario Outline: Validate Updated Order Details
    When search a order with specific IM Order number <order_id>
    Then Validate the IM Order number <order_id> is listed
    When Click on searched IM order number
    When Verify order status <order_status> falls under edit category
    Then Validate Cancel update of end user po and reseller po
    Then Update end user po and reseller po
    When Click on Billing tab on Order Details page
    Then Cancel ship to and end user info details and validate
    Then Update ship to and end user info
    When Click on Order lines tab on Order Details page
    Then Cancel order line changes and validate it
    Then Update order line special bid unit price and quantity
    Then Click on resubmit order
    When fetch sales order details via api for <order_id> of type <order_type> created on <order_date> via <entry_channel>
    Then Validate header data contains Order value and Order type
    Then Validate fields under reference number section
    Then Validate carrier code
    Then Validate end user po and reseller po updated
    When Click on Billing tab on Order Details page
    Then Validate ship to and end user info updated
    Then Validate fields under Ship from info section
    Then Validate fields under Bill to info section
    Then Validate fields under Ship to info section
    Then Validate fields under End user info section
    When Click on Order lines tab on Order Details page
    Then Validate ACOP field is present and has valid value
    Then Validate order line changes are updated
    Then Validate fields under Order lines tab
    When Click on Additional attributes tab on Order Details page
    Then Verify that title on the header of the order details page contains Ingram order number and Order Status
    Then Validate payment terms code
    Then Click on order management link
    Examples:
    | order_id    | order_date | order_status         | entry_channel | order_type |
#    | 20-VNW5G-11 | 2023-11-21 | Customer Hold(IM)    | X4C           | Stock      |
#    |  20-VNVWH-11| 2023-11-20 | Order Hold(IM)       | X4C           | Stock      |
    | 20-VNZCQ-11 | 2023-11-22 | Order Hold(IM)       | X4C           | Stock      |
#    | 20-VNRLB-11 | 2023-11-07 | Order Hold(IM)    | TELESALES     | Stock      |
#    | 20-VNRL9-11 | 2023-11-07 | Order Hold(IM)    | 20-VNRL9-11   | Direct     |

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