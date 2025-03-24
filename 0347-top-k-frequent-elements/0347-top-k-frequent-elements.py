class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1
        
        s  = sorted(counter.items(), key=lambda item: item[1], reverse = True)

        ans = []
        for i in range(k):
            ans.append(s[i][0])

        return ans