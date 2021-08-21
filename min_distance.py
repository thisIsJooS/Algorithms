# 배열에서 가장 가까운 두 항목을 찾아 거리를 찾아 반환하는 알고리즘

from collections import deque
import time

#O(N^2)인 brute-force algorithm
def min_distance(A):
  n=len(A)
  dmin=float("inf")
  for i in range(n):
    for j in range(n):
      if i!=j and abs(A[i]-A[j]) < dmin:
        dmin = abs(A[i]-A[j])
  return dmin


#Radix Sort. 시간복잡도는 O(N)
def countingSort(arr, digit):
  n = len(arr)

  output = [0] * (n)
  count = [0] * (10)

  for i in range(0, n):
    index = int(arr[i]/digit) 
    count[ (index)%10 ] += 1

  for i in range(1,10):
      count[i] += count[i-1]   
  i = n - 1
  while i >= 0:
    index = int(arr[i]/digit)
    output[ count[ (index)%10 ] - 1] = arr[i]
    count[ (index)%10 ] -= 1
    i -= 1
  
  for i in range(0,len(arr)): 
      arr[i] = output[i]

def radixSort(arr):
  maxValue = max(arr)  
  digit = 1
  while int(maxValue/digit) > 0: 
    countingSort(arr,digit)
    digit *= 10
  
#Radix Sort를 활용하여 dmin 구하기
def min_distance_quick(A):
  radixSort(A)
  n = len(A)
  dmin = float("inf")
  for i in range(n-1):
    if abs(A[i]-A[i+1])<dmin:
      dmin = abs(A[i]-A[i+1])
  return dmin

# 실제 걸린 시간 측정
list = []
for i in range(2000,0,-1):
  list.append(i)
  
t1=time.time()
val1 = min_distance(list)
t2=time.time()
val2 = min_distance_quick(list)
t3=time.time()

print("min_distance 시간 : ",  t2-t1)
print("min_distance_quick 시간 : ", t3-t2)



###############################################
# 결과
# min_distance 시간 :  6.194323301315308
# min_distance_quick 시간 :  0.013263225555419922
###############################################