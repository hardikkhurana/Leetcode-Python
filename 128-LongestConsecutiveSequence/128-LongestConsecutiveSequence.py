[
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        d={i:1 for i in nums}

        for i in d.keys():
            if i-1 in d:
                continue
            n = i
            while n+1 in d:
                n+=1
                d[n+1]=d[n]+1
        return max(d.values())
