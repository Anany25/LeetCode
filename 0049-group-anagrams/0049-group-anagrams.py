class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        pairs = defaultdict(list)
        for word in strs:
            signature = "".join(sorted(word))
            pairs[signature].append(word)

        return list(pairs.values())