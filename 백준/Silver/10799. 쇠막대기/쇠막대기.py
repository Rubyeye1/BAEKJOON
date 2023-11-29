str = input()                                  # 먼저 괄호를 입력받는다.

stack = []                                     # 스택 선언.
result = 0                                     # 총 개수 변수 선언.
for i in range(len(str)):                      # 입력받은 괄호에 대하여
    if str[i] == '(':                          # 만약 (면 스택에 추가한다.
        stack.append('(')
    elif str[i] == ')' and str[i-1] == '(' :   # )인데 그 전이 (면 레이저를 쏘는 것이므로 (하나를 pop한 후의 총 개수에 스택의 개수를 더해준다.
        stack.pop()
        result = result + len(stack)
    elif str[i] == ')' and str[i-1] == ')':    # )인데 그 전이 )면 레이저를 쏘는 것이 아닌 쇠파이프 하나를 종료했다는 뜻이므로 총 개수에 +1이 된다.
        stack.pop()
        result = result + 1

print(result)
