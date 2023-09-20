from db.dao.X4ASalesOrderLinesDAO import X4ASalesOrderLinesDAO
from db.util.SqlUtil import SqlUtil


class X4ASalesOrderLinesDbManagementService:

    def save_sales_order_lines_data(self, db_path, x4a_sales_order_lines_list):
        sql_util = SqlUtil(db_path)
        x4a_sales_order_lines_dao = X4ASalesOrderLinesDAO()
        return x4a_sales_order_lines_dao.insert_records(sql_util, x4a_sales_order_lines_list)

    def get_order_lines_data(self, db_path, im_order_number):
        sql_util = SqlUtil(db_path)
        x4a_sales_order_lines_dao = X4ASalesOrderLinesDAO()
        return x4a_sales_order_lines_dao.get_x4a_order_lines_by_im_order(sql_util, im_order_number)
