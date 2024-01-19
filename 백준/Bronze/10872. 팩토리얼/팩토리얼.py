import sys
N = int(sys.stdin.readline())

def factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * factorial(N-1)
    
if N == 0:
    print(1)
else:
    result = factorial(N)
    print(result)
