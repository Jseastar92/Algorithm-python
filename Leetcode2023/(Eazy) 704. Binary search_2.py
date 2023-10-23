from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums : 
            return -1
        
        idx = 0
        while len(nums) > 1 :
            midian = int(len(nums)/2)
            idx += midian
            curr = nums[midian] # 현재 중간 값
            
            if target == curr:
                return idx

            if target > curr:    # 현재 값이 더 낮으면 오른쪽.
                nums = nums[midian+1:] # 현재 인덱스는 제외하고 다음인덱스부터 오른쪽 배열
                idx += 1
                
            if target < curr:    # 현재 값이 더 높으면 왼쪽
                nums = nums[:midian]
                idx -= len(nums)
        
        if not nums :
            return -1
        else:
            return -1 if nums[0] != target else idx