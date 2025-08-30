class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        embed_row = {
            0: 0, 1: 0, 2: 0,
            3: 4, 4: 4, 5: 4,
            6: 7, 7: 7, 8: 7,
        }

        embed_col = {
            0: 0, 1: 0, 2: 0,
            3: 1, 4: 1, 5: 1,
            6: 2, 7: 2, 8: 2,
        }

        col_map = {
            0: set(), 1: set(), 2: set(),
            3: set(), 4: set(), 5: set(),
            6: set(), 7: set(), 8: set(),
        }

        emb_map = {
            0: set(), 1: set(), 2: set(),
            4: set(), 5: set(), 6: set(), 
            7: set(), 8: set(), 9: set(), 
        }

        for row in range(9):
            row_map = set()
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                
                # check row
                if val in row_map:
                    return False
                else:
                    row_map.add(val)

                # check col
                if val in col_map[col]:
                    return False
                else:
                    col_map[col].add(val)

                # check emb
                emb = embed_row[row] + embed_col[col]
                if val in emb_map[emb]:
                    return False
                else:
                    emb_map[emb].add(val)
        
        return True
