import queue

graph={
  "A" : {"B", "C"},
  "B" : {"A", "D"},
  "C" : {"A", "D", "E"},
  "D" : {"B", "C", "F"},
  "E" : {"C", "G", "H"},
  "F" : {"D"},
  "G" : {"E", "H"},
  "H" : {"E", "G"}
}

# Depth First Search
def dfs(graph, start, visited):
  if start not in visited:
    visited.add(start)
    print(start, end=' ')
    nbr = graph[start] - visited
    
    for v in nbr:
      dfs(graph, v, visited)
      

# Breadth First Search
def bfs(graph, start):
  visited = { start }
  que = queue.Queue()
  que.put(start)
  
  while not que.empty():
    v = que.get()
    print(v, end = " ")
    nbr = graph[v] - visited
    for u in nbr:
      visited.add(u)
      que.put(u)


# 알고리즘 테스트

print('DFS : ', end='')
dfs(graph, "A", set())
print()

print('BFS : ',end='')
bfs(graph, "A")


############################################################################
# 결과 - 딕셔너리는 순서가 없으므로 실핼할 때 마다 결과가 달라진다. 그렇다고 틀린 건 아니다.
#
# DFS : A C E G H D F B
# BFS : A C B E D G H F
############################################################################