from CommonUtilities.logGeneration import LogGenerator
from db.model.X4AUserData import X4AUserData
from db.model.X4AinputOrder import X4AInputOrder


class PrepareObject:
    logger = LogGenerator.logGen()

    def __init__(self, driver):
        self.driver = driver

    def prepare_x4a_inp_ord_data_obj(self, test_data):
        x4a_input_order_obj = X4AInputOrder(test_data.get("FeatureFileName"), test_data.get("ResellerBCN"),
                                            test_data.get("IMOrderNo"), test_data.get("OrderType"), test_data.get("ResellerPO"),
                                            test_data.get("VendorName"), test_data.get("OrderStatus"), test_data.get("CustomerPO"),
                                            test_data.get("TotalRevenueMin"), test_data.get("TotalRevenueMax"), test_data.get("CustomerName"))
        return x4a_input_order_obj
    def prepare_x4a_user_data_obj(self, test_data):
        x4a_user_data_obj = X4AUserData(test_data.get("FeatureFileName"),
                                            test_data.get("Associate_Name"),
                                            test_data.get("Associate_Email"),
                                            test_data.get("Associate_Roles"),
                                            test_data.get("Associate_Countries"))
        return x4a_user_data_obj
