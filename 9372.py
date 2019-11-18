from collections import deque

import sys

sys.setrecursionlimit(10 ** 6)

Test_case = int(sys.stdin.readline())
airplane_min_num = deque()
for i in range(0,Test_case):
    temp_type = sys.stdin.readline()
    country_num,airplan_type = map(int,temp_type.split())
    airplane_min_num.append(country_num-1)
    for j in range(0,airplan_type):
        temp = sys.stdin.readline()
 
#deque
try:
    while airplane_min_num:
        print(airplane_min_num.popleft())
except IndexError:
    print("ERROR")
