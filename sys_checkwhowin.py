# color set
BRIGHT_BLACK_PIECE = '\033[90m'  # 亮黑色（灰色）
RED_PIECE = '\033[31m'           # 紅色
RESET_COLOR = '\033[0m'          # 重置顏色

def check_whowin(board):

    colored_row = []

    for row in board:
        if '將' in row:
            colored_row.append(BRIGHT_BLACK_PIECE + "黑方獲勝" + RESET_COLOR)
        if '帥' in row:
            colored_row.append(RED_PIECE  + "紅方獲勝" + RESET_COLOR)

    print(''.join(colored_row))