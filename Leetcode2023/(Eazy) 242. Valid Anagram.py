class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sd, td = dict(), dict()    
        for c in s[:]:
            sd.setdefault(c, 0)
            sd[c] += 1

        for c in t[:]:
            td.setdefault(c, 0)
            td[c] += 1

        return True if sd==td else False


sol = Solution()
test_case1 = "anagram"
test_case2 = "nagaram"
sol.isAnagram(test_case1,test_case2)
