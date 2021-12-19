def bisect_right(arr, target, low=0, high=None):
    if high is None:
        high = len(arr)
        
    while low < high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid
        else:
            low = mid+1
    
    return high