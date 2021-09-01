# 문자열 매칭 - 길이가 n인 문자열 T와 길이가 m인 패턴 문자열 P에서, T에서 가장 먼저 나타나는 P의 위치

def string_matching_bf(T, P):
  n=len(T)
  m=len(P)
  for i in range(n-m+1):
    j=0
    while j<m and P[j]==T[i+j]:
      j=j+1
    if j==m:
      return i
  return -1
  
T="dmikijkladajskladjalsjsakdsklmikidskjads"
P="miki"

print(string_matching_brute(T,P))