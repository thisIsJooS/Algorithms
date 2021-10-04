from queue import Queue
import random

def radixSort(A, BUCKETS, DIGITS):
    n = len(A)
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())
    factor = 1
    
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor)%10].put(A[i])
        
        j=0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10
        print('Step ', d+1, A)
        
arr = []
for i in range(10):
    arr.append(random.randint(1, 9999))

radixSort(arr, 10, 4)
print('Radix :', arr)



#######################################################################
# 결과
#
# Step  1 [8370, 751, 6331, 1362, 7272, 1842, 3457, 6487, 9688, 6918]
# Step  2 [6918, 6331, 1842, 751, 3457, 1362, 8370, 7272, 6487, 9688]
# Step  3 [7272, 6331, 1362, 8370, 3457, 6487, 9688, 751, 1842, 6918]
# Step  4 [751, 1362, 1842, 3457, 6331, 6487, 6918, 7272, 8370, 9688]
# Radix : [751, 1362, 1842, 3457, 6331, 6487, 6918, 7272, 8370, 9688]
#######################################################################
