import turtle
colors = ['red','green','yellow','orange','blue','pink']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
mainloop()    

