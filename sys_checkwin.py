def check_winner(board):
    has_king = False  
    has_general = False  
    
    for row in board:
        if '將' in row:
            has_king = True
        if '帥' in row:
            has_general = True

        if has_king and has_general:
            return 1