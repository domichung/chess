import zone_reset as rz
def create_chess_board():
    chess_board = [['空' for _ in range(9)] for _ in range(10)]
    rz.initialize_chess_board(chess_board)
    return chess_board