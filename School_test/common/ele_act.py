# -*- coding:utf-8 -*-
# Author:wangjian

# 页面的各种动作。。。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common.modul import *
import time

ele = ["ID","XPATH","CSS_SELECTOR","CLASS_NAME","NAME","TAG_NAME","LINK_TEXT"]
class Page(object):
    # screen_path =
    """页面方法"""
    def __init__(self,driver):
        self.driver = driver
    def ele_(self,ele,addr):
        #定位元素
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
    def eles(self,ele,addr):
        #定位元素组
        if ele == "ID":
            return self.driver.find_elements(By.ID,addr)
        elif ele == "XPATH":
            return self.driver.find_elements(By.XPATH,addr)
        elif ele == "CSS_SELECTOR":
            return self.driver.find_elements(By.CSS_SELECTOR,addr)
        elif ele == "TAG_NAME":
            return self.driver.find_elements(By.TAG_NAME,addr)
        elif ele == "CLASS_NAME":
            return self.driver.find_elements(By.CLASS_NAME,addr)
        elif ele == "LINK_TEXT":
            return self.driver.find_elements(By.LINK_TEXT,addr)
        elif ele == "NAME":
            return self.driver.find_elements(By.NAME,addr)
        else:
            print("定位方式输入不对")

    def act(self,ele,addr,txt=None,s=0):
        if s == 0:
            return self.ele_(ele,addr).send_keys(txt)
        elif s == 1:
            return self.ele_(ele,addr).click()
        elif s == 2:
            return self.ele_(ele,addr).clear()
        elif s == 3:
            return self.ele_(ele,addr).get_attribute(txt)
        elif s == 4:
            text = self.ele_(ele,addr).text
            return text

    def max_(self):
        try:
            self.driver.maximize_window()
        except Exception as e:
            raise e
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
    def alert(self):
        try:
            self.driver.switch_to_alert()
        except Exception as e:
            raise e
    def active_ele(self):
        #定位到当前聚焦的元素
        try:
            self.driver.switch_to.active_element()
        except Exception as e:
            raise e
    def handle_(self):
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for h in handles:
            if h != handle:
                self.driver.switch_to_window(h)
    def frame_(self,ele,addr):
        try:
            frame = self.ele_(ele,addr)
            self.driver.switch_to_frame(frame)
        except Exception as e:
            raise e
    def par_frame(self):
        try:
            self.driver.switch_to.parent_frame()
        except Exception as e:
            raise e
    def out_frame(self):
        #切换到主页面
        try:
            self.driver.switch_to_default_content()
        except Exception as e:
            raise e
    def wait(self):
        self.driver.implicitly_wait(30)
    def url(self):
        return self.driver.current_url()
    def AC(self,ele,addr,ele_=None,addr_=None,s=0):
        ac = ActionChains(self.driver)
        m = self.ele_(ele, addr)
        if s == 0:
            return ac.move_to_element(m).perform()
        elif s == 1:
            return ac.click_and_hold(m).perform()
        elif s == 2:
            return ac.context_click(m).perform()
        elif s == 3:
            return ac.double_click(m).perform()
        elif s == 4:
            n = self.ele_(self,ele_.addr_)
            return ac.drag_and_drop(m,n).perform()
    def screen_(self):
        #获取截图
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dirPath = createDir(path,"screen")
        os.chdir(dirPath)
        now = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))
        try:
            self.driver.get_screenshot_as_file(dirPath+"\\"+now+r".png")
        except Exception as e:
            raise e
    def get_ele_to_see(self,ele,addr):
        #把元素拉到可见位置
        try:
            target = self.ele_(ele,addr)
            self.driver.execute_script("arguments[0].scrolllntoView();",target)
        except Exception as e:
            raise e

    def scroll_down(self):
        #滚动条拉到最下方
        try:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        except Exception as e:
            raise e

if __name__ == "__main__":
    p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p = os.path.join(p,"screen")
    now = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))
    print(p+"\\"+now+r".png")
