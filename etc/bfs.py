from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


def bfs(graph, start):
    q = deque()
    
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
        print(now, end = ' ')
        
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
            
            
visited = [False] * len(graph)

bfs(graph, 1)