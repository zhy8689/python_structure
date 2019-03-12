# -*-coding:utf-8 -*-

'''
Created on 2019��3��10��

@author: Administrator
'''
from log import log_tool
log = log_tool.My_Log().get_logger()

from log import log_tool
log = log_tool.My_Log().get_logger()

class Node(object):
    '''  双链表的节点描述   '''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
        
    def get_item(self):
        ''' 获取双链表的节点值 '''
        return self.item
    
    def get_next_item(self):
        ''' 获取当前节点的下一个节点值'''
        return self.next
    

    def get_prev_item(self):
        ''' 获取当前节点的前一个节点值'''
        return self.prev
    
    
    def set_next_item(self, item):
        ''' 给当前节点添加 next节点 '''
        self.next = item
        
    def set_prev_item(self, item):
        ''' 给当前节点添加前一个节点 '''
        self.prev = item
        
        
class Double_Link(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        