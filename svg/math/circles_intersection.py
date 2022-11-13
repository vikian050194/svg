from . import quadratic_equation

def solve(a, b):
    (xa, ya, ra2) = a
    (xb, yb, rb2) = b

    if ya==yb:
        x = (ra2-rb2+xb**2-xa**2)/(2*(xb-xa))
        a = 1
        b = (-2)*ya
        c = ya**2+(x-xa)**2-ra2
        y = quadratic_equation.solve(a, b, c)

        if len(y)==0:
            return []

        if len(y)==1:
            return [(x,y[0])]

        y1, y2 = y
        return [(x, y1), (x, y2)]

    la = (xb-xa)/(ya-yb)
    lb1 = (xa**2+ya**2-xb**2-yb**2)/(2*(ya-yb))
    lb2 = (rb2-ra2)/(2*(ya-yb))
    lb = lb1+lb2
    a = 1 + la**2
    b = 2*la*(lb-ya)-2*xa
    c = xa**2+(lb-ya)**2-ra2
    
    x = quadratic_equation.solve(a, b, c)

    if len(x)==0:
        return []

    if len(x)==1:
        y = la*x[0]+lb
        return [(x,y)]

    [x1, x2] = x

    y1 = la*x1+lb
    y2 = la*x2+lb

    return [(x1, y1), (x2, y2)]
