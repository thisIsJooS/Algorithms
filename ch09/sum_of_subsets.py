# 집합 S의 부분집합 중에 원소의 합이 M이 되는 모든 가능한 부분집합 탐색 - 백트래킹 이용

def all_sum_of_subsets(S, M):
  f(S, M, 0, [], sum(S))


def DFS_sum_of_subsets(S, M, level, sol, remaining):  # remaining : 현재 해에 선택되지 않고 남은 집합 S의 모든 숫자들의 합
  if sum(sol) == M:
    print(sol)
    return  # 백트래킹
  
  # 추가적인 백트래킹 조건
  if sum(sol) > M or remaining + sum(sol) < M:  # 부분해가 이미 M보다 크거나, 부분해에 S의 남은 원소를 다 더해도 M보다 작은 경우 더 탐색할 필요가 없음
    return # 백트래킹
  
  for i in range(level, len(S)): # index 이후의 모든 숫자에 대해
    sol.append(S[i])  # 현재 해 갱신
    DFS_sum_of_subsets(S, M, i+1, sol, remaining - S[i])  #S에 남은 원소의 합이 갱신되어야 함 
    sol.pop() # 현재 해 복구 

nums = [3, 34, 4, 12, 5, 2]
M = 9

all_sum_of_subsets(nums, M)


####################
# 결과
#
# [3, 4, 2]
# [4, 5]
####################