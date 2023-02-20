import pgzrun

box = Rect((50,50), (150,100))
box2= Rect((600,50), (100,100))
bvx = 2
b2vx = -2

def draw():
    screen.fill('red')
    screen.draw.filled_rect(box, 'yellow')
    screen.draw.filled_rect(box2, 'green')
    

def update():
    global bvx, b2vx
    box.x += bvx
    box2.x += b2vx
    if box.colliderect(box2):
        bvx = -bvx
        b2vx = -b2vx
        sounds.kgf.play()
    if box.left < 0:
        bvx = -bvx
        sounds.kgf.play()
    if box2.right > 800:
        b2vx = -b2vx    
        sounds.kgf.play()
    
    

pgzrun.go()        