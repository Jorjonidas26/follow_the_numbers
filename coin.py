import pgzrun
from random import randint
from pygame import K_RETURN, K_KP_ENTER, time
from pgzero import actor

WIDTH = 800
HEIGHT = 600
INITIAL_TIME = 7.0

score = 0
game_over = False

time_left = 0
fox = actor.Actor("fox")
fox.pos = 100, 100
coin = actor.Actor("coin")
coin.pos = 200, 200

gameClock = time.Clock()

def draw() :
    global score, game_over
    screen.fill((0,200,10))
    fox.draw()
    coin.draw()
    screen.draw.text("Score: {score}".format(score=score), color="black", topleft=(10, 10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final score: {score}\nPress enter to play again".format(score = score), topleft=(10, 10), fontsize=60)

def placecoin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
    
def time_up() :
    global game_over, gameClock
    delay = gameClock.tick(60)
    game_over = True
    
def update():
    global score, game_over, time_left, gameClock
    if game_over:
        return
    if keyboard.left:
        fox.x = max(fox.x - 2, 15)
    elif keyboard.right:
        fox.x = min(fox.x + 2, WIDTH-15)
    if keyboard.up:
        fox.y = max(fox.y - 2, 15)
    elif keyboard.down:
        fox.y = min(fox.y + 2, HEIGHT-15)
    if fox.colliderect(coin):
        score = score + 10
        placecoin()
        delay = gameClock.tick(60)/1000
        print("delay is {delay}".format(delay=delay))
        if time_left == 0.0:
            time_left = INITIAL_TIME
        else:
            time_left = time_left - delay + INITIAL_TIME/2
        print("time_left is {time}".format(time=time_left))   
        clock.schedule_unique(time_up, time_left)
        
        
        
def on_key_up(key):
    global game_over, score, fox, time_left
    if not game_over:
        return
    if key == K_RETURN or key == K_KP_ENTER:
        score = 0
        game_over = False
        fox.pos = 100, 100
        coin.pos = 200, 200
        time_left = 0
    
pgzrun.go()