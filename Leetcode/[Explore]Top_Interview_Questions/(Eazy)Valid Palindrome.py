class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        todo: retry it! use index first and last!
        '''
        og_string = [ele for ele in s.lower() if 'a'<= ele <= 'z' or ele.isdigit() ]
        return og_string == og_string[::-1]