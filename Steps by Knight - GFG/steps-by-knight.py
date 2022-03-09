from collections import deque
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    w,x=KnightPos
		endX,endY=TargetPos
		moveX=[1,2,1,2,-1,-2,-1,-2]
	    moveY=[2,1,-2,-1,-2,-1,2,1]
		def valid(x,y):
		    return x>0 and y>0 and x<=N and y<=N
	
	    visited=set()
	    visited.add((w,x))
	    rn=deque()
	    rn.append((w,x,0))
	    
	    k=0
	    while rn:
	        a,b,mov=rn.popleft()
	        if a==endX and b==endY:
	            return mov
	        for p,q in zip(moveX,moveY):
	            if valid(a+p,b+q) and (a+p,b+q) not in visited:
	                rn.append((a+p,b+q,mov+1))
	                visited.add((a+p,b+q))
	        #print(visited)
	   
	        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends