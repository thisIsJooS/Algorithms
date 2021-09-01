# Shell Sort Algorithm

def shell_sort(A):
  gap = len(A) // 2
  
  while gap > 0:
    i = 0
    j = gap
    while j<len(A):
      if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]
      
      i += 1
      j += 1
      k = i
      
      while k - gap > -1:
        if A[k - gap] > A[k]:
          A[k - gap], A[k] = A[k], A[k - gap]
        k -= 1
    
    gap //= 2
    
# 알고리즘 테스트
data=[5,3,8,4,9,1,6,2,7]
shell_sort(data)

print("Sorted array >> ", data)

##############################################
# 결과
# Sorted array >>  [1, 2, 3, 4, 5, 6, 7, 8, 9]
##############################################