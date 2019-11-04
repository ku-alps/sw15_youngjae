import sys
house_num, router_num =  map(int,sys.stdin.readline().split()) # 집의 개수, 공유기의 개수
result = 0
distance_arr = []

for i in range(0,house_num):
    distance_arr.append(int(sys.stdin.readline()))

distance_arr = sorted(distance_arr)


min_val = 1
max_val = distance_arr[house_num-1]

while min_val <= max_val:
    
    cnt = 1
    avg = int((min_val+max_val)/2)
    temp = distance_arr[0]

    for i in range(1,house_num):
        if distance_arr[i]-temp >= avg:
            cnt += 1
            temp = distance_arr[i]

    if cnt >= router_num:
        result = avg
        min_val = avg+1
    else:
        max_val = avg-1

print(result)