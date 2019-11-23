#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author : Effort
# @Time : 2019/10/14 0014 14:30

import pymysql

def class_dev():
        # 创建连接
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mysql123', db='oldboy')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 执行SQL，并返回收影响行数
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        print(class_list)