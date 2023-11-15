class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) -1
        j = len(b) -1
        carry = 0
        stack = list()
        while i >= 0 or j >= 0 or carry:
            bit1 = int(a[i]) if i >= 0 else 0
            bit2 = int(b[j]) if j >= 0 else 0
            bit_sum = bit1 + bit2 + carry
            
            carry = 0
            putvalue = 0
            if bit_sum > 1:
                carry = 1
                putvalue = bit_sum-2
            else :
                carry = 0
                putvalue = bit_sum
            
            stack.append(putvalue)
            i -= 1
            j -= 1
            
        return ''.join(str(c) for c in stack[::-1])

# Solution.addBinary(Solution, "11", "1")
Solution.addBinary(Solution, "1010", "1011")

