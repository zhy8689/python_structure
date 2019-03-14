# -*-coding:utf-8 -*-
'''
Created on 2019年3月14日21:42:14

@author: Administrator
'''

class Node(object):
    ''' 二叉树的节点信息  '''


    def __init__(self, item):
        ''' 构造函数  '''
        self.item = item
        self.left = None
        self.right = None
