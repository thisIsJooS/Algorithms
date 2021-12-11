# O(V^2)

import sys

input = sys.stdin.readline

# 노드의 개수, 간선의 개수, 시작 노드 번호를 입력받기
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    

INF = int(1e9)
visited = [False] * (n+1)
distance = [INF] * (n+1)


# 방문하지 않는 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    
    for i in range(1, n+1):
        if not visited[i] and min_value > distance[i]:
            min_value = distance[i]
            index = i
            
    return index



def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            distance[j[0]] = min(cost, distance[j[0]])
            
        
dijkstra(start)

print(distance[1:])


# 입력예시 1
# 6 11 
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# 출력예시 1
# 0 2 3 1 2 4