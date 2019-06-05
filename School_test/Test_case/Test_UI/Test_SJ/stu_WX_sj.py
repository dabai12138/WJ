# -*- coding:utf-8 -*-
# Author:wangjian

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import time,sleep,ctime
from common.modul import *
from common import config,ele_act
from WX_data import page_ele as PE
from multiprocessing import Process
import sys,os
# b = os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0]
# sys.path.append(os.path.join(b,"ALL_driver"))
import unittest
import pymssql



class Test_sj_ad(unittest.TestCase):
    """试卷用例"""
    def setUp(self):
        try:
            self.driver = cdriver(self,PE.lists[1])
        except:
            self.driver = webdriver.Firefox()
        self.P = ele_act.Page(self.driver)
        self.Wait = ele_act.Page(self.driver)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.cs_url = config.cs_url
        login(self)
        self.Wait.wait()


    def test_sj(self):
        """学生试卷页"""
        self.P.act(PE.ele[1],PE.ssj_xp,s=1)
        sleep(4)
        self.assertEqual("1","1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
