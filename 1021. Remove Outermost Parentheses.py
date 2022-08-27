class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count_left = 0
        left = True
        new_string = ""
        for i in range(len(s)):
            if count_left != 0 and s[i] == '(':
                new_string += s[i]
            if s[i] == '(':
                count_left += 1
            elif s[i] == ')':
                count_left -= 1
            if count_left != 0 and s[i] == ')':
                new_string += s[i]
        return new_string
