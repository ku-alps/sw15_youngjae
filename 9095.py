import sys 
from collections import deque 

sys.setrecursionlimit(10 ** 6)

def dp(d_val):
    Q = deque([(d_val)]) 
    cnt = 0
    while Q:
        
        d_val = Q.popleft()
        if d_val == 0:
            cnt = cnt+1
        if d_val-1 >= 0:
            Q.append(d_val-1)
        if d_val-2 >= 0:
            Q.append(d_val-2)
        if d_val-3 >= 0:
            Q.append(d_val-3)
    
    print(cnt)

test_case = int(sys.stdin.readline())
test_arr = [0]
for i in range (1,test_case+1):
    test_num = int(sys.stdin.readline())
    test_arr.append(test_num)

for i in range (1,len(test_arr)):
    dp(test_arr[i])