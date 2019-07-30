def longest_consec(strarr, k):
    # your code
    #s.append(max(strarr,key=len))
    # tmp=""
    # for i in range(k):
    #     tmp += max(strarr, key=len)
    #     strarr.remove(max(strarr, key=len))
    tmp = ""
    return ''.join([max(strarr, key=len) for i in range(k) if i == max(strarr, key=len)])

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
