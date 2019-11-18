from collections import deque
from itertools import chain
import sys
import heapq

sys.setrecursionlimit(10 ** 6)
sum_cost = 0

def parent_find(v):

    if parent[v] != v:
        parent[v] = parent_find(parent[v])

    return parent[v]

def union(v,u,c):

    global sum_cost
    root1 = parent_find(v)
    root2 = parent_find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            rank[root1] += 1
            parent[root2] = root1
        else:
            rank[root2] += 1
            parent[root1] = root2

        sum_cost += c

computer_num = int(sys.stdin.readline())
connect_line_num = int(sys.stdin.readline())
adj = []
visited = [False]*(computer_num+1)
parent= [i for i in range(0,computer_num+1)]
rank = [1]*(computer_num+1)

for i in range(1,connect_line_num+1):
    a,b,c = map(int,sys.stdin.readline().split())
    heapq.heappush(adj,deque([c,b,a]))

try:
    while adj:
        adj_info = heapq.heappop(adj)
        cost,start,end = adj_info[0],adj_info[1],adj_info[2]
        union(start,end,cost)
except IndexError:
    print("ERROR")

print(sum_cost)
#print(rank)
#print(parent)