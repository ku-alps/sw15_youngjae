#1.25 5 2, 2-14-11-21-17   2.25 5 2 ,17-19-22-23-24
import math
import sys

target_distance, stone_island_num, remove_num = map(int,sys.stdin.readline().split()) #돌섬으로부터 탈출구의 거리, 작은 돌섬의 수, 제거할 수 있는 작은 돌섬의 수
distance_info = []
difference_arr = [] 
for i in range(0,stone_island_num):
    distance_info.append(int(input()))

distance_info.sort()
distance_info.append(target_distance)
min = 0
max = distance_info[stone_island_num]
while min <= max:
    cnt = 0
    avg = int((min+max)/2)
    pos = 0
    for i in range (1,len(distance_info)):
        if distance_info[i] - distance_info[pos] >= avg:
            cnt = cnt +1
        else:
            pos = i

    if cnt <= (stone_island_num-remove_num):
        min = avg+1
        result = avg
    else:
        max = avg-1
print(result)