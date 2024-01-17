import sys

N = int(sys.stdin.readline())                                   # 배열의 크기 N을 입력받는다.
L = list(map(int, sys.stdin.readline().split()))                # 원소를 입력받는다.
S = int(sys.stdin.readline())                                   # 교환 횟수인 S를 입력받는다.

                                                                # 착안점 : 문제를 보고 생각해보니 결국 앞에 제일 큰 숫자가 오는게 사전순으로 뒷서는 조건에 가장 좋은것인데.
                                                                # 그러면 배열에서 일단 제일 큰 숫자가 맨 앞에 올 수 있으면 좋은 것이다.
                                                                # 그러므로 만약 교환가능횟수(S) 안에서 맨 앞에 max가 놓일 수 있는 상황이면.
                                                                # 무조건 max를 앞에 보내는것이 가장 사전순으로 뒷서는 것이므로 먼저 max의 인덱스를 구한 후에.
                                                                # S안에서 max가 가장 앞에 올 수 있는지부터 검사해본다.

for i in range(N):                                              # for문으로 i가 0부터 시작한다.
    mx = max(L[i:min(N, i+S+1)])                                # i부터 교환가능횟수로 최대한 앞으로 끌어올 수 있을 때까지의 범위 안의 max값을 설정.
    mxi = L.index(mx)                                           # 이 max값의 인덱스를 얻고.

    for j in range(mxi, i, -1):                                 # 이 max값의 인덱스에서 i까지 스왑하면서 범위안에서 가장 큰 값을 i까지 끌어온다.
        L[j-1], L[j] = L[j], L[j-1]

    S = S - (mxi-i)                                             # S에서 교환한 횟수를 빼준다.
    if S == 0:                                                  # 만약 S가 0이되면 종료.
        break

for i in range(N):                                              # 최종 결과 출력!
    print(L[i], end = " ")