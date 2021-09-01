# 2차원 평면상의 n개의 점이 있음. 가장 인접한 쌍의 거리 구하기

# brute-force
def closest_pair_bf(p):
  n=len(p)
  mindist-float("inf")
  for i in range(n-1):
    for j in range(i+1,n):
      dist=distance(p[i],p[j])
      if dist < mindist:
        mindist=dist
  return mindist

