arr_size = int(input())
sum = 0
a_val = input()
b_val = input()

a_arr = a_val.split()
b_arr = b_val.split()

for i in range (0,len(a_arr)):
    a_arr[i] = int(a_arr[i])
    b_arr[i] = int(b_arr[i])

a_arr.sort()
b_arr.sort(reverse=True)

for i in range (0,len(a_arr)):
   sum += a_arr[i]*b_arr[i]


print(sum)


