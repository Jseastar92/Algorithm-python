def longest_consec(strarr, k):
    n = strarr.index(max(strarr,key=len))
    print(n)
    if n == 0 and k > n and k <= 0:
        return ""
    else :
        if len(''.join( strarr[n+i] for i in range(k))) >= len(''.join( strarr[n-i] for i in range(k) )) :
            return
        else :
            midx = strarr.index(max(strarr))-k
            return

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
