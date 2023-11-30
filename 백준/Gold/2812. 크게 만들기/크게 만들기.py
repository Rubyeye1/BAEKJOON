N, K = map(int, input().split())
num = list(input())
stack = []
res = K
"""
for i in range(len(num)):
    if K == 0 :
        while i < len(num):
            stack.append(num[i])
            i = i+1
        break
    elif i == 0 :
        stack.append(num[i])
    else :
         if len(stack) == 1 :
            if K == 0:
                break
            if num[i] > stack[0]:
                print(stack.pop())
                K = K-1
         else:
            for j in range(len(stack) - 1, -1, -1):
                if K == 0:
                    break
                if num[i] > stack[j]:
                    print(stack.pop())
                    K = K - 1
         stack.append(num[i])
"""
for i in range(len(num)):
    while len(stack) > 0 and stack[-1] < num[i] and K > 0:
        stack.pop()
        K = K-1
    stack.append(num[i])

print(''.join(stack[:N-res]))
