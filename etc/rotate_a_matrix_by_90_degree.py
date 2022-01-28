def rotate_a_matrix_by_90_degree(a):    # 시계방향 회전 
    n, m = len(a), len(a[0])    # 행, 열
    
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
            
    return result


def rotate_a_matrix_by_90_degree_reverse(a):    # 반시계방향 회전 
    n, m = len(a), len(a[0])    # 행, 열
    
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m-1-j][i] = a[i][j]
            
    return result


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for a in rotate_a_matrix_by_90_degree(arr):
    print(a)
    
print("=========")
for a in rotate_a_matrix_by_90_degree_reverse(arr):
    print(a)
    
    
# 출력결과
#
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]
# =========
# [3, 6, 9]
# [2, 5, 8]
# [1, 4, 7]
