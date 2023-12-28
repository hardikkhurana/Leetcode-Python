[
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
            mid=(l+r)//2
                r=mid-1
        return -1
