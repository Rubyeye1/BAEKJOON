import math
import sys

x, y = map(int, sys.stdin.readline().split())
result = 0

if x == 1:
    result = y % 7
elif x == 2:
    result = (y+31) % 7
elif x == 3:
    result = (y+59) % 7
elif x == 4:
    result = (y+90) % 7
elif x == 5:
    result = (y+120) % 7
elif x == 6:
    result = (y+151) % 7
elif x == 7:
    result = (y+181) % 7
elif x == 8:
    result = (y+212) % 7
elif x == 9:
    result = (y+243) % 7
elif x == 10:
    result = (y+273) % 7
elif x == 11:
    result = (y+304) % 7
elif x == 12:
    result = (y+334) % 7

if result == 1:
    print("MON")
elif result == 2:
    print("TUE")
elif result == 3:
    print("WED")
elif result == 4:
    print("THU")
elif result == 5:
    print("FRI")
elif result == 6:
    print("SAT")
elif result == 0:
    print("SUN")