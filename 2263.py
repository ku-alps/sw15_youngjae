import sys

sys.setrecursionlimit(10 ** 6)

def pre_order_search(i_start,i_end,p_start,p_end):
    global in_order,post_order,pre_order

    if i_start > i_end or p_start > p_end:
        return

    root = post_order[p_end]
    pre_order.append(root)
    root_idx = in_order_idx[root]
    left    =  root_idx-i_start

    pre_order_search(i_start, root_idx-1, p_start, p_start+left-1)
    pre_order_search(root_idx+1, i_end, p_start+left, p_end-1)

node_num = int(sys.stdin.readline()) #node_num = 노드의 개수

in_temp   = sys.stdin.readline()
post_temp = sys.stdin.readline()

in_order   = list(map(int,in_temp.split()))
post_order = list(map(int,post_temp.split()))
pre_order = []

in_order.insert(0,0)
post_order.insert(0,0)

in_order_idx = [0]*(node_num+1)
for i in range(1,node_num+1):
    in_order_idx[in_order[i]] = i

pre_order_search(1,node_num,1,node_num)

for i in range(0,node_num-1):
    print(pre_order[i],end=' ')

print(pre_order[node_num-1])