class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dia = defaultdict(list)
        
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                dia[i + j].append(val)

        ans = []
        for s in sorted(dia.keys()):
            ans.extend(reversed(dia[s]))
        
        return ans