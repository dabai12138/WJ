# -*- coding:utf-8 -*-
# Author:wangjian

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import time,sleep,ctime
from common import config,ele_act
from wj_data import page_ele as PE
from common.modul import *
from multiprocessing import Process
import sys,os
# b = os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0]
# sys.path.append(os.path.join(b,"ALL_driver"))
import unittest
import pymssql



class Test_sj_ad(unittest.TestCase):
    """新建试卷页用例"""
    def setUp(self):
        self.driver = cdriver(self,PE.lists[0]["host"], PE.lists[0]["browser"])
        self.P = ele_act.Page(self.driver)
        self.Wait = ele_act.Page(self.driver)
        self.Wait.wait()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.cs_url = config.cs_url
        login(self)
        self.Wait.wait()

    def test_sj(self):
        """进入试卷管理"""
        self.P.act(PE.ele[1],PE.sj_xpath,s=1)
        self.Wait.wait()
        t = self.P.act(PE.ele[1],PE.xj_xpath,s=4)
        self.assertEqual(t,"新建试卷")

    def test_sj_01(self):
        self.P.act(PE.ele[1],PE.sj_xpath,s=1)
        self.Wait.wait()
        t = self.P.act(PE.ele[1],PE.xj_xpath,s=4)
        self.assertEqual(t,"新建试卷")

    def test_sj_02(self):
        self.P.act(PE.ele[1],PE.sj_xpath,s=1)
        self.Wait.wait()
        t = self.P.act(PE.ele[1],PE.xj_xpath,s=4)
        self.assertEqual(t,"新建试卷")

    def test_sj_03(self):
        self.P.act(PE.ele[1],PE.sj_xpath,s=1)
        self.Wait.wait()
        t = self.P.act(PE.ele[1],PE.xj_xpath,s=4)
        self.assertEqual(t,"新建试卷")

    def test_sj_04(self):
        self.P.act(PE.ele[1],PE.sj_xpath,s=1)
        self.Wait.wait()
        t = self.P.act(PE.ele[1],PE.xj_xpath,s=4)
        self.assertEqual(t,"新建试卷")

    def test_sj_05(self):
        self.P.act(PE.ele[1],PE.sj_xpath,s=1)
        self.Wait.wait()
        t = self.P.act(PE.ele[1],PE.xj_xpath,s=4)
        self.assertEqual(t,"新建试卷")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
