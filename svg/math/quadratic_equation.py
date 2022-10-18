from typing import List

import math

def solve(a: int, b: int, c: int) -> List[int]:
    d2 = b**2-4*a*c

    if d2 < 0:
        return []

    d = math.sqrt(d2) 

    xc_1 = ((-1)*b+d)/(2*a)
    xc_2 = ((-1)*b-d)/(2*a)

    if d2 == 0:
        return [xc_1]
    else:
        return [xc_1, xc_2]
