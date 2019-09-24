import sys
from collections import Counter

#가장많은애들이 가리키는거 빼야함 그리고 가장많은 애들을 가리키는거빼야함
people_target = []
people_result = []
key_idx_arr = []
people_num = int(sys.stdin.readline())
result_num = people_num

for i in range(0,people_num):
    input_number = int(sys.stdin.readline())
    people_target.append(input_number) 
    people_result.append([input_number,None])

result = Counter(people_target) 
max_num = max(result,key=result.get) #가장 많은애들이 가지고 있는 값

for  i in range(0,people_num): #서로가 가리키고 있는지 체크
    if i+1 == people_result[people_result[i][0]-1][0]:
        if people_result[people_result[i][0]-1][1] == None:
            if people_result[i][1] == None:
                result_num = result_num - 1 
                people_result[people_result[i][0]-1][1] = True
                people_result[i][1] = True


for i in range(0,people_num):
    if i == max_num-1: #가장 많은 애들이 가리키는거
        if people_result[i][1] == None :
            result_num = result_num - 1 
            people_result[i][1] = True
    

    if people_result[people_result[i][0]-1][0] == max_num: #가장 많은 애들을 가리키는거
        if people_result[i][1] == None:
            result_num = result_num - 1 
            people_result[i][1]  = True

if result_num == 1:
    print(result_num)
else:
    if result_num < people_num - result_num:
        print(people_num-result_num)
    else:
        print(result_num)