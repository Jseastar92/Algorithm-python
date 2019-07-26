def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2] # " //2 " 는 정수 몫으로 반환
    less, greater, equal = [], [] ,[]
    for num in arr:
        if (pivot > num) :
            less.append(num)
        elif (pivot < num ):
            greater.append(num)
        else:
            equal.append(num)
    return quick(less) + equal + quick(greater)

print(quick([4,64,2,42,62,4,123,4123,46,3,3,1]))
