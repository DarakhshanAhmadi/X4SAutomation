from db.dao.X4ASalesOrderDetailsDAO import X4ASalesOrderDetailsDAO
from db.util.SqlUtil import SqlUtil


class X4ASalesOrderDetailsDbManagementService:

    def save_sales_order_details_data(self, db_path, x4a_sales_order_details_list):
        sql_util = SqlUtil(db_path)
        x4a_sales_order_details_dao = X4ASalesOrderDetailsDAO()
        return x4a_sales_order_details_dao.insert_records(sql_util, x4a_sales_order_details_list)

    def get_id_by_im_order_number(self, db_path, im_order_number):
        sql_util = SqlUtil(db_path)
        x4a_sales_order_details_dao = X4ASalesOrderDetailsDAO()
        return x4a_sales_order_details_dao.get_id_from_im_order_number(sql_util, im_order_number)

    def get_order_details(self, db_path, im_order_number):
        sql_util = SqlUtil(db_path)
        x4a_sales_order_details_dao = X4ASalesOrderDetailsDAO()
        return x4a_sales_order_details_dao.get_x4a_order_detail(sql_util, im_order_number)