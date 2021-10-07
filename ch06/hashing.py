M = 10
table = [None] * M

def hashFn(key):
    return key % M


def lp_insert(key):
    count = M
    id = hashFn(key)
    
    while count > 0 and table[id] != None and table[id] != -1:
        id = (id + 1 + M) % M
        count -= 1
    
    if count > 0:
        table[id] = key
        
    return


def lp_search(key):
    count = M
    id = hashFn(key)
    
    while count > 0:
        if table[id] == key:
            return table[id]
        
        if table[id] == None:
            return None
        
        id = (id + 1 + M) % M
        count -= 1
    
    return 


def lp_delete(key):
    count = M
    id = hashFn(key)
    
    while count > 0:
        if table[id] == key:
            table[id] = -1
            return
        
        if table[id] == None:
            return
        
        id = (id + 1 + M) % M
        count -= 1
        
    return 

print('   최초 : ', table)
lp_insert(45); print('45 삽입 : ', table)
lp_insert(27); print('27 삽입 : ', table)
lp_insert(88); print('88 삽입 : ', table)
lp_insert(9); print(' 9 삽입 : ', table)
lp_insert(71); print('71 삽입 : ', table)
lp_insert(60); print('60 삽입 : ', table)
lp_insert(46); print('46 삽입 : ', table)
lp_insert(38); print('38 삽입 : ', table)
lp_insert(24); print('24 삽입 : ', table)
lp_delete(60); print('60 삭제 : ', table)
lp_insert(20); print('20 삽입 : ', table)
print('46 탐색 : ', lp_search(46))


###########################################################################
# 결과
#
#    최초 :  [None, None, None, None, None, None, None, None, None, None]
# 45 삽입 :  [None, None, None, None, None, 45, None, None, None, None]
# 27 삽입 :  [None, None, None, None, None, 45, None, 27, None, None]
# 88 삽입 :  [None, None, None, None, None, 45, None, 27, 88, None]
#  9 삽입 :  [None, None, None, None, None, 45, None, 27, 88, 9]
# 71 삽입 :  [None, 71, None, None, None, 45, None, 27, 88, 9]
# 60 삽입 :  [60, 71, None, None, None, 45, None, 27, 88, 9]
# 46 삽입 :  [60, 71, None, None, None, 45, 46, 27, 88, 9]
# 38 삽입 :  [60, 71, 38, None, None, 45, 46, 27, 88, 9]
# 24 삽입 :  [60, 71, 38, None, 24, 45, 46, 27, 88, 9]
# 60 삭제 :  [-1, 71, 38, None, 24, 45, 46, 27, 88, 9]
# 20 삽입 :  [20, 71, 38, None, 24, 45, 46, 27, 88, 9]
# 46 탐색 :  46
###########################################################################


