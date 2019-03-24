people_num = int(input())
people_arr = [[0]*3 for i in range(0,people_num)]
people_grade_txt = "" 


#========================================================================================
# 사람에대한 키,몸무게 입력
#========================================================================================
for i in range(0,people_num):
    people_info = input()
    people_info = people_info.split()
    people_arr[i][0] = people_info[0]
    people_arr[i][1] = people_info[1]
    people_arr[i][2] = 1
#========================================================================================


for i in range(0,people_num):
    for j in range(0,people_num):
        if(i != j):
            #========================================================================================
            #  자기 자신보다 몸무게,키 두개다 큰 사람이 있으면 순위를 더해준다.
            #========================================================================================
            if(people_arr[i][0] < people_arr[j][0] and people_arr[i][1] < people_arr[j][1]):
                people_arr[i][2] +=1
             #========================================================================================

for i in range(0,people_num):
    people_grade_txt  += str(people_arr[i][2])+" "

print(people_grade_txt)