import str_lang as sl
import os
import logic.red
import move_serch_r as msr
# red 0
red_pieces = {'俥', '傌', '相', '仕', '帥', '炮', '兵'}
# black 1
black_pieces = {'車', '馬', '象', '士', '將', '砲', '卒'}

def is_valid_input(x, y):
    try:
        x = int(x)
        y = int(y)
        
        if 0 <= x <= 8 and 0 <= y <= 9:
            return True  
        else:
            return False  
    except ValueError:
        return False

def check_chess(team,zone,x,y):
    if not (is_valid_input(x,y)):
        os.system("cls")
        sl.label_print("e_msg_3 ")
        print('--------------------------')
        return -1
    now = zone[int(y)][int(x)]
    if (now == "空"):
        os.system("cls")
        sl.label_print("e_msg_0 ")
        print('--------------------------')
        return -1

    if now in red_pieces and team == 1:
        os.system("cls")
        sl.label_print("e_msg_1 ")
        print('--------------------------')
        return -1
    if now in black_pieces  and team == 0:
        os.system("cls")
        sl.label_print("e_msg_1 ")
        print('--------------------------')
        return -1
    
    move_status = move_temp(zone,x,y)
    
    if (move_status == -1):
        os.system("cls")
        sl.label_print("e_msg_2 ")
        print('--------------------------')
        return -1

    return 1

def move_temp(zone,x,y):
    chess = zone[int(y)][int(x)]
    print("你選擇了"+chess)
    if (chess in red_pieces):
       check_choose = msr.r_move_main(chess,x,y,zone)
       if (check_choose == -1):
           return -1
       else:
           return 1
    #elif (chess in black_pieces):
    else:
        print("fuck up")

    #a = input()

def move_real(x,y,cx,cy,zone):
    x = int(x)
    y = int(y)
    cx= int(cx)
    cy= int(cy)
    chess = zone[y][x]
    zone[y][x] = '空'
    temp = zone[cy][cx]
    zone[cy][cx] = chess
    return temp