# -*-coding:utf-8 -*-
'''
Created on 2019年3月17日08:04:51

@author: Administrator
'''


Graph = {'A':  ['B', 'C', 'D'],                        # 构建树
             'B':  ['E'],
             'C':  ['D', 'F'],
             'D':  ['B', 'E', 'G'],
             'E':  [],
             'F':  ['D', 'G'],
             'G':  ['E']}
def search_graph(graph, start, end):
    ''' 实现搜索树 '''
    results = []
    generatePath(graph, start, end, results)
    results.sort(key=lambda x:len(x))
    return results


def generatePath(graph, path, end, results):
    ''' 从图结构中找出所以的路径 '''
    start = path[-1]
    if start == end:
        results.append(path)
    else:
        for node in graph[start]:
            if node not in path:
                generatePath(graph, path + node, end, results)
                
if __name__ == "__main__":
    results = search_graph(Graph, 'A', 'D') 

    for i in results:
        print(i)