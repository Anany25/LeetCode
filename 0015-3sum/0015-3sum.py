class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos = defaultdict(int)
        neg = defaultdict(int)
        zero = 0
        ans = []

        for num in nums:
            if num > 0:
                pos[num] += 1
            elif num < 0:
                neg[num] += 1
            else:
                zero += 1

        if zero > 0:
            if zero > 2:
                ans.append([0,0,0])

            for p in pos:
                if -p in neg:
                    ans.append([0,p,-p])

        pos_keys = list(pos.keys())
        neg_keys = list(neg.keys())

        for i in range(0,len(pos_keys)):
            if pos[pos_keys[i]]>= 2:
                if -(2 * pos_keys[i]) in neg:
                    ans.append([pos_keys[i],pos_keys[i],-(2 * pos_keys[i])])

            for j in range(i+1,len(pos_keys)):
                if -(pos_keys[i] + pos_keys[j]) in neg:
                    ans.append([pos_keys[i],pos_keys[j],-(pos_keys[i] + pos_keys[j])])

        for i in range(0,len(neg_keys)):
            if neg[neg_keys[i]] >= 2:
                if -(2 * neg_keys[i]) in pos:
                    ans.append([neg_keys[i],neg_keys[i],-(2 * neg_keys[i])])

            for j in range(i+1,len(neg_keys)):
                if -(neg_keys[i] + neg_keys[j]) in pos:
                    ans.append([neg_keys[i],neg_keys[j],-(neg_keys[i] + neg_keys[j])]) 

        return ans
        
