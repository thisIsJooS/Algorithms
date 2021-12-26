import math

n = 1000
arr = [True for i in range(n+1)]
arr[1] = False    # 1은 소수가 아니다

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1
            
            
for i in range(2, n+1):
    if arr[i]:
        print(i, end = ' ')
        
        
# O(NloglogN)으로 사실상 선형시간에 동작할 정도로 빠르다.