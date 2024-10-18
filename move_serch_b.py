import logic.black
import movelogic as ml

def b_move_main(chess,x,y,zone):
    if (chess == "卒"):
        accept_move = logic.black.b_soldier(x,y,zone)      
    elif (chess == "車"):
        accept_move = logic.black.b_car(x,y,zone)
    elif (chess == "馬"):
        accept_move = logic.black.b_horse(x,y,zone)
    elif (chess == "砲"):
        accept_move = logic.black.b_artillery(x,y,zone)
    elif (chess == "士"):
         accept_move = logic.black.b_sergeant(x,y,zone)
    elif (chess == "象"):
         accept_move = logic.black.b_elephant(x,y,zone)
    elif (chess == "將"):
         accept_move = logic.black.b_king(x,y,zone)
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