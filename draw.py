from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #switch coordinates if x0>x1
    
    if (x0>x1):
        z = x0
        x0 = x1
        x1 = z
        z = y0
        y0= y1
        y1 = z
    
    
    x  = x0
    y = y0
    
    A = y1-y0  #change in y
    B = -1.* (x1-x0)   # - change in x
    if(B == 0):
        while (y<=y1):
            plot(screen, color,x,y)
            y+=1
        return
            
    m = -1. * (A/B)

  
            
    #octants 1, 5
    if (m >= 0 and m <= 1):
        d = 2*A+ B
        while (x<= x1):
            plot(screen, color, x, y)
            if (d>0):
                y+=1
                d += 2*B
            x+=1
            d += 2*A
        

    #octants 2, 6
    elif (m > 1):
        d = A + 2*B
        while (y<= y1):
            plot(screen, color, x,y)
            if (d<0):
                x+=1
                d += 2*A
            y+=1
            d+=2*B

    #quadrants 3, 7
    elif (m <= -1):
        d = A + 2*B
        while (y>=y1):
            plot(screen,color, x,y)
            if (d>0):
                x+=1
                d += 2*A
            y-=1
            d-= 2*B
            
    #quadrants 4, 8
    elif (m<0 and m>-1):
        d = 2*A + B
        while (x<=x1):
            plot(screen,color, x,y)
            if (d<0):
                y -=1
                d -= 2*B
            x+=1
            d+=2*A

    else:
        print "what the"
        print m
