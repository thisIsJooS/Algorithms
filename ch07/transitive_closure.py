def transitiveClosure(mat):
    n = len(mat)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    mat[i][j] = mat[i][j] or (mat[i][k] and mat[k][j])
                
    return mat


mat = [
    [0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]


M = transitiveClosure(mat)
for m in M:
    print(m)
    
    

#####################
# 결과
#
# [0, 1, 1, 1, 1, 0]
# [1, 0, 1, 1, 1, 0]
# [0, 0, 0, 0, 1, 0]
# [1, 1, 1, 0, 1, 0]
# [0, 0, 1, 0, 0, 0]
# [0, 0, 1, 0, 1, 0]
#####################
    