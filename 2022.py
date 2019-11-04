import math
import sys

X,Y,C = map(float,sys.stdin.readline().split())
left = 0
right = min(X,Y)

while(right-left > 0.000001): #직선의 방정식 이용
    D = (left+right)/2
    x_height = math.sqrt(X*X-D*D)
    y_height = math.sqrt(Y*Y-D*D)
    k = D * C / y_height
    f = (-x_height*k/D)+x_height
    # C 보다 큰 값이 나오면 D를 늘려서 높이를 낮추고 반대일경우 D를 낮춰서 높이를 높인다. 
    if f > C:
        left = D
    else: 
        right = D
print('%.3f' % left) # 소수점 셋째자리까지 출력