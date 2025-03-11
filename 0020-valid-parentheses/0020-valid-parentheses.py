class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Loop through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack.
            if char in "([{":
                stack.append(char)
            else:
                # If it's a closing bracket and the stack is empty, it's invalid.
                if not stack:
                    return False
                # Pop the last opening bracket from the stack.
                top = stack.pop()
                # Check if the popped bracket matches the current closing bracket.
                if char == ')' and top != '(':
                    return False
                if char == ']' and top != '[':
                    return False
                if char == '}' and top != '{':
                    return False
        # After processing all characters, the stack should be empty for a valid string.
        return len(stack) == 0
