# 0-1 knapsack problem - branch and bound

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

    newBound = bound(obj, W, level, newWeight, newProfit)
    
    if newBound >= maxProfit:    # 한계가치 >= 최고가치 : 탐색 계속 진행
      sol.append(obj[level][2])
      maxProfit = knapsack_bnb(obj, W, level+1, newWeight, newProfit, maxProfit, sol, newBound)
      sol.pop()

      
  # level 번째 노드를 안 넣는 경우
  newWeight = weight
  newProfit = profit
  newBound = bound(obj, W, level, newWeight, newProfit)

  if newBound >= maxProfit:  
    maxProfit = knapsack_bnb(obj, W, level+1, newWeight, newProfit, maxProfit, sol, newBound)
    
  return maxProfit


# 어떤 노드 N의 한계가치를 구하는 함수
# N의 한계합 = N의 확정된 가치합 + 아직 결정하지 않은 모든 물건의 가치합
def bound(obj, W, level, weight, profit):
  if weight > W:
    return 0
  
  pBound = profit
  
  for i in range(level+1, len(obj)):
    pBound += obj[i][1]
  
  return pBound


# 알고리즘 테스트
obj=[ (2.5, 30, "A"), (3.2, 50, "B"), (1.7, 70, "C"), (5, 60, "D"), (4.1, 40, "E") ]

print(obj)
print("0-1 knapsack problem (Branch and Bound) : ", knapsack_bnb(obj, 10, 0, 0, 0, 0, [], 0))



##########################################################################################
# 결과
#
# [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E')]
# Level 0 []                  : 0.0Kg   노드의 가치합 / 한계합 =   0.0 /   0.0 >   0.0(최고합)
# Level 1 ['A']               : 2.5Kg   노드의 가치합 / 한계합 =  30.0 / 250.0 >  30.0(최고합)
# Level 2 ['A', 'B']          : 5.7Kg   노드의 가치합 / 한계합 =  80.0 / 250.0 >  80.0(최고합)
# Level 3 ['A', 'B', 'C']     : 7.4Kg   노드의 가치합 / 한계합 = 150.0 / 250.0 > 150.0(최고합)
# Level 4 ['A', 'B', 'C']     : 7.4Kg   노드의 가치합 / 한계합 = 150.0 / 190.0 > 150.0(최고합)
# Level 5 ['A', 'B', 'C']     : 7.4Kg   노드의 가치합 / 한계합 = 150.0 / 150.0 > 150.0(최고합)
# Level 3 ['A', 'B']          : 5.7Kg   노드의 가치합 / 한계합 =  80.0 / 180.0 > 150.0(최고합)
# Level 2 ['A']               : 2.5Kg   노드의 가치합 / 한계합 =  30.0 / 200.0 > 150.0(최고합)
# Level 3 ['A', 'C']          : 4.2Kg   노드의 가치합 / 한계합 = 100.0 / 200.0 > 150.0(최고합)
# Level 4 ['A', 'C', 'D']     : 9.2Kg   노드의 가치합 / 한계합 = 160.0 / 200.0 > 160.0(최고합)
# Level 5 ['A', 'C', 'D']     : 9.2Kg   노드의 가치합 / 한계합 = 160.0 / 160.0 > 160.0(최고합)
# Level 1 []                  : 0.0Kg   노드의 가치합 / 한계합 =   0.0 / 220.0 > 160.0(최고합)
# Level 2 ['B']               : 3.2Kg   노드의 가치합 / 한계합 =  50.0 / 220.0 > 160.0(최고합)
# Level 3 ['B', 'C']          : 4.9Kg   노드의 가치합 / 한계합 = 120.0 / 220.0 > 160.0(최고합)
# Level 4 ['B', 'C', 'D']     : 9.9Kg   노드의 가치합 / 한계합 = 180.0 / 220.0 > 180.0(최고합)
# Level 5 ['B', 'C', 'D']     : 9.9Kg   노드의 가치합 / 한계합 = 180.0 / 180.0 > 180.0(최고합)
# 0-1 knapsack problem (Branch and Bound) :  180
##########################################################################################
    