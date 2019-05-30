# -*- coding:utf-8 -*-
# Author:wangjian

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ele = ["ID","XPATH","CSS_SELECTOR","CLASS_NAME","NAME","TAG_NAME","LINK_TEXT"]
class Page(object):
    """页面方法"""
    def __init__(self,driver):
        self.driver = driver
    def eles(self,ele,addr):
        if ele == "ID":
            return self.driver.find_element(By.ID,addr)
        elif ele == "XPATH":
            return self.driver.find_element(By.XPATH,addr)
        elif ele == "CSS_SELECTOR":
            return self.driver.find_element(By.CSS_SELECTOR,addr)
        elif ele == "TAG_NAME":
            return self.driver.find_element(By.TAG_NAME,addr)
        elif ele == "CLASS_NAME":
            return self.driver.find_element(By.CLASS_NAME,addr)
        elif ele == "LINK_TEXT":
            return self.driver.find_element(By.LINK_TEXT,addr)
        elif ele == "NAME":
            return self.driver.find_element(By.NAME,addr)
        else:
            print("定位方式输入不对")

    def act(self,ele,addr,txt=None,s=0):
        if s == 0:
            return self.eles(ele,addr).send_keys(txt)
        elif s == 1:
            return self.eles(ele,addr).click()
        elif s == 2:
            return self.eles(ele,addr).clear()
        elif s == 3:
            text = self.eles(ele,addr).text
            return text
    def talert(self):
        alert = EC.alert_is_present()(self.driver)
        if alert:
            alert.accept()
        else:
            pass
    def falert(self):
        alert = EC.alert_is_present()(self.driver)
        if alert:
            alert.dismiss()
        else:
            pass
    def handle_(self):
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for h in handles:
            if h != handle:
                self.driver.switch_to_window(h)
    def frame_(self,ele,addr):
        frame = self.eles(ele,addr)
        self.driver.switch_to_frame(frame)
    def wait(self):
        self.driver.implicitly_wait(30)
    def url(self):
        return self.driver.current_url()
    def AC(self,ele,addr,ele_=None,addr_=None,s=0):
        ac = ActionChains(self.driver)
        m = self.eles(ele, addr)
        if s == 0:
            return ac.move_to_element(m).perform()
        elif s == 1:
            return ac.click_and_hold(m).perform()
        elif s == 2:
            return ac.context_click(m).perform()
        elif s == 3:
            return ac.double_click(m).perform()
        elif s == 4:
            n = self.eles(ele_.addr_)
            return ac.drag_and_drop(m,n).perform()

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

