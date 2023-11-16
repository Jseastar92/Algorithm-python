# O(logN)
# set으로 ransom의 중복문자 없앤 후 문자열에서 각 문자 Count
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c) :
                return False
        return True
    
Solution.canConstruct(Solution, "aa", "aab")


# 첫번쨰 풀이, Hash table 이용한 Brute force.
# 시간 O(n) 필요없는 코드 줄일 필요있을듯.

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         alphas = dict()
#         alphas2 = dict()

#         for c in ransomNote[:]:
#             alphas[c] = alphas.get(c, 0) + 1
            
#         for c in magazine[:]:
#             alphas2[c] = alphas2.get(c, 0) + 1
        
#         for key in alphas.keys():
#             if not alphas2.get(key, None) :
#                 return False

#             if alphas[key] <= alphas2[key] :
#                 continue
#             else :
#                 return False
        
#         return True
    
# Solution.canConstruct(Solution, "aa", "aab")