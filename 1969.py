input_info = input() #입력정보 (DNA수,문자열 길이)
temp = input_info.split() #temp[0] = DNA 수  ,temp[1] = 문자열 길이
dna_info = [] #dna 정보
result_alphabet = [] #최종 DNA
sum_distance = 0 #Hamming Distance

#====================================================================================
# DNA 정보 입력 (시작)
#====================================================================================
for i in range (int(temp[0])):  
    temp_info = list(input())
    dna_info.append(temp_info)
#====================================================================================
# DNA 정보 입력 (끝)
#====================================================================================


for i in range (int(temp[1])):
    a_count,c_count,g_count,t_count = 0,0,0,0 #각 알파벳 초기화 

    for j in dna_info:
        if j[i] == "A":
            a_count += 1 
        elif j[i] == "C":
            c_count += 1
        elif j[i] == "G":
            g_count += 1
        elif j[i] == "T":
            t_count += 1 

    max_val = max([a_count,c_count,g_count,t_count]) #가장 많이 나온 알파벳 개수
    max_index = [a_count,c_count,g_count,t_count].index(max_val) #가장 많이 나온 알파벳 인덱스
    sum_distance += int(temp[0])-max_val #hamming distance 계산

    #최종 알파벳 추가 부분
    if max_index == 0:
        result_alphabet.append("A")
    elif max_index == 1:
        result_alphabet.append("C")
    elif max_index == 2:
        result_alphabet.append("G")
    elif max_index == 3:
        result_alphabet.append("T")

print(''.join(result_alphabet))
print(sum_distance)