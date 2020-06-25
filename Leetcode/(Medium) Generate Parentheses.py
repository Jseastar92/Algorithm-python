'''
need more practice
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def draw(s = '',l = 0, r = 0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            
            if l < n : 
                draw(s + '(', l+1, r)
            if r < l :
                draw(s+')', l, r+1)
            
        draw()
        return ans