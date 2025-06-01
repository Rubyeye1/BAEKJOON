import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

k = input()

if len(k) <= 2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    temp = int(k[0]) - int(k[1])
    chk = 0

    for i in range(1, len(k) - 1):
        if int(k[i]) - int(k[i + 1]) != temp:
            chk = 1
            break
                
    if chk == 0:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    else:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")