"""

NAME : dfs

USER : admin

DATE : 10/11/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""

# 定义一个无向图的邻接列表表示
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# 执行DFS
start_node = 'A'
visited = set()  # 用于存储已经访问过的节点
print("DFS starting from node", start_node)
dfs(graph, start_node, visited)
