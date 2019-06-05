# -*- coding:utf-8 -*-
# Author:wangjian


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Tools import HTMLTestRunner
from multiprocessing import Process,Manager,Value,Lock,Pipe,Queue
import multiprocessing
from threading import Thread
from tomorrow import threads
import unittest
import smtplib
import sys,os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"common"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Test_case"))


curr_path = os.path.dirname(os.path.abspath(__file__))
discover = []
rule = ["ad*.py","stu*.py","test*.py"]

def add_case(rule,caseName="Test_case\Test_UI"):
    """用例添加"""
    case_path = os.path.join(curr_path,caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover

def run_case(suite,reportName="report"):
    """执行用例，生成报告"""
    report_path = os.path.join(curr_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    result_path = os.path.join(report_path,"result.html")
    print("report_path:%s"%result_path)
    fp = open(result_path,"wb")
    mu = []
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                title=u"自动化测试报告",
                                description=u"用例执行情况：")
        m = Thread(target=runner.run,args=(i,))
        mu.append(m)
    for i in mu:
        i.start()
    for i in mu:
        i.join()
    fp.close()

def get_new_report_file(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print(u"最新生成报告：%s"%lists[-1])
    report_file = os.path.join(report_path,lists[-1])
    return report_file

def send_mail(sender,psw,receiver,smtpserver,report_file,port):
    """发送邮件"""
    with open(report_file,"rb") as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype='html',_charset="utf-8")
    body["Content-Type"] = 'application/octet-stream'
    body.add_header('Content-Disposition', 'attachment', filename='report.html')
    text_info = u"测试报告附件："
    text_sub = MIMEText(text_info,'plain', 'utf-8')
    msg.attach(text_sub)
    msg['Subject'] = u"自动化测试报告"
    msg['from'] = sender
    # msg['to'] = ",".join(receiver)
    msg['to'] = receiver
    msg.attach(body)
    try:
        smtp = smtplib.SMTP(smtpserver,25)
        # smtp.connect(smtpserver)
        smtp.login(sender,psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("test_report email has send out!")
if __name__ == "__main__":
    adcase = add_case(rule[0])
    stucase = add_case(rule[1])
    for i in adcase:
        discover.append(i)
    for j in stucase:
        discover.append(j)
    run_case(discover)

    #发送邮件
    # report_path = os.path.join(curr_path, "report")
    # report_file = get_new_report_file(report_path)
    # send_mail(sender="977653367@qq.com",psw="tegqsdxhdwyzbejf",receiver="3339496459@qq.com",
    #           smtpserver="smtp.qq.com",report_file=report_file,port=465)
