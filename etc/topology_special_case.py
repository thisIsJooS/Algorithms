# 위상 정렬은 2가지 특이 케이스가 존재한다.
# 1. 사이클이 존재하는 경우
# 2. 위상 정렬의 결과가 1개가 아니라 여러가지인 경우
# 3. 위 2가지 경우에 해당하지 않는다면 위상정렬을 수행한 결과는 오직 하나

from collections import deque
N = 10

def check(graph):
    inDeg = [0] * (N+1)
    inDeg[0] = -1
    for i in range(1, N+1):
        for j in graph[i]:
            inDeg[j] += 1
            
    q = deque()
    for i in range(1, N+1):
        if inDeg[i] == 0:
            q.append(i)

    certain = True
    cycle = False
    
    for _ in range(N):
        if len(q) == 0:
            cycle = True
            break
        
        if len(q) >= 2:
            certain = False
            break
        
        now = q.popleft()
        
        for j in graph[now]:
            inDeg[j] -= 1
            if inDeg[j] == 0:
                q.append(j)

    
    if cycle:
        return 2
    elif not certain:
        return 1
    else:
        return 0