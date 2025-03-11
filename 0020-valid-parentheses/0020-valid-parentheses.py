class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n == 0:
            return True

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if i == ')' and top != '(':
                    return False
                elif i == ']' and top != '[':
                    return False
                elif i == '}' and top != '{':
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False