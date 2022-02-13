

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		ans=0
		temp=nums.copy()
		h={}
		temp.sort()
		for i in range(len(nums)):
		    h[nums[i]]=i
		init=0
		for i in range(len(nums)):
		    if nums[i] != temp[i]:
		        ans+=1
		        init=nums[i]
		        nums[i],nums[h[temp[i]]] = nums[h[temp[i]]],nums[i]
		        h[init] = h[temp[i]]
		        h[temp[i]]=i
		
	    return ans

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends