# -*- coding:utf-8 -*-
# Author:wangjian

# 页面的各种动作。。。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common.modul import *
from common.decorators import log_exception
import win32api
import win32con
import time


ele = ["ID","XPATH","CSS_SELECTOR","CLASS_NAME","NAME","TAG_NAME","LINK_TEXT"]
class Page(object):
    # screen_path =
    """页面方法"""
    def __init__(self,driver):
        self.driver = driver
    def __ele(self,ele,addr):
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
            return self.__ele(ele,addr).send_keys(txt)
        elif s == 1:
            return self.__ele(ele,addr).click()
        elif s == 2:
            return self.__ele(ele,addr).clear()
        elif s == 3:
            return self.__ele(ele,addr).get_attribute(txt)
        elif s == 4:
            text = self.__ele(ele,addr).text
            return text
        elif s == 5:
            return self.__ele(ele,addr).size
        elif s == 6:
            return self.__ele(ele,addr).tag_name()
        elif s == 7:#能否编辑
            return self.__ele(ele,addr).is_enabled()
        elif s == 8:
            return self.__ele(ele,addr).is_displayed()
        elif s == 9:#是否选中
            return self.__ele(ele,addr).is_selected()
        # elif s == 10:#获取css属性的值
        #     return self.__ele(ele,addr).value_of_css_property()




    @log_exception
    def select(self,ele,addr,s,flag=True):
        #select下拉框选择
        if isinstance(s,int):
            if flag:
                Select(self.__ele(ele,addr)).select_by_index(s)
            else:
                Select(self.__ele(ele,addr)).select_by_value(s)
        else:
            Select(self.__ele(ele,addr)).select_by_visible_text(s)

    @log_exception
    @property
    def max_(self):
        #窗口最大化
        self.driver.maximize_window()

    @log_exception
    @property
    def refresh(self):
        #刷新页面
        self.driver.refresh()

    @log_exception
    def EC_alert(self,s):
        #判断是否有alert
        alert = EC.alert_is_present()(self.driver)
        if alert and s == 1:
            alert.accept()
        elif alert and s == 2:
            alert.dismiss()

    @log_exception
    def alert(self,s=1,txt=None):
        #各种警告框的操作
        alert= self.driver.switch_to_alert()
        if s == 1:
            alert.accept()
        elif s == 2:
            alert.dismiss()
        elif s == 3:
            alert.send_keys(txt)
        elif s == 4:
            text = alert.text
            return text

    @log_exception
    @property
    def active_ele(self):
        #定位到当前聚焦的元素
        self.driver.switch_to.active_element()

    @log_exception
    def handle_(self):
        #跳转到新页面
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for h in handles:
            if h != handle:
                self.driver.switch_to_window(h)

    @log_exception
    def frame_(self,ele,addr):
        frame = self.__ele(ele,addr)
        self.driver.switch_to_frame(frame)

    @log_exception
    def par_frame(self):
        #跳回父frame
        self.driver.switch_to.parent_frame()

    @log_exception
    def out_frame(self):
        #切换到主页面
        self.driver.switch_to_default_content()

    @log_exception
    def wait(self):
        #隐式等待
        self.driver.implicitly_wait(30)

    @log_exception
    def url(self):
        #获取当前url
        return self.driver.current_url()


    @log_exception
    def AC(self,ele,addr,ele_=None,addr_=None,s=0):
        #鼠标各种操作
        ac = ActionChains(self.driver)
        m = self.__ele(ele, addr)
        if s == 0:
            return ac.move_to_element(m).perform()
        elif s == 1:
            return ac.click_and_hold(m).perform()
        elif s == 2:
            return ac.context_click(m).perform()
        elif s == 3:
            return ac.double_click(m).perform()
        elif s == 4:
            n = self.__ele(self,ele_.addr_)
            return ac.drag_and_drop(m,n).perform()

    @log_exception
    def screen_(self):
        #获取截图
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dirPath = createDir(path,"screen")
        os.chdir(dirPath)
        now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
        self.driver.get_screenshot_as_file(dirPath+"\\"+now+r".png")

    @log_exception
    def get_ele_to_see(self,ele,addr):
        #把元素拉到可见位置
        target = self.__ele(ele,addr)
        self.e_js("arguments[0].scrolllntoView();",target)

    @log_exception
    def scroll_down(self):
        #滚动条拉到最下方
        self.e_js("window.scrollTo(0,document.body.scrollHeight);")

    @log_exception
    def e_js(self,js,*args):
        #执行js代码
        self.driver.execute_script(js,args)

    @log_exception
    def p_source(self):
        #获取源码
        self.driver.page_source()

    @log_exception
    def cpage(self,s=1):
        # 窗口回退或前进
        if s == 1:
            self.driver.back()
        else:
            self.driver.forward()
    @log_exception
    def up_file(self,ele,addr):
        #上传文件
        pass

    @log_exception
    def  pywin(self):
        pass



if __name__ == "__main__":
    p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p = os.path.join(p,"screen")
    now = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))
    print(p+"\\"+now+r".png")

