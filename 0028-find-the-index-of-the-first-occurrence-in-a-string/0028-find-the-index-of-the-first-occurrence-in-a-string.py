class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            temp = i
            if haystack[i] == needle[0]:
                j = 0
                while j < len(needle) and i< len(haystack):
                    print(i)
                    print(j)
                    if haystack[i] != needle[j]:
                        break
                    else:
                        i+=1
                        j+=1
                    if j == len(needle):
                        return temp
            
            i = temp
        return -1