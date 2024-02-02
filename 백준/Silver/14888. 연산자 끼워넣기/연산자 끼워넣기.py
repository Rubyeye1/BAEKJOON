import sys

N = int(sys.stdin.readline())                                   # N을 입력 받는다.
L = list(map(int, sys.stdin.readline().split()))                # L을 입력 받는다.
Y = list(map(int, sys.stdin.readline().split()))                # Y를 입력 받는다.

Max = float("-inf")                                             # Max와 Min을 각각 무한대의 음과 양의 값으로 지정해준다.
Min = float("inf")

def backtracking(depth, result):                                # 백트래킹으로 문제를 푸는데 depth와 result를 매개변수로 받는다.
    global Max, Min                                             # Max와 Min은 계속 비교해야하므로 global로 지정해준다.
    if depth == N-1:                                            # 만약 depth가 N-1이라는 것은 연산자를 전부 사용했다는 것이므로.
        Max = max(result, Max)                                  # Max와 Min을 비교해주고 return한다.
        Min = min(result, Min)
        return

    for i in range(4):                                          # 연산자가 4개이므로 for문을 4로 지정해서 만들어준다.
        temp = result                                           # 현재 result를 임시로 temp에 입력해주고.

        if Y[i] == 0:                                           # 만약 지정된 연산자의 개수가 0이면 밑을 실행하지 않고 바로 넘겨준다.
            continue
        if i == 0:                                              # 만약 i가 0이면 연산자가 더하기 이므로 result에 L 리스트의 다음 값을 더해준다.
            result = result + L[depth+1]
        elif i == 1:                                            # 만약 i가 1이면 연산자가 빼기 이므로 result에 L 리스트의 다음 값을 빼준다.
            result = result - L[depth+1]
        elif i == 2:                                            # 만약 i가 2이면 연산자가 곱하기 이므로 result에 L 리스트의 다음 값을 곱해준다.
            result = result * L[depth+1]
        else:                                                   # 만약 i가 3이면 연산자가 나누기 이므로 result에 L 리스트의 다음 값을 나누어준다.
            result = int(result / L[depth+1])

        Y[i] = Y[i] - 1                                         # 그리고 연산자 하나를 사용했으므로 그 연산자의 개수를 하나 빼준다.
        backtracking(depth + 1, result)                         # 이후 다음 인덱스와 result를 넘겨주고 backtraking함수를 다시 실행한다.
        Y[i] = Y[i] + 1                                         # 연산자의 개수와 result(지금까지의 누적값)을 원래대로 돌려준다.
        result = temp

backtracking(0, L[0])                                     # 초기값인 depth 0과 result L[0]으로 함수를 실행해준다.
print(Max)                                                      # 최종결과 출력!
print(Min)