        meetings.sort()
        busy = [] #(end,room)
        available = ([i for i in range(n)])
        heapify(available)
        count = defaultdict(int)
        mx = 0
        
        for start,end in meetings:
            while busy and busy[0][0]<=start:
                _,r = heappop(busy)
                heappush(available,r)
            
            if available:
                r = heappop(available)
                heappush(busy,(end,r))
            else:
                time,r = heappop(busy)
                heappush(busy,(time+end-start,r))
            
            
            count[r]+=1
            mx = max(mx,count[r])
        
        for i in range(n):
            if count[i]==mx:
                return i
