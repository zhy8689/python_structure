# -*-coding:utf-8 -*-

'''
Created on 2019��3��10��

@author: Administrator
'''
from log import log_tool
log = log_tool.My_Log().get_logger()

class Node(object):
    '''  双链表的节点描述   '''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
        
        
class Double_Link(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._head = None
        self._tail = None
        
    
    def add(self, item):
        ''' 向双链表中添加一个元素 '''
        
        node = Node(item)
        if self._head == None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
    
    
    def pop(self):
        ''''''
        if self._head == None:
            raise Exception("Current link has no node.......")
        cur_node = self._tail
        prev_node = self._tail.prev
        value = cur_node.item
        
        if prev_node == None:  
            self._head = None
            self._tail = None
        else:
            prev_node.next = None
            self._tail = prev_node
        
        return value
    
    
    def insert(self, index, item):
        ''''''
        cur_node = None
        
        for i, node in enumerate(self.iter_nodes()):
            if i == index:
                cur_node = node
                break
            
        if cur_node == None or index < 0:
            raise Exception("invalid index")
        
        node = Node(item)
        prev_node = cur_node.prev
        next_node = cur_node
        
        if prev_node == None:
            self._head = node
            node.next = next_node
            next_node.prev = node
        else:
            prev_node.next = node
            next_node.prev = node
            node.prev = prev_node
            node.next = next_node
            
            
    def remove(self, index):
        ''''''
        if self._tail == None:
            raise Exception("empty link")
        cur_node = None
        
        for i, node in enumerate(self.iter_nodes()):
            if i == index:
                cur_node = node
                break
            
        if cur_node == None or index < 0:
            raise Exception("invalid index")
        
        prev_node = cur_node.prev
        next_node = cur_node.next
    
        if prev_node == None and next_node == None:
            self._head = None
            self._tail = None
        elif prev_node == None:  #头节点
            self._head = next_node
            next_node.prev = None
        elif next_node == None:  #尾节点
            prev_node = None
            self._tail = prev_node
        else:  #中间节点
            prev_node.next = next_node
            next_node.prev = prev_node
            
        del cur_node
            
    def iter_nodes(self):
        ''' ''' 
        cur_node = self._head
        
        while cur_node:
            yield cur_node
            cur_node = cur_node.next
    
     
    def is_empty(self):
        '''判断双链表是否为空 '''
        return self._head == None
    
    
    def travle(self):
        ''' 遍历整个链表，将列表元素打印处理 '''
        if not self.is_empty():
            cur_node = self._head
            while cur_node.next != None:
                print("%s"%cur_node.item)
                cur_node = cur_node.next
        else:
            print("empty link")
        
    
    
if __name__ == "__main__":
    link = Double_Link()
    for item in range(10):
        link.add(item)
    
    link.insert(2, 30)
    link.remove(2)
    link.travle()
    
    
    
    