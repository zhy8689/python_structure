
# -*-coding:utf-8 -*-
'''
Created on 2019��3��15��

@author: zhy
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。 
输入描述:   一行字符串，非空，长度小于5000。

输出描述:   整数N，最后一个单词的长度。

示例1
输入  hello world
输出  5
'''
# s = input()
# print(len(s.split(' ')[-1]))

#写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
# str = input()
# str = str.lower()  
# word = input()
# word = word.lower()
# print(str.count(word))



num = int(input())
l = [int(input()) for _ in range(num)]
l2 = sorted(set(l))
   
for i in l2:
    print(i)
