# LIS, Longest Increasing Subsequence
# 가장 긴 증가하는 부분수열

arr = [10, 20, 10, 30, 20, 50]
dp = [1] * len(arr)

for i in range(1, len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(dp)

# [1, 2, 1, 3, 2, 4]