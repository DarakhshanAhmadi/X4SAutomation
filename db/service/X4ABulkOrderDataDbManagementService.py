from db.dao.X4AUserDataDAO import X4AUserDataDAO
from db.dao.X4AbulkOrderDataDAO import X4AbulkOrderDataDAO
from db.util.SqlUtil import SqlUtil


class X4ABulkOrderDataDbManagementService:

    def save_scenario_details(self, db_path, x4a_user_data_list):
        sql_util = SqlUtil(db_path)
        x4a_bulk_order_data_dao = X4AbulkOrderDataDAO()
        return x4a_bulk_order_data_dao.insert_records(sql_util, x4a_user_data_list)

    def get_scenario_details(self, db_path, scenario_no):
        sql_util = SqlUtil(db_path)
        x4a_bulk_order_data_dao = X4AbulkOrderDataDAO()
        return x4a_bulk_order_data_dao.get_scenario_details(sql_util, scenario_no)