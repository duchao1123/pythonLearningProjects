"""
==================  ==================
"""
import pymysql
import day11.studentsystem.db.dbhelper as db


def connect_mysql():

    # 创建链接
    # connection = pymysql.connect(host="127.0.0.1", port=3306,
    #                              user='root', passwd='123456',
    #                              db='first_db_by_learn', charset='utf8mb4')
    connection = pymysql.connect(host="127.0.0.1", port=3306,
                                 user='root', passwd='123456', charset='utf8mb4')

    # 创建游标, 返回字典
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # 执行语句
    # row_count = cursor.execute("show tables;")
    # row_count = cursor.execute("create database StudentSystem")
    row_count = cursor.execute("show databases;")
    # 查询所有数据
    result = cursor.fetchall()
    # 返回一行
    # result_one = cursor.fetchone()
    # # 返回10行数
    # result_n = cursor.fetchmany(10)
    # 提交
    connection.commit()
    print(result)
    # 关闭资源
    cursor.close()
    connection.close()


if __name__ == '__main__':
    # connect_mysql()
    # db.create_db("teststudent")
    db.drop_db("teststudent")




