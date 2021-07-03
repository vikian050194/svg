from ..common import *


def serp():
    iterIndx = 8
    palette = Palette(Gravit)
    color = palette.get_color()
    elements = []

    def recF (e, xa, ya, xb, yb, xc, yc, i):
        if i == 0:
            l = Line(xa, ya, xc, yc)
            l.stroke = color
            e.append(l)
            l = Line(xa, ya, xb, yb)
            l.stroke = color
            e.append(l)
            l = Line(xb, yb, xc, yc)
            l.stroke = color
            e.append(l)
        else:
            prevXA = xa
            prevYA = ya 
            prevXB = xb
            prevYB = yb 
            prevXC = xc
            prevYC = yc 
            nextxa = (prevXA + prevXC)/2
            nextya = (prevYA + prevYC)/2    
            nextxb = (prevXB + prevXA)/2
            nextyb = (prevYB + prevYA)/2    
            nextxc = (prevXC + prevXB)/2
            nextyc = (prevYC + prevYB)/2    
            
            recF(e, prevXA, prevYA, nextxa, nextya, nextxb, nextyb, i - 1);
            recF(e, nextxa, nextya, nextxc, nextyc, prevXC, prevYC, i - 1);
            recF(e, nextxb, nextyb, prevXB, prevYB, nextxc, nextyc, i - 1);

    recF(elements, dx, 1, width - 1, height - 1, 1, height - 1, iterIndx)
    return elements


__all__ = ["serp"]
