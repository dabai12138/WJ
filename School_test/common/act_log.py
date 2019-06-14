# -*- coding:utf-8
# Author:wangjian

#打印log日志

import logging,time,os
import functools
now = time.strftime("%Y-%m-%d")+"错误日志"
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
        elif level == "exception":
            self.logger.exception(message)
        elif level == "error":
            self.logger.error(message)

        #避免日志输出重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()
    #打印info信息
    def info(self,message):
        self.__console("info",message)
    #打印debug信息
    def debug(self,message):
        self.__console("debug",message)
    #打印warning信息
    def warning(self,message):
        self.__console("warning",message)
    #打印exception信息
    def exception(self,message):
        self.__console("exception",message)
    #打印error信息
    def error(self,message):
        self.__console("error",message)

    def log(self,message):
        logging.log(level=logging.DEBUG,msg=message,exc_info=True)

if __name__ == "__main__":
    Log()
