# 투포인터를 활용한 부분합이 5인 부분 연속 수열의 개수 구하기

n = 5
m = 5
data = [1, 2, 3, 2, 5]

interval_sum = 0
count = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
        
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    
    print(f'interval_sum : {interval_sum}, end : {end}')
    interval_sum -= data[start]
    
print(count)