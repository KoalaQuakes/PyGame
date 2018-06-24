#First go at making a game

import pygame as py, sys, random, time

check_errors = py.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, "
          + "exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame Successfully Initalised!")

#play surface
playSurface = py.display.set_mode((720, 460))
py.display.set_caption("Sname Game!")

#Colours
red = py.Color(255,0,0)  # gameover
green = py.Color(0, 255, 0)  # snake
black = py.Color(0,0,0)  # score
white = py.Color(255,255,255) # background
brown = py.Color(165,42,42)  # food

#FPScontroller
fpsController = py.time.Clock()

#ImportantVariables
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0

#gameOver function
def gameOver():
    myFont = py.font.SysFont('monaco',72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    py.display.flip()
    showScore(0)
    time.sleep(4)
    py.quit()
    sys.exit()

def showScore(choice = 1):
    sFont = py.font.SysFont('monaco', 24)
    sSurf = sFont.render('Score: {0}'.format(score), True, black)
    sRect = sSurf.get_rect()
    if choice == 1:
        sRect.midtop = (80, 10)
    else:
        sRect.midtop = (360, 125)
    playSurface.blit(sSurf, sRect)
    py.display.flip()
#Main game logic
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == py.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == py.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == py.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == py.K_ESCAPE:
                py.event.post(py.event.Event(QUIT))

    #  validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'


    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    #  snale body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    foodSpawn = True

    playSurface.fill(white)

    for pos in snakeBody:
        py.draw.rect(playSurface, green, py.Rect(pos[0], pos[1], 10, 10))

    py.draw.rect(playSurface, brown,
    py.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] >= 720 or snakePos[0] <= 0:
        gameOver()
    if snakePos[1] >= 460 or snakePos[1] <= 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block [0] and snakePos[1] == block[1]:
            gameOver()

    py.display.flip()
    showScore()
    fpsController.tick(23)
