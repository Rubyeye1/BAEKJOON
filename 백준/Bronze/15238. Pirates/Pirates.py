import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
L = input()
L = list(L)
result = [0] * 26

for i in range(len(L)):
    if L[i] == "a":
        result[0] += 1
    elif L[i] == "b":
        result[1] += 1
    elif L[i] == "c":
        result[2] += 1
    elif L[i] == "d":
        result[3] += 1
    elif L[i] == "e":
        result[4] += 1
    elif L[i] == "f":
        result[5] += 1
    elif L[i] == "g":
        result[6] += 1
    elif L[i] == "h":
        result[7] += 1
    elif L[i] == "i":
        result[8] += 1
    elif L[i] == "j":
        result[9] += 1
    elif L[i] == "k":
        result[10] += 1
    elif L[i] == "l":
        result[11] += 1
    elif L[i] == "m":
        result[12] += 1
    elif L[i] == "n":
        result[13] += 1
    elif L[i] == "o":
        result[14] += 1
    elif L[i] == "p":
        result[15] += 1
    elif L[i] == "q":
        result[16] += 1
    elif L[i] == "r":
        result[17] += 1
    elif L[i] == "s":
        result[18] += 1
    elif L[i] == "t":
        result[19] += 1
    elif L[i] == "u":
        result[20] += 1
    elif L[i] == "v":
        result[21] += 1
    elif L[i] == "w":
        result[22] += 1
    elif L[i] == "x":
        result[23] += 1
    elif L[i] == "y":
        result[24] += 1
    elif L[i] == "z":
        result[25] += 1

temp = max(result)

for i in range(len(result)):
    if result[i] == temp:
        temp = i
        break
rt = max(result)

if temp == 0:
    print("a " + str(rt))
elif temp == 1:
    print("b " + str(rt))
elif temp == 2:
    print("c " + str(rt))
elif temp == 3:
    print("d " + str(rt))
elif temp == 4:
    print("e " + str(rt))
elif temp == 5:
    print("f " + str(rt))
elif temp == 6:
    print("g " + str(rt))
elif temp == 7:
    print("h " + str(rt))
elif temp == 8:
    print("i " + str(rt))
elif temp == 9:
    print("j " + str(rt))
elif temp == 10:
    print("k " + str(rt))
elif temp == 11:
    print("l " + str(rt))
elif temp == 12:
    print("m " + str(rt))
elif temp == 13:
    print("n " + str(rt))
elif temp == 14:
    print("o " + str(rt))
elif temp == 15:
    print("p " + str(rt))
elif temp == 16:
    print("q " + str(rt))
elif temp == 17:
    print("r " + str(rt))
elif temp == 18:
    print("s " + str(rt))
elif temp == 19:
    print("t " + str(rt))
elif temp == 20:
    print("u " + str(rt))
elif temp == 21:
    print("v " + str(rt))
elif temp == 22:
    print("w " + str(rt))
elif temp == 23:
    print("x " + str(rt))
elif temp == 24:
    print("y " + str(rt))
elif temp == 25:
    print("z " + str(rt))