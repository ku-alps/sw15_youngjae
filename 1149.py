house_num = int(input())
color_arr = [[0]*house_num for i in range(0,house_num)] #색깔배열
distance = [[0]*3 for i in range(0,house_num+1)]
for i in range (0,house_num):
    color_str = input()
    color = color_str.split()
    for j in range(0,len(color)):
        if(j==0):
            distance[i][0] += min(int(distance[i-1][1]),int(distance[i-1][2]))+int(color[j])
        if(j==1):
            distance[i][1] += min(int(distance[i-1][0]),int(distance[i-1][2]))+int(color[j])
        if(j==2):
            distance[i][2] += min(int(distance[i-1][0]),int(distance[i-1][1]))+int(color[j])

print(min(distance[house_num-1][0],distance[house_num-1][1],distance[house_num-1][2]))
