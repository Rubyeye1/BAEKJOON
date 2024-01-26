import sys

N = int(sys.stdin.readline())                                   # N을 입력받는다.
a = [list(map(int, input().split())) for _ in range(N)]         # 2차원 배열을 입력받는다.

white = 0                                                       # 하얀색 색종이의 수 white.
blue = 0                                                        # 파란색 색종이의 수 blue.

def recur(x, y, N):                                             # 분할정복으로 문제를 해결한다.
    global white, blue                                          # 최종 결과값을 안에서 증가 시켜줘야 하기 때문에 global로 지정한다.
    for i in range(x, x+N):                                     # 예제와 같이 N이 8이 들어오면 x, y 좌표를 0부터 8까지 for문을 통해서 검사한다.
        for j in range(y, y+N):
            if a[x][y] != a[i][j]:                              # 이때 검사 하는 것은 a[x][y] 즉 지금 범위 상태내의 가장 왼쪽 위의 원소와 그 범위 안의 다른 원소들이 같은지 다른지 검사한다.
                recur(x, y, N // 2)                             # 만약 다르다면 범위를 4개로 쪼개서 분할정복으로 재귀함수를 이용하여 다시 검사하는데.
                recur(x, y+N // 2, N // 2)                      # 이 때 x, y, N//2(1사분면) x, y+N//2, N//2(2사분면) x+N//2, y, N//2(3사분면) x+N//2, y+N//2, N//2(4사분면).
                recur(x+N // 2, y, N // 2)                      # 이렇게 4개의 N/2 x N/2의 색종이로 나누는 식으로 재귀함수를 구성해준다.
                recur(x+N // 2, y+N // 2, N // 2)
                return

    if a[x][y] == 0:                                            # 위의 반복문을 다 검사하고 여기까지 내려왔다는 것은 범위 안의 원소들이 전부 같은 색이라는 의미이므로.
        white = white + 1                                       # 색깔에 맞게 +1을 해준다.
    else:
        blue = blue + 1

recur(0, 0, N)
print(white)                                                    # 최종 결과 출력!
print(blue)
