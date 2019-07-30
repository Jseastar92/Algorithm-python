def tribonacci(signature, n):
    #code by sst
    nums=len(signature)
    if n < 4:
        if n==0:
            return list()
        else:
            return signature[:n]
    else:
        while nums < n:
            signature.append(sum(signature[nums-3:nums]))
            nums +=1
        return signature

#결과출력
print(tribonacci([11,11,16],36))
# tribonacci([0,0,1],10)
# tribonacci([0,1,1],10)
# tribonacci([0,0,0],10)
# tribonacci([1,2,3],10)
# tribonacci([3,2,1],10)
# tribonacci([1,1,1],1)
print(tribonacci([300,200,100],0))
#print(tribonacci([0.5,0.5,0.5],30))
