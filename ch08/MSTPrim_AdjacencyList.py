# Prim's MST Algorithm

vertex = ['A','B','C','D','E','F','G']
adj = [
  [None, 29, None, None, None, 10, None],
  [29, None, 16, None, None, None, 15],
  [None, 16, None, 12, None, None, None],
  [None, None, 12, None, 22, None, 18],
  [None, None, None, 22, None, 27, 25],
  [10, None, None, None, 27, None, None],
  [None, 15, None, 18, 25, None, None]
]

INF=9999

# dist 배열에서 최소 가중치를 가진 정점을 찾는 함수. 배열의 인덱스 값을 리 한다.
def getMinVertex(dist, selected):
  minv=-1
  mindist=INF
  
  for v in range(len(dist)):
    if not selected[v] and dist[v] < mindist:
      minv = v
      mindist = dist[v]
  
  return minv

def MSTPrim(vertex, adj):
  vsize = len(vertex)
  dist = [INF]*vsize
  dist[0] = 0
  selected = [False]*vsize
  
  for i in range(vsize):  # 정점의 수 만큼 반복
    u = getMinVertex(dist, selected)
    selected[u] = True  # u는 이제 선택됨
    print(vertex[u], end = ':')
    print(dist)
    
    for v in range(vsize):
      if adj[u][v] != None:  #(u, v) 간선이 있을 떄
        if selected[v] == False and adj[u][v] < dist[v]: # 그 정점이 선택되지 않았고, 가중치가 dist[v]보다 작으면 갱신
          dist[v] = adj[u][v]

print("MST By Prim's Algorithm")
MSTPrim(vertex, adj)


################################################
# 결과
#
# MST By Prim's Algorithm
# A:[0, 9999, 9999, 9999, 9999, 9999, 9999]
# F:[0, 29, 9999, 9999, 9999, 10, 9999]
# E:[0, 29, 9999, 9999, 27, 10, 9999]
# D:[0, 29, 9999, 22, 27, 10, 25]
# C:[0, 29, 12, 22, 27, 10, 18]
# B:[0, 16, 12, 22, 27, 10, 18]
# G:[0, 16, 12, 22, 27, 10, 15]
################################################