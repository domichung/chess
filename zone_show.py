import str_lang as sl

# color set
BLACK_PIECE = '\033[90m'  # 亮黑色（灰色）
RED_PIECE = '\033[31m'           # 紅色
RESET_COLOR = '\033[0m'          # 重置顏色

# black
black_pieces = {'車', '馬', '象', '士', '將', '砲', '卒'}

# red
red_pieces = {'俥', '傌', '相', '仕', '帥', '炮', '兵'}

# show
def show_zone(array):
    for i, row in enumerate(array):
        if i == 5: 
            print('--------------------------')
            sl.label_print("river  river  river ")
            print('--------------------------')
        colored_row = []
        for piece in row:
            if piece in black_pieces:
                colored_row.append(BLACK_PIECE + piece + RESET_COLOR)
                #sl.c_label_print(piece,"B")
            elif piece in red_pieces:
                colored_row.append(RED_PIECE + piece + RESET_COLOR)
                #sl.c_label_print(piece,"R")
            else:
                colored_row.append(piece) 
                #sl.label_print(piece)
        print(' '.join(colored_row))

def show_nowteam(team):
    #top = []
    if team == 0:
        #top.append(RED_PIECE + "目前為紅子的回合" + RESET_COLOR)
        sl.c_label_print("r_move ","R")
    else:
        #top.append(BLACK_PIECE + "目前為黑子的回合" + RESET_COLOR)
        sl.c_label_print("b_move ","B")

    #sl.label_print(top)