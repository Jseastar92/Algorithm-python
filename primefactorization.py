# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form :

import random
import math


def primeFactors(n):
    # 제곱근 바빌로니아법 알고리즘
    # a = n
    # x = a/2
    # for i in range(20):
    #     x = (x + ( a/x ) )/2
    d_pn = {}
    x = round(math.sqrt(n))
    num = n

    for i in range(2, x + 1):
        while (num % i == 0):
            num = num // i


    # print(d_pn)

    return 0


primeFactors(86240)