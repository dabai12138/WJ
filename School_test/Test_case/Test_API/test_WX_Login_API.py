# -*- coding:utf-8 -*-
# Author:wangjian


from common import config, reqMethod
import unittest,json

rm = reqMethod.RequestMethod()

def login_post():
    s,t = rm.post_requests(config.base_Url, config.par, config.headers, json.dumps(config.data))
    config.headers3["token"] = t["token"]
    config.headers3["Referer"] = "https://cqxwxx.xx.cn/aroom/"
    return s,t

class Test_Login(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_home_01(self):
        r = rm.get_requests(config.home_Url,config.par2,config.headers2)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])

    def test_home_02(self):
        r = rm.get_requests(config.home_Url_sceond,config.par3,config.headers3)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])

    def test_login_01(self):
        s,t = rm.post_requests(config.base_Url, config.par, config.headers, json.dumps(config.data))
        config.headers4["token"] = t["token"]
        r = s.get(url=config.base_Url_2,params=config.par,headers=config.headers4,verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])

    def test_login_02(self):
        # s,t = rm.post_requests(config.base_Url, config.par, config.headers, json.dumps(config.data))
        # config.headers3["token"] = t["token"]
        # config.headers3["Referer"] = "https://cqxwxx.xx.cn/aroom/"
        s, t = login_post()
        r = s.get(url=config.base_Url_3, params=config.par, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])

    def test_login_03(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_4, params=config.par4, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_04(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_5, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_05(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_6, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_06(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_7, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_07(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_8, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_08(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_9, params=config.par5, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_09(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_10, params=config.par6, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_10(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_11, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_11(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_12, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_12(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_13, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])
    def test_login_13(self):
        s,t = login_post()
        r = s.get(url=config.base_Url_14, params=config.par3, headers=config.headers3, verify=False)
        self.assertEqual(200,r.status_code)
        self.assertTrue(r.json()["success"])

if __name__ == "__main__":
    # t = Test_Login()
    # t.test_login_01()
    unittest.main()