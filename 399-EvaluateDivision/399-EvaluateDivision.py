            while q:
                node,val=q.popleft()
                if node==end:
                    return val
                visited.add(node)
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        q.append((neighbor, val * weight))
            return -1.0


        for eq,val in zip(equations,values):
            graph[eq[0]][eq[1]]=val
            graph[eq[1]][eq[0]]=1/val
        
        res=[]
        print(graph)
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                res.append(-1.0)
            else:
                result = bfs(dividend, divisor)
                res.append(result)
        
        return res
