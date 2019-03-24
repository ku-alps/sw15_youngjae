#===============================================================================
# 단지 부분 입력 받는 부분
#===============================================================================
danji_size = int(input())
danji_num = 0 #단지개수
danji_arr = [[0]*int(danji_size) for i in range(int(danji_size))] # 단지에 대한 정보
danji_chk = [[0]*int(danji_size) for i in range(int(danji_size))] # 단지 들렸는지 체크 하는 변수
danji_num_arr = [0]*(int(danji_size)*int(danji_size)+1)

for i in range (0,int(danji_size)):
    danji_val = input() #단지에 해당하는 값 (0 or 1)
    for k in range (0,int(danji_size)):
        danji_arr[i][k] = (int(danji_val[k:k+1])) #문자열 잘라서 단지 변수에 삽입

def fn_danji_chk(first_index,second_index,danji_index):
    global danji_chk
    global danji_arr
    global danji_size
    global danji_num_arr
    
    if(danji_chk[first_index][second_index] == 1):
        return
    else:
        danji_chk[first_index][second_index] = 1
        if(danji_arr[first_index][second_index]==1):
            danji_num_arr[danji_index] += 1
            if(first_index > 0 and danji_chk[first_index-1][second_index] == 0): #상 검색
                fn_danji_chk(first_index-1,second_index,danji_index)
            if(second_index < danji_size-1 and danji_chk[first_index][second_index+1] == 0): #우 검색
                fn_danji_chk(first_index,second_index+1,danji_index)
            if(first_index < danji_size-1 and danji_chk[first_index+1][second_index] == 0): #하 검색
                fn_danji_chk(first_index+1,second_index,danji_index)
            if(second_index > 0 and danji_chk[first_index][second_index-1] == 0): #좌 검색
                fn_danji_chk(first_index,second_index-1,danji_index)

            

danji_index = 0
for i in range (0,int(danji_size)):
    for k in range (0,int(danji_size)):
        if danji_arr[i][k] == 1 and danji_chk[i][k] == 0:
            fn_danji_chk(i,k,danji_index)
            danji_num+=1
            danji_index = danji_index+1

print(danji_num)
danji_num_arr.sort()
for i in range(0,len(danji_num_arr)):
    if(danji_num_arr[i] != 0):
        print(danji_num_arr[i])
    

