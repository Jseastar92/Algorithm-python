'''
Brute Force modifying
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ''' Brute force'''
        max_size = 9
        
        def valid(list1):
            for ind, val in enumerate(list1):
                if val.isdigit():
                    if val in list1[ind+1:]:
                        return False
            return True
            
        for origin_list in board:
            if not valid(origin_list) :
                return False

        for n in range(max_size):
            vertical_list = [board[j][n] for j,v in enumerate(board)]
            if not valid(vertical_list) :
                return False
                            
        for i in range(max_size):
            inner_list = []
            outer_ind = int(i/3)*3
            
            for i1 in range(outer_ind, outer_ind+3):
                for i2 in range(i%3*3,i%3*3+3):
                    inner_list.append(board[i1][i2])        
        
            if not valid(inner_list) :
                return False
            
        return True

'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ''' Brute force'''
        max_size = 9
        
        ori_list = board[:]
        for l1 in ori_list:
            for ind, l in enumerate(l1):
                if l.isdigit():
                    if l in l1[ind+1:]:
                        print(l)
                        return False
                
        # print("ori")
        # print(ori_list)
        
        vertical_list = []
        for n in range(max_size):
            a = [board[j][n] for j,v in enumerate(board)]
            for ind, val in enumerate(a):
                if val.isdigit():
                    if val in a[ind+1:]:
                        print(val)
                        return False
                
            vertical_list.append(a)
        # print("ver")
        # print(vertical_list)
                    
        box_list = []
        for i in range(9):
            inner_list = []
            outer_ind = int(i/3)
            
            for i1 in range(outer_ind*3, outer_ind*3+3):
                for i2 in range(i%3*3,i%3*3+3):
                    inner_list.append(board[i1][i2])        
                    
            for ind, val in enumerate(inner_list):
                if val.isdigit():
                    if val in inner_list[ind+1:]:
                        print(val)
                        return False

            box_list.append(inner_list)
        # print("box")
        # print(box_list)
        
        return True
'''