# 알고리즘에 따른 제곱수 계산 시간 비교

import time

# O(1)
def compute_square_A(n):
  return n*n

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

