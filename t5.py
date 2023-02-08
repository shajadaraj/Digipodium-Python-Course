from turtle import *

side = 6
for i in range(side):
    pencolor('black')
    fd(100)
    lt(360/side)
    pencolor('green')
    dot(30)
    for i in range(side):
        fd(50)
        lt(1440/side)

mainloop()