import zone_show as zs
import zone_reset as zr
import zone_new as zn
import sys_checkwin as wcheck
import sys_checkwhowin as wcheckw
import os

chess_zone = zn.create_chess_board()
zs.show_zone(chess_zone)

while (1):
    os.system("cls")
    while (wcheck.check_winner(chess_zone)):
        a = input()
        b = input()
        chess_zone[int(a)][int(b)] = '空'
        os.system("cls")
        zs.show_zone(chess_zone)
    
    os.system("cls")
    wcheckw.check_whowin(chess_zone)
    print("\n\n\n遊戲結束是否要再開一局 y/n")
    c = input()
    if (c == 'y'):
        chess_zone = zn.create_chess_board()
        zs.show_zone(chess_zone)
        continue
    else:
        break