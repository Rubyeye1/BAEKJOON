import sys                                          # sys.stdin.readline()을 사용하기 위한 sys import.
import heapq                                        # 우선순위 큐를 사용하기 위한 heapq.

heap = []                                           # heap 배열 생성.
n = int(sys.stdin.readline())                       # n 입력받기.
for i in range(n):                                  # n번 입력받는다.
    temp = int(sys.stdin.readline())                # 정수를 입력받고.
    if temp != 0:                                   # 만약 정수가 0이 아니면
        heapq.heappush(heap, (-temp))               # 지금은 최대 힙을 구현해야하므로 heapq.headpush로 파이썬의 최소 힙을 기반한 우선순위큐 삽입을 쓰되 -를 붙인다.
                                                    # 나중에 pop할때 -1을 곱해서 pop을 해주면 최대 힙처럼 쓸 수 있게 된다.
    else:                                           # 만약 정수가 0이면.
        try:                                        # 예외(에러)가 발생하지 않았을 경우 우선순위 큐의 루트노드를 pop하고 거기에 -1을 곱해서 출력한다.
            print(-1 * heapq.heappop(heap))
        except:                                     # 예외가 발생했을 경우 0을 출력한다.
            print(0)