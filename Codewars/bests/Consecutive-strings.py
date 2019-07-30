def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
