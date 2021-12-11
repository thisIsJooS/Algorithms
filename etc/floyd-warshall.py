import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())    # 노드의 수
m = int(input())    # 간선의 수

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자시능로 가는 비용은 0 으로 초기화
for i, j in zip(range(1, n+1), range(1, n+1)):
    graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    

# 점화식에 따라 floyd-warshall 알고리즘을 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for g in graph[1:]:
    print(g[1:])
    
    

# 입력예시 1
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

# 출력예시 1
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0