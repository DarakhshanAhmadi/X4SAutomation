from db.dao.X4AInputOrderDAO import X4AInputOrderDAO
from db.util.SqlUtil import SqlUtil


class X4AInputOrderDbManagementService:

    def save_im360_input_order(self, db_path, x4a_input_order_list):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.insert_records(sql_util, x4a_input_order_list)
