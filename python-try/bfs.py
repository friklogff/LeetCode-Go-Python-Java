"""

NAME : bfs

USER : admin

DATE : 10/11/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""
from collections import deque

# 定义一个无向图的邻接列表表示
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    visited = set()  # 用于存储已经访问过的节点
    queue = deque()  # 用于存储待访问的节点

    visited.add(start)  # 将起始节点加入已访问集合
    queue.append(start)  # 将起始节点加入队列

    while queue:
        node = queue.popleft()  # 从队列中取出一个节点
        print(node, end=' ')

        # 遍历该节点的邻居节点
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 从节点'A'开始执行BFS
start_node = 'A'
print("BFS starting from node", start_node)
bfs(graph, start_node)

