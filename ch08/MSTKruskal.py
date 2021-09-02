# MST - Kruskal's Algorithm

class disjointSets:
  def __init__(self, n):
    self.parent = [-1]*n
    self.set_size = n
    
  def find(self, id):
    while(self.parent[id] >= 0):
      id = self.parent[id]
    return id
  
  def union(self, s1, s2):
    self.parent[s1] = s2
    self.set_size -= 1
    
def MSTKruskal(V, adj):
  n = len(V)
  dsets = disjointSets(n)
  E = []
  
  for i in range(n-1):
    for j in range(i+1, n):
      if adj[i][j] != None:
        E.append( (i, j, adj[i][j]) )
  
  E.sort(key = lambda e:e[2])
  
  ecount = 0
  
  for e in E:
    uset = dsets.find(e[0])
    vset = dsets.find(e[1])
    
    if uset != vset:
      dsets.union(uset, vset)
      print("간선 추가 : (%s, %s, %d)" % (V[e[0]], V[e[1]], e[2]))
      ecount += 1
      
      if ecount == n-1:
        break

vertex=['A','B','C','D','E','F','G']
adj=[
  [None, 29, None, None, None, 10, None],
  [29, None, 16, None, None, None, 15],
  [None, 16, None, 12, None, None, None],
  [None, None, 12, None, 22, None, 18],
  [None, None, None, 22, None, 27, 25],
  [10, None, None, None, 27, None, None],
  [None, 15, None, 18, 25, None, None]
]

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, adj)

#############################
# 결과
# MST By Kruskal's Algorithm
# 간선 추가 : (A, F, 10)
# 간선 추가 : (C, D, 12)
# 간선 추가 : (B, G, 15)
# 간선 추가 : (B, C, 16)
# 간선 추가 : (D, E, 22)
# 간선 추가 : (E, F, 27)
#############################