# Huffman codes

import heapq

def make_heap_tree(freq, label):
  n = len(freq)
  h = []
  
  for i in range(n):
    heapq.heappush(h, (freq[i], label[i]))
    
  for i in range(1, n):
    e1 = heapq.heappop(h)  # 가장 작은 트리
    e2 = heapq.heappop(h)  # 다음 작은 트리
    
    heapq.heappush(h, (e1[0]+e2[0], e1[1]+e2[1]))
    print(e1, "+", e2)
    
  print(heapq.heappop(h))  # 최종 트리의 루트 출력
  

label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
freq = [24, 3, 8, 10, 33, 6, 4, 12]
make_heap_tree(freq, label)


################################################
# 결과
#
# (3, 'B') + (4, 'G')
# (6, 'F') + (7, 'BG')
# (8, 'C') + (10, 'D')
# (12, 'H') + (13, 'FBG')
# (18, 'CD') + (24, 'A')
# (25, 'HFBG') + (33, 'E')
# (42, 'CDA') + (58, 'HFBGE')
# (100, 'CDAHFBGE')
################################################