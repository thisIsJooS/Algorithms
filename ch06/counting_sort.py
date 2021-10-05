# If there are no negative numbers in array.

def countingSort(A, MAX_VAL):
    n = len(A)
    count = [0] * (MAX_VAL+1)
    output = [0] * n
    
    for k in A:
        count[k] += 1
        
    for i in range(1, MAX_VAL+1):
        count[i] += count[i-1]
        
    for k in A:
        output[count[k]-1] = k
        count[k] -= 1
    
    A = output
    
    return A

arr = [1, 4, 1, 2, 7, 5, 2]
arr = countingSort(arr, 7)
print(arr)


#########################
# 결과
#
# [1, 1, 2, 2, 4, 5, 7]
#########################