from queue import Queue


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
        j=0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10