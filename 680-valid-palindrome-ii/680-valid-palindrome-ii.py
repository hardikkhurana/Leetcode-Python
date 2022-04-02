class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(lo,hi,removed):
            while lo<hi:
                if s[lo]!=s[hi]:
                    if removed:
                        return False
                    return helper(lo+1,hi,True) or helper(lo,hi-1,True)
                lo += 1
                hi -= 1
            return True
        
        return helper(0,len(s)-1,False)
        