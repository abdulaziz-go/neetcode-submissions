class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row = [x for x in board[r] if x != "."]
            if len(row) != len(set(row)):
                return False
            
        
        for c in range(9):
            col = [board[r][c] for r in range(9) if board[r][c] != "."]
            if len(col) != len(set(col)):
                return False
            
        for br in (0,3,6):
            for bc in (0,3,6):
                box = []
                for r in range(br , br+3):
                    for c in range(bc , bc+3):
                        if board[r][c] != ".":
                            box.append(board[r][c])
                if len(box) != len(set(box)):
                    return False
        
        return True
