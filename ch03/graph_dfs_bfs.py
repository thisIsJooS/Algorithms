import queue

graph={
  "A":{"B","C"},
  "B":{"A","D"},
  "C":{"A","D","E"},
  "D":{"B","C","F"},
  "E":{"C","G","H"},
  "F":{"D"},
  "G":{"E","H"},
  "H":{"E","G"}
}

# 깊이 우선 탐색
def dfs(graph, start, visited):
  if start not in visited:
    visited.add(start)
    print(start, end=' ')
    nbr=graph[start]-visited
    for v in nbr:
      dfs(graph, v, visited)
      
print('DFS : ', end='')
dfs(graph, "A", set())
print()

# 너비 우선 탐색
def bfs(graph, start):
  visited={start}
  que=queue.Queue()
  que.put(start)
  while not que.empty():
    v=que.get()
    print(v, end=" ")
    nbr=graph[v]-visited
    for u in nbr:
      visited.add(u)
      que.put(u)

print('BFS : ',end='')
bfs(graph, "A")
print()


############################################################################
# 결과 - 딕셔너리는 순서가 없으므로 실핼할 때 마다 결과가 달라진다. 그렇다고 틀린 건 아니다.
# DFS : A C E G H D F B
# BFS : A C B E D G H F
############################################################################