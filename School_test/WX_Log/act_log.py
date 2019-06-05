# -*- coding:utf-8
# Author:wangjian

import logging,time,os
import functools
now = time.strftime("%Y-%m-%d")
log_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logpath = os.path.join(log_dir,"WX_Log")

class Log(object):
    #封装logging模块
    def __init__(self):
        self.log_path = os.path.join(logpath,"{}.log".format(now))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        #Logger:日志 LogRecord:日志记录器 Handler:处理器 Filter:过滤器 Formatter:格式化器
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')

    def __console(self,level,message):
        #创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.log_path,"a",encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        #避免日志输出重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()

    def info(self,message):
        self.__console("info",message)

    def debug(self,message):
        self.__console("debug",message)

    def warning(self,message):
        self.__console("warning",message)

    def error(self,message):
        self.__console("error",message)

    def log(self,message):
        logging.log(level=logging.DEBUG,msg=message,exc_info=True)

def create_logger():
    logger = logging.getLogger("err_log")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(now+"err.log")
    fmt = "\n[%(asctime)s-%(name)s-%(levelname)s]:%(message)s"
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def log_exception(fn):
    #当报错时，把错误写入log文件
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        logger = create_logger()
        try:
            fn(*args,**kwargs)
        except Exception as e:
            logger.exception("[Error in {}] msg: {}".format(__name__,str(e)))
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
