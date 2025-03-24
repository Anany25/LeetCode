class Solution(object):
    def isValidSudoku(self, board):
        ans = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    ans += [(i, val), (val , j), (i // 3, j // 3, val)]
        
        print(ans, set(ans))

        return len(ans) == len(set(ans))