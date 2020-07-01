class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def intersection(arr1, arr2):
            ans = []
            for i in arr1 :
                if i in arr2:
                    ans.append(i)
                    arr2.remove(i)
            return ans
    
        if len(nums1) < len(nums2):
            return intersection(nums1, nums2)
        else: 
            return intersection(nums2, nums1)
                        