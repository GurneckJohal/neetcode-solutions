class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = {}
        col_set = {}
        box_set = {}
        
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                val = board[i][j]

                if val == ".":
                    continue

                box_index = (i // 3 , j // 3)

                if i not in row_set:
                    row_set[i] = set()
                if j not in col_set:
                    col_set[j] = set()
                if box_index not in box_set:
                    box_set[box_index] = set()
                
                if val in row_set[i] or val in col_set[j] or val in box_set[box_index]:
                    return False
                
                row_set[i].add(val)
                col_set[j].add(val)
                box_set[box_index].add(val)
        
        return True