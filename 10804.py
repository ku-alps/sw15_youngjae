card = []
for i in range(1,21):
    card.append(i)

for i in range(0,10):
    number_temp = input().split()
    number_start = int(number_temp[0])-1
    number_end   = int(number_temp[1])
    temp_card =  card[number_start:number_end] #시작 인덱스 부터 끝나는 인덱스까지 문자열 잘라서 부분 삭제하고 다시 넣기
    for j in range(number_start,number_end):
        del card[j]
        card.insert(j,temp_card.pop())

for i in card:
    print(i, end=' ')
