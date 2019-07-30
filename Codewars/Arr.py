def find_even_index(arr):
    #your code here
    lsum=int()
    rsum=int()
    idx = -1
    for i in range(len(arr)):
        lsum=sum(arr[i::-1])
        rsum=sum(arr[i::1])
        if lsum == rsum :
            idx = i
            print("*************************It's same!************************* index :",idx)
            break;
        print(i," test")
        print("left :",arr[i::-1],"lsum is ",lsum)
        print("right :",arr[i::1],"rsum is ",rsum)
        print("")
        print(idx)
    #print("index num is ",i)
find_even_index(range(1,100))
