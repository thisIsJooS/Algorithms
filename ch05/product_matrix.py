A = [
    [1, 1],
    [1, 0]
]

B = [
    [1, 1],
    [1, 0]
]

def productMatrix(A, B):
    C = [[0 for _ in range(len(A))] for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
                
    return C
