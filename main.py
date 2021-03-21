class Board:
    BN = "BN"
    BR = "BR"
    BB = "BB"
    BQ = "BQ"
    BK = "BK"
    BP = "BP"
    WN = "WN"
    WR = "WR"
    WB = "WB"
    WQ = "WQ"
    WK = "WK"
    WP = "WP"
    EM = "  "

    fileMap = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }

    board = [
        [BR, BN, BB, BQ, BK, BB, BN, BR],
        [BP, BP, BP, BP, BP, BP, BP, BP],
        [EM, EM, EM, EM, EM, EM, EM, EM],
        [EM, EM, EM, EM, EM, EM, EM, EM],
        [EM, EM, EM, EM, EM, EM, EM, EM],
        [EM, EM, EM, EM, EM, EM, EM, EM],
        [WP, WP, WP, WP, WP, WP, WP, WP],
        [WR, WN, WB, WQ, WK, WB, WN, WR]
    ]
    curMove = "W"


def makeMove(move, board):
    file = int(move[1])
    rank = move[0]

    print(rank, file)

    # Change Turn
    board.curMove = "B" if board.curMove == "W" else "W"


def printBoard(b):
    print("------------------------------------------------")
    for i in range(len(b.board)):
        print("", end="|")
        for j in range(len(b.board[0])):
            print(" " + b.board[i][j], end=" | ")
        print()
        print("------------------------------------------------")


def main():
    b = Board()
    makeMove("e4", b)
    printBoard(b)


main()
