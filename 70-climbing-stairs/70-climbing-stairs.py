class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        x,y=1,2
        for _ in range(n-2):
            z=x+y
            x=y
            y=z
        return z