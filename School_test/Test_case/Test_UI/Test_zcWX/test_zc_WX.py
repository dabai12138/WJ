# -*- coding:utf-8 -*-
# Author:wangjian

#注册网校---先登录后台删除网校，再用真实信息创建网校

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from common import config,ele_act
from WX_data import page_ele as PE
from common.modul import login
import time
import unittest

code = 123456
url = "https://www.xx.cn/"
list = ["中英均可，字符长度不超过50个字","5-20位英文、数字组成","请输入您的手机号","3-20位英文、数字，区分大小写","请输入您的真实姓名","请输入验证码"]
list_ = ["大白","wangjian",15257588041,"wj111111","王健",code]
class Test_zc_wx(unittest.TestCase):
    def setUp(self):
        self.driver = ele_act.cdriver(self,PE.lists[0]["host"], PE.lists[0]["browser"])
        self.P = ele_act.Page(self.driver)
        self.Wait = ele_act.Page(self.driver)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.Wait.wait()
    def test_01(self):
        """免费创建网校"""
        self.driver.get(url)
        self.P.max_()
        self.Wait.wait()
        self.P.act(PE.ele[1],PE.zc_xp,s=1)
        ist = self.P.eles(PE.ele[3],PE.zc_cn)
        for i in ist:
            for j in range(len(list)):
                if i.get_attribute("title") == list[j]:
                    i.send_keys(list_[j])
        self.P.act(PE.ele[0],PE.xy_id,s=1)
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

