#String Matching - brute force

def sm(T, P):  
    for i in range(len(T)):
        j = 0 
        while j < len(P) and T[i+j] == P[j]:
            j += 1
        if j == len(P):
            return i    # 일치하는 패턴의 인덱스 반환
    return -1

T = "matsuur"
P = "suu"

print(sm(T,P))

#######
# 결과
#
# 3
########