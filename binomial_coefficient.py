#이항계수 구하기
#by resursion
def bino_coef_dc(n,k):
  if k==0 or k==n:
    return 1
  return bino_coef_dc(n-1,k-1) + bino_coef_dc(n-1,k)

print(bino_coef_dc(6,3))


#by tabling
def bino_coef_dp(n,k):
  C=[[-1 for _ in range(k+1)] for _ in range(n+1)]
  
  for i in range(n+1):
    for j in range(min(i,k)+1):
      if j==0 or j==i:
        C[i][j]=1
      else:
        C[i][j]=C[i-1][j-1]+C[i-1][j]
  return C[n][k]
  
print(bino_coef_dp(6,3))


#by memoization
mem=[[None for _ in range(4)] for _ in range(7)]

def bino_coef_dp2(n,k):
  if mem[n][k]==None:
    if k==0 or n==k:
      mem[n][k]=1
    else:
      mem[n][k]=bino_coef_dp2(n-1,k-1)+bino_coef_dp2(n-1,k)
  return mem[n][k]
    
print(bino_coef_dp2(6,3))
