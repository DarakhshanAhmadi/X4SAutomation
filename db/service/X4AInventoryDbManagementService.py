from db.dao.X4AInventoryDAO import X4AInventoryDAO
from db.util.SqlUtil import SqlUtil


class X4AInventoryDbManagementService:

    def save_x4a_inventory_data(self, db_path, x4a_inventory_list):
        sql_util = SqlUtil(db_path)
        x4a_inventory_dao = X4AInventoryDAO()
        return x4a_inventory_dao.insert_records(sql_util, x4a_inventory_list)

    def get_x4a_inventory_test_case_detail(self, db_path, feature_file_name):
        sql_util = SqlUtil(db_path)
        x4a_inventory_dao = X4AInventoryDAO()
        return x4a_inventory_dao.get_x4a_inventory_test_case_detail(sql_util, feature_file_name)