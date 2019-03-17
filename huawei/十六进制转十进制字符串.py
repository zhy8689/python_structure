# -*-coding:utf-8 -*-

'''
Created on 2019年3月16日22:19:40

@author: Administrator
@description:写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）
'''
while True:
    try:
        str = input()
        num = int(str,16)
        print(num)
    except:
        break
    