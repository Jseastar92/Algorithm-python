class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for n in nums[1:]:
            curSum = max(n, curSum+n)
            maxSum = max(maxSum, curSum)
        
        return maxSum
Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])