class Pawn:
    def __init__(color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.is_starting_position = True
    
    # checks if the position is valid
    def is_valid_square(row, col):
        return 0 <= row < 8 and 0 <= col < 8

    # gets all the legal moves
    def get_legal_pawn_moves(chessboard, row, col, color):
        legal_moves = []
        if color == "white":
            direction = -1  # white piece move from bottom to top
        else:
            direction = 1   # black piece move from top to bottom

        # move one step forward
        new_row = row + direction
        new_col = col
        if is_valid_square(new_row, new_col) and chessboard[new_row][new_col] == "--":
            legal_moves.append((new_row, new_col))

        # move two steps forward if at the starting position
        if is_valid_square(new_row, new_col) and self.is_starting_position and chessboard[new_row][new_col] == "--":
            legal_moves.append((new_row, new_col))
            self.is_starting_position = False

        # capture
        attack_moves = [(row + direction, col - 1), (row + direction, col + 1)]
        for move in attack_moves:
            new_row, new_col = move
            if is_valid_square(new_row, new_col) and chessboard[new_row][new_col] != "--" and chessboard[new_row][new_col][0] != color:
                legal_moves.append((new_row, new_col))

        return legal_moves
