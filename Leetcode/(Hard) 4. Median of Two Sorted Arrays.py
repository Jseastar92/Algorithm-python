class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_list = sorted(nums1 + nums2)
        mid = int(len(sorted_list)/2)
        if (len(sorted_list)%2) == 0:
            return (sorted_list[mid-1] + sorted_list[mid])/2
        else:
            return sorted_list[mid]