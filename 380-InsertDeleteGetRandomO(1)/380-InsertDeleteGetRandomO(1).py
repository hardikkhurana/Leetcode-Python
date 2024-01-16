class RandomizedSet:

    def __init__(self):
        self.d={}
        self.l=[]


    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val) 
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        indRemove = self.d[val]
        last = self.l[-1]
        self.d[last] = indRemove
        self.l[indRemove],self.l[-1] = self.l[-1],self.l[indRemove]
        self.l.pop()
        self.d.pop(val)
        return True
        

    def getRandom(self) -> int:
