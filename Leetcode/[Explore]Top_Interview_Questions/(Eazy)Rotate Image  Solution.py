class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = matrix
        mat_len = len(matrix)
        # 총 길이가 n은 n/2회 반복
        # 3-2 4-2 5-2 6은 3회
        total_cnt = int(mat_len/2)
        first_index = 0
        last_index = mat_len-1
        for i in range(total_cnt):
            # 루프 당 각 매트릭스 길이만큼인데 들어갈수록 길이가 -2 됨. (첫인덱스는+1 라스트는-1)
            # 퍼스트부터 1씩 증가하는거 하나, 라스트부터 1씩 줄어드는거 하나
            f = 0
            print(first_index, last_index)
            for j in range(first_index, last_index):
                m[i][j] , m[j][last_index], m[last_index][last_index-f], m[last_index-f][i] = \
                m[last_index-f][i], m[i][j] , m[j][last_index], m[last_index][last_index-f]
                f+=1
                print(matrix)
            first_index+=1
            last_index-=1

'''
컴프리헨션으로 짠 코드 ( 레퍼런스 )
matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
'''
