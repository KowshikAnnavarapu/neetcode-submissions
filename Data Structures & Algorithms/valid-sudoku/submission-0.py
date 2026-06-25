class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                if num == "." :
                    continue
                box = (row//3,col//3)

                if row not in rows:
                    rows[row] = set()
                if col not in cols:
                    cols[col] = set()
                if box not in boxes:
                    boxes[box] = set()
                    
                if num in rows[row] or num in cols[col] or num in boxes[box]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)
        return True
        