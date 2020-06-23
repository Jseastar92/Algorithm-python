class Solution:
    def reverse(self, x: int) -> int:
        a = list(str(x))
        zero_flag=True
        t=[]

        if x == 0  :
            return 0
        elif x < 0:
            t.append(a[0])
            del a[0]
        
        for i in range(0,len(a)):
            v= a.pop()
            if zero_flag :
                if v != '0':
                    t.append(v)
                    zero_flag= False
            else:
                t.append(v)
        
        r = int("".join(t))
        if abs(r) >= (2**31-1):
            return 0
        return r