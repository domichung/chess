import logic.red
import movelogic as ml
def r_move_main(chess,x,y,zone):
    if (chess == "兵"):
        accept_move = logic.red.r_soldier(x,y,zone)      
    elif (chess == "俥"):
        accept_move = logic.red.r_car(x,y,zone)
    elif (chess == "傌"):
        accept_move = logic.red.r_horse(x,y,zone)
    elif (chess == "炮"):
        accept_move = logic.red.r_artillery(x,y,zone)
    elif (chess == "仕"):
         accept_move = logic.red.r_sergeant(x,y,zone)
    elif (chess == "相"):
         accept_move = logic.red.r_elephant(x,y,zone)
    elif (chess == "帥"):
         accept_move = logic.red.r_king(x,y,zone)
    else:
         return -2
    
    for i in range(0, len(accept_move), 2):
            print(f"{i//2} : ({accept_move[i]}, {accept_move[i+1]})")
    
    print(f"{len(accept_move)//2} : 取消選棋")

    move_choose = input()
    move_choose = int(move_choose)

    if (move_choose == (len(accept_move)//2)):
         return -1
    else:     
        ml.move_real(x,y,accept_move[move_choose*2],accept_move[move_choose*2+1],zone)
        return 1