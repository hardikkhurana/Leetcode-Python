class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res=[]
        a=1
        s=set(['a', 'e', 'i', 'o','u',"I","O","U","A","E"])
        for word in sentence.split():
            if word[0] in s:
                res.append((word+"ma"+("a"*a)))
            else:
                res.append((word[1:]+word[0]+"ma"+("a"*a)))
            a+=1
        return " ".join(res)