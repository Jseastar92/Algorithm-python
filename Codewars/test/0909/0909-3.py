def move_zeros(arr):
    z=0
    i=0
    l=len(arr)-1
    while(l) :
        print("l :", l)
        if arr[i] is bool():
            l-=1
            continue
        elif arr[i] is None:
            l-=1
            continue
        elif arr[i] == z :
            arr.pop(i)
            arr.append(z)
            l-=1
            continue
        #print(arr)
        i+=1
        l-=1
    return arr
# print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
# print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
# print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([0,1,None,2,False,1,0]))
