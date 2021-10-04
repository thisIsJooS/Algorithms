# Lomuto partition
def partition(A, left, right):
    pivotIndex = right
    
    i = left - 1
    j = left
    
    while j < right:
        if A[j] <= A[pivotIndex]:
            i += 1
            A[i], A[j] = A[j], A[i]
        
        j += 1
    
    A[i+1], A[pivotIndex] = A[pivotIndex], A[i+1]
    
    return i+1

def quickSortImpl(A, left, right):
    if left < right:
        pivotIndex = partition(A, left, right)
        quickSortImpl(A, left, pivotIndex-1)
        quickSortImpl(A, pivotIndex+1, right)


def quickSort(A):
    quickSortImpl(A, 0, len(A)-1)


arr = [7, 4, 9, 6, 3, 8, 7, 5]
quickSort(arr)
print(arr)