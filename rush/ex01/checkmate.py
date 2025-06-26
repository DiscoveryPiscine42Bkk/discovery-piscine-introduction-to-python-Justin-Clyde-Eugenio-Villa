from visual_chess import *

def checkmate(board_string):
    try:
        # Split string into list of rows
        board = board_string.strip().splitlines() #like split('\n')
        n = len(board)
        
        visual_display(board)

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

        def check_dirs(directions, targets, board, ki, kj, n):
            threats = []
            for dy, dx in directions:
                y, x = ki + dy, kj + dx
                while 0 <= y < n and 0 <= x < n:
                    cell = board[y][x]
                    if cell == '.':
                        y += dy
                        x += dx
                        continue
                    elif cell in targets:
                        threats.append((cell, y + 1, x + 1))  # 1-based coordinates
                        break  # stop after first threat in this direction
                    else:
                        break
            return threats

        threats = []

        threats += check_dirs(rook_dirs, {'R', 'Q'} , board ,ki , kj ,n)
        threats += check_dirs(bishop_dirs, {'B', 'Q'}, board ,ki , kj ,n)

        # Pawn attack (coming from top-left/top-right)
        for dx in [-1, 1]:
            pi, pj = ki - 1, kj + dx
            if 0 <= pi < n and 0 <= pj < n and board[pi][pj] == 'P':
                threats.append(('P', y+1 , x+1))
                return

        if threats:
            for piece , y , x in threats:
                print(f'Success: The {piece} checks the King at ({y} , {x})')
        else :
            print('Fail')
            
    except Exception:
        print(f'Invalid input, Please try again')
        return