class Solution:
    def majorityElement(self, nums: [int]) -> int:
        num_dict = dict()
        
        for n in nums:
            num_dict[n] = int(num_dict.get(n, 0)) + 1
            
        max(num_dict, key=num_dict.get)
        print(num_dict)
        
Solution.majorityElement(Solution, [2,2,1,1,1,2,2])