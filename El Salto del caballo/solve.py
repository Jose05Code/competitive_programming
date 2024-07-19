def main():
    start_x, start_y, end_x, end_y = map(int, input().split())
    result = can_knight_reach(start_x, start_y, end_x, end_y)
    print("yes" if result else "no")

def can_knight_reach(start_x, start_y, end_x, end_y):
    chessboard = initialize_chessboard(start_x - 1, start_y - 1)
    return chessboard[end_x - 1][end_y - 1]

def initialize_chessboard(start_x, start_y):
    board = [[False for _ in range(8)] for _ in range(8)]
    mark_reachable_squares(board, start_x, start_y)
    return board

def mark_reachable_squares(board, x, y):
    knight_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1)]
    queue = [(x, y)]
    while queue:
        current_x, current_y = queue.pop(0)
        for move in knight_moves:
            next_x, next_y = current_x + move[0], current_y + move[1]
            if 0 <= next_x < 8 and 0 <= next_y < 8 and not board[next_x][next_y]:
                board[next_x][next_y] = True
                queue.append((next_x, next_y))

if __name__ == "__main__":
    main()
