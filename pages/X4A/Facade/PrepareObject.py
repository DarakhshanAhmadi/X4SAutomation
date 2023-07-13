from CommonUtilities.logGeneration import LogGenerator
from db.model.X4AinputOrder import X4AInputOrder


class PrepareObject:
    logger = LogGenerator.logGen()

    def __init__(self, driver):
        self.driver = driver

    def prepare_x4a_inp_ord_data_obj(self, test_data):
        x4a_input_order_obj = X4AInputOrder(test_data.get("FeatureFileName"), test_data.get("ResellerBCN"),
                                            test_data.get("IMOrderNo"), test_data.get("OrderType"),
                                            test_data.get("ResellerPO"), test_data.get("VendorName"), test_data.get("OrderStatus"))
        return x4a_input_order_obj
