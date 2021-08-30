#그래프에서 모든 정점간의 최단경로 거리 계산 
import copy

def shortest_path_floyd(vertex ,w):
  vsize=len(vertex)
  D=copy.deepcopy(w)
  
  for k in range(vsize):
    for i in range(vsize):
      for j in range(vsize):
        D[i][j] = min(D[i][k]+D[k][j], D[i][j])
    printD(D)

def printD(D):
  vsize=len(D)
  print("==================================")
  for i in range(vsize):
    for j in range(vsize):
      if(D[i][j]==INF) : print(" INF ", end="")
      else : print("%4d "%D[i][j], end='')
    print("")

INF=9999
vertex = ['A','B','C','D','E','F','G']
weight = [
  [0, 7, INF, INF, 3, 10, INF],
  [7, 0, 4, 10, 2, 6, INF],
  [INF, 4, 0, 2, INF, INF, INF],
  [INF, 10, 2, 0, 11, 9, 4],
  [3, 2, INF, 11, 0, 13, 5],
  [10, 6, INF, 9, 13, 0, INF],
  [INF, INF, INF, 4, 5, INF, 0]
]

print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vertex, weight)

###################################################
# 결과
# 
# Shortest Path By Floyd's Algorithm
# ==================================
#    0    7  INF  INF    3   10  INF
#    7    0    4   10    2    6  INF
#  INF    4    0    2  INF  INF  INF
#  INF   10    2    0   11    9    4
#    3    2  INF   11    0   13    5
#   10    6  INF    9   13    0  INF
#  INF  INF  INF    4    5  INF    0
# ==================================
#    0    7   11   17    3   10  INF
#    7    0    4   10    2    6  INF
#   11    4    0    2    6   10  INF
#   17   10    2    0   11    9    4
#    3    2    6   11    0    8    5
#   10    6   10    9    8    0  INF
#  INF  INF  INF    4    5  INF    0
# ==================================
#    0    7   11   13    3   10  INF
#    7    0    4    6    2    6  INF
#   11    4    0    2    6   10  INF
#   13    6    2    0    8    9    4
#    3    2    6    8    0    8    5
#   10    6   10    9    8    0  INF
#  INF  INF  INF    4    5  INF    0
# ==================================
#    0    7   11   13    3   10   17
#    7    0    4    6    2    6   10
#   11    4    0    2    6   10    6
#   13    6    2    0    8    9    4
#    3    2    6    8    0    8    5
#   10    6   10    9    8    0   13
#   17   10    6    4    5   13    0
#   ==================================
#    0    5    9   11    3   10    8
#    5    0    4    6    2    6    7
#    9    4    0    2    6   10    6
#   11    6    2    0    8    9    4
#    3    2    6    8    0    8    5
#   10    6   10    9    8    0   13
#    8    7    6    4    5   13    0
# ==================================
#    0    5    9   11    3   10    8
#    5    0    4    6    2    6    7
#    9    4    0    2    6   10    6
#   11    6    2    0    8    9    4
#    3    2    6    8    0    8    5
#   10    6   10    9    8    0   13
#    8    7    6    4    5   13    0
# ==================================
#    0    5    9   11    3   10    8
#    5    0    4    6    2    6    7
#    9    4    0    2    6   10    6
#   11    6    2    0    8    9    4
#    3    2    6    8    0    8    5
#   10    6   10    9    8    0   13
#    8    7    6    4    5   13    0
###################################################