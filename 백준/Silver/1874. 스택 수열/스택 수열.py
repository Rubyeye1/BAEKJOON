n = int(input())

stack = []
result = []
mx = 0
for i in range(n):
    temp = int(input())
    for j in range(mx, temp):
        stack.append(j+1)
        result.append("+")
    if temp < stack[-1]:
        print("NO")
        break
    else:
        stack.pop()
        result.append("-")
    if mx < temp:
        mx = temp
    if i == n-1:
        for k in range(len(result)):
            print(result[k])