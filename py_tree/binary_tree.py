# -*-coding:utf-8 -*-
'''
Created on 2019年3月14日21:42:14

@author: Administrator
'''
#from py_tree import Node

class Node(object):
    ''' 二叉树的节点信息  '''


    def __init__(self, item):
        ''' 构造函数  '''
        self.item = item
        self.left = None
        self.right = None
        
        
class BinaryTree(object):
    ''' 二叉树结构  '''
    def __init__(self, node = None):
        ''' 构造函数 '''
        self._root = node
    
    
    def add(self, item):
        ''' 向二叉树中添加元素 '''
        node = Node(item)
        if self._root == None:
            self._root = node
        else:
            quene = []
            quene.append(self._root)
            while len(quene) > 0:
                cur_node = quene.pop(0)
                if cur_node.left == None:
                    cur_node.left = node
                    break
                elif cur_node.right == None:
                    cur_node.right = node
                    break
                else:
                    quene.append(cur_node.left)
                    quene.append(cur_node.right)
                    
    
    def pre_order(self, node):
        ''' 使用递归的方式实现二叉树的先序遍历  '''
        if node == None:
            return 
        print(node.item, end = " ")
        self.pre_order(node.left)
        self.pre_order(node.right)
    
    
    def in_order(self, node):
        ''' 使用递归的方式实现二叉树中序遍历 '''
        if node == None:
            return 
        self.pre_order(node.left)
        print(node.item, end = " ")
        self.pre_order(node.right)
    
    
    def post_order(self, node):
        ''' 使用递归的方式实现二叉树的后序遍历 '''
        if node == None:
            return 
        self.pre_order(node.left)
        self.pre_order(node.right)
        print(node.item, end = " ")
    
    
    def level_order(self, root):
        ''' 使用递归的方式实现二叉树的层序遍历 '''
        if self._root == None:
            return
        queue = []
        queue.append(self._root)
        while len(queue) > 0:
            cur_node = queue.pop(0)
            print(cur_node.item, end = " ")
            if cur_node.left != None:
                queue.append(cur_node.left)
            if cur_node.right != None:
                queue.append(cur_node.right)
        
    
    def get_root(self):
        ''' 获取二叉树的根节点 '''
        return self._root
    
    
if __name__ == "__main__":
    tree = BinaryTree()
    for item in range(10):
        tree.add(item)
    print("\n**************pre_order*******************\n")
    tree.pre_order(tree.get_root())
    print("\n**************in_order********************\n")
    tree.in_order(tree.get_root())
    print("\n**************post_order******************\n")
    tree.post_order(tree.get_root())
    print("\n**************level_order*****************\n")
    tree.level_order(tree.get_root)
    
    