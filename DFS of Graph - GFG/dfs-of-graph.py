#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        ans=[]
        visited=set()
        st=[0]
        while len(st)!=0:
            s=st.pop()
            if s not in visited:
                ans.append(s)
                visited.add(s)
                for j in reversed(adj[s]):
                    if j not in visited:
                        st.append(j)
        return ans
                
        
        
        
        
    """
    def dfsOfGraph(self, V, adj):
        ans=[]
        def dfs(ele,visited):
            if ele in visited:
                return
            ans.append(ele)
            visited.add(ele)
            
            for i in adj[ele]:
                dfs(i,visited)
                
        dfs(0,set())
        return ans
            
    """
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends