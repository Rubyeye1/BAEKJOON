import sys                                      # sys.stdin.readline()을 사용하기 위한 sys import.
import heapq                                    # 우선순위 큐를 파이썬에서 사용하기 위한 heapq import.

heap = []                                       # heap 배열 만들기.
n = int(sys.stdin.readline())                   # n 입력받기.
for i in range(n):                              # n번 반복하여 우선순위 큐에 정수를 삽입.
    temp = int(sys.stdin.readline())
    heapq.heappush(heap, temp)            # heappush로 우선순위 큐로 삽입.

result = 0                                      # 최종 결과인 result 변수.

for i in range(1, n):                           # 최솟값 두 개를 합치고 그걸 다시 우선순위 큐에 넣어서 최소 힙이 되도록 정렬한다.
                                                # 반복문이 왜 1부터 시작하냐면 마지막에 2개가 남았을 경우 비교할 것 없이 그냥 합치면 끝나서 비교횟수가 하나 필요없기 때문이다.
    a = heapq.heappop(heap)                     # 최솟값을 하나 빼고.
    b = heapq.heappop(heap)                     # 그 다음 최솟값을 빼고.
    temp2 = a + b                               # 더한 다음.
    result = result + temp2                     # 일단 최종결과값에 합친 횟수를 더해주고.
    heapq.heappush(heap, temp2)           # 합친 횟수를 다시 우선순위 큐에 넣어서 최소 힙으로 정렬한다.

print(result)                                   # 최종 결과값을 출력한다.