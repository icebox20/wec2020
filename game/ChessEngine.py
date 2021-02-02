"""
Responsible for storing information about the current state of the chess game
"""
def is_valid_square(boardNum,board,x,y):
    boardSize = [8, 10, 12, 14, 16]
    if x >= boardSize[boardNum] or y >= boardSize[boardNum] or x < 0 or y < 0:
        return False
    if board[y][x] == "--":
        return True
    return False 

def is_empty(board, x, y):
    if board[y][x] == "--" or board[y][x][0] == "":
        return True
    return False

class GameState():
    def __init__(self):
        # The possible board sizes are 8x8, 10x10, 12x12, 14x14, 16x16
        # First char represents colour of piece 'b' or 'w'
        # Second char represents the type of the piece
        self.board = [[
            ["bR", "bN", "bB", "bK", "bQ", "bB", "bN", "bR"],
            ["bV", "bP", "bP", "bP", "bP", "bP", "bP", "bV"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wV", "wP", "wP", "wP", "wP", "wP", "wP", "wV"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ],
        [
            ["bR", "bN", "bN", "bB", "bK", "bQ", "bB", "bN", "bN", "bR"],
            ["bV", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bV"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wV", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wV"],
            ["wR", "wN", "wN", "wB", "wQ", "wK", "wB", "wN", "wN", "wR"]
        ],
        [
            ["bR", "bN", "bN", "bB", "bB", "bQ", "bK", "bB", "bB", "bN", "bN", "bR"],
            ["bV", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bV"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wV", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wV"],
            ["wR", "wN", "wN", "wB", "wB", "wK", "wQ", "wB", "wB", "wN", "wN", "wR"]
        ],
        [
            ["bR", "bR", "bN", "bN", "bB", "bB", "bQ", "bK", "bB", "bB", "bN", "bN", "bR", "bR"],
            ["bV", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bV"],
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
            ["wV", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wV"],
            ["wR", "wR", "wN", "wN", "wB", "wB", "wK", "wQ", "wB", "wB", "wN", "wN", "wR", "wR"]
        ],
        [
            ["bR", "bR", "bN", "bN", "bB", "bB", "bQ", "bK", "bQ", "bQ", "bB", "bB", "bN", "bN", "bR", "bR"],
            ["bV", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bV"],
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
            ["wV", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wV"],
            ["wR", "wR", "wN", "wN", "wB", "wB", "wQ", "wQ", "wK", "wQ", "wB", "wB", "wN", "wN", "wR", "wR"]
        ]
        ]
        self.whiteToMove = True
        self.vanguardleft = 3
        self.moveLog = []
        self.whiteKingLocation = (0, 0)
        self.blackKingLocation = (0, 0)

    def kings_locs (self, boardNum):
        self.boardSize = [6, 8, 10, 12, 14]
        self.whiteKingLocation = (self.boardSize[boardNum]+1, (self.boardSize[boardNum])/2)
        self.blackKingLocation = (0, ((self.boardSize[boardNum])/2) + 1)
    

    # doesn't work for castling, pawn promotion, and en-passant
    def makeMove(self, move, boardNum):
        self.board[boardNum][move.startRow][move.startCol] = "--"
        self.board[boardNum][move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)  # log the move
        self.whiteToMove = not self.whiteToMove  # swap players
        #update the king locations
        if move.pieceMoved == "wK":
            self.whiteKingLocation = (move.endRow, move.endCol)
        elif move.pieceMoved == "bK":
            self.blackKingLocation = (move.endRow, move.endCol)
        
        

    def undoMove(self, boardNum):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[boardNum][move.startRow][move.startCol] = move.pieceMoved
            self.board[boardNum][move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
                    #update the king locations
            if move.pieceMoved == "wK":
                self.whiteKingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved == "bK":
                self.blackKingLocation = (move.startRow, move.startCol)

    def allValidMoves(self, boardNum):
        
        moves=self.allPossibleMoves(boardNum)
        
        for i in range(len(moves)-1, -1, -1):
            self.makeMove(moves[i], boardNum)
            self.whiteToMove = not self.whiteToMove
            if self.inCheck(boardNum, moves):
                print("In Check ", "White" if self.whiteToMove else "Black")
                moves.remove(moves[i])
            self.whiteToMove =not self.whiteToMove
            self.undoMove(boardNum)
        # for move in moves
        #     if board[boardNum][move.startRow][move.startCol][1] == "K":
        #         moves.remove(moves[i])
        return  moves
    
    
    def inCheck (self, boardNum, moves):
        for move in moves:
            if self.board[boardNum][move.startRow][move.startCol][1] == "K":
                return True
    
    def squareUnderAttack(self, boardNum,r, c):
        print("-------------------------------------------------------------------SUA")
        self.whiteToMove = not self.whiteToMove
        oppMoves = self.allPossibleMoves(boardNum)
        self.whiteToMove = not self.whiteToMove
        for move in oppMoves:
            if move.endRow == r and move.endCol == c:
                return True
        return False
        

    def allPossibleMoves(self, boardNum):
        print("-------------------------------------------------------------------")
        moves_list = []
        for y in range(len(self.board[boardNum])):
            for x in range(len(self.board[boardNum][y])):
                userTurn = self.board[boardNum][y][x][0]
                if (userTurn == "w" and self.whiteToMove) or (userTurn == "b" and (self.whiteToMove == False)):

                    userPiece = self.board[boardNum][y][x][1]
                    if userPiece == "P":
                        self.PawnMove(boardNum, y, x, moves_list)
                    elif userPiece == "R":
                        self.RookMove(boardNum, y, x, moves_list)
                    elif userPiece == "N":
                        self.KnightMove(boardNum, y, x, moves_list)
                    elif userPiece == "B":
                        self.BishopMove(boardNum, y, x, moves_list)
                    elif userPiece == "Q":
                        self.QueenMove(boardNum, y, x, moves_list)
                    elif userPiece == "K":
                        self.KingMove(boardNum, y, x, moves_list)
                    else:
                        self.VanguardMove(boardNum, y, x, moves_list)
        return moves_list

    def PawnMove(self, boardNum, y, x, moves_list):
        # Regular movement of White pawn
        #print("Check:",y,x )
        #print("----------------")
        boardSize = [6, 8, 10, 12, 14]
        if self.whiteToMove == True: 
            #print("White")
            for i in range(1,4):
                if self.board[boardNum][y - i][x] == "--":
                    moves_list.append(Move((y, x), (y - i, x), self.board[boardNum]))
                    #print("W:",y + i,x, y, x)
            # capturing piece to left
            if (x - 1) >= 0 and self.board[boardNum][y - 1][x][0] == "b":
                if self.board[boardNum][y - 1][x - 1][0] == "b":
                    moves_list.append(Move((y, x), (y - 1, x - 1), self.board[boardNum]))
            # capturing piece to right
            if (x + 1) <= boardSize[boardNum]+1 and self.board[boardNum][y - 1][x][0] == "b":
                if self.board[boardNum][y - 1][x + 1][0] == "b":
                    moves_list.append(Move((y, x), (y - 1, x + 1), self.board[boardNum]))
        # Regular movement of Black pawn
        else:
            #print("Black")
            for i in range(1, 4):
                if y >= boardSize[boardNum] or x >= boardSize[boardNum] or y < 0 or x < 0:
                    break
                if self.board[boardNum][y + i][x] == "--":
                    moves_list.append(Move((y, x), (y + i, x), self.board[boardNum]))
                    #print("B:",y + i,x, y, x)
            # capturing piece to left
            if (x + 1) >= 0 and self.board[boardNum][y + 1][x][0] == "w":
                if self.board[boardNum][y + 1][x - 1][0] == "w":
                    moves_list.append(Move((y, x), (y + 1, x - 1), self.board[boardNum]))
            # capturing piece to right
            if (x - 1) <= boardSize[boardNum]-1 and self.board[boardNum][y + 1][x][0] == "w":
                if self.board[boardNum][y + 1][x + 1][0] == "w":
                    moves_list.append(Move((y, x), (y + 1, x + 1), self.board[boardNum]))

    def RookMove(self, boardNum, y, x, moves_list):
        direction = ((-1, 0), (0, -1), (1, 0), (0, 1))
        boardSize = [8, 10, 12, 14, 16]
        if self.whiteToMove:
            oppositeColour = "b"
        else:
            oppositeColour = "w"

        for i in direction:
            for j in range(1, boardSize[boardNum]):
                RowEnd = y + i[0] * j
                ColumnEnd = x + i[1] * j
                if 0 <= RowEnd < boardSize[boardNum] and 0 <= ColumnEnd < boardSize[boardNum]:
                    Limit = self.board[boardNum][RowEnd][ColumnEnd]
                    if Limit == "--":
                        moves_list.append(Move((y, x), (RowEnd, ColumnEnd), self.board[boardNum]))
                    elif Limit[0] == oppositeColour:
                        moves_list.append(Move((y, x), (RowEnd, ColumnEnd), self.board[boardNum]))
                        break
                    else:
                        break
                else:
                    break

    def BishopMove(self, boardNum, r, c, moves_list):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))  # 4 diagonal
        # check enemy's color
        if self.whiteToMove:
            enemyColor = "b"
        else:
            enemyColor = "w"
        # check board size
        boardSize = [6, 8, 10, 12, 14]

        for d in directions:
            for i in range(1, boardSize[boardNum] + 2):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < boardSize[boardNum] + 2 and 0 <= endCol < boardSize[boardNum] + 2:
                    endPiece = self.board[boardNum][endRow][endCol]
                    if endPiece == "--":
                        moves_list.append(Move((r, c), (endRow, endCol), self.board[boardNum]))
                    elif endPiece[0] == enemyColor:
                        moves_list.append(Move((r, c), (endRow, endCol), self.board[boardNum]))
                        break
                    else:
                        break
                else:
                    break            

    def KnightMove(self, boardNum, y, x, moves_list):
        # striaght =[(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        # print("Col                 Row")
        # for i in striaght:
        #     print(i)
        #     for j in range(2,5):
        #         RowEnd = y + i[1] + (j*i[1])
        #         ColumnEnd =  x + i[0] + (j*i[0])
        #         if is_valid_square(boardNum, RowEnd, ColumnEnd):
        #             if is_empty(self.board[boardNum],ColumnEnd,RowEnd):
        #                 moves_list.append(Move((y, x), (RowEnd, ColumnEnd), self.board[boardNum]))   
        #                 print(x,"+", i[0],"+", (j*i[0]),"=",x + i[0] + (j*i[0]),"|",y + i[1] + (j*i[1]),"=", y,"+", i[1],"+", (y*i[1]))
        #                 pass
            
        direction = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        boardSize = [8, 10, 12, 14, 16]
        if self.whiteToMove:
            oppositeColour = "b"
        else:
            oppositeColour = "w"

        for i in direction:
            for j in range(2, 5):
                RowEnd = y + i[0] * j
                ColumnEnd = x + i[1] * j
                if 0 <= RowEnd < boardSize[boardNum] and 0 <= ColumnEnd < boardSize[boardNum]:
                    Limit = self.board[boardNum][RowEnd][ColumnEnd]
                    if Limit == "--":
                        moves_list.append(Move((y, x), (RowEnd, ColumnEnd), self.board[boardNum]))
                    elif Limit[0] == oppositeColour:
                        moves_list.append(Move((y, x), (RowEnd, ColumnEnd), self.board[boardNum]))
                        break
                    else:
                        break
                else:
                    break

    # QueenTurns = [0, 0, 0]
    def QueenMove(self, boardNum, y, x, moves_list):
        # global QueenTurns
        # QueenNum = 0
        # if boardNum != 4:
        #     if QueenTurns[QueenNum] > len(moves_list) + 5 or QueenTurns[QueenNum] == 0:
        #         self.RookMove(boardNum, y, x, moves_list)
        #         self.BishopMove(boardNum, y, x, moves_list)
        #         QueenTurns[QueenNum] = len(moves_list)
        # else:
        #     for QueenNum in range(0,3):
        #         if QueenTurns[QueenNum] > len(moves_list) + 5 or QueenTurns[QueenNum] == 0:
        #                 self.RookMove(boardNum, y, x, moves_list)
        #                 self.BishopMove(boardNum, y, x, moves_list)
        #                 QueenTurns[0] = len(moves_list)
        #                 break
        #         else:
        #             break
        #print("Validate Queen")
        self.RookMove(boardNum, y, x, moves_list)
        self.BishopMove(boardNum, y, x, moves_list)

    def KingMove(self, boardNum, y, x, moves_list):
        boardSize = [6, 8, 10, 12, 14]
        kingMoves = ((-1, -1), (-1, 0), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        allyColor = "w" if self.whiteToMove else "b"
        for i in range(8):
            endY = y + kingMoves[i][0]
            endX = x + kingMoves[i][1]
            if 0 <= endY < boardSize[boardNum] and 0 <= endX < boardSize[boardNum]:
                endPiece = self.board[boardNum][endY][endX]
                if endPiece[0] != allyColor:
                    moves_list.append(Move((y,x), (endY, endX), self.board[boardNum]))

    def VanguardMove(self,boardNum, y, x, moves_list):
        boardSize = [6, 8, 10, 12, 14]
        vanguardMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColor = "w" if self.whiteToMove else "b"
        for m in vanguardMoves:
            for j in range(-boardSize[boardNum]+1, boardSize[boardNum]):
                endY = y + m[0] + j
                for i in range(-boardSize[boardNum]+1, boardSize[boardNum]):
                    endX = x + m[1] + i
                    if 0 <= endY < boardSize[boardNum] and 0 <= endX < boardSize[boardNum]:
                        endPiece = self.board[boardNum][endY][endX]
                        if endPiece[0] != allyColor:
                            #print((endY,endX))
                            moves_list.append(Move((y, x), (endY, endX), self.board[boardNum]))
                            break
                    else:
                        break
    def MakeVanguard(self,boardNum, y, x):
        print("MAKING VAN",y,x)
        if self.board[boardNum][y][x][1] == "P":
            if self.board[boardNum][y][x][0] == "w":
                self.board[boardNum][y][x] = "wV"
            else:
                self.board[boardNum][y][x] = "bV"
            self.whiteToMove = not self.whiteToMove

    def VanguardMoveAlternative(self,boardNum, starty, startx, endy, endx):
        if self.whiteToMove:
            if self.board[boardNum][starty][startx][0] == "b":
                return False
        else:
            if self.board[boardNum][starty][startx][0] == "w":
                return False
        #print(self.board[boardNum][starty][startx][0] == "b" , (self.whiteToMove))
        print("Start Row:",starty, "Col:", startx )
        print("End Row:",endy, "Col:", endx )
        if starty == endy or startx == endx:
            return False
        #-1 if starty > endy else 1
        print("Path1")
        path = True
        for i in range(1,abs(starty-endy)+1):
            print("Checking Row:",starty + i*(-1 if starty > endy else 1),"Col",startx )
            if  not is_valid_square(boardNum,self.board[boardNum] ,startx, starty + i*(-1 if starty > endy else 1)):
                path = False
                break
        if path:
            for i in range(1,abs(startx-endx)):
                print("Checking Row:",endy,"Col",startx + i*(-1 if startx > endx else 1) )
                if not is_valid_square(boardNum,self.board[boardNum], startx + i*(-1 if starty > endy else 1), endy ):
                    path = False
                    break
            if path:
                return True
        print("Path2")
        path = True
        for i in range(1,abs(startx-endx)+1):
            print("Checking Row:",starty,"Col",startx + i*(-1 if startx > endx else 1) )
            if not is_valid_square(boardNum,self.board[boardNum], startx + i*(-1 if starty > endy else 1), starty ):
                path = False
                break
        if path:
            for i in range(1,abs(starty-endy)):
                print("Checking Row:",starty + i*(-1 if starty > endy else 1),"Col",endx )
                if not is_valid_square(boardNum,self.board[boardNum], endx, starty + i*(-1 if starty > endy else 1)):
                    return False
            return True
        return False

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
