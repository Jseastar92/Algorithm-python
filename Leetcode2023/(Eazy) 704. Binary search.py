from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            m = (l + r)//2
            curr = nums[m]
            if target > curr:
                l = m+1
            elif target < curr:
                r = m-1
            else :
                return m
        return -1