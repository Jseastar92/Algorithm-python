class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_list = []
        max_len = 0
        
        for r in s :
            if r in char_list:
                char_list = char_list[char_list.index(r)+1:]
            
            char_list.append(r)
            max_len = max(max_len, len(char_list))
        return max_len