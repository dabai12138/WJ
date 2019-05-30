# -*- coding:utf-8 -*-

from common import config
import requests
import configparser as cparser
import os,json
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# import csv
# data = csv.reader(open("file.txt","r"))
#
# base_path = os.path.dirname(os.path.abspath(__file__))


class RequestMethod(object):
    """定义请求类型"""

    def get_requests(self,url,par,headers,s=requests.Session()):
        r = s.get(url=url,params=par,headers=headers,verify=False)
        return r

    def post_requests(self,url,par,headers,data,s=requests.Session()):
        r = s.post(url=url,params=par,headers=headers,data=data,verify=False)
        t = r.json()["data"]
        # print(r.status_code)
        # print(r.json()["success"])
        return s,t

if __name__ == "__main__":
    pass
