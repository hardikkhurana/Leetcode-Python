class Solution:
    def calculate(self, s: str) -> int:
        return int(eval("".join([char if char != '/' else '//' for char in s if char != ' '])))
                