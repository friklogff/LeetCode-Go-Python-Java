"""

NAME : floyd

USER : admin

DATE : 10/11/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""
# 定义一个有向带权图的邻接矩阵表示，使用无穷大表示不可达
inf = float('inf')
graph = [
    [0, inf, 3, inf, inf],
    [2, 0, inf, inf, 1],
    [inf, inf, 0, 5, inf],
    [inf, inf, inf, 0, 2],
    [inf, 6, inf, inf, 0]
]

def floyd_warshall(graph):
    num_nodes = len(graph)

    # 初始化距离矩阵
    distances = [row[:] for row in graph]

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

# 执行Floyd-Warshall算法
shortest_distances = floyd_warshall(graph)

# 输出所有节点对之间的最短距离
num_nodes = len(graph)
for i in range(num_nodes):
    for j in range(num_nodes):
        print(f'Shortest distance from node {i} to node {j} is {shortest_distances[i][j]}')
