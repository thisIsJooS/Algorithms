arr = [1, 3, 4, 6, 7, 9, 10, 11]

def binary_search_by_recursion(A, key):
    if len(A) == 0:
        return -1 
    
    midIndex = len(A) // 2
    
    if key > A[midIndex]:
        return binary_search_by_recursion(A[midIndex+1 : ], key)
    
    elif key < A[midIndex]:
        return binary_search_by_recursion(A[:midIndex], key)
    
    elif key == A[midIndex]:
        return A[midIndex]
    
    return -1


def binary_search_byIteration(A, key):
    while len(A) != 0:
        midIndex = len(A) // 2
        
        if key > A[midIndex]:
            A = A[midIndex+1:]
        
        elif key < A[midIndex]:
            A = A[:midIndex]
        
        elif key == A[midIndex]:
            return key
        
    return -1

