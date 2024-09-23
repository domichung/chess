import logic.red
import movelogic as ml
def r_move_main(chess,x,y,zone):
    if (chess == "兵"):
        accept_move = logic.red.r_soldier(x,y,zone)      
    elif (chess == "俥"):
        accept_move = logic.red.r_car(x,y,zone)
    elif (chess == "炮"):
        accept_move = logic.red.r_artillery(x,y,zone)
    
    for i in range(0, len(accept_move), 2):
            print(f"{i//2} : ({accept_move[i]}, {accept_move[i+1]})")

    move_choose = input()
    move_choose = int(move_choose)
    ml.move_real(x,y,accept_move[move_choose*2],accept_move[move_choose*2+1],zone)
