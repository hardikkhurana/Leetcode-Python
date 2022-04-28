class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(idx, arr):
            arr.append(idx)
            visited[idx] = True
            for nei in graph[idx]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei, arr)
            
        graph = collections.defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        n = len(s)
        s_list = list(s)
        visited = [False] * n
        for idx in range(n):
            if not visited[idx]:
                arr = []
                dfs(idx, arr)
                arr.sort()
                letter = [s[i] for i in arr]
                letter.sort()
                for i in range(len(arr)):
                    s_list[arr[i]] = letter[i]
        return ''.join(s_list)