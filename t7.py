from turtle import *
side = 12
bgcolor('black')
for i in range (side):
    pencolor('black')
    fd(50)
    lt(360/side)
    pencolor('green')
    dot(30)
    for i in range(side):
        fd(25)
        lt(360/side)
               
mainloop()    
