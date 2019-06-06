# -*- coding:utf-8 -*-
# Author:wangjian

import os,sys
#导入需要的模块

u = os.popen(r"pip install unittest","r")
s = os.popen(r"pip install smtplib","r")
sw = os.popen(r"pip install selenium","r")
msql = os.popen(r"pip install pymysql","r")
sql = os.popen(r"pip install pymssql","r")
py = os.popen(r"pip install pywin32","r")
print(u.read())
print(s.read())
print(sw.read())
print(msql.read())
print(sql.read())
print(py.read())