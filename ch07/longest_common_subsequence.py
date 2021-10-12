X = "HELLO WORLD"
Y = "GAME OVER"

# recursion
def lcs(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0
    
    elif X[-1] == Y[-1]:
        return 1 + lcs(X[:-1], Y[:-1])
    else:
        return max(lcs(X[:-1], Y), lcs(X, Y[:-1]))


# tabling
def lcs(X, Y):
    t = [[0 for _ in range(len(Y))] for _ in range(len(X))]
    
    for x in range(1, len(X)):
        for y in range(1, len(Y)):
            if X[x] == Y[y]:
                t[x][y] = 1 + t[x-1][y-1]
            
            else:
                t[x][y] = max(t[x-1][y], t[x][y-1])
        
    print(lcs_traceback(X, Y, t))
    return t[x][y]

  

def lcs_traceback(X, Y, table):
    lcs = ''
    x, y = len(X)-1, len(Y)-1
    
    while x > 0 and y > 0:
        v = table[x][y]
        
        if v > table[x-1][y] and v > table[x][y-1] and v > table[x-1][y-1]:
            lcs = X[x] + lcs
            x -= 1
            y -= 1
            
        elif v == table[x-1][y] and v > table[x][y-1]:
            x -= 1
        
        else:
            y -= 1
    
    return lcs
  
  
print(lcs(X, Y))


###############
# 결과
#
# E OR
# 4
###############