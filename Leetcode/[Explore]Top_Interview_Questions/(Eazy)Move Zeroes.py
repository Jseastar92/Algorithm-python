class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for v in nums:
            if not v:
                nums.append(v)
                nums.remove(v)


'''
return nums.sort(key=lambda x: [x == 0])
'''