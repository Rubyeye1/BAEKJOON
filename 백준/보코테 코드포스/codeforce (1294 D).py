import sys                                          # sys.stdin.readline 함수를 사용하기 위한 sys import.

q, x = map(int, sys.stdin.readline().split())       # q, x를 입력받는다.

map = {}                                            # 맵을 사용하기 위한 map 선언.
mex = 0                                             # mex는 0으로 지정해놓는다.
for _ in range(q):                                  # q번 입력받는다.
    y = int(sys.stdin.readline())                   # y로 입력받고.
    if y % x in map:                                # 만약 y를 x로 나눈 값이 map의 키로 존재하면
        if y % x + x*map[y%x] in map:               # 그리고 y를 x로 나눈 값에 x 곱하기 map의 밸류값이 맵에 존재하면
            map[y % x + x * map[y%x]] += 1          # 맵의 키값에 해당하는 밸류값을 1 증가한다.
        else:                                       # y를 x로 나눈 값에 x 곱하기 map의 밸류값이 맵에 존재하지 않으면.
            map[y % x + x * map[y%x]] = 1           # 맵의 키값을 설정하고 1로 밸류값을 설정한다.
        map[y % x] += 1                             # 최소부터 차곡차곡 쌓기 위해서 map의 key값을 y%x로 하고 1을 더한다.
    else:                                           # y를 x로 나눈 값이 map의 키로 존재하지 않으면.
        map[y % x] = 1                              # map의 key값을 y%x로 하고 1로 지정한다.

while mex in map:
    mex = mex + 1
print(mex)                                          # mex값을 출력!.