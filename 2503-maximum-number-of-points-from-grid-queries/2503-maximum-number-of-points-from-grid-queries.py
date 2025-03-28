from heapq import heappop, heappush
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        m, n = len(grid), len(grid[0])
        k = len(queries)

        queries_sorted = sorted([val, idx] for idx , val in enumerate(queries))
        ans = [0] * k

        visited = [[False] * n for i in range(m)]

        heap = [(grid[0][0], 0 ,0)]
        visited[0][0] = True
        count = 0

        def dfs(val):
            nonlocal count
            while heap and heap[0][0] < val:
                g, x, y = heappop(heap)
                count += 1
                for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny <n and visited[nx][ny] is False:
                        visited[nx][ny] = True
                        heappush(heap, (grid[nx][ny],nx,ny))

        
        for val, idx in queries_sorted:
            dfs(val)
            ans[idx] = count


        return ans
