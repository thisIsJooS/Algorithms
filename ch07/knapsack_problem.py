def knapSack(W, wt, val, n):
    if W == 0 or n == 0:
        return 0
    
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)
    
    else:
        valWith = val[n-1] + knapSack(W-wt[n-1], wt, val, n-1)
        valWithout = knapSack(W, wt, val, n-1)
        return max(valWith, valWithout)
    

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)

print("0-1 배낭문제(분할정복) :", knapSack(W, wt, val, n))


def knapSack(W, wt, val, n):
    f = [[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                f[i][w] = f[i-1][w]
            else:
                valWith = val[i-1] + f[i-1][w-wt[i-1]]
                valWithout = f[i-1][w]
                f[i][w] = max(valWith, valWithout)
                
    return f[n][W]

print("0-1 배낭문제(동적계획) :", knapSack(W, wt, val, n))



###########################
# 결과
#
# 0-1 배낭문제(분할정복) : 480
# 0-1 배낭문제(동적계획) : 480
###########################