import sys
from checkmate import checkmate

def read_board_from_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            return content
    except Exception:
        print(f'Error, Can not read {filename} please try again with new file')
        return None

def main():
    if len(sys.argv) < 2:
        print("Error: No input files")
        return

    for file in sys.argv[1:]:
        board = read_board_from_file(file)
        result = checkmate(board)

if __name__ == "__main__":
    main()
