# Hoare partition
def partition(A, left, right):
  pivotIndex = left
  low = pivotIndex + 1
  high = right

  while low <= high:
    while low <= right and A[pivotIndex] > A[low]:
      low += 1

    while high >= left and A[pivotIndex] < A[high]:
      high -= 1

    if low < high:
      A[low], A[high] = A[high], A[low]

  A[pivotIndex], A[high] = A[high], A[pivotIndex]

  return high


def quickSortImpl(A, left, right):
  if left < right:
    pivotIndex = partition(A, left, right)
    quickSortImpl(A, left, pivotIndex-1)
    quickSortImpl(A, pivotIndex+1, right)


def quickSort(A):
  quickSortImpl(A, 0, len(A)-1)
    
    
arr = [1, 3, 5, 8, 2, 4, 7, 9]
quickSort(arr)
print(arr)



#########################
# 결과
#
# [1, 2, 3, 4, 5, 7, 8, 9]
#########################