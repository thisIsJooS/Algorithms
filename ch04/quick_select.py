def nth_smallest_sort(A, n):
    A.sort()
    return A[n-1]

def quick_select(A, n):
    if n > len(A) or n <= 0:
        return -1
    
    pivotIndex = partitionAndReturnPivotIndex(A)
    
    if n > pivotIndex+1:
        return quick_select(A[pivotIndex+1 :], n-pivotIndex-1)
    
    elif n < pivotIndex+1:
        return quick_select(A[:pivotIndex], n)
    
    elif n == pivotIndex+1:
        return A[n-1]
    
def partitionAndReturnPivotIndex(A):
    pivotIndex = 0 
    low = pivotIndex + 1
    high = len(A) - 1
    
    while low <= high:
        while low <= len(A)-1 and A[low] < A[pivotIndex]:
            low += 1
        
        while high >= pivotIndex and A[high] > A[pivotIndex]:
            high -=1
        
        if low < high:
            A[low], A[high] = A[high], A[low]
    
    A[pivotIndex], A[high] = A[high], A[pivotIndex]
    
    return pivotIndex

  
arr = [3, 8, 4, 6, 5, 7, 9, 2, 1]

print("입력 리스트 : ", arr)
print("[정렬기법] 3번째 작은 수 : ", nth_smallest_sort(arr, 3))
print("[정렬기법] 6번째 작은 수 : ", nth_smallest_sort(arr, 6))
print("[축소정복] 3번째 작은 수 : ", quick_select(arr, 3))
print("[축소정복] 6번째 작은 수 : ", quick_select(arr, 6))


##########################################
# 결과
#
# 입력 리스트 :  [3, 8, 4, 6, 5, 7, 9, 2, 1]
# [정렬기법] 3번째 작은 수 :  3
# [정렬기법] 6번째 작은 수 :  6
# [축소정복] 3번째 작은 수 :  3
# [축소정복] 6번째 작은 수 :  6
##########################################

##########################################
# 복잡도 분석
#
#
# 최선의 경우 : 한번의 분할 만으로 선택이 완료되는 경우이다. O(n)
#
# 최악의 경우 : 분할할 때 마다 부분리스트의 한쪽은 항목이 없고 다른 한쪽에만 모든 항목이 들어가는 경우이다.
#   예를들어, 이미 정렬된 리스트에서 가장 큰 항목을 찾는 것. O(n^2)
##########################################