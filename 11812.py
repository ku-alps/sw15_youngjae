import sys
node_num,num,ex_num = map(int,sys.stdin.readline().split()) #node_num = 노드의 개수 num = k진트리 ex_num = 구하고 싶은 거리의 개수

def get_Parent(x,k):
    return int((x+k-2)/k)

distance_arr = []

for i in range(0,ex_num):
    x,y = map(int,sys.stdin.readline().split())
    distance = 0
    if num == 1:
        distance = abs(x-y)
        distance_arr.append(distance)
        continue
    else:
        while x != y:
            while x > y:
                distance +=1
                x = get_Parent(x,num)
            while x < y:
                distance +=1
                y = get_Parent(y,num)
        
    distance_arr.append(distance)

for i in distance_arr:
    print(i)