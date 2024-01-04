        res=0
        for num,freq in c.items():
            tmp=freq
            if tmp==1:
                return -1

            if (tmp+1)%3==0:
                tmp-=2
                res+=1
            
            
            if (tmp-1)%3==0:
                tmp-=4
                res+=2


            if tmp and tmp%3==0:
                rem=tmp//3
                tmp-=(rem*3)
                res+=rem
            
            
        return res
    def minOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        print(c)
class Solution:
