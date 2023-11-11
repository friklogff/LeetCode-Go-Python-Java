"""

NAME : Prim

USER : admin

DATE : 10/11/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""
# 定义一个带权的无向图的邻接列表表示
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 7)],
    'C': [('A', 4), ('F', 5)],
    'D': [('B', 2)],
    'E': [('B', 7), ('F', 3)],
    'F': [('C', 5), ('E', 3)]
}


def prim(graph):
    # 选择一个起始节点
    start_node = list(graph.keys())[0]

    # 创建一个集合用于存储已经包含在最小生成树中的节点
    included_nodes = set()
    # 创建一个列表用于存储最小生成树的边
    minimum_spanning_tree = []

    # 将起始节点添加到已包含的节点中
    included_nodes.add(start_node)

    while len(included_nodes) < len(graph):
        min_edge = None
        for node in included_nodes:
            for neighbor, weight in graph[node]:
                if neighbor not in included_nodes:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (node, neighbor, weight)

        if min_edge:
            minimum_spanning_tree.append(min_edge)
            included_nodes.add(min_edge[1])

    return minimum_spanning_tree


# 执行Prim算法
minimum_spanning_tree = prim(graph)

# 输出最小生成树的边和权重
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
