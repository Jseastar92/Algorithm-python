def nb_year(p0, percent, aug, p):
    n=0
    while p0 <= p:
        p0 += (p0 * percent / 100) + aug
        n= n+1
        #print(n, p0, percent, aug, p)
    return n #ye

print(nb_year(3652425.9226,4.03, 17470, 4734512))
