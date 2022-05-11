class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        self.res=[]
        
        def helper(path,start,k,target):
            if k==0 and target==0:
                self.res.append(path)
                return
            if k==0 or target<=0:
                return 
            for i in range(start,10):
                helper(path+[i],i+1,k-1,target-i)
        
        helper([],1,k,n)
        return self.res