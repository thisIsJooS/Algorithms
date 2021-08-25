# Selection Sort Algorithm - O(N^2)

def selection_sort(A):
  n=len(A)
  for i in range(n-1):
    least=i
    for j in range(i+1,n):
      if(A[j]<A[least]):
        least=j
    A[i],A[least]=A[least],A[i]
    printStep(A,i+1)
    
def printStep(arr, val):
  print("   Step%2d =  " %val, end="")
  print(arr)

# 알고리즘 테스트
data=[5,3,8,4,9,1,6,2,7]
print(" Original : ", data)
selection_sort(data)
print("Selection : ", data)


###########################################
# 결과
#  Original :  [5, 3, 8, 4, 9, 1, 6, 2, 7]
#    Step 1 =  [1, 3, 8, 4, 9, 5, 6, 2, 7]
#    Step 2 =  [1, 2, 8, 4, 9, 5, 6, 3, 7]
#    Step 3 =  [1, 2, 3, 4, 9, 5, 6, 8, 7]
#    Step 4 =  [1, 2, 3, 4, 9, 5, 6, 8, 7]
#    Step 5 =  [1, 2, 3, 4, 5, 9, 6, 8, 7]
#    Step 6 =  [1, 2, 3, 4, 5, 6, 9, 8, 7]
#    Step 7 =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    Step 8 =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Selection :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
###########################################