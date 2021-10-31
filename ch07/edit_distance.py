def editDistance(X, Y):
  m = len(X)
  n = len(Y)
  mem = [[None for _ in range(m+1)] for _ in range(n+1)]
  
  return editDistanceImpl(X, Y, mem)


# mem[n][m] 임에 주의할 것
def editDistanceImpl(X, Y, mem):
  m = len(X)
  n = len(Y)
  
  if m == 0:
    mem[n][m] = n
  
  if n == 0:
    mem[n][m] = m
    
  if mem[n][m] == None:
    if X[-1] == Y[-1]:
      mem[n][m] = editDistanceImpl(X[:-1], Y[:-1], mem)
    
    else:
      mem[n][m] = 1 + min(editDistanceImpl(X[:-1], Y, mem), editDistanceImpl(X, Y[:-1], mem), editDistanceImpl(X[:-1], Y[:-1], mem))
      
    
  return mem[n][m]


X = 'tuesday'
Y = 'thursday'

print(editDistance(X, Y))

# 2