K = int(input())                         # 정수 K

stack = []                               # 스택 선언
for i in range(K):                       # K번 정수를 입력받는다.
    res = int(input())
    if res != 0:                         # 만약 입력받은 정수가 0이 아니라면
        stack.append(res)                # 스택에 정수를 넣는다
    else:                                # 만약 입력받은 정수가 0이라면
        stack.pop()                      # pop한다.

temp = len(stack)                        # 스택의 성분들을 전부 합해서 출력해야하므로 스택의 몇 개가 들어있는지를 저장할 temp 변수 선언
result = 0                               # 최종 결과 result 선언.

for j in range(temp):                    # 스택에 들어있는 개수만큼 반복해서
    result = result + stack[j]           # 최종결과를 만든다.

print(result)                            # 최종결과를 출력한다!