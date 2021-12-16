# SCREEN CONSTANTS
WIDTH = 600
HEIGHT = 500
TITLE = 'Space Fighter'

# COLORS
BLACK = (0, 0, 0)

# ACTORS
ship = Actor('ship')
ship.centerx = WIDTH / 2
ship.bottom = HEIGHT
meteor = Actor('meteor1')
meteor.centerx = WIDTH / 2
meteor.top = 0
laser = Actor('laser')
laser.x = -100


# Keys Dictionary
keymap = {'up' : False, 'down' : False, 'left' : False, 'right' : False}


def draw():
    screen.fill(BLACK)
    meteor.draw()
    ship.draw()
    laser.draw()

def update():
    update_ship()
    update_meteor()
    update_laser()

def update_laser():
    if laser.x >= 0:
        laser.y -= 6
    if laser.y < 0:
        laser.x = -100

def update_meteor():
    meteor.y += 1
    if meteor.colliderect(laser):
        meteor.x = -200
    
def update_ship():
    if keymap['up']:
        ship.y -= 4
        if ship.top < 0:
            ship.top = 0
    if keymap['down']:
        ship.y += 4
        if ship.bottom > HEIGHT:
            ship.bottom = HEIGHT
    if keymap['left']:
        ship.x -= 4
        if ship.left < 0:
            ship.left = 0
    if keymap['right']:
        ship.x += 4
        if ship.right > WIDTH:
            ship.right = WIDTH
    
def fire():
    laser.bottom = ship.top
    laser.centerx = ship.centerx

def on_key_down(key):
    if key == keys.UP or key == keys.W:
        keymap['up'] = True
    if key == keys.DOWN or key == keys.S:
        keymap['down'] = True
    if key == keys.LEFT or key == keys.A:
        keymap['left'] = True
    if key == keys.RIGHT or key == keys.D:
        keymap['right'] = True
    if key == keys.SPACE:
        fire()

def on_key_up(key):
    if key == keys.UP or key == keys.W:
        keymap['up'] = False
    if key == keys.DOWN or key == keys.S:
        keymap['down'] = False
    if key == keys.LEFT or key == keys.A:
        keymap['left'] = False
    if key == keys.RIGHT or key == keys.D:
        keymap['right'] = False
