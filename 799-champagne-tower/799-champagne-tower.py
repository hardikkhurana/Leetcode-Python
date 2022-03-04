class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass=[poured]
        for i in range(query_row):
            glass_next=[0 for _ in range(len(glass)+1)]
            for j in range(len(glass)):
                amount=(glass[j]-1)/2
                if amount<0:
                    continue
                glass_next[j]+=amount
                glass_next[j+1]+=amount
            glass=glass_next
        return min(1,glass[query_glass])