K, N, M = map(int, input().split())
temp = K * N
if temp > M:
    result = temp - M
    print(result)
else:
    print(0)