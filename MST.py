vertex=['A','B','C','D','E','F','G']
weight=[
  [None, 29, None, None, None, 10, None],
  [29, None, 16, None, None, None, 15],
  [None, 16, None, 12, None, None, None],
  [None, None, 12, None, 22, None, 18],
  [None, None, None, 22, None, 27, 25],
  [10, None, None, None, 27, None, None],
  [None, 15, None, 18, 25, None, None]
]

INF=9999

def getMinVertex(dist, selected):
  minv=-1
  mindist=INF
  
  for v in range(len(dist)):
    if not selected[v] and dist[v]<mindist:
      minv=v
      mindist=dist[v]
  
  return minv

def MSTPrim(vertex, adj):
  vsize=len(vertex)
  dist=[INF]*vsize
  dist[0]=0
  selected=[False]*vsize
  
  for i in range(vsize):
    u = getMinVertex(dist, selected)
    selected[u]=True
    print(vertex[u], end=':')
    print(dist)
    
    for v in range(vsize):
      if adj[u][v]!=None:
        if selected[v]==False and adj[u][v]<dist[v]:
          dist[v]=adj[u][v]

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)


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