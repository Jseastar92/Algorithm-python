from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         # brute force
        
        lenthOfPrices = len(prices)
        i = 0
        min, max_profit = 0, 0
        min = prices[i]
        while lenthOfPrices > i:
            if i == 0:
                i+=1
                continue

            if min < prices[i] : 
                compareV = prices[i] - min
                if max_profit < compareV :
                    max_profit = compareV
            else :
                min = prices[i]
            i+=1
            
        return max_profit if max_profit > 0 else 0

sol = Solution()


# test_case = [1,2,3,4,5]
test_case = [7,1,5,3,6,4]
sol.maxProfit(test_case)
