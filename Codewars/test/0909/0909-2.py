def move_zeros(arr):
    # [array.append(array.pop(i)) for i, v in enumerate(array) if v==0])
    # return array
    z=0
    temp=[]
    i=0
    l=len(arr)-1
    while(l) :
        if arr[i] is bool():
            continue
        elif int(arr[i]) == z :
            arr.pop(i)
            arr.append(z)
            print("T")
            l-=1
            continue
        print(arr)
        i+=1
        l-=1
    return arr
    #your code here
#print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
#print(move_zeros([0,1,None,2,False,1,0]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
