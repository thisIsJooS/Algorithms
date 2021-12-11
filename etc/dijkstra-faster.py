# O(E logV)

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드 번호를 입력받기
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    

distance = [INF] * (n+1)
path = [start] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
            
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                path[j[0]] = now
                heapq.heappush(q, (cost, j[0]))
    
    
    
dijkstra(start)

print(distance[1:])



# 최종 경로를 출력하기 위한 코드
for end in range(1, n+1):
    if end != start:
        print("[최단경로 : %d -> %d] %d" % (start, end, end), end = '')
    
        while path[end] != start:
            print(" <- %d" % path[end], end = '')
            end = path[end]
            
        print(" <- %s" % path[end])

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
# [최단경로 : 1 -> 2] 2 <- 1
# [최단경로 : 1 -> 3] 3 <- 5 <- 4 <- 1
# [최단경로 : 1 -> 4] 4 <- 1
# [최단경로 : 1 -> 5] 5 <- 4 <- 1
# [최단경로 : 1 -> 6] 6 <- 5 <- 4 <- 1