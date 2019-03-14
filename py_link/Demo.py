# -*-coding:utf-8 -*-

'''
Created on 2019年3月13日
@author: zhy
'''

'''
    对于一个链表，请设计一个时间复杂度为O(n),额外空间复杂度为O(1)的算法，判断其是否为回文结构。
    给定一个链表的头指针A，请返回一个bool值，代表其是否为回文结构。保证链表长度小于等于900。
    测试样例：
    1->2->2->1
    返回：true
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None 

class PalindromeList:
    def chkPalindrome(self, A):
        # write code here 
        cur_node = A
        list = []
        while cur_node != None:
            list.append(cur_node.val)
            cur_node = cur_node.next
        
        return True if list == list[::-1] else False
    

if __name__ == '__main__':
    pass