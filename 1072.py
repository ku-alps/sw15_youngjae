import sys

X, Y = map(int,sys.stdin.readline().split()) #X,Y 정보 입력
stand_val = int(Y * 100 / X) #기준값설정
first = 0
last = 1000000000
result=-1

if stand_val >= 99:
    print(-1)
else:
    while first <= last:    #이분탐색 사용 
        mid = int((first+last)/2)
        temp = int(100 * (Y+mid) / (X+mid))
        if temp > stand_val:
            last = mid-1
        else:
            first = mid+1
            result = first

    print(result)


# 추가적으로 100을 X 뒤에 곱해줬는데 백준에서 오류가 뜸 앞에다 곱하니깐 답이 됨...  ex Y*100/X 정답 Y/X*100 오답 
# 참고사이트 https://mygumi.tistory.com/82