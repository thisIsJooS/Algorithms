NO_OF_CHARS = 128
def shift_table(pattern):
    m = len(pattern)
    table = [m] * NO_OF_CHARS
    
    for i in range(m-1):
        table[ord(pattern[i])] = (m-1) - i
        
    return table


def search_horspool(T, P):
    n = len(T)
    m = len(P)
    table = shift_table(P)
    lastCharIndex = m-1
    
    while lastCharIndex < n:
        matchedCnt = 0
        while matchedCnt <= m-1 and T[lastCharIndex - matchedCnt] == P[(m-1) - matchedCnt]:
            matchedCnt += 1
        
        if matchedCnt == m:
            return lastCharIndex - (m-1)
        
        else:
            lastCharIndex += table[ord(T[lastCharIndex])]
    
    return -1

search_horspool("APPLEMANGOBANANAGRAPE", "BANANA")



#10
