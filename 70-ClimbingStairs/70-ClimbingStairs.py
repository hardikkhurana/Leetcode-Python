2
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n-1):
            c = a+b
            a=b
            b=c
        return b
