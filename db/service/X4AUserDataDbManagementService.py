from db.dao.X4AUserDataDAO import X4AUserDataDAO
from db.util.SqlUtil import SqlUtil


class X4AUserDataDbManagementService:

    def save_associate_details(self, db_path, x4a_user_data_list):
        sql_util = SqlUtil(db_path)
        x4a_user_data_dao = X4AUserDataDAO()
        return x4a_user_data_dao.insert_records(sql_util, x4a_user_data_list)

    def get_associate_details(self, db_path):
        sql_util = SqlUtil(db_path)
        x4a_user_data_dao = X4AUserDataDAO()
        return x4a_user_data_dao.get_associate_details(sql_util)