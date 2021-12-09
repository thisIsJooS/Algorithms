# binary_search - iteration

n, key = map(int, input().split())

arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
            
    return None

print(binary_search(arr, key, 0, len(arr)-1)+1)


# 입력예시 1
# 10 7
# 1 3 5 7 9 11 13 15 17 19


# 출력예시 1
# 4