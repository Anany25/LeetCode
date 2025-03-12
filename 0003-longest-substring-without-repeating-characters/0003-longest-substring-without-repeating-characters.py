class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vocab = []
        maxi = 0
        left = 0
        for char in s:
            if char in vocab[left:]:

                while vocab[left] != char:
                    left += 1
                left += 1
            vocab.append(char)

            print(vocab[left:])

            maxi = max(maxi, len(vocab[left:]))
        
        return maxi