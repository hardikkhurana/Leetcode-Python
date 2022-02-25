class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        res=[]
        h={"0":[],"1":[],"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        def helper(s,i):
            if i==len(digits):
                res.append(s)
                return
            for j in h[digits[i]]:
                helper(s+j,i+1)
            
        helper("",0)
        return res
        