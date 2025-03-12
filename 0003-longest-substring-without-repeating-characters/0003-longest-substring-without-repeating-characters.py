class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vocab = []
        maxi = 0
        for char in s:
            if char in vocab:
                i = 0
                while vocab[i] != char:
                    vocab.pop(0)
                vocab.pop(0)
                vocab.append(char)

            else:
                vocab.append(char)

            print(vocab)

            maxi = max(maxi, len(vocab))
        
        return maxi