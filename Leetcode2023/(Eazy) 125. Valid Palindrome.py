from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(c for c in s if c.isalnum()).upper()
        return result == result[::-1]

sol = Solution()
# test_case = "0P"
test_case = "A man, a plan, a canal: Panama"
sol.isPalindrome(test_case)
