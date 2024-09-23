import zone_show as zs
import zone_reset as zr
import zone_new as zn
import sys_checkwin as wcheck
import sys_checkwhowin as wcheckw
import os
import movelogic as ml
import str_lang as sl

chess_zone = zn.create_chess_board()
zs.show_zone(chess_zone)

while (1):
    #============初始化============
    nowteam = 0
    # 0 紅 1 黑
    #=============================
    os.system("cls")
    while (wcheck.check_winner(chess_zone)):
        zs.show_nowteam(nowteam)
        zs.show_zone(chess_zone)
        a = input()
        b = input()
        #print(a+" "+b)
        try:
            status = ml.check_chess(nowteam,chess_zone,a[0],b[0])
        except:
            os.system("cls")
            sl.label_print("e_msg_3 ")
            print('----------------------------')
            continue
        #chess_zone[int(a)][int(b)] = '空'
        #os.system("cls")
        #zs.show_nowteam(nowteam)
        #zs.show_zone(chess_zone)
        #os.system("cls")
        if (status == 1):
            nowteam = (int(nowteam)+1)%2
#======================測試完要加回去=============================
            #os.system("cls")
#================================================================    
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
