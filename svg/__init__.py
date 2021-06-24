# pl = Polyline()
# pl.stroke = palette.get_color()
# pl.stroke_width = 5
# pl.append(50, 50)
# pl.append(100, 50)
# pl.append(100, 100)
# svg.append(pl)

# pg = Polygon()
# pg.stroke = palette.get_color()
# pg.stroke_width = 5
# pg.fill = palette.get_color()
# pg.append(150, 150)
# pg.append(150, 200)
# pg.append(200, 200)
# svg.append(pg)

# n = 3
# sc = palette.get_color()
# fc = palette.get_color()

# for i in range(0, n):   
#     rg = Rectangle(r_x(), 0, 100, height)
#     rg.stroke = sc
#     rg.stroke_width = 5
#     rg.fill = fc
#     svg.append(rg)

# color = palette.get_color()
# f = lambda x: 0.02*(x**3)
# for x in range(-dx, dx, 1):
#     y = round(dy-round(f(x),2),2)
#     if 0<=y<=height:
#         c = Circle(x+dx, y, 5)
#         c.fill = color
#         c.stroke_width = 0
#         svg.append(c)

# p = Path()
# p.stroke = palette.get_color()
# p.fill = palette.get_color()
# p.stroke_width = 5

# move = MoveTo(dx, dy)
# move.name = "M"
# p.append(move)

# p.append(HorizontalLine(100))
# p.append(VerticalLine(100))
# p.append(HorizontalLine(-100))
# p.append(VerticalLine(-100))

# p.append(MoveTo(100, 100))
# p.append(LineTo(300, 0))
# p.append(LineTo(0, 100))
# p.append(ClosePath())

# svg.append(p)

# print(svg)
# save(svg)
