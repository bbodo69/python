theBoard = [' '] * 10
print(theBoard)

board = [' '] * 10

def drawBoard(board):

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("-----------")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

drawBoard(board)

print(board[7], " = board[7]")

board[7] = 'O'

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)

    return dupeBoard

print(getBoardCopy(board), '= getBoardCopy')
print(drawBoard(board), '=drawBoard')
