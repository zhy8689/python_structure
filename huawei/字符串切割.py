# -*-coding:utf-8 -*-
'''
Created on 2019��3��16��

@author: Administrator
'''

def cut_str(str):
    ''' 
    •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组； 
    •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。 
    '''
    if len(str)>0 and len(str)<8:
        str += '0' * (8 - len(str))
        print(str)
    elif len(str) == 8:
        print(str)
    elif len(str) > 8:
        print(str[:8])
        cut_str(str[8:])
       
while True:
    try:
        str = input()
        cut_str(str)
    except:
        break