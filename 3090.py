import sys
integer_num,operation_num = map(int,sys.stdin.readline().split())
initial_arr = list(map(int,sys.stdin.readline().split()))
temp_arr = []

for i in range(0,len(initial_arr)):
    prev_val = 0
    next_val = 0
    if i-1 >= 0:
        prev_val = abs(initial_arr[i]-initial_arr[i-1])
    if i+1 < len(initial_arr):
        next_val = abs(initial_arr[i+1]-initial_arr[i])

    val = initial_arr[i]

    temp_arr.append([prev_val,val,next_val])
for i in range(0,operation_num):

    max_index = 0
    max_num = 0
    max_val = 0
    for j in range (0,len(initial_arr)):
        for k in range (0,2):
            if k == 1: 
                continue
            else:
                if max_num <= temp_arr[j][k]:
                    if max_val <= temp_arr[j][1]:
                        max_num = temp_arr[j][k]
                        max_index = j
                        max_val = temp_arr[j][1]
    
    temp_arr[max_index][1] -=1

    if max_index+1 < len(initial_arr):
        temp_arr[max_index+1][0] =  abs(temp_arr[max_index+1][1]-temp_arr[max_index][1])
        temp_arr[max_index][2] = temp_arr[max_index+1][0]

    if max_index-1 >= 0:
        temp_arr[max_index-1][2] =  abs(temp_arr[max_index-1][1]-temp_arr[max_index][1])
        temp_arr[max_index][0] = temp_arr[max_index-1][2]

#print(temp_arr)

for i in range(integer_num):
    print(temp_arr[i][1],end=' ')