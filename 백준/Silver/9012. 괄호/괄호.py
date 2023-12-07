T = int(input())                                     # 정수 T를 입력받는다!

for i in range(T):                                   # T번 문자열을 입력받고 검사한다.
    stack = []                                       # 스택을 선언
    res = input()                                    # 괄호로 이루어진 문자열을 입력받고
    res = list(res)                                  # 하나씩 끊어서 리스트화한 후에 저장한다.
    temp = len(res)                                  # 리스트 안의 개수를 저장하는 temp

    for j in range(temp):                            # 리스트화한 res의 성분을 하나씩 검사한다.
        if res[j] == ")" and len(stack) == 0 :       # 만약 스택안에 아무것도 쌓여있지 않고 )가 들어오면
            print("NO")                              # VPS가 아니므로 NO를 반환한 후에 break로 반복문을 끝낸다
            break

        if res[j] == "(":                            # 위의 경우가 아니면서 (가 들어온 경우에는
            stack.append("(")                        # 스택에 (를 하나씩 쌓는다.

        else:                                        # )가 들어오면 pop으로 스택에 쌓인 (를 하나씩 꺼낸다.
            stack.pop()

        if j == temp -1 and len(stack) >= 1:         # 만약 맨 위의 if조건문에서 걸리지 않고 마지막까지 왔는데 스택에 (가 한 개 이상 쌓여있다는 것은
            print("NO")                              # VPS가 아님을 뜻하기 때문에 NO를 반환한다.
        elif j == temp -1 and len(stack) == 0:       # 맨 위의 if문에서 걸리지 않고 마지막까지 왔는데 스택에 아무것도 없다는 것은 개수가 딱 떨어진 VPS를 의미하므로
            print("YES")                             # YES를 반환한다.