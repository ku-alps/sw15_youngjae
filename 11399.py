people_time = []
people_num = input()

def min_time(arr):
    time_sum = 0
    arr.sort()

    for i in range (0,len(arr)):
        for j in range (0,i+1):
            time_sum += int(arr[j])  
    
    print(time_sum)

if 1 <= int(people_num) and int(people_num) <= 1000:  #사람 수 입력 (1부터 1000명까지)
    
    temp_num = input()
    temp_num = temp_num.split()
    for i in range(len(temp_num)):
        people_time.append(int(temp_num[i]))

    min_time(people_time)
else:
    print("사람 수는 1부터 1000까지만 가능합니다.")

