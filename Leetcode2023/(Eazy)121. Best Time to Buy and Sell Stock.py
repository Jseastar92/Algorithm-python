from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         # brute force
        min, max_profit = prices[0], 0
        
        for price in prices[1:]:
            if min > price :
                min = price
            elif max_profit < price - min :
                max_profit = price - min
        return max_profit

sol = Solution()


# test_case = [1,2,3,4,5]
test_case = [7,1,5,3,6,4]
sol.maxProfit(test_case)
