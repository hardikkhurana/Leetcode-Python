"
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        if not digits:
            return []
        }

        res=[]
        def helper(ind,curr):
            if ind==len(digits):
                res.append(curr)
            for c in d[digits[ind]]:
                helper(ind+1,curr+c)
        helper(0,"")
                return
        return res
