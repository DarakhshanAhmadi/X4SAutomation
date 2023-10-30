from db.dao.X4AUserDataDAO import X4AUserDataDAO
from db.dao.X4AemailToOrderDataDAO import X4AemailToOrderDataDAO
from db.util.SqlUtil import SqlUtil


class X4AEmailToOrderDataDbManagementService:

    def save_scenario_details(self, db_path, x4a_user_data_list):
        sql_util = SqlUtil(db_path)
        x4a_email_to_order_data_dao = X4AemailToOrderDataDAO()
        return x4a_email_to_order_data_dao.insert_records(sql_util, x4a_user_data_list)

    def get_scenario_details(self, db_path, scenario_no):
        sql_util = SqlUtil(db_path)
        x4a_email_to_order_data_dao = X4AemailToOrderDataDAO()
        return x4a_email_to_order_data_dao.get_scenario_details(sql_util, scenario_no)