# -*-coding:utf-8 -*-

'''
Created on 2019年3月9日
@author: zhy
'''
from log import log_tool
log = log_tool.My_Log().get_logger()

class Node(object):
    '''  单链表的节点描述   '''
    def __init__(self, item):
        self.item = item
        self.next = None
        
    def get_item(self):
        ''' 获取单链表的节点值 '''
        return self.item
    
    def get_next_item(self):
        ''' 获取当前节点的下一个节点值'''
        return self.next
    

    def set_next_item(self, item):
        ''' 给当前节点添加next节点 '''
        self.next = item
        
    
  
class Single_Link(object):
    ''' python实现单链表 '''


    def __init__(self):
        '''  单链表的构造函数  '''
        self.__head = None
        
    def is_node_type(self, item):
        '''  判断传入的参数是否为一个Node类型  '''
        if not isinstance(item, Node):
            temp_node = Node(item)
        else:
            temp_node = item
        return temp_node
    
    
    def is_empty(self):
        ''' 判断单链表是否为空  '''
        return self.__head == None
    
    
    def get_size(self):
        ''' 获取单链表的长度 '''
        cur_node = self.__head
        count = 1
        while not self.is_empty() and cur_node.get_next_item() != None:
            count += 1
            cur_node = cur_node.get_next_item()
        log.info("the length of current single_link is ：%d"%count)
        return count
    
    
    def add_from_head(self, item):
        ''' 单链表的头插法添加元素 '''
        node = self.is_node_type(item)
        node.set_next_item(self.__head)
        self.__head = node
        log.info("add node from head ,value is %d"%node.item)

      
    def add_from_tail(self, item):
        ''' 单链表的尾插法添加元素 '''
        node = Node(item)
        if self.__head == None:
            self.__head = node
        else:
            cur_node = self.__head
            while cur_node.get_next_item() != None:
                cur_node = cur_node.get_next_item()
            cur_node.set_next_item(node)
        log.info("add node from tail ,value is %d"%node.item)
    
    def insert(self, position, item):
        ''' 向单链表中的某个位置插入一个元素 '''
        node = self.is_node_type(item)
        if position > self.get_size():
            self.add_from_tail(node)
        elif position <= 1:
            self.add_from_head(node)
        else:
            pre = None
            count = 1
            cur_node = self.__head
            
            while count < position:
                count+=1
                pre = cur_node
                cur_node = cur_node.get_next_item()
                
            pre.set_next_item(node)
            node.set_next_item(cur_node)
            
    
    def travle(self):
        '''  遍历单链表中的元素 '''
        cur_node = self.__head
        while cur_node != None:
            print(cur_node.get_item())
            cur_node = cur_node.get_next_item() 
    
    
    def remove(self, item):
        ''' 删除单链表中的某个元素 '''
        cur_node = self.__head
        pre = None
        
        while cur_node != None:
            if cur_node.get_item() == item:
                if pre == None:
                    self.__head = cur_node.get_next_item()
                else:
                    pre.set_next_item(cur_node.get_next_item())
                break
            else:
                pre = cur_node
                cur_node = cur_node.get_next_item()    
    
    
    def search(self, item):
        ''' 在单链表中查找某个具体的元素 '''
        cur_node = self.__head
        count = 0
        found = False
        while found == False and cur_node != None:
            count += 1
            if cur_node.get_item() == item:
                found = True
            else:
                cur_node = cur_node.get_next_item()
        if found == True:
            return count
        
        else:
            log.info("%s is not in this single_link"%item)
            
    
    
if __name__ == "__main__":
    single_node = Single_Link()
    
    single_node.add_from_tail(55)
    single_node.add_from_tail(66)
    single_node.add_from_tail(77)
    single_node.insert(1,30)
    print(single_node.get_size())
    print(single_node.travle())
    print(single_node.search(66))
    
    single_node.remove(66)
    print(single_node.travle())
    
    
        