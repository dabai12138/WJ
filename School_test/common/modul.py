# -*- coding:utf-8 -*-
# Author:wangjian

from twilio.rest import Client
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wj_data import page_ele as PE
from common import config,ele_act


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

