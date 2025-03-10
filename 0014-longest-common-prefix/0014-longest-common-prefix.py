class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in range(1, len(strs)):
            temp = []
            j = 0
            while j < len(lcp) and j <len (strs[i]) and lcp[j] == strs[i][j]:
                temp.append(strs[i][j])
                j+=1

            if len(temp) < len(lcp):
                lcp = temp

        lcp = "".join(lcp)
        return lcp