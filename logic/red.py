red_pieces = {'俥', '傌', '相', '仕', '帥', '炮', '兵'}
black_pieces = {'車', '馬', '象', '士', '將', '砲', '卒'}

def r_soldier(x,y,zone):
    if (int(y)>=5):
        boundary = []
        boundary += str(x)+str(int(y)-1)
        return boundary
    else:
        boundary = []
        if (int(y)-1>=0):
            boundary+=str(x)+str(int(y)-1)
        if (int(x)-1>=0):
            boundary+=str(int(x)-1)+str(y)
        if (int(x)+1<=8):
            boundary+=str(int(x)+1)+str(y)
        
        return boundary

def r_car(x,y,zone):
    
    x = int(x)
    y = int(y)

    boundary = []

    t_y = y
    
    while (t_y-1>=0):
        t_y-=1
        if (zone[t_y][x] in red_pieces):
            break
        boundary += str(int(x))+str(int(t_y))
        if (zone[t_y][x] in black_pieces):
            break
        #print(boundary)

    t_y = y

    while (t_y+1<=9):
        t_y+=1
        if (zone[t_y][x] in red_pieces):
            break
        boundary += str(int(x))+str(int(t_y))
        if (zone[t_y][x] in black_pieces):
            break

    t_x = x

    while (t_x-1>=0):
        t_x-=1
        if (zone[y][t_x] in red_pieces):
            break
        boundary += str(int(t_x))+str(int(y))
        if (zone[y][t_x] in black_pieces):
            break
    
    t_x = x

    while (t_x+1<=8):
        t_x+=1
        if (zone[y][t_x] in red_pieces):
            break
        boundary += str(int(t_x))+str(int(y))
        if (zone[y][t_x] in black_pieces):
            break
    
    #print(boundary)
    return boundary

def r_artillery (x,y,zone):

    x = int(x)
    y = int(y)

    boundary = []

    t_y = y
    eat_flag = 0

    while (t_y-1>=0):
        t_y-=1
        if (eat_flag==0):
            if ((zone[t_y][x] in red_pieces) or (zone[t_y][x] in black_pieces)):
                eat_flag = 1
                continue
            else:
                boundary += str(int(x))+str(int(t_y))
                continue
        if (zone[t_y][x] in red_pieces):
            break
        if (zone[t_y][x] in black_pieces):
            boundary += str(int(x))+str(int(t_y))

    t_y = y      
    eat_flag = 0

    while (t_y+1<=9):
        t_y+=1
        if (eat_flag==0):
            if ((zone[t_y][x] in red_pieces) or (zone[t_y][x] in black_pieces)):
                eat_flag = 1
                continue
            else:
                boundary += str(int(x))+str(int(t_y))
                continue
        if (zone[t_y][x] in red_pieces):
            break
        if (zone[t_y][x] in black_pieces):
            boundary += str(int(x))+str(int(t_y))
    
    t_x = x
    eat_flag = 0

    while (t_x-1>=0):
        t_x-=1
        if (eat_flag==0):
            if ((zone[y][t_x] in red_pieces) or (zone[y][t_x] in black_pieces)):
                eat_flag = 1
                continue
            else:
                boundary += str(int(t_x))+str(int(y))
                continue
        if (zone[y][t_x] in red_pieces):
            break
        if (zone[y][t_x] in black_pieces):
            boundary += str(int(t_x))+str(int(y))
    
    t_x = x
    eat_flag = 0

    while (t_x+1<=8):
        t_x+=1
        if (eat_flag==0):
            if ((zone[y][t_x] in red_pieces) or (zone[y][t_x] in black_pieces)):
                eat_flag = 1
                continue
            else:
                boundary += str(int(t_x))+str(int(y))
                continue
        if (zone[y][t_x] in red_pieces):
            break
        if (zone[y][t_x] in black_pieces):
            boundary += str(int(t_x))+str(int(y))

    #print(boundary)
    return boundary