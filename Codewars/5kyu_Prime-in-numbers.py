# 5kyu - Prime in numbers

# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form :
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors
#
# print(prime_factors(123863))
import math

def primeFactor(num):

        # 제곱근 바빌로니아법 알고리즘
        # x = ( x + ( a/x ) ) / 2 식의 반복연산을 통해 제곱근 결과의 정확도를 높일 수 있음
        # a = n
        # x = a/2
        # for i in range(20):
        #     x = (x + ( a/x ) )/2
    d_pn = {}
    x = math.sqrt(num)
    i=2
    while i <= x :
        if num % i :
            i+=1
        else :
            num //= i
            try :
                d_pn[i] += 1
            except KeyError :
                d_pn[i] = 1
            print(num)
    if num > 1 :
        d_pn[num] = 1

    return sorted(d_pn.items())

def primeFactors(n):

    pf = primeFactor(n) # prime factor dictionary
    str_arr = []
    for key,value in pf:
        if value == 1 :
            str_arr.append( "(" + str(key) + ")" )
        else:
            str_arr.append( "(" + str(key) + "**" + str(value) +")")

    result = ''.join(str_arr)
    print(result)
    print(n)
    return result

primeFactors(933555431)
