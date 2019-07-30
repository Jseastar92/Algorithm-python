def longest_consec(strarr, k):
    max1 = strarr.index(max(strarr,key=len))
    rmax = strarr.index(max(reversed(strarr),key=len))
    #print(n)
    lst = []
    lst1 = []
    if not strarr :
        return ""
    else :
        for i in range(k) :
            if not strarr[max1+i] :
                break
            else : lst.append(strarr[max1+i])

        for i in range(k) :
            if not strarr[max1+i] :
                break
            else : lst1.append(strarr[rmax+i])

        for i in range(k) :
            lst1.insert(0,strarr[n-i])


        if len(''.join(lst))>len(''.join(lst1)):
            return ''.join(lst)
        else :
            return ''.join(lst1)

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
