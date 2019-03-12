# -*-coding:utf-8 -*-
'''
Created on

@author: zhy
'''
import logging
import time


class My_Log(object):
    ''' 将log封装成独立的模块，供其他模块进行调用'''

    def __init__(self):
        ''' 构造函数'''
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.INFO)
        
        #创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y-%m-%d")
        self.log_path = "../log"
        self.log_name = self.log_path + self.log_time + "log.log"
        
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8') 
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()
        
        
    def get_logger(self):
        return self.logger
    
    
    
    
    
    