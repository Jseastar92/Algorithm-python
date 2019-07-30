def solution(number):
    sum = 0
    for i in range(number) :
      if (i%3 and i%5) == 0 :
          sum += i
    return sum
print(solution(10))
