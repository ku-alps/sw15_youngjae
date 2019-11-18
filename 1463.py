import sys

sys.setrecursionlimit(10 ** 6)


def one_change(number,count):

    if number == 1:
        return count

    if number % 3 == 0:
        count += 1
        return one_change(int(number/3),count)
    elif (number-1) % 3 == 0:
        count += 1
        return one_change(int(number-1),count)
    elif number % 2 == 0:
        count += 1
        return one_change(int(number/2),count)
    elif (number-1) % 2 == 0:
        count += 1
        return one_change(int(number-1),count)

number = int(sys.stdin.readline())
a = one_change(number,0)
print(a)