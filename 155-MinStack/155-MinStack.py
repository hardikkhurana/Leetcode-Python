[
    def __init__(self):
        

    def push(self, val: int) -> None:
        
    def pop(self) -> None:
        

    def top(self) -> int:
        
    def getMin(self) -> int:
        


        self.st=[] #[int,min]
            self.st.append([val,min(self.st[-1][1],val)])
        if self.st:
        else:
            self.st.append([val,val])
        return self.st[-1][0]
        return self.st[-1][1]
        if self.st: self.st.pop()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
class MinStack:

