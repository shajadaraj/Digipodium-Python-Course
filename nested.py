from turtle import *

pencolor('black')
fillcolor('yellow')
pensize(3)
side = 6
for i in range(side):
    fd(75)
    begin_fill()
    for i in range(side):
        fd(75) 
        for i in range(side):
            fd(75/2)
            lt(360/side)
            dot(15)
        rt(360/side)    
    end_fill() 
    lt(360/side)   
hideturtle()
mainloop()