class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        
        for i in range(m):
            for j in range(n):
                heapq.heappush(diagonals[i - j], mat[i][j])  
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = heapq.heappop(diagonals[i - j])

        return mat