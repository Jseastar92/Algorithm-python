from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(image, row, col, color, target):    
            if row < 0 or col < 0:
                return
            
            if row >= len(image) or col >=  len(image[0]):
                return 
         
            if image[row][col] != target or image[row][col] == color:
                return
            
            image[row][col] = color
            dr = [0, 0, -1, 1] # top, bot, left, right
            dc = [-1, 1, 0, 0]
            for i in range(0, 4):
                bfs(image, dr[i]+row, dc[i]+col, color, target)
        bfs(image, sr, sc, color, image[sr][sc])
        return image

# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# color = 2
image =[[0,0,0],[0,0,0]]
sr =1
sc =0
color =2

Solution.floodFill(Solution, image, sr, sc, color)