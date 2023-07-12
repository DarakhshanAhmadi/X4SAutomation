from db.dao.X4AInputOrderDAO import X4AInputOrderDAO
from db.util.SqlUtil import SqlUtil


class X4AInputOrderDbManagementService:

    def save_x4a_input_order(self, db_path, x4a_input_order_list):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.insert_records(sql_util, x4a_input_order_list)

    def get_bcn_by_feature_file_name(self, db_path, feature_file_name):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.get_bcn_by_feature_file_name(sql_util, feature_file_name)

    def get_im_order_number_by_feature_file_name(self, db_path, feature_file_name):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.get_im_order_number_by_feature_file_name(sql_util, feature_file_name)

    def get_order_type_by_feature_file_name(self, db_path, feature_file_name):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.get_order_type_by_feature_file_name(sql_util, feature_file_name)

    def get_vendor_name_by_feature_file_name(self, db_path, feature_file_name):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.get_vendor_name_by_feature_file_name(sql_util, feature_file_name)

    def get_reseller_po_by_feature_file_name(self, db_path, feature_file_name):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.get_reseller_po_by_feature_file_name(sql_util, feature_file_name)

    def get_order_status_by_feature_file_name(self, db_path, feature_file_name):
        sql_util = SqlUtil(db_path)
        x4a_input_order_dao = X4AInputOrderDAO()
        return x4a_input_order_dao.get_order_status_by_feature_file_name(sql_util, feature_file_name)