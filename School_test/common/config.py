# -*- coding:utf-8 -*-
# Author:wangjian

cs_url = "http://wangjian.test.xx.cn/aroom/#/user/login"
Url = "https://cqxwxx.xx.cn/"
Url2 = "https://cqxwxx.xx.cn/aroom/#/user/login"
base_Url = "https://cqxwxx.xx.cn/api/jwt/login"
base_Url_2 = "https://cqxwxx.xx.cn/api/jwt/getLoginUser"
base_Url_3 = "https://cqxwxx.xx.cn/api/jwt/getPlatform"
base_Url_4 = "https://cqxwxx.xx.cn/api/right/getList"
base_Url_5 = "https://cqxwxx.xx.cn/api/school/getSchoolorPlatformInfoByHostName"
base_Url_6 = "https://cqxwxx.xx.cn/api/school/schooInfo"
base_Url_7 = "https://cqxwxx.xx.cn/api/school/operatorLog"
base_Url_8 = "https://cqxwxx.xx.cn/api/school/creditAccountRanking"
base_Url_9 = "https://cqxwxx.xx.cn/api/course/getPopularityCourseInfo"
base_Url_10 = "https://cqxwxx.xx.cn/api/score/listRankingByScore"
base_Url_11 = "https://cqxwxx.xx.cn/api/school/courseStudyCount"
base_Url_12 = "https://cqxwxx.xx.cn/api/school/baseSetting"
base_Url_13 = "https://cqxwxx.xx.cn/api/school/getBalance"
base_Url_14 = "https://cqxwxx.xx.cn/api/course/getCourseCollect"

home_Url = "https://cqxwxx.xx.cn/api/course/getCourseInfoByIds"
home_Url_sceond = "https://cqxwxx.xx.cn/api/school/getSchoolorPlatformInfoByHostName"
headers = {"Host": "cqxwxx.xx.cn",
           "Connection": "keep-alive",
           "Accept": "application/json",
           "Origin": "https://cqxwxx.xx.cn",
           "X-Requested-With": "XMLHttpRequest",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
           "Content-Type": "application/json;charset=UTF-8",
           "Referer": "https://cqxwxx.xx.cn/",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9"}
headers2 = {"Host": "cqxwxx.xx.cn",
           "Connection": "keep-alive",
           "Accept": "application/json, text/javascript, */*; q=0.01",
           "X-Requested-With": "XMLHttpRequest",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
           "Content-Type": "application/json;charset=UTF-8",
           "Referer": "https://cqxwxx.xx.cn/",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9"}
headers2.pop("Content-Type")
headers.pop("Origin")
headers4 = headers
headers3 = headers2
par = {"projectid":45}
par2 = {"projectid":12,"mainClassify":1,"childClassify":2,"beginNum":1,"endNum":10}
par3 = {"projectid":12}
par4 = {"projectid":7}
par5 = {"projectid":12,"num":4}
par6 = {"projectid":40}
data = {"encrypted": True, "username": "jialaoshi", "password": "Y2PGVLEjTvQMsajbxA4tZw==", "type": "account"}

#SQL_信息
sql_server = "101.71.142.95"
sql_user = "root"
sql_pwd = "Svnlan!#%852"
test_db = "video_ulimit_test"
yfb_db = ""
port = 16033