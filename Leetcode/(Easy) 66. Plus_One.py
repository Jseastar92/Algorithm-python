class Solution:
     def plusOne(self, digits: List[int]) -> List[int]:
         t = []

         while(digits):
             v = digits.pop()
             if v >= 9 :
                 t.append(v)
             else :
                 digits.append(v+1)
                 break

         if not digits:
             digits.append(1)
         for v in t:
             digits.append(0)

         return digits