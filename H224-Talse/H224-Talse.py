class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace("/", "//")
        return eval(s)
