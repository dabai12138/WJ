# -*- coding:utf-8 -*-
# Author:wangjian

#自建装饰器方法

from common import act_log
import functools

#打印错误信息的装饰器
def log_exception(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        log = act_log.Log()
        try:
            func(*args,**kwargs)
        except Exception as e:
            log.exception("[Error in {}] msg: {}".format(__name__,str(e)))
            raise
    return wrapper

if __name__ == "__main__":
    @log_exception
    def tain(x):
        x = 10
        def nat():
            print(x.encode("utf-8"))
        nat()
    tain(1)