triangle_size = int(input())
triangle_arr  = [[0]*triangle_size for i in range(int(triangle_size))]

#====================================================================================
# 정수삼각형 정보 입력
#====================================================================================
for i in range(0,triangle_size):
    triangle_val = input()
    triangle_val = triangle_val.split()    
    for j in range(0,len(triangle_val)):
        triangle_arr[i][j] =  int(triangle_val[j])
#====================================================================================

#print(triangle_arr)

for i in range(1,triangle_size):
    for j in range(0,i+1):
        if j == 0:  #맨왼쪽값
            triangle_arr[i][j] += triangle_arr[i-1][j]
        elif i == j:    #맨오른쪽값
            triangle_arr[i][j] += triangle_arr[i-1][j-1]
        else:   #중간값(대각선 중에 큰애들선택)
            triangle_arr[i][j] = max(triangle_arr[i][j]+triangle_arr[i-1][j-1],triangle_arr[i][j]+triangle_arr[i-1][j])

print(max(triangle_arr[triangle_size-1]))