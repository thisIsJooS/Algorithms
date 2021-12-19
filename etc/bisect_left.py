def bisect_left(arr, target, low=0, high=None):
    if high is None:
        high = len(arr)
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid+1
        else:
            high = mid
            
    return low