from CommonUtilities.logGeneration import LogGenerator
from db.model.X4AInventory import X4AInventory
from db.model.X4AUserData import X4AUserData
from db.model.X4AbulkOrderData import X4AbulkOrderData
from db.model.X4AemailToOrderData import X4AEmailToOrderData
from db.model.X4AinputOrder import X4AInputOrder


class PrepareObject:
    logger = LogGenerator.logGen()

    def __init__(self, driver):
        self.driver = driver

    def prepare_x4a_inp_ord_data_obj(self, test_data):
        x4a_input_order_obj = X4AInputOrder(test_data.get("FeatureFileName"), test_data.get("ResellerBCN"),
                                            test_data.get("IMOrderNo"), test_data.get("OrderType"),
                                            test_data.get("ResellerPO"),
                                            test_data.get("VendorName"), test_data.get("OrderStatus"),
                                            test_data.get("CustomerPO"),
                                            test_data.get("TotalRevenueMin"), test_data.get("TotalRevenueMax"),
                                            test_data.get("CustomerName"),
                                            test_data.get("OrderValue"), test_data.get("ReferenceNumbers"),
                                            test_data.get("BillingToInfo"), test_data.get("ShipToInfo"),
                                            test_data.get("EndUserInfo"),
                                            test_data.get("OrderLinesTab"), test_data.get("SerialNumbers"),
                                            test_data.get("AdditionalAttributes"),
                                            test_data.get("FraudCancelOrderConfirmationId"),
                                            test_data.get("FraudReprocessOrderConfirmationId"),
                                            test_data.get("DataErrorResubmitOrderConfirmationId"),
                                            test_data.get("ResellerName"),
                                            test_data.get("EndUserName"), test_data.get("CreatedOn"),
                                            test_data.get("FilterOrderType"),
                                            test_data.get("FilterOrderStatus"),
                                            test_data.get("ModifyReferenceDetailsDataErrorOrderID"),
                                            test_data.get("ModifyShippingNotesDataErrorOrderID"),
                                            test_data.get("ModifyVMFDetailsDataErrorOrderID"),
                                            test_data.get("ModifyEndUserDetailsDataErrorOrderID"), test_data.get("EndUserPO"),
                                            test_data.get("EditOrderLines"),
                                            test_data.get("ModifyBillingAddressDataErrorOrderID"),
                                            test_data.get("OrderLineDataErrorOrderID"),
                                            test_data.get("ModifyOrderLineDataErrorOrderID"),
                                            test_data.get("IM360DataErrorOrderConfirmationId"))
        return x4a_input_order_obj

    def prepare_x4a_user_data_obj(self, test_data):
        x4a_user_data_obj = X4AUserData(test_data.get("FeatureFileName"),
                                        test_data.get("Associate_Name"),
                                        test_data.get("Associate_Email"),
                                        test_data.get("Associate_Roles"),
                                        test_data.get("Associate_Countries"))
        return x4a_user_data_obj

    def prepare_x4a_bulk_order_data_obj(self, test_data):
        x4a_bulk_order_data_obj = X4AbulkOrderData(test_data.get("FeatureFileName"),
                                                   test_data.get("Scenario"),
                                                   test_data.get("Operator_ID"),
                                                   test_data.get("Country_Code"),
                                                   test_data.get("Customer_Branch_and_Number"),
                                                   test_data.get("Reseller_PO"),
                                                   test_data.get("Carrier_Code"),
                                                   test_data.get("Order_Type"),
                                                   test_data.get("Header_Comment_1"),
                                                   test_data.get("Header_Comment_2"),
                                                   test_data.get("Ingram_SKU"),
                                                   test_data.get("Qty"),
                                                   test_data.get("Vendor_Part_Number"))
        return x4a_bulk_order_data_obj

    def prepare_x4a_inventory_data_obj(self, test_data):
        x4a_inventory_data_obj = X4AInventory(test_data.get("FeatureFileName"),
                                        test_data.get("UnderperformingSKU"),
                                        test_data.get("UnderperformingMFRPartNumber"),
                                        test_data.get("VendorBusinessManager"),
                                        test_data.get("VendorName"),
                                        test_data.get("Country"),
                                        test_data.get("Actions"),
                                        test_data.get("Comment"),
                                        test_data.get("AgingSKU"),
                                        test_data.get("AgingMFRPartNumber"),
                                        test_data.get('Customer'),
                                        test_data.get("EditCustomer"))
        return x4a_inventory_data_obj

    def prepare_x4a_email_to_order_data_obj(self, test_data):
        x4a_email_to_data_obj = X4AEmailToOrderData(test_data.get("FeatureFileName"),
                                                   test_data.get("Scenario"),
                                                   test_data.get("Account"),
                                                   test_data.get("Country"),
                                                   test_data.get("Order_Status"),
                                                   test_data.get("Customer_Name"),
                                                   test_data.get("Customer_PO"),
                                                   test_data.get("Sales_Order"),
                                                   test_data.get("Processed"),
                                                   test_data.get("Additional_Information"))
        return x4a_email_to_data_obj
