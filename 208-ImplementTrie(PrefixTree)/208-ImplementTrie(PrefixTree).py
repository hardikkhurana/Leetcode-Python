[

    def search(self, word: str) -> bool:

        curr.word=True
        
            if c not in curr.ch:
                curr.ch[c]=TrieNode()
            curr = curr.ch[c]
        curr=self.t
        for c in word:
    def startsWith(self, prefix: str) -> bool:
        curr=self.t
        


        curr=self.t
        for c in word:
            if c not in curr.ch:
                return False
            curr = curr.ch[c]
        return curr.word
        for c in prefix:
            if c not in curr.ch:
                return False
            curr = curr.ch[c]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
