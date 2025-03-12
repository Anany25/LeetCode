class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        if nums[mid] < 0:
            while nums[mid]<=0 and mid <= right:
                mid += 1
            return mid
        elif nums[mid] > 0:
            while nums[mid] >= 0 and mid >= left:
                mid -=1
            return right-mid 
        elif nums[mid] == 0:
            mid2 = mid
            while nums[mid]==0:
                mid += 1
            while nums[mid2]==0:
                mid2 -= 1
            return max(mid2+1,right-mid+1) 
