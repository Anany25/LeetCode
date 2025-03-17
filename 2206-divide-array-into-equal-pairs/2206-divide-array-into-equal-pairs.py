
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for count in counter.values():
            if count % 2 != 0:
                return False
        return True
