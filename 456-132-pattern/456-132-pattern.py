class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        maxi=float("-inf")
        st=[]
        n=len(nums)
        for i in range(n-1,-1,-1):
            if(nums[i]<maxi):
                return True
            while(st and st[-1]<nums[i]):
                maxi=st.pop()
            st.append(nums[i])
        return False