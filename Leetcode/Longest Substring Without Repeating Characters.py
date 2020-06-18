class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a= {}
        l = 0
        if len(s) <= 1:
            return len(s)
        
        for i,v in enumerate(s):
            a[i]= [v]
            
            if (i+1) > len(s):
                break
                
            for j, k in enumerate(s[i+1:]):
                if k in a[i] :
                    break
                else :
                    a[i].append(k)

        for k,v in a.items():
            if l < len(v):
                l = len(v)
        return l

