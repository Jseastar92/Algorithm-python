# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0;
        r = n;
        ans = 0;
        while l <= r:
            m = (l+r)//2
            if isBadVersion(m) :
                ans = m
                r = m-1
            else:
                l = m+1

        return ans
    
# Loop 1~n까지 돌면 O(n)으로 풀리지만 시간복잡도 줄이기 위해선 O(logN)으로 풀어야했음
# binary search로 구현해서 logN.