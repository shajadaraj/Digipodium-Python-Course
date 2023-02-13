from turtle import *


def polygon(side, dis):
    for i in range(side):
        fd(dis)
        lt(360/side)
polygon(3, 100)
polygon(4, 100)
polygon(5, 100)
polygon(6, 100)
polygon(7, 100)
polygon(8, 100)
polygon(9, 100)

hideturtle()
mainloop()