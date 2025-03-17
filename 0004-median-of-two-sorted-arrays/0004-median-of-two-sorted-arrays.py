class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        total = len(nums)
        left, right = min(nums), max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            
            less = 0     # count how many values < mid
            same = 0     # count how many values == mid
            more = 0     # count how many values > mid
            mini = float('-inf')  # largest number < mid
            maxi = float('inf')   # smallest number > mid
            
            # Tally up counts and track nearest neighbors
            for val in nums:
                if val < mid:
                    less += 1
                    mini = max(mini, val)
                elif val > mid:
                    more += 1
                    maxi = min(maxi, val)
                else:
                    same += 1
            
            # ----- Odd total length -----
            if total % 2 == 1:
                midpos = (total // 2) + 1  # 1-based index of the median
                
                # Figure out which "zone" that position lands in
                if midpos <= less:
                    # The median is actually in the 'less' zone
                    median_val = mini
                elif midpos > less + same:
                    # The median is in the 'more' zone
                    median_val = maxi
                else:
                    # The median is exactly mid
                    median_val = mid
                
                # If 'mid' truly covers that position, return it
                # else adjust left/right below
                if less <= (total // 2) < less + same:
                    return float(median_val)
            
            # ----- Even total length -----
            else:
                m1 = total // 2       # 1-based index for lower median
                m2 = m1 + 1           # 1-based index for upper median
                
                # Check which side each median position falls into:
                #  -- If m2 <= less, both median positions are in the 'less' zone.
                #     We should move `right` down and keep searching.
                #  -- If m1 > less+same, both are in the 'more' zone.
                #     We should move `left` up and keep searching.
                #  -- Otherwise, we've found a split around mid.  Pick each zone’s
                #     representative value (mini, mid, or maxi) and return the average.
                
                if m2 <= less:
                    # Both median positions lie in the "less" region => go smaller
                    right = mid - 1
                    continue
                elif m1 > (less + same):
                    # Both are in the "more" region => go bigger
                    left = mid + 1
                    continue
                else:
                    # At least one of m1 or m2 is in [less+1 .. less+same]
                    # or they straddle the boundary between less and same/more.
                    
                    def zone_value(pos):
                        """Return the actual value for the pos-th element (1-based)."""
                        if pos <= less:
                            # It's in the 'less' zone => that element is effectively `mini`
                            return mini
                        elif pos > less + same:
                            # It's in the 'more' zone => that element is `maxi`
                            return maxi
                        else:
                            # It's in the 'same' zone => that element is `mid`
                            return mid
                    
                    lower_val = zone_value(m1)
                    upper_val = zone_value(m2)
                    
                    return (lower_val + upper_val) / 2.0
            
            # If we haven't returned yet, we adjust the binary search range
            if less > total // 2:
                # Too many elements are < mid => we need a smaller 'mid'
                right = mid - 1
            else:
                # Otherwise, not enough elements <= mid => increase 'mid'
                left = mid + 1
        
        # Should never actually land here
        return -1
