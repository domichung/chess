# color set
BRIGHT_BLACK_PIECE = '\033[90m'  # 亮黑色（灰色）
RED_PIECE = '\033[31m'           # 紅色
RESET_COLOR = '\033[0m'          # 重置顏色

# black
bright_black_pieces = {'車', '馬', '象', '士', '將', '砲', '卒'}

# red
red_pieces = {'俥', '傌', '相', '仕', '帥', '炮', '兵'}

# show
def show_zone(array):
    for i, row in enumerate(array):
        if i == 5: 
            print('----------------------------')
            print('楚河漢界')
            print('----------------------------')
        colored_row = []
        for piece in row:
            if piece in bright_black_pieces:
                colored_row.append(BRIGHT_BLACK_PIECE + piece + RESET_COLOR)
            elif piece in red_pieces:
                colored_row.append(RED_PIECE + piece + RESET_COLOR)
            else:
                colored_row.append(piece) 
        print(' '.join(colored_row))

