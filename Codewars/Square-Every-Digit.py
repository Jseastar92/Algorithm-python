
# if input 9119, output is 811181
# because 9^2 is 81, 1^2 is 1

def square_digits(num):

    lst = str(num)
    lst2 = list()
    for n in range(len(lst)):
        b = int(lst[n]) ** 2
        lst2.append(str(b))
    a = ''.join(lst2)
    a = int(a)
    return a
