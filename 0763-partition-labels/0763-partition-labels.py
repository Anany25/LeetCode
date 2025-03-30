class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        ans = []
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i

        start = end = 0

        for i in range(len(s)):
            end = max(end, last_index[s[i]])
            if i == end:
                ans.append(end-start+1)
                start = i + 1 


        return ans
             