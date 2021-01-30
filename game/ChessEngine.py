"""
Responsible for storing information about the current state of the chess game
"""


class GameState():
    def __init__(self):
        # The possible board sizes are 8x8, 10x10, 12x12, 14x14, 16x16
        # First char represents colour of piece 'b' or 'w'
        # Second char represents the type of the piece
        self.board = [[
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]
        ],
        [
            ["bR", "bN", "bN", "bB", "bQ", "bK", "bB", "bN", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wN", "wB", "wK", "wQ", "wB", "wN", "wN", "wR"]
        ],
        [
            ["bR", "bN", "bN", "bB", "bB", "bQ", "bK", "bB", "bB", "bN", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bV"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wV"],
            ["wR", "wN", "wN", "wB", "wB", "wK", "wQ", "wB", "wB", "wN", "wN", "wR"]
        ],
        [
            ["bR", "bR", "bN", "bN", "bB", "bB", "bQ", "bK", "bB", "bB", "bN", "bN", "bR", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bV", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wV", "wP", "wP"],
            ["wR", "wR", "wN", "wN", "wB", "wB", "wK", "wQ", "wB", "wB", "wN", "wN", "wR", "wR"]
        ],
        [
            ["bR", "bR", "bN", "bN", "bB", "bB", "bQ", "bQ", "bK", "bQ", "bB", "bB", "bN", "bN", "bR", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bV", "bV", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wV", "wV", "wP", "wP", "wP"],
            ["wR", "wR", "wN", "wN", "wB", "wB", "wQ", "wK", "wQ", "wQ", "wB", "wB", "wN", "wN", "wR", "wR"]
        ]
        ]
        self.whiteToMove = True
        self.moveLog = []

    # doesn't work for castling, pawn promotion, and en-passant
    def makeMove(self, move, boardNum):
        self.board[boardNum][move.startRow][move.startCol] = "--"
        self.board[boardNum][move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)  # log the move
        self.whiteToMove = not self.whiteToMove  # swap players

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    # self.moveLibrary = {"pawn": self.getPawnMove, "vanguard": self.getVanguardMove,
    #                     "rook": self.getRookMove, "knight": self.getKnightMove,
    #                     "bishop": self.getBishopMove, "queen": self.getQueenMove, "king": self.getKingMove}

    def getValidMoves(self):
        return self.getPossibleMoves()

    def getPossibleMoves(self, boardNum):
        moves_list = []
        for y in range(len(self.board[boardNum])):
            for x in range(len(self.board[boardNum][y])):
                userTurn = self.board[boardNum][y][x][0]
                if (userTurn == "white" and self.whiteToMove) or (userTurn == "black" and self.blackToMove):
                    userPiece = self.board[boardNum][y][x][1]
                    self.moveLibrary[userPiece](y, x, moves_list)

        return moves_list

    def getPawnMove(self, boardNum, y, x, moves_list):
        # Regular movement of White pawn
        boardSize = [6, 8, 10, 12, 14]
        if self.whiteToMove:
            if self.board[y - 1][x] == "--":
                moves_list.append(Move((y, x), (y - 1, x), self.board))
                if y == boardSize[boardNum] and self.board[y-2][x] == "--":
                    moves_list.append(Move((y, x), (y - 2, x), self.board))

            # capturing piece to left
            if (x - 1) >= 0:
                if self.board[y - 1][x - 1][0] == "black":
                    moves_list.append(Move((y, x), (y - 1, x - 1), self.board))

            # capturing piece to right
            if (x + 1) <= boardSize[boardNum]+1:
                if self.board[y - 1][x + 1][0] == "black":
                    moves_list.append(Move((y, x), (y + 1, x + 1), self.board))

        # Regular movement of Black pawn
        else:
            if self.board[y + 1][x] == "--":
                moves_list.append(Move((y, x), (y + 1, x), self.board))
                if y == 2 and self.board[y+2][x] == "--":
                    moves_list.append(Move((y, x), (y + 2, x), self.board))

            # capturing piece to left
            if (x + 1) <= boardSize[boardNum]+1:
                if self.board[y + 1][x + 1][0] == "black":
                    moves_list.append(Move((y, x), (y + 1, x + 1), self.board))

            # capturing piece to right
            if (x - 1) >= 0:
                if self.board[y + 1][x - 1][0] == "black":
                    moves_list.append(Move((y, x), (y - 1, x - 1), self.board))

class Move():
    # Chess notation
    ranksToRows = [{"1": 7, "2": 6, "3": 5, "4": 4,
                    "5": 3, "6": 2, "7": 1, "8": 0},

                   {"1": 9, "2": 8, "3": 7, "4": 6, "5": 5,
                    "6": 4, "7": 3, "8": 2, "9": 1, "10": 0},

                   {"1": 11, "2": 10, "3": 9, "4": 8, "5": 7, "6": 6,
                    "7": 5, "8": 4, "9": 3, "10": 2, "11": 1, "12": 0},

                   {"1": 13, "2": 12, "3": 11, "4": 10, "5": 9, "6": 8, "7": 7,
                    "8": 6, "9": 5, "10": 4, "11": 3, "12": 2, "13": 1, "14": 0},

                   {"1": 15, "2": 14, "3": 13, "4": 12, "5": 11, "6": 10, "7": 9, "8": 8,
                    "9": 7, "10": 6, "11": 5, "12": 4, "13": 3, "14": 2, "15": 1, "16": 0},
                   ]

    rowsToRanks = [{v: k for k, v in ranksToRows[0].items()},
                   {v: k for k, v in ranksToRows[1].items()},
                   {v: k for k, v in ranksToRows[2].items()},
                   {v: k for k, v in ranksToRows[3].items()},
                   {v: k for k, v in ranksToRows[4].items()}]

    filesToCols = [{"a": 0, "b": 1, "c": 2, "d": 3,
                    "e": 4, "f": 5, "g": 6, "h": 7},
                   {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
                    "f": 5, "g": 6, "h": 7, "i": 8, "j": 9},
                   {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
                    "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11},
                   {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,
                    "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13},
                   {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,
                    "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15}
                   ]

    colsToFiles = [{v: k for k, v in filesToCols[0].items()},
                   {v: k for k, v in filesToCols[1].items()},
                   {v: k for k, v in filesToCols[2].items()},
                   {v: k for k, v in filesToCols[3].items()},
                   {v: k for k, v in filesToCols[4].items()}]

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRank[r]
