# 4) 충돌을 체인법을 사용하여 처리한다

M = 11
table = [None] * M

class Node:
    def __init__(self, data, next = None) :
        self.data = data
        self.next = next
        

def hashFn(k):
    return k % M


def insert_chaining(k):
    idx = hashFn(k)
    
    if table[idx] == None:
        table[idx] = Node(k)
    
    elif table[idx] != None:
        node = table[idx]
        while node.next != None:
            node = node.next
        node.next = Node(k)
    

def search_chaining(k):
    idx = hashFn(k)
    node = table[idx]
    
    while node != None:
        if node.data == k:
            return idx

        else:
            node = node.next
    
    return None


def delete_chaining(k):
    idx = hashFn(k)
    node = table[idx]
    preNode = None
    
    while node != None:
        if node.data == k:
            if preNode == None:
                table[idx] = node.next
            else:
                preNode.next = node.next
            return True
    
        preNode = node
        node = node.next
        
    return False
    

def printTable(table):
    for i in range(len(table)):
        node = table[i]
    
        print('table[%2d] : ' % i, end = '')

        if node is not None:
            print(node.data, end = '')
            while node.next != None:
                node = node.next
                print(' ->', node.data, end = '')

        print()

        
# Test
arr = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

# insert
for a in arr:
    insert_chaining(a)

# print table
printTable(table)

# search
for i in arr:
    print(search_chaining(i), end = ' ')
    
# delete
for i in range(10, 20):
    delete_chaining(i)
    

# print table
print()
printTable(table)



########################################
# 결과
#
# table[ 0] : 44 -> 88 -> 11
# table[ 1] : 12 -> 23
# table[ 2] : 13
# table[ 3] :
# table[ 4] :
# table[ 5] : 16 -> 5
# table[ 6] : 94 -> 39
# table[ 7] :
# table[ 8] :
# table[ 9] : 20
# table[10] :
# 1 0 2 0 1 6 0 6 9 5 5
# table[ 0] : 44 -> 88
# table[ 1] : 23
# table[ 2] :
# table[ 3] :
# table[ 4] :
# table[ 5] : 5
# table[ 6] : 94 -> 39
# table[ 7] :
# table[ 8] :
# table[ 9] : 20
# table[10] :
########################################