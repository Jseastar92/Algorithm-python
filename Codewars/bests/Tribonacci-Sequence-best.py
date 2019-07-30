def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res


#결과 출력
print(tribonacci([11,11,16],36))
# print(tribonacci([0,0,1],10))
# print(tribonacci([0,1,1],10))
# print(tribonacci([0,0,0],10))
# print(tribonacci([1,2,3],10))
# print(tribonacci([3,2,1],10))
# print(tribonacci([1,1,1],1))
# print(tribonacci([300,200,100],0))
# print(tribonacci([0.5,0.5,0.5],30))
