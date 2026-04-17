class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map1=set()
        hash_map2=set()
        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] not in hash_map1:
                        hash_map1.add(board[i][j])
                    else:
                        return False
                if board[j][i].isnumeric():
                    if board[j][i] not in hash_map2:
                        hash_map2.add(board[j][i])
                    else:
                        return False
            hash_map1=set()
            hash_map2=set()
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                matrix=set()
                for i in range(3):
                     for j in range(3):
                        if board[box_row+i][box_col+j].isnumeric():
                            if board[box_row+i][box_col+j] not in matrix:
                                matrix.add(board[box_row+i][box_col+j]) 
                            else:
                                return False         
        return True
                



        

        