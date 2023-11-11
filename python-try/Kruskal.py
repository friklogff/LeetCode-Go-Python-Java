"""

NAME : Kruskal

USER : admin

DATE : 10/11/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""
# 定义一个带权的无向图的边集合，每个边表示为(节点1, 节点2, 权重)
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'D', 2),
    ('B', 'E', 7),
    ('C', 'F', 5),
    ('E', 'F', 3)
]

def kruskal(graph):
    def find(parent, node):
        if parent[node] != node:
            parent[node] = find(parent, parent[node])
        return parent[node]

    def union(parent, rank, node1, node2):
        root1 = find(parent, node1)
        root2 = find(parent, node2)

        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1

    edges.sort(key=lambda edge: edge[2])  # 按权重升序排序边

    minimum_spanning_tree = []
    parent = {}
    rank = {}

    for node1, node2, weight in edges:
        if node1 not in parent:
            parent[node1] = node1
            rank[node1] = 0
        if node2 not in parent:
            parent[node2] = node2
            rank[node2] = 0

        if find(parent, node1) != find(parent, node2):
            minimum_spanning_tree.append((node1, node2, weight))
            union(parent, rank, node1, node2)

    return minimum_spanning_tree

# 执行Kruskal算法
minimum_spanning_tree = kruskal(edges)

# 输出最小生成树的边和权重
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
