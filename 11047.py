coin_info = input()
coin_temp = coin_info.split()
coin_type_num = int(coin_temp[0])
goal_price = int(coin_temp[1])
coin_type = []  #동전 분류
coin_idx = 0    #동전 인덱스
coin_num = 0    #필요한 총 개수 
coin_chk = 0    #Flag값 목표가격보다 큰 액수를 가진 동전이 있는지 체크하는 변수 있으면 1 없으면 0
for i in range(0,coin_type_num):
   coin_type.append(int(input()))

while goal_price != 0: #코인종류중에 목표가격이 넘는 코인이 있는지 찾은뒤에 있으면 그 넘는 코인 인덱스 바로 전꺼부터 목표값에서 나눈다. 없을경우 마지막 인덱스를 가져온다.
    
    for i in range(0,coin_type_num):
        if coin_type[i] > goal_price:
            if i != 0:
                coin_idx = i-1
                coin_chk = 1
            break

    if coin_chk == 0:
        coin_idx = coin_type_num-1
        
    coin_num += int(goal_price/coin_type[coin_idx])
    goal_price = goal_price % coin_type[coin_idx]


print(coin_num)


