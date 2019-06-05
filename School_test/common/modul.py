# -*- coding:utf-8 -*-
# Author:wangjian

#公共功能方法

from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WX_data import page_ele as PE
from common import config,ele_act,sql_connect
import os


def login(self):
    #网校登录
    self.P = ele_act.Page(self.driver)
    self.driver.get(self.cs_url)
    self.driver.maximize_window()
    self.Wait.wait()
    self.P.act(PE.ele[0], PE.cu_ID, PE.stuuser)
    self.P.act(PE.ele[0], PE.cps_ID, PE.stupwd)
    self.P.act(PE.ele[1], PE.cbu_xpath, s=1)
    WebDriverWait(self.driver, 20).until(EC.title_contains("网校"))

def cdriver(self,*args):
    #不同节点，不同浏览器运行选择
    self.driver = webdriver.Remote(
        command_executor=args[0],
        desired_capabilities={
            "platfrom": 'ANY',
            "browserName": args[1],
            "version": "",
            "javascriptEnabled": True
        }
    )
    return self.driver

def createDir(path,dirName):
    #创建文件夹
    dirPath = os.path.join(path,dirName)
    if os.path.exists(dirPath):
        return dirPath
    else:
        os.mkdir(dirPath)
        return dirPath

def act_sql(sql):
    #操作数据库 ，返回数据
    s = sql_connect.SQL_conn(sql)
    s.sql_conn()
    data = s.sql_search()
    s.sql_close()
    return data

def act_log():
    #打印日志方法
    pass




