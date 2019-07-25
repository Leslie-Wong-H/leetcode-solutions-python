#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nAliveCnt = 0
        boardRow = len(board)
        boardColumn = len(board[0])

        copyBoard = [[0 for col in range(boardColumn)] for row in range(boardRow)]
        
        for i in range(boardRow):
            for j in range(boardColumn):
                copyBoard[i][j] = board[i][j]

        for i in range(boardRow):
            for j in range(boardColumn):
                nAliveCnt = 0

                if (i - 1 >= 0) and (j - 1 >= 0) and (board[i - 1][j - 1] == 1):
                    nAliveCnt += 1
                
                if (i - 1 >= 0) and (board[i - 1][j] == 1):
                    nAliveCnt += 1

                if (i - 1 >= 0) and (j + 1 < boardColumn) and (board[i - 1][j + 1] == 1):
                    nAliveCnt += 1
                
                if (j - 1 >= 0) and (board[i][j - 1] == 1):
                    nAliveCnt += 1
                
                if (j + 1 < boardColumn) and (board[i][j + 1] == 1):
                    nAliveCnt += 1
                
                if (i + 1 < boardRow) and (j - 1 >= 0) and (board[i + 1][j - 1] == 1):
                    nAliveCnt += 1
                
                if (i + 1 < boardRow) and (board[i + 1][j] == 1):
                    nAliveCnt += 1
                
                if (i + 1 < boardRow) and (j + 1 < boardColumn) and (board[i + 1][j + 1] == 1):
                    nAliveCnt += 1

                
                if board[i][j] == 1:
                    if (nAliveCnt == 2 or nAliveCnt == 3):
                        copyBoard[i][j] = 1
                    else:
                        copyBoard[i][j] = 0
                    
                if board[i][j] == 0:
                    if nAliveCnt == 3:
                        copyBoard[i][j] = 1

        for i in range(boardRow):
            for j in range(boardColumn):
                board[i][j] = copyBoard[i][j]

    
