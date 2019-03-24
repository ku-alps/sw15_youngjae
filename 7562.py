test_case = int(input()) #경우의수

now_location = [[0]*2 for i in range(0,test_case)] #현재위치
move_location = [[0]*2 for i in range(0,test_case)] #최종위치
result_arr    = []  #결과 담을 변수

def night(now_arr,move_location,length):

    global chess_board #방문체크

    temp_arr = []
    temp_arr.append([now_arr[0],now_arr[1],0]) #현재 위치 리스트에 추가
    chess_board[now_arr[0]][now_arr[1]] == 1
    depth = 1

    while(temp_arr):
        now_arr = temp_arr.pop(0) #맨앞에원소 꺼내고 그 값에 해당하는 애들로 다시 검색
        if(now_arr[0] == move_location[0] and now_arr[1] == move_location[1]): #최종위치에 다다르면 결과 리턴
            return now_arr[2]

        #============================================================================================
        # 이동 위치 탐색 부분 (시간날때 for문으로 바꾸기) 
        #============================================================================================
        if(now_arr[0]-2 >= 0 and now_arr[0]-2 < length and now_arr[1]+1 < length and now_arr[1]+1 >= 0):
            if(chess_board[now_arr[0]-2][now_arr[1]+1] == 0):
                chess_board[now_arr[0]-2][now_arr[1]+1] = 1
                temp_arr.append([now_arr[0]-2,now_arr[1]+1,now_arr[2]+1])
            
        if(now_arr[0]-1 >= 0 and now_arr[0]-1 < length and now_arr[1]+2 < length and now_arr[1]+2 >= 0):
            if(chess_board[now_arr[0]-1][now_arr[1]+2] == 0):
                chess_board[now_arr[0]-1][now_arr[1]+2] = 1
                temp_arr.append([now_arr[0]-1,now_arr[1]+2,now_arr[2]+1])
            

        if(now_arr[0]+1 >= 0 and now_arr[0]+1 < length and now_arr[1]+2 < length and now_arr[1]+2 >= 0):
            if(chess_board[now_arr[0]+1][now_arr[1]+2] == 0):
                chess_board[now_arr[0]+1][now_arr[1]+2] = 1
                temp_arr.append([now_arr[0]+1,now_arr[1]+2,now_arr[2]+1])

        if(now_arr[0]+2 >= 0 and now_arr[0]+2 < length and now_arr[1]+1 < length and now_arr[1]+1 >= 0):
            if(chess_board[now_arr[0]+2][now_arr[1]+1] == 0):
                chess_board[now_arr[0]+2][now_arr[1]+1] = 1
                temp_arr.append([now_arr[0]+2,now_arr[1]+1,now_arr[2]+1])

        if(now_arr[0]+2 >= 0 and now_arr[0]+2 < length and now_arr[1]-1 < length and now_arr[1]-1 >= 0):
            if(chess_board[now_arr[0]+2][now_arr[1]-1] == 0):
                chess_board[now_arr[0]+2][now_arr[1]-1] = 1
                temp_arr.append([now_arr[0]+2,now_arr[1]-1,now_arr[2]+1])

        if(now_arr[0]+1 >= 0 and now_arr[0]+1 < length and now_arr[1]-2 < length and now_arr[1]-2 >= 0):
            if(chess_board[now_arr[0]+1][now_arr[1]-2] == 0):
                chess_board[now_arr[0]+1][now_arr[1]-2] = 1
                temp_arr.append([now_arr[0]+1,now_arr[1]-2,now_arr[2]+1])

        if(now_arr[0]-2 >= 0 and now_arr[0]-2 < length and now_arr[1]-1 < length and now_arr[1]-1 >= 0):
            if(chess_board[now_arr[0]-2][now_arr[1]-1] == 0):
                chess_board[now_arr[0]-2][now_arr[1]-1] = 1
                temp_arr.append([now_arr[0]-2,now_arr[1]-1,now_arr[2]+1])

        if(now_arr[0]-1 >= 0 and now_arr[0]-1 < length and now_arr[1]-2 < length and now_arr[1]-2 >= 0):
            if(chess_board[now_arr[0]-1][now_arr[1]-2] == 0):
                chess_board[now_arr[0]-1][now_arr[1]-2] = 1
                temp_arr.append([now_arr[0]-1,now_arr[1]-2,now_arr[2]+1])
        
        depth = depth+1
        #============================================================================================    
            

for i in range(0,test_case):
    length = int(input())

    now_str = input()
    now_str = now_str.split()
    now_location[i][0] = int(now_str[0])
    now_location[i][1] = int(now_str[1])

    move_str = input()
    move_str = move_str.split()

    move_location[i][0] = int(move_str[0])
    move_location[i][1] = int(move_str[1])

    chess_board = [[0]*length for i in range(0,length)]
    
    val = night(now_location[i],move_location[i],length)  #현재있는위치, #결과위치, #체스판 크기
    result_arr.append(val)


for i in range(0,test_case):
    print(result_arr[i])