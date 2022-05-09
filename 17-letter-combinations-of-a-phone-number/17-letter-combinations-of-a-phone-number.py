class Solution:
    def sol(self,digits,i,curr,out,d):
        if i>=len(digits):
            out.append(curr)
            return
        letters=d[digits[i]]
        for j in letters:
            curr+=j
            self.sol(digits,i+1,curr,out,d)
            curr=curr[:-1]
        return
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if digits=="":
            return []
         
        out=[]
        i=0
        self.sol(digits,i,"",out,d)
        return out
        
        