N = int(input())

result1 = 0
result0 = 0
for i in range(N):
    temp = int(input())
    if temp == 1:
        result1 = result1 + 1
    else:
        result0 = result0 + 1

if result1 > result0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")