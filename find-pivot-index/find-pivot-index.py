class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lside,rside=[0 for i in range(len(nums)+2)],[0 for i in range(len(nums)+2)]
        prev=0
        for i in range(len(nums)):
            lside[i+1]=prev+nums[i]
            prev=lside[i+1]
        prev=0
        for i in range(len(nums)-1,-1,-1):
            rside[i+1]=prev+nums[i]
            prev=rside[i+1]         
        for i in range(1,len(nums)+1):
            if lside[i-1]==rside[i+1]:
                return i-1
        return -1