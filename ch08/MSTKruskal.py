# MST - Kruskal's Algorithm

#서로소 집합
class disjointSets:
  def __init__(self, n):
    self.parent = [-1]*n   # 각 노드는 모두 루트 노드
    self.set_size = n
    
  def find(self, id):  # 정점 id가 속한 집합의 대표번호 탐색
    while(self.parent[id] >= 0):  # 부모가 있으면
      id = self.parent[id]  # id를 부모 id로 갱신
    return id  #루트노드 반환
  
  def union(self, s1, s2):  # 두 집합을 병합한다. s1을 s2에 병합시킨다.
    self.parent[s1] = s2
    self.set_size -= 1
    
def MSTKruskal(V, adj):
  n = len(V)
  dsets = disjointSets(n)
  E = []  # 간선 리스트
  
  for i in range(n-1):  # 모든 간선을 리스트에 넣는다
    for j in range(i+1, n):
      if adj[i][j] != None:
        E.append( (i, j, adj[i][j]) )
  
  E.sort(key = lambda e:e[2])  # 간선 리스트 E를 가중치를 중심으로 오름차순으로 정렬한다.
  
  ecount = 0  #MST에 포함된 간선의 수 
  
  for e in E:
    uset = dsets.find(e[0])  #간선의 양쪽 정점이 속한 집합의 루트를 뽑는다.
    vset = dsets.find(e[1])
    
    if uset != vset:
      dsets.union(uset, vset)
      print("간선 추가 : (%s, %s, %d)" % (V[e[0]], V[e[1]], e[2]))
      ecount += 1
      
      if ecount == n-1:  # 만약 n-1개를 MST에 넣었으면 완료된 것이다.
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