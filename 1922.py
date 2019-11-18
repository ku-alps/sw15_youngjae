from collections import deque
import sys
import heapq

sys.setrecursionlimit(10 ** 6)

def prim(v):
    q = []
    visited[v] = True
    d = 0
    cnt = 1 
    for i in adj[v]:
        heapq.heappush(q,i)

    while q:
        c,v = heapq.heappop(q)
        if not visited[v]:
            visited[v] = True
            cnt +=1
            d += c
            for i in adj[v]:
                heapq.heappush(q,i)
        if cnt == computer_num:
            return d

computer_num = int(sys.stdin.readline())
connect_line_num = int(sys.stdin.readline())
adj = deque([] for _ in range(computer_num+1))
visited = [False]*(computer_num+1)

for i in range(1,connect_line_num+1):
    a,b,c = map(int,sys.stdin.readline().split())
    adj[a].append([c,b])
    adj[b].append([c,a])

print(prim(1))
