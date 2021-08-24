# 자연수의 2진수 변환에서 총 비트 수 계산
import time

#반복 구조  O(logN)
def binary_digits_A(n):
  count=1
  while n>1:
    count=count+1
    n=n//2
  return count

# 순환 구조 O(logN)
def binary_digits_B(n):
  if n<=1:
    return 1
  else:
    return 1+binary_digits_B(n//2)
