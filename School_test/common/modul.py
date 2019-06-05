# -*- coding:utf-8 -*-
# Author:wangjian

#公共功能模块

from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wj_data import page_ele as PE
from common import config,ele_act
import os


def login(self):
    """网校登录"""
    self.P = ele_act.Page(self.driver)
    self.driver.get(self.cs_url)
    self.driver.maximize_window()
    self.Wait.wait()
    self.P.act(PE.ele[0], PE.cu_ID, PE.stuuser)
    self.P.act(PE.ele[0], PE.cps_ID, PE.stupwd)
    self.P.act(PE.ele[1], PE.cbu_xpath, s=1)
    WebDriverWait(self.driver, 20).until(EC.title_contains("网校"))

def cdriver(self,host,browser):
    self.driver = webdriver.Remote(
        command_executor=host,
        desired_capabilities={
            "platfrom": 'ANY',
            "browserName": browser,
            "version": "",
            "javascriptEnabled": True
        }
    )
    return self.driver

def createDir(path,dirName):
    """创建文件夹"""
    dirPath = os.path.join(path,dirName)
    if os.path.exists(dirPath):
        return dirPath
    else:
        os.mkdir(dirPath)
        return dirPath




