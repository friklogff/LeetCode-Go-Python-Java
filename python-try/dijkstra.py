"""

NAME : dijkstra

USER : admin

DATE : 10/11/2023

PROJECT_NAME : README.md

CSDN : friklogff
"""
import heapq

# 定义一个加权有向图的邻接列表表示
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 7},
    'C': {'A': 4, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 7, 'F': 3},
    'F': {'C': 5, 'E': 3}
}

def dijkstra(graph, start):
    # 创建一个字典来存储从起始节点到其他节点的最短距离
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 创建一个优先队列（最小堆），用于按距离排序节点
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果当前节点的距离大于已知的最短距离，跳过
        if current_distance > distances[current_node]:
            continue

        # 遍历当前节点的邻居节点
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 如果通过当前节点到邻居节点的距离更短，更新距离
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 执行Dijkstra算法
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

# 输出从起始节点到每个节点的最短距离
for node, distance in shortest_distances.items():
    print(f'Shortest distance from {start_node} to {node} is {distance}')
