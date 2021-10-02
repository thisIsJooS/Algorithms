def merge(left, right):
  res = []
  
  while len(left) > 0 or len(right) > 0:
    if len(left) > 0 and len(right) > 0:
      if left[0] < right[0]:
        res.append(left[0])
        left = left[1:]
      
      elif left[0] > right[0]:
        res.append(right[0])
        right = right[1:]
      
    elif len(left) > 0:
      res.append(left[0])
      left = left[1:]
    
    elif len(right) > 0:
      res.append(right[0])
      right = right[1:]
    
  return res


def mergeSort(A):
  n = len(A)
  
  if n <= 1:
    return A
  
  mid = n // 2
  
  leftList = mergeSort(A[:mid])
  rightList = mergeSort(A[mid:])
  
  return merge(leftList, rightList)


arr = [1, 3, 5, 8, 2, 4, 6, 9]
print(mergeSort(arr))


##########################
# 결과
#
# [1, 2, 3, 4, 5, 6, 8, 9]
##########################