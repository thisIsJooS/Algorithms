# 배열에서 가장 가까운 두 항목을 찾아 거리를 찾아 반환하는 알고리즘

from collections import deque
from queue import Queue
import time

#Radix Sort (기수정렬) 함수
BUCKETS = 10
DIGITS = 4

def radix_sort(A):
  queues = []
  for i in range(BUCKETS):
    queues.append(Queue())
  n = len(A)
  factor = 1
  for d in range(DIGITS):
    for i in range(n):
      queues[(A[i]//factor)%10].put(A[i])
    j = 0
    for b in range(BUCKETS):
      while not queues[b].empty():
        A[j] = queues[b].get()
        j += 1
    factor *= 10

#Counting Sort 함수
MAX_VAL = 2010
def counting_sort(A):
  output = [0] * len(A)
  count = [0] * MAX_VAL
  
  for i in A:
    count[i] += 1
  
  for i in range(MAX_VAL):
    count[i] += count[i-1]
    
  for i in range(len(A)):
    output[count[A[i]] - 1] = A[i]
    count[A[i]] -= 1
    
  for i in range(len(A)):
    A[i] = output[i]

#O(N^2)인 brute-force algorithm
def min_distance_brute(A):
  n=len(A)
  dmin=float("inf")
  for i in range(n):
    for j in range(n):
      if i!=j and abs(A[i]-A[j]) < dmin:
        dmin = abs(A[i]-A[j])
  return dmin


#Radix Sort를 활용하여 dmin 구하기
def min_distance_radix(A):
  radix_sort(A)
  n = len(A)
  dmin = float("inf")
  for i in range(n-1):
    if abs(A[i]-A[i+1])<dmin:
      dmin = abs(A[i]-A[i+1])
  return dmin

#Counting Sort를 활용하여 dmin 구하기
def min_distance_counting(A):
  counting_sort(A)
  n = len(A)
  dmin = float("inf")
  for i in range(n-1):
    if abs(A[i]-A[i+1])<dmin:
      dmin = abs(A[i]-A[i+1])
  return dmin
    
  
# 실제 걸린 시간 측정
list1 = []
list2 = []
for i in range(2000,0,-1):
  list1.append(i)
  list2.append(i)
  
t1=time.time()
val1 = min_distance_brute(list1)
t2=time.time()
val2 = min_distance_radix(list1)
t3=time.time()
val3 = min_distance_counting(list2)
t4 = time.time()

print("min_distance_brute 시간 : ",  t2-t1)
print("min_distance_radix 시간 : ", t3-t2)
print("min_distance_counting 시간 : ", t4-t3)



###############################################
# 결과
# min_distance_brute 시간 :  6.0872883796691895
# min_distance_radix 시간 :  0.4752662181854248
# min_distance_counting 시간 :  0.004540205001831055
###############################################