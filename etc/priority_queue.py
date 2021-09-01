# 우선순위 큐를 이용해 숫자를 정렬.

import queue

q = queue.PriorityQueue()

li = [24,62,12,643,2,54,21,6,32,67,523,91]
sorted_li = []

for i in li:
  q.put(i)

while not q.empty():
  sorted_li.append(q.get())

print(sorted_li)

###############################################
# 결과
# [2, 6, 12, 21, 24, 32, 54, 62, 67, 91, 523, 643]
###############################################
