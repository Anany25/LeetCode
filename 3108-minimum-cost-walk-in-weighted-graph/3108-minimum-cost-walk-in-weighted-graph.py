class UF:
    def __init__(self, n):
        self.par = list(range(n))
        self.depth = [1] * n
        self.val = [(1 << 17) - 1] * n
    
    def union(self, i, j, w):
        ri = self.find(i)
        rj = self.find(j)
        val = self.val[ri] & self.val[rj] & w
        if self.depth[ri] >= self.depth[rj]:
            self.par[rj] = ri
            self.val[ri] = val
            if self.depth[ri] == self.depth[rj]:
                self.depth[ri] += 1
        else:
            self.par[ri] = rj
            self.val[rj] = val
            
    def find(self, i):
        if self.par[i] == i:
            return i
        self.par[i] = self.find(self.par[i])
        return self.par[i]
    
    def get_val(self, i):
        return self.val[self.find(i)]
        

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UF(n)
        for a, b, w in edges:
            uf.union(a, b, w)
        
        res = []
        for a, b in query:
            if a == b:
                res.append(0)
            elif uf.find(a) == uf.find(b):
                res.append(uf.get_val(a))
            else:
                res.append(-1)
        return res