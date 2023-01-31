import pgzrun
from math import sin, cos, pi
from random import randint
from curve import Curve

TITLE = 'Lissajous Curve Table'
WIDTH = 1000 + 200
HEIGHT = 600 + 200


ROWS = 5
COLS = 8
SPACING_COLS = WIDTH // (COLS + 1)
SPACING_ROWS = HEIGHT // (ROWS + 1)
RADIUS_COLS = min((.7 * SPACING_COLS) // 2, (.7 * SPACING_ROWS) // 2)
RADIUS_ROWS = RADIUS_COLS

angle = 0
curves = [[Curve((randint(0, 255), randint(0, 255), randint(0, 255))) for _ in range(COLS)] for _ in range(ROWS)]

def update():
    global angle, curves
    angle += 2 * pi / 180
    
    
    if angle > 2 * pi:
        angle = 0
        for row in curves:
            for curve in row:
                curve.clear()
            

def draw():
    screen.clear()
    
    # Guide lines
    for i in range(ROWS):
        for j in range(COLS):
            x = j * SPACING_COLS + SPACING_COLS
            y = i * SPACING_ROWS + SPACING_ROWS
            # screen.draw.line((0, y), (WIDTH, y), color='white')
            # screen.draw.line((x, 0), (x, HEIGHT), color='white')
    
    # Left circles
    for i in range(ROWS):
        centerx = SPACING_COLS // 2
        centery = (i + 1) * SPACING_ROWS + SPACING_ROWS // 2
        
        x = centerx + cos(angle * (i+1)) * RADIUS_ROWS
        y = centery - sin(angle * (i+1)) * RADIUS_ROWS
        
        screen.draw.line((x, y), (WIDTH, y), (40, 40, 40))
        screen.draw.circle((centerx, centery), RADIUS_ROWS, (100, 100, 100))    
        screen.draw.filled_circle((x, y), 5, (250, 250, 250))
        
        for j in range(COLS):
            curves[i][j].set_y(y)
        
        
    
    # Top circles
    for j in range(COLS):
        centerx = (j + 1) * SPACING_COLS + SPACING_COLS // 2
        centery = SPACING_ROWS // 2
        
        x = centerx + cos(angle * (j+1)) * RADIUS_COLS
        y = centery - sin(angle * (j+1)) * RADIUS_COLS
        
        
        screen.draw.line((x, y), (x, HEIGHT), (40, 40, 40))
        screen.draw.circle((centerx, centery), RADIUS_COLS, (100, 100, 100))    
        screen.draw.filled_circle((x, y), 5, (250, 250, 250))
        
        for i in range(ROWS):
            curves[i][j].set_x(x)
            
    for row in curves:
        for curve in row:
            curve.add_current_point()
            curve.draw(
                lambda start, end, color: screen.draw.line(start, end, color), 
                lambda pos, color: screen.draw.filled_circle(pos, 5, color)
            )        

pgzrun.go()