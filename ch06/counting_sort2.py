# If there are negative numbers in array

def countingSort2(A, MIN_VAL, MAX_VAL):
    n = len(A)
    count = [0] * (MAX_VAL - MIN_VAL + 1)
    output = [0] * n
    
    for i in range(n):
        A[i] += (-MIN_VAL)
    
    for k in A:
        count[k] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    for k in A:
        output[count[k]-1] = k
        count[k] -= 1
        
    for i in range(n):
        output[i] -= (-MIN_VAL)
    
    A = output
    
    return A

arr = [-1, 4, 5, 2, 6, 7, 8, -3, 2, -4]
arr = countingSort2(arr, -4, 8)
print(arr)




#######################################
# 결과
#
# [-4, -3, -1, 2, 2, 4, 5, 6, 7, 8]
#######################################