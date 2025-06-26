def checkmate(board_string):
    try:
        # Split string into list of rows
        board = board_string.strip().splitlines() #like split('\n')
        n = len(board)

        if not all(len(row) == n for row in board):
            print("Error: Board is not square")
            return

        # Find King
        king_position = None
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'K':
                    if king_position:
                        print("Error: More than one King found")
                        return
                    king_position = (i, j)

        if not king_position:
            print("Error: No King found")
            return

        ki, kj = king_position

        # Directions
        rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        def check_dirs(directions, targets):
            for dy, dx in directions:
                y, x = ki + dy, kj + dx
                while 0 <= y < n and 0 <= x < n:
                    cell = board[y][x]
                    if cell == '.':
                        y += dy
                        x += dx
                        continue
                    elif cell in targets:
                        return True
                    else:
                        break
            return False

        if check_dirs(rook_dirs, {'R', 'Q'}):
            print("Success")
            return
        if check_dirs(bishop_dirs, {'B', 'Q'}):
            print("Success")
            return

        # Pawn attack (coming from top-left/top-right)
        for dx in [-1, 1]:
            pi, pj = ki - 1, kj + dx
            if 0 <= pi < n and 0 <= pj < n and board[pi][pj] == 'P':
                print("Success")
                return

        print("Fail")
        
    except Exception:
        print(f'Invalid input, Please try again')
        return