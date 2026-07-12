class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def compare(comp):
            filtered_comp = [x for x in comp if x != "."]
            return len(filtered_comp) == len(set(filtered_comp))

        for row in board:
            if not compare(row):
                return False

        for col in range(9):
            comp = [
                board[0][col],
                board[1][col],
                board[2][col],
                board[3][col],
                board[4][col],
                board[5][col],
                board[6][col],
                board[7][col],
                board[8][col]
                ]
            if not compare(comp):
                return False

        for j in range(0,9,3):
            for i in range(0,9,3):
                comp = [
                        board[j][i + 0],
                        board[j][i + 1],
                        board[j][i + 2],
                        board[j + 1][i + 0],
                        board[j + 1][i + 1],
                        board[j + 1][i + 2],
                        board[j + 2][i + 0],
                        board[j + 2][i + 1],
                        board[j + 2][i + 2],
                    ]
                if not compare(comp):
                    return False

        return True