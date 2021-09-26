directedGraph = {
  'A' : {'C', 'D'},
  'B' : {'D', 'E'},
  'C' : {'D', 'F'},
  'D' : {'F'},
  'E' : {'F'},
  'F' : {}
}

def topological_sort(graph):
  degrees = {}

  for v in graph:
    degrees[v] = 0
  
  for v in graph:
    for u in graph[v]:
      degrees[u] += 1
  
  vlist = []

  for v in graph:
    if degrees[v] == 0 :
      vlist.append(v)
  
  while vlist:
    v = vlist.pop()
    print(v)
    for u in graph[v]:
      degrees[u] -= 1
      if degrees[u] == 0:
        vlist.append(u)

topological_sort(directedGraph)
print() 