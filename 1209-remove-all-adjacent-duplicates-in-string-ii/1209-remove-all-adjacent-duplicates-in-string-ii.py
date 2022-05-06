class Solution:
    def removeDuplicates(self, s, k):
        stack = [['#',0]]
        for c in s:
            x, n = stack[-1]
            if c == x:
                if k-1 == n: stack.pop()
                else: stack[-1] = [c, n+1]
            else: stack.append([c, 1])
        return "".join(x*n for x,n in stack)