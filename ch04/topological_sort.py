directedGraph = {
  'A' : {'C', 'D'},
  'B' : {'D', 'E'},
  'C' : {'D', 'F'},
  'D' : {'F'},
  'E' : {'F'},
  'F' : {}
}

def topologicalSort_DAC(graph):
  inDeg = {}

  for v in graph:
    inDeg[v] = 0
  
  for v in graph:
    for u in graph[v]:
      inDeg[u] += 1
  
  vlist = []

  for v in graph:
    if inDeg[v] == 0 :
      vlist.append(v)
  
  while vlist:
    v = vlist.pop()
    print(v, end = ' ')
    
    for u in graph[v]:
      inDeg[u] -= 1
      if inDeg[u] == 0:
        vlist.append(u)

topologicalSort_DAC(directedGraph)
print()

###############
# 결과
#
# B E A C D F
################




def topologicalSort_DFS(graph):
  inDeg = {}
  starts = []
  
  for v in graph:
    inDeg[v] = 0
    
  for v in graph:
    for u in graph[v]:
      inDeg[u] += 1
  
  for v in graph:
    if inDeg[v] == 0:
      starts.append(v)
      
  for start in starts:
    dfs(graph, start, [], inDeg)


def dfs(graph, v, visited, inDeg):
  if v not in visited:
    visited.append(v)
    print(v, end = ' ')
    
    for u in graph[v]:
      inDeg[u] -= 1
    
    for u in graph[v]:
      if inDeg[u] == 0:
        dfs(graph, u, visited, inDeg)
        
topologicalSort_DFS(directedGraph)
print()



###############
# 결과
#
# A C B E D F
################