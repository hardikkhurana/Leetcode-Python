#User function Template for python3
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        
        
        def bfs(s):
            ans=[]
            visit=set()
            queue=[]
            queue.append(s)
            visit.add(s)
            while queue:
                s=queue.pop(0)
                ans.append(s)
                for i in adj[s]:
                    if i not in visit:
                        queue.append(i)
                        visit.add(i)
            return ans
        return bfs(0)
                        
            
            
        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends