# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         ans_mat = mat.copy()
#         for i in range(0, len(mat)):
#             for j in range(0, len(mat[i])):
#                 self.bfs(ans_mat, i, j, 0)
#         return ans_mat
    
#     def bfs(self, mat, x, y, depth):
#         if mat[x][y] == 0:
#             return depth
        
#         dx = [0, 0, 1, -1]
#         dy = [1, -1, 0, 0]
        
#         min_depth = inf
#         for i in range(0,4):
#             cur_dep = self.bfs(mat, dx[i] , dy[i], depth+1)
#             min_depth = min(min_depth, cur_dep)
#         return min_depth

# Time limit

from typing import List
from collections import deque
 
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:        
        m, n = len(mat), len(mat[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r,c))
                else :
                    mat[r][c] = -1

        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        while q:
            r, c = q.popleft()
            for i in range(4): # 4방향 순회 - bfs
                nr, nc = r + dr[i], c + dc[i]
                # print(nr, nc)
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1:
                    continue
                
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr,nc))
        return mat
    
    
Solution.updateMatrix(Solution, [[0,0,0],[0,1,0],[1,1,1]])