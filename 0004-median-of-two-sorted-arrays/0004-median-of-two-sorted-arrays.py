class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        N = len(nums1)
        if N%2 == 1:
            return nums1[N//2]
        else:
            return (nums1[N//2] + nums1[N//2 - 1])/2