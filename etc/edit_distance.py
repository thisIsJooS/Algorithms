a = input()
b = input()

def edit_distance(a, b):
    n = len(a)
    m = len(b)
    arr = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                arr[i][j] = j
                continue
            if j==0:
                arr[i][j] = i
                continue

            if a[i-1] == b[j-1]:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j]) + 1

    return arr[n][m]

print(edit_distance(a, b))
