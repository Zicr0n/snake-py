import pygame
import time
import random
import math

pygame.init()

clock = pygame.time.Clock()

pixel_Size = 24
gridSize = 32
screen_x = pixel_Size * gridSize    
screen_y = pixel_Size * gridSize

maximumSnakeSize = (screen_x / pixel_Size)**2
game_over = False
hasQuit = False

## Display
display = pygame.display.set_mode([screen_x, screen_y])
pygame.display.set_caption("Snake Game by the one and only Samir")

inputDir = "right"
movementDir = inputDir

snake = [(pixel_Size * 2, pixel_Size * 2), (pixel_Size, pixel_Size * 2)]
snakeSize = 3
applePosition = [pixel_Size, pixel_Size]

## Snake game settings
snakeSpeed : int = 10
snakeColor = pygame.Color(125,5,20)
appleColor = pygame.Color(255,0,0)

## Score header
color_header = (255,255,255)

## Regnbåge
colorvalue = 0

def rainbow_color(value):
    step = (value // 256) % 6
    pos = value % 256

    if step == 0:
        return (255, pos, 0)
    if step == 1:
        return (255-pos, 255, 0)
    if step == 2:
        return (0, 255, pos)
    if step == 3:
        return (0, 255-pos, 255)
    if step == 4:
        return (pos, 0, 255)
    if step == 5:
        return (255, 0, 255-pos)

def spawnAppleAtRandomPosition():
    isOverlapping = True
    isSnakeOverlapping = False

    if len(snake) == maximumSnakeSize:
        print("win")
        return

    print(pixel_Size**2)

    while isOverlapping == True:
        randX = random.randrange(0, screen_x, pixel_Size)
        randY = random.randrange(0, screen_y, pixel_Size)

        randPosition = [randX, randY]

        for snakePiece in range(0,len(snake) - 1):
            if snake[snakePiece][0] == randPosition[0] and snake[snakePiece][1] == randPosition[1]:
                isSnakeOverlapping = True
                print("Apple wants to spawn in snake, not okay")
                break
            else:
                isSnakeOverlapping = False
        
        if isSnakeOverlapping == False:
            isOverlapping = False

    return [randPosition[0], randPosition[1]]

def show_score(choice, color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(len(snake) - 2), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    display.blit(score_surface, score_rect)


while game_over == False:
    # Event management
    events = pygame.event.get()

    ## REGNBÅGSORMEN
    snakeColor = rainbow_color(colorvalue)

    ## EVENTS ##
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                inputDir = "up"
            if event.key == pygame.K_DOWN:
                inputDir = "down"
            if event.key == pygame.K_LEFT:
                inputDir = "left"
            if event.key == pygame.K_RIGHT:
                inputDir = "right"

        if event.type == pygame.QUIT:
            game_over = True
            next
    
    ## SPELARENS INPUT ##
    if inputDir == "right" and movementDir != "left":
        movementDir = "right"

    if inputDir == "left" and movementDir != "right":
        movementDir = "left"

    if inputDir == "down" and movementDir != "up":
        movementDir = "down"

    if inputDir == "up" and movementDir != "down":
        movementDir = "up"
    
    ## RÖRELSE TILL ORMEN ##
    newHead = ()
    if movementDir == "right":
        newHead = (snake[0][0] + pixel_Size, snake[0][1])
    elif movementDir == "left":
        newHead = (snake[0][0] - pixel_Size, snake[0][1])
    elif movementDir == "down":
        newHead = (snake[0][0], snake[0][1]  + pixel_Size)
    elif movementDir == "up":
        newHead = (snake[0][0], snake[0][1]  - pixel_Size)
    
    snake.insert(0, newHead)

    ## Äppelfunktionen
    ## if touch apple then dont remove last else remove
    if snake[0][0] == applePosition[0] and snake[0][1] == applePosition[1]:
        applePosition = spawnAppleAtRandomPosition()
    else:
        snake.pop()
    
    ## Win state om man tar på sin svans
    if snake[0][0] == snake[len(snake) - 1][0] and snake[0][1] == snake[len(snake) - 1][1]:
        print("Win")
    
    ## game over status
    if (snake[0] in snake[1:]) or (snake[0][0] > screen_x or snake[0][0] < 0) or (snake[0][1] > screen_y or snake[0][1] < 0):
        game_over = True

    display.fill("black")

    ## RENDERING ##
    for snakePiece in snake:
        if snake.index(snakePiece) == 0:
            pygame.draw.rect(display, (255,255,255), pygame.Rect(snakePiece[0], snakePiece[1], pixel_Size, pixel_Size))
        else:
            pygame.draw.rect(display, snakeColor, pygame.Rect(snakePiece[0], snakePiece[1], pixel_Size, pixel_Size))
        
    
    pygame.draw.rect(display, appleColor, pygame.Rect(applePosition[0], applePosition[1] , pixel_Size, pixel_Size))
    show_score(1, color_header, 'impact', 20)

    pygame.display.update()

    colorvalue = (colorvalue + 20) % (256 * 6)
    ################
    
    ## FPS ##
    clock.tick(snakeSpeed)
        
pygame.quit()