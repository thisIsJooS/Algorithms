# 0-1 knapsack problem - branch and bound

# 한계합 계산방법의 개선
# 한계가치를 계산할 때 아직 결정하지 않고 남은 물건을 넣는 것이 아니라 남은 물건들을 용량을 초과하지 않는 만큼만 넣음 
# 물건들을 먼저 단위 무게당 가치 순으로 정렬하여야 한다.

# 상태공간트리의 탐색과정에 어떤 노드의 서브 트리를 더 분기해 나갈지(탐색할지) 가지치기(한정)를 하고 더 탐색할지 말지를 좀 더 적극적으로 탐색
# 서브트리에서 기대할 수 있는 최대 가치합 (N 까지의 확정가치 + 서브트리 최대 기대가치) < (현재 알고 있는 최대 가치)  ->  N에서 백트래킹

def knapsack_bnb(obj, W, level, weight, profit, maxProfit, sol, bnd):
  print("Level %d %-20s: %.1fKg   노드의 가치합 / 한계합 = %5.1f / %5.1f > %5.1f(최고합) " %(level, sol, weight, profit, bnd, maxProfit))  # 노드 탐색 과정 출력 
  
  if level == len(obj):    # 단말 노드까지 처리된 경우 
    return maxProfit      # 지금까지의 최대 가치를 반환

  
  # level 번째 노드를 넣는 경우
  if weight + obj[level][0] < W: 
    
    newWeight = weight + obj[level][0]
    newProfit = profit + obj[level][1]

    if newProfit > maxProfit:
      maxProfit = newProfit

    newBound = bound2(obj, W, level, newWeight, newProfit)
    
    if newBound >= maxProfit:    # 한계가치 >= 최고가치 : 탐색 계속 진행
      sol.append(obj[level][2])
      maxProfit = knapsack_bnb(obj, W, level+1, newWeight, newProfit, maxProfit, sol, newBound)
      sol.pop()

      
  # level 번째 노드를 안 넣는 경우
  newWeight = weight
  newProfit = profit
  newBound = bound2(obj, W, level, newWeight, newProfit)

  if newBound >= maxProfit:  
    maxProfit = knapsack_bnb(obj, W, level+1, newWeight, newProfit, maxProfit, sol, newBound)
    
  return maxProfit


# 어떤 노드 N의 한계가치를 구하는 함수
# N의 한계합 = N의 확정된 가치합 + 아직 결정하지 않은 모든 물건의 가치합
def bound2(obj, W, level, weight, profit):
  if weight > W:
    return 0
  
  pBound = profit
  tWeight = weight  # 추가
  
  # for i in range(level+1, len(obj)):
  #   pBound += obj[i][1]
  
  j = level + 1
  n = len(obj)
  
  while j < n and tWeight + obj[j][0] <= W:
    tWeight += obj[j][0]
    pBound += obj[j][1]
    j += 1
  
  if j < n:    # 배낭에 남은 용량에 대해 처리하는 코드
    pBound += (W - tWeight) * (obj[j][1] / obj[j][0])
  
  return pBound


# 알고리즘 테스트
obj=[ (2.5, 30, "A"), (3.2, 50, "B"), (1.7, 70, "C"), (5, 60, "D"), (4.1, 40, "E") ]
obj.sort(key = lambda e : e[1]/e[0], reverse=True) # 추가 

print(obj)
print("0-1 knapsack problem (Branch and Bound) : ", knapsack_bnb(obj, 10, 0, 0, 0, 0, [], 0))


##########################################################################################
# 결과
#
# [(1.7, 70, 'C'), (3.2, 50, 'B'), (2.5, 30, 'A'), (5, 60, 'D'), (4.1, 40, 'E')]
# Level 0 []                  : 0.0Kg   노드의 가치합 / 한계합 =   0.0 /   0.0 >   0.0(최고합)
# Level 1 ['C']               : 1.7Kg   노드의 가치합 / 한계합 =  70.0 / 181.2 >  70.0(최고합)
# Level 2 ['C', 'B']          : 4.9Kg   노드의 가치합 / 한계합 = 120.0 / 181.2 > 120.0(최고합)
# Level 3 ['C', 'B', 'A']     : 7.4Kg   노드의 가치합 / 한계합 = 150.0 / 181.2 > 150.0(최고합)
# Level 4 ['C', 'B', 'A']     : 7.4Kg   노드의 가치합 / 한계합 = 150.0 / 175.4 > 150.0(최고합)
# Level 5 ['C', 'B', 'A']     : 7.4Kg   노드의 가치합 / 한계합 = 150.0 / 150.0 > 150.0(최고합)
# Level 3 ['C', 'B']          : 4.9Kg   노드의 가치합 / 한계합 = 120.0 / 181.0 > 150.0(최고합)
# Level 4 ['C', 'B', 'D']     : 9.9Kg   노드의 가치합 / 한계합 = 180.0 / 181.0 > 180.0(최고합)
# Level 5 ['C', 'B', 'D']     : 9.9Kg   노드의 가치합 / 한계합 = 180.0 / 180.0 > 180.0(최고합)
# 0-1 knapsack problem (Branch and Bound) :  180
##########################################################################################