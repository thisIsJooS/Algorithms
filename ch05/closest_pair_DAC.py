def closest_pair_DAC(P):
    n = len(P)
    mid = n//2
    
    if n <= 3:
        return closest_pair_BF(P)
    
    dmin_left = closest_pair_DAC(P[:mid])
    dmin_right = closest_pair_DAC(P[mid:])
    
    dmin = min(dmin_left, dmin_right)
    
    Pm = []
    
    for i in range(n):
        if abs(P[i][0] - P[mid][0]) < dmin:
            Pm.append(P[i])
            
    dmin_strip = strip_closest_pair(Pm, dmin)
    
    return min(dmin_strip, dmin)


def strip_closest_pair(P, d):
    n = len(P)
    P.sort(key = lambda point : point[1])
    dmin = d
    
    for i in range(n-1):
        j = i+1
        while j < n and P[j][1] - P[i][1] < dmin:
            dij = distance(P[j], P[i])
            if dij < dmin:
                dmin = dij
        j += 1
    
    return d


def distance(A, B):
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2) ** (0.5)
    

def closest_pair_BF(P):
    n = len(P)
    dmin = float('inf')
    
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(P[i], P[j])
            if dmin > dist:
                dmin = dist
                
    return dmin

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
p.sort(key = lambda point : point[0])
closest_pair_DAC(p)

