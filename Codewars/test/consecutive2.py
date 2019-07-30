def longest_consec(strarr, k):

    if strarr :
        n = strarr.index(max(strarr,key=len))
        # print("n is ", n)
        # print("test 1 : ",''.join(strarr[n:n+k]))
        # print("test 2 : ",)

        if len(''.join(strarr[n:n+k])) >= len(''.join(strarr[n-k+1 : n+1])) :
            #print("+2",''.join(strarr[n:n+k]))
            return ''.join(strarr[n:n+k])
        else :
            #print("-2",''.join(strarr[n-k+1 : n+1:]))
            return ''.join(strarr[n-k+1 : n+1:])
    else :
        return ""
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
