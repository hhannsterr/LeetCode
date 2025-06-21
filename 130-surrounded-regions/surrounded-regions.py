class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            stack = [(r, c)]
            safe.add((r, c))
            while stack:
                row, col = stack.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 'O' and (nr, nc) not in safe:
                            safe.add((nr, nc))
                            stack.append((nr, nc))
        
        if not board or not board[0]:
            return board
        
        rows, cols = len(board), len(board[0])
        safe = set()

        for c in range(cols):
            if board[0][c] == 'O' and (0, c) not in safe:
                dfs(0, c)
            if board[rows-1][c] == 'O' and (rows-1, c) not in safe:
                dfs(rows-1, c)
        
        for r in range(rows):
            if board[r][0] == 'O' and (r, 0) not in safe:
                dfs(r, 0)
            if board[r][cols-1] == 'O' and (r, cols-1) not in safe:
                dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'
        
        return board
        