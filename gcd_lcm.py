# Euclid's algorithm
# gcd(a,b) = gcd(b, a mod b)

def gcd_iter(a,b):
  while b!=0:
    r=a%b
    a=b
    b=r
  return a

def gcd_recur(a,b):
  if b==0:
    return a
  return gcd_recur(b, a%b)

print("60과 28의 최대공약수 - 반복 : " , gcd_iter(60,28))
print("60과 28의 최대공약수 - 순환 : " , gcd_recur(60,28))

def lcm(a, b):
  return int(a * b / gcd_recur(a,b));


print("6과 8의 최소공배수 : ", lcm(6,8))