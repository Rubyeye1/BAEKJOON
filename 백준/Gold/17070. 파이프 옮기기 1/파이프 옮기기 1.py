import sys
def Recursive(x, y, shape):                                                                         # 재귀함수 선언. shape 0은 가로 1은 세로 2는 대각선으로 상황을 지정.
    global result, N                                                                                # 함수에서 최종결과값과 N을 사용해야하므로 global로 받기.
    if x > N-1 or y > N-1:                                                                          # 만약 좌표 x,y가 범위를 벗어나면 return
        return
    if x == N-1 and y == N-1:                                                                       # 만약 좌표 x,y가 최종목적지에 도착하면 result + 1
        result = result + 1
    if y + 1 < N and a[x][y+1] == 0 and (shape == 0 or shape == 2):                                 # shape가 가로나 대각선일때 가로로 움직이는게 가능하므로 검사해주고 재귀함수 호출.
        Recursive(x, y+1, 0)
    if x + 1 < N and a[x+1][y] == 0 and (shape == 1 or shape == 2):                                 # shape가 세로나 대각선일때 세로로 움직이는게 가능하므로 검사해주고 재귀함수 호출.
        Recursive(x+1, y, 1)
    if x + 1 < N and y + 1 < N and a[x + 1][y] == 0 and a[x][y + 1] == 0 and a[x + 1][y + 1] == 0:  # 모든 shape에서 대각선은 가능하므로 범위를 벗어나는지 검사해주고 재귀함수 호출.
        Recursive(x + 1, y + 1, 2)

N = int(sys.stdin.readline())                                                                       # N 입력 받기.

a = [list(map(int, input().split())) for _ in range(N)]                                             # 2차원 배열 입력 받기.

result = 0                                                                                          # 최종결과값.
if a[N-1][N-1] == 1:
    print(0)                                                                                        # 만약 최종목적지에 1이 존재하면 그냥 0 출력.
else:
    Recursive(0, 1, 0)                                                                  # (N-1, N-1)에 도착하는 것이 목표이므로 초기값(꼬리)좌표인 (0, 1)로 지정하고 재귀함수 사용.
    print(result)                                                                                   # 최종 결과 출력!