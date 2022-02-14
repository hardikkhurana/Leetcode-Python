#User function template for Python

class Solution:
	def shortest_distance(self, G):
	    for i in range(len(G)):
	        for j in range(len(G[0])):
	            if G[i][j]==-1:
	                G[i][j]=float("inf")
	    nV=len(G)
	    def print_solution(distance):
            for i in range(nV):
                for j in range(nV):
                    if(distance[i][j] == float("inf")):
                        G[i][j]=-1
                    else:
                        G[i][j]=distance[i][j]
                        
                        
                        	    
	    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
        for k in range(nV):
            for i in range(nV):
                for j in range(nV):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        print_solution(distance)


#{ 
#  Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends