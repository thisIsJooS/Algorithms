# binary_search - recursion

n, key = map(int, input().split())

arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid -1)
        
    else:
        return binary_search(arr, target, mid + 1, end)        


print(binary_search(arr, key, 0, len(arr)-1) + 1)



# 입력예시 1
# 10 7
# 1 3 5 7 9 11 13 15 17 19


# 출력예시 1
# 4