from collections import deque                    # 디큐를 사용하기 위한 deque import.
def direction_change(d, c):                      # 방향을 전환하기 위한 direction_change 함수!
    if c == "L":                                 # 만약 왼쪽으로 방향 전환을 할 시 0(위쪽이면) 3(왼쪽). 1(오른쪽이면) 0(위쪽) 이렇게 나와야 하므로.
        d = (d - 1) % 4                          # 맞춰서 방향을 설정해주고.
    else:                                        # 만약 오른쪽으로 방향 전환을 할 시 0(위쪽이면) 1(오른쪽). 1(오른쪽이면) 2(아래쪽) 이렇게 나와야 하므로.
        d = (d + 1) % 4                          # 맞춰서 방향값을 설정해준다.
    return d

N = int(input())                                 # N을 입력받는다.
arr = [[0] * N for _ in range(N)]                # N x N 크기만큼 2차원 배열인 arr을 만들어둔다.

K = int(input())                                 # 사과의 개수 K를 입력받고.
for i in range(K):                               # 사과의 좌표를 입력받고.
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1                            # 그 좌표에 사과가 있음을 1로 표시를 해둔다.

times = {}                                       # 방향 전환 정보를 받을 컨테이너를 선언.
L = int(input())                                 # 방향 전환 정보의 개수를 입력받고.
for i in range(L):
    X, C = input().split()
    times[int(X)] = C                            # X(시간)을 키값으로, C(오른쪽(D), 왼쪽(L))을 입력받아서 컨테이너에 저장한다.

dy = [-1, 0, 1, 0]                               # 방향을 효율적으로 전환하기 위한 dy, dx를 만들어둔다.
dx = [0, 1, 0, -1]                               # 여기서 dy[0] dx[0] 이렇게 호출하게 되면 y에서 -1을 빼는 것 즉 위쪽 방향으로 한 칸 이동을 의미한다.
                                                 # 이런식으로 방향전환을 쉽게 할 수가 있다.

direction = 1                                    # 현재의 방향을 나타내는 direction 변수.
time = 1                                         # 현재 시간을 나타내는 time 변수.
x, y = 0, 0                                      # x, y 현재 좌표를 나타낸다.
snake = deque([[y,x]])                           # 그리고 꼬리를 만들어둬야 하는데 입력해둔값을 먼저 나가게끔 선입선출을 해야하므로 큐를 사용한다.
arr[y][x] = 2                                    # 현재 뱀의 위치를 모두 2로 표시한다.

while True:                                      # 반복문을 실행한다.
    y, x = y + dy[direction], x + dx[direction]  # 현재의 방향대로 한 칸을 이동한다.
    if 0 <= y < N and 0 <= x < N and arr[y][x] != 2: # 벽에 부딪히지 않거나 자기 자신의 위치로 이동하지 않으면.
        if not arr[y][x] == 1:                   # 그리고 지금 자리에 수박이 있지 않으면.
            delY, delX = snake.popleft()         # 꼬리를 하나 제거해야하므로 pop을 하고 delY, delX에 저장을 해주고.
            arr[delY][delX] = 0                  # 뱀의 위치가 지금 이동되었기 때문에 2에서 0으로 바꾸어준다.
        arr[y][x] = 2                            # 그리고 한 칸 이동한 현재 뱀의 위치를 2로 바꾸어준다.
        snake.append([y, x])                     # 이후 현재 위치를 큐에 추가해준다.
        if time in times.keys():                 # 방향 전환을 마지막에 고려해주는데 이는 X초가 끝난 뒤에 방향을 회전시키므로 반복문의 맨 아래쪽에 만들어준다.
            direction = direction_change(direction, times[time]) # 만약 times의 keys들중에 time이 존재하면, 그 키값에 맞는 결과값을 direction_change 함수에 넣어서 방향값을 리턴한다.
        time += 1                                # 초를 하나 증가시킨다.
    else:
        break

print(time)                                      # 마지막으로 최종 출력한다.
