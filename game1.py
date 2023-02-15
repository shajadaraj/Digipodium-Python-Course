import pgzrun

box = Rect((50,50), (150,100))
box2= Rect((600,50), (100,100))
box3 = Rect((300,50), (100,100))

def draw():
    screen.fill('red')
    screen.draw.filled_rect(box, 'yellow')
    screen.draw.filled_rect(box2, 'green')
    screen.draw.filled_rect(box3, 'blue')

def update():
    box.x +=2    # move box to the right every frame
    box2.x -=2   # move box to the left every frame
    box3.y +=2   # move box to the down every frame

pgzrun.go()        