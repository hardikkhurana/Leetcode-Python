[
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
            l,r=0,len(nums)-1
            res=-1
            while l<=r:
                if nums[mid]<target:

                    l=mid+1
                mid = (l+r)//2
                else:
        def binary(left_bias):
                    res = mid
                elif nums[mid]>target:
                    r=mid-1
                    if left_bias:
                    else:
                        l=mid+1
                        r=mid-1
            return res
        return [binary(True),binary(False)]
