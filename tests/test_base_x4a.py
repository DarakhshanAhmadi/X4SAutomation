import pytest
from CommonUtilities.logGeneration import LogGenerator


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    logger = LogGenerator.logGen()

    def filtered_orders_by_feature_file(self, test_data_order, feature_file_name):
        filtered_order_data = test_data_order.loc[(test_data_order.FeatureFileName == feature_file_name)]
        return filtered_order_data
