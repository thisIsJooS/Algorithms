import time

def powerByBruteForce(x, n):
    ret = 1
    
    for i in range(n):
        ret *= x
    
    return ret

def powerByDAC(x, n):
    if n == 1:
        return x
    
    if n%2 == 0:
        return powerByDAC(x*x, n//2)
    
    else:
        return x * powerByDAC(x*x, n//2)

t1 = time.time()
val1 = powerByBruteForce(8, 100000)
t2 = time.time()
val2 = powerByDAC(8, 100000)
t3 = time.time()
print("Brute Force 시간 : ", t2 - t1)
print("Decrease and Conquer 시간 : ", t3 - t2)



#######################################################
# 결과 
#
# Brute Force 시간 :  3.341778516769409
# Decrease and Conquer 시간 :  0.011495828628540039
#####################################################