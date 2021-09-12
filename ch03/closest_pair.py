# 2차원 평면상의 n개의 점이 있음. 가장 인접한 쌍의 거리 구하기

import math

def distance(p1, p2):  # Euclidean 거리 계산 함수
  return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# brute-force
def closest_pair_bf(p):
  n = len(p)
  mindist = float("inf")
  
  for i in range(n - 1):
    for j in range(i + 1, n):
      dist = distance(p[i], p[j])
      if dist < mindist:
        mindist = dist
        
  return mindist


# 알고리즘 테스트
p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("최근접 거리 : %.3f" % closest_pair_bf(p))



########################
# 결과
#
# 최근접 거리 : 1.414
########################