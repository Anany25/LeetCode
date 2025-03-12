class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vocab = set()
        maxi = 0
        left = 0
        for char in s:

            while char in vocab:
                vocab.remove(s[left])
                left += 1
                
            vocab.add(char)

            maxi = max(maxi, len(vocab))
        
        return maxi