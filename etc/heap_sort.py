# Heap Sort Algorithm - O(NlogN)

def heapify(A, n, i):
  largest = i
  left = 2*i + 1
  right = 2*i + 2
  
  if left<n and A[largest]<A[left]:
    largest = left
  
  if right<n and A[largest]<A[right]:
    largest = right
    
  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    heapify(A, n, largest)
    
def heap_sort(A):
  n = len(A)
  for i in range(n//2 - 1, -1, -1):
    heapify(A, n ,i)
  
  for i in range(n-1, 0, -1):
    A[i], A[0] = A[0], A[i]
    heapify(A, i, 0)
    
# 알고리즘 테스트 
arr = [7, 6, 5, 8, 3, 5, 9, 1, 6]
heap_sort(arr)
print("Sorted array >> ", arr)

#################################################
# 결과
# Sorted array >>  [1, 3, 5, 5, 6, 6, 7, 8, 9]
#################################################