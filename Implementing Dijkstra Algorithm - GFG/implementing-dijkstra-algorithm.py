import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    
    def dijkstra(self, V, adj, S):
        ans=[0 for i in range(V)]
        visited=set()
        minheap=[(0,S)]
        while minheap:
            new_weight,new_node=heapq.heappop(minheap)
            if new_node in visited:
                continue
            ans[new_node]=new_weight
            visited.add(new_node)
            for node,weight in adj[new_node]:
                if node not in visited:
                    heapq.heappush(minheap,[weight+new_weight,node])
        return ans  
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends