# -*-coding:utf-8 -*-
'''
Created on 2019年3月7日
@author: zhouhongyao

'''
from util import My_Log

log = My_Log().get_logger()

class Stack(object):
    '''  自定义栈结构  '''

    def __init__(self):
        '''  构造函数    '''
        self.list = []
        
    
    def is_empty(self):
        '''  判断栈是否为空    '''
        return True if len(self.list) == 0 else False
    
    
    def size(self):
        '''  获取栈中元素的个数    '''
        return len(self.list)
    
    
    def peek(self):
        ''' 获取栈顶元素  '''
        if not self.is_empty():
            return self.list[-1]
    
    
    def push(self, item):
        '''  向栈中添加元素  '''
        self.list.append(item)
    
    
    def pop(self):
        '''  从栈中取出一个栈顶元素  '''
        if not self.is_empty():
            return self.list.pop()
        
        
if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print("当前栈是否为空：%s"%stack.is_empty())
    print("当前栈中元素个数：%s"%stack.size())
    print("当前栈的栈顶元素：%s"%stack.peek())
    print("从当前栈中取出一个栈顶元素：%s"%stack.pop())
    
    