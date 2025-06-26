def visual_display(board):
    print("\nVisual Chessboard:\n")
    for row in board:
        print('+' + '---+' * len(row))
        print('| ' + ' | '.join(row) + ' |') # use the patten for every cell
    print('+' + '---+' * len(board[0]))  # Bottom line