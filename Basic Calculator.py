class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign = 1
        result = 0
        num = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = stack[-1]
            elif char == '-':
                result += sign * num
                num = 0
                sign = -stack[-1]
            elif char == '(':
                stack.append(sign)
            elif char == ')':
                result += sign * num
                num = 0
                stack.pop()
            i += 1
        result += sign * num
        return result
