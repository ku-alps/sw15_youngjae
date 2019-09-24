people_num = int(input())  #출입기록 수
result = dict()  #결과담을 dictionary
for i in range(0,people_num): 
    people_info = input()
    temp = people_info.split() #temp[0] = 사람 이름 ,temp[1] = 출입 체크

    if temp[1] == "enter": #출입일 경우 사람이름을 키로 가지는 dictionary 요소 추가
        result[temp[0]] = None
    else: 
        del result[temp[0]] 

for j in sorted(result.keys(),reverse=True):
    print(j)
