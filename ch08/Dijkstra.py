# Dijkstra's Algorithm - 한 정점에서 출발하여 다른 모든 정점으로 가는 최단거리를 찾는다.

# dist 배열에서 최소 가중치를 가진 정점을 찾는 함수. 배열의 인덱스 값을 리 한다.
def getMinVertex(dist, selected):
  minv=-1
  mindist=INF
  
  for v in range(len(dist)):
    if not selected[v] and dist[v] < mindist:
      minv = v
      mindist = dist[v]
  
  return minv

def shortest_path_dijkstra(vertex, adj, start):
  vsize = len(vertex)
  dist = list(adj[start])
  dist[start] = 0
  path = [start] * vsize  # 바로 이전 정점을 저장하는 배열
  found = [False] * vsize
  found[start] = True
  
  for i in range(vsize):
    print("Step%2d : " %(i+1), dist)
    u = getMinVertex(dist, found)
    found[u] = True
    
    for w in range(vsize):
      if not found[w]:
        if dist[u] + adj[u][w] < dist[w]:
          dist[w] = dist[u] + adj[u][w]
          path[w] = u
    
  return path  # 찾아진 최단경로 반환

vertex = ['A','B','C','D','E','F','G']

INF = 9999

adj = [
  [0, 7, INF, INF, 3, 10, INF],
  [7, 0, 4, 10, 2, 6, INF],
  [INF, 4, 0, 2, INF, INF, INF],
  [INF, 10, 2, 0, 11, 9, 4],
  [3, 2, INF, 11, 0, 13, 5],
  [10, 6, INF, 9, 13, 0, INF],
  [INF, INF, INF, 4, 5, INF, 0]
]

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, adj, start)

# 최종 경로를 출력하기 위한 코드
for end in range(len(vertex)):
  if end != start:
    print("[최단경로 : %s -> %s] %s" % (vertex[start], vertex[end], vertex[end]), end='')
    while(path[end] != start):
      print(" <- %s" % vertex[path[end]], end='' )
      end = path[end]
    print(" <- %s" % vertex[path[end]])

############################################
# 결과
#
# Shortest Path By Dijkstra Algorithm
# Step 1 :  [0, 7, 9999, 9999, 3, 10, 9999]
# Step 2 :  [0, 5, 9999, 14, 3, 10, 8]
# Step 3 :  [0, 5, 9, 14, 3, 10, 8]
# Step 4 :  [0, 5, 9, 12, 3, 10, 8]
# Step 5 :  [0, 5, 9, 11, 3, 10, 8]
# Step 6 :  [0, 5, 9, 11, 3, 10, 8]
# Step 7 :  [0, 5, 9, 11, 3, 10, 8]
# [최단경로 : A -> B] B <- E <- A
# [최단경로 : A -> C] C <- B <- E <- A
# [최단경로 : A -> D] D <- C <- B <- E <- A
# [최단경로 : A -> E] E <- A
# [최단경로 : A -> F] F <- A
# [최단경로 : A -> G] G <- E <- A
############################################