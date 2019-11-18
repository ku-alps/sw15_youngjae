from collections import deque
import sys
import heapq
import math

sys.setrecursionlimit(10 ** 6)

def prim(v):
    q = []
    visited[v] = True
    d = 0
    cnt = 1 
    for i in cost_info[v]:
        heapq.heappush(q,i)

    while q:
        c,v = heapq.heappop(q)
        if not visited[v]:
            visited[v] = True
            cnt +=1
            d += c
            for i in cost_info[v]:
                heapq.heappush(q,i)
        if cnt == star_num:
            return d

star_num = int(sys.stdin.readline())
adj = deque([] for _ in range(star_num+1))
visited = [False]*(star_num+1)
star_info = deque()
star_info.append([0.0,0.0])

for i in range(1,star_num+1):
    star_x, star_y = map(float,sys.stdin.readline().split())
    star_info.append([star_x,star_y])

cost_info = deque([] for _ in range(star_num+1))
#cost 계산
for i in range(1,star_num+1):
    for j in range(i, star_num+1):
        cost = round(math.sqrt(((star_info[i][0] - star_info[j][0])**2) + ((star_info[i][1] - star_info[j][1])**2)),2)
        cost_info[i].append([cost,j])
        cost_info[j].append([cost,i])
print(prim(1))
