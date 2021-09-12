# 알고리즘에 따른 제곱수 계산 시간 비교

import time

# O(1)
def compute_square_A(n):
  return n * n

# O(n)
def compute_square_B(n):
  sum = 0
  for i in range(n):
    sum = sum + n
  return sum

# O(n^2)
def compute_square_C(n):
  sum = 0
  for i in range(n):
    for j in range(n):
      sum = sum + 1
  return sum


# 알고리즘 테스트
t1 = time.time()
compute_square_A(8000)
t2 = time.time()
compute_square_B(8000)
t3 = time.time()
compute_square_C(8000)
t4 = time.time()

print("compute_square_A(8000) 걸린 시간 : %.8f" % (t2-t1))
print("compute_square_B(8000) 걸린 시간 : %.8f" % (t3-t2))
print("compute_square_C(8000) 걸린 시간 : %.8f" % (t4-t3))

########################################################
# 결과
#
# compute_square_A(8000) 걸린 시간 : 0.00000238
# compute_square_B(8000) 걸린 시간 : 0.00282288
# compute_square_C(8000) 걸린 시간 : 26.80734563
########################################################
