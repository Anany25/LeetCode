class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = list(a)
        y = list(b)
        if len(x) < len(y):
            while len(x) != len(y):
                x.insert(0,0)
        elif len(x) > len(y):
            while len(x) != len(y):
                y.insert(0,0)
        ans = []
        carry = 0
        i = len(x)-1
        while i >= 0:
            z = int(x[i]) + int(y[i]) + carry
            if z == 1:
                ans.append(1)
                carry = 0
            elif z == 2:
                ans.append(0)
                carry = 1
            elif z == 3:
                ans.append(1)
                carry = 1
            elif z == 0:
                ans.append(0)
                carry = 0
            i -= 1
        if carry == 1:
            ans.append(1)

        ans.reverse()
        print(ans)
        ans = "".join(map(str,ans))
        return ans