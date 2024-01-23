import sys
def hanoi(N, start, to, end):                           # 재귀함수 정의
    if N == 1:                                          # N이 1일때에는 원반이 한 개 남았다는 뜻이므로 이는 출발지에서 원하는 목적지로 그냥 이동해주면 되기 때문에 print로 출력해준다.
        print(start, end)
    else:                                           
        hanoi(N-1, start, end, to)                      # 원반이 1개보다 많이 남았을 경우 일단 출발지의 N-1개의 원반을 경유지의 원반에 다 옮겨야 하기 때문에 재귀함수로 경유지를 목적지로 호출해준다.
        print(start, end)                               # 만약 경유지로 N-1개의 원반을 다 옮겼으면 제일 큰 한 개의 원반이 남았을텐데 이는 목적지로 그냥 옮겨준다.
        hanoi(N-1, to, start, end)                      # 제일 큰 원반을 옮겼으면 경유지에 남은 N-1개의 원반을 start를 경유지로 삼아 원래의 목적지로 옮겨준다.


N = int(sys.stdin.readline())                           # N 입력받기.
print(2 ** N - 1)                                       # 2의 n승에서 1을 빼면 실행값이 나온다.
hanoi(N, 1, 2, 3)                         # N을 입력받은 재귀함수 실행.