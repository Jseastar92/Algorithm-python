class Solution:
    def majorityElement(self, nums: [int]) -> int:
        num_dict = dict()
        
        for n in nums:
            num_dict[n] = int(num_dict.get(n, 0)) + 1
            
        max(num_dict, key=num_dict.get)
        print(num_dict)
        
Solution.majorityElement(Solution, [2,2,1,1,11,2,3,1,321,23,213,213,213,213,21,321,321,3,5,15,15,12,412,4521,2,2])

# nums 전부 순회할때 남은 요소 개수 따져서 시간 줄일 수도 있겠다.
