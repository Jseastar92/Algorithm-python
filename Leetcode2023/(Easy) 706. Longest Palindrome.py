class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaire_chars = set()
        
        for c in s :
            if c in unpaire_chars:
                pairs += 1
                unpaire_chars.remove(c)
            else:
                unpaire_chars.add(c)
        return pairs * 2 + 1 if unpaire_chars else pairs * 2
    
#Hasht Table #Set #Greedy