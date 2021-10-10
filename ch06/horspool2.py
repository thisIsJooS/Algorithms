# 패턴의 모든 위치 찾기 (2개 이상일 시)

NO_OF_CHARS = 128

def getShiftTable(pattern):
    m = len(pattern)
    table = [m] * NO_OF_CHARS
    
    for i in range(m-1):
        table[ord(pattern[i])] = m-1 - i
    
    return table


def horspool_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lastCharIndex = m-1
    table = getShiftTable(pattern)
    
    while lastCharIndex < n:
        matchedCnt = 0
        while matchedCnt < m and text[lastCharIndex - matchedCnt] == pattern[(m-1) - matchedCnt]:
            matchedCnt += 1
        
        if matchedCnt == m:
            print(lastCharIndex - (m-1))
            
        lastCharIndex += table[ord(text[lastCharIndex])]
            
    return

text = "MAFFANAFFANAFFA"

horspool_search(text, 'FFA')


# 2 7 12