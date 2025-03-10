class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        lcp = strs[0]
        
        for i in range(1, len(strs)):
            j = 0
            while j < len(lcp) and j < len(strs[i]) and lcp[j] == strs[i][j]:
                j += 1
            lcp = lcp[:j]
            if lcp == "":
                break
                
        return lcp
