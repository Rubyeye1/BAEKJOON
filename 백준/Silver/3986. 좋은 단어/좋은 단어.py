N = int(input())                         # 정수 N.


result = 0                               # 좋은 단어가 몇 개 인지 저장할 result 변수를 선언
for i in range(N):                       # N개의 단어를 입력받고 검사한다.

    stack = []                           # 스택을 선언
    res = input()
    res = list(res)                      # 입력받은 단어를 리스트에 한 단어씩 쪼개서 저장.
    temp = len(res)                      # res를 검사하기 위해서 필요한 res의 길이를 저장하는 변수 temp

    for j in range(temp):                # res를 검사한다.
        if len(stack) == 0:              # 만약 스택에 아무것도 없을 때 반복문이 돌아가고 있으면
            stack.append(res[j])         # 그 단어를 스택에 넣는다.
        else:                            # 스택에 무엇인가 있는경우
            if stack[-1] == res[j]:      # 그 성분이 현재의 res[j]와 같으면
                stack.pop()              # pop 한다.
            else:                        # 그 성분이 현재의 res[j]와 다르면 ex) A, B
                stack.append(res[j])     # 스택에 res[j]를 넣는다.

    if len(stack) == 0:                  # 위에서 단어를 검사한 후에 스택의 길이가 0이라는 말은 즉 좋은 단어임을 뜻하기 때문에
        result = result + 1              # 최종적으로 출력할 result의 개수를 하나 증가시킨다!

print(result)                            # 좋은 단어의 개수를 출력한다.