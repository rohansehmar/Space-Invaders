import pygame
import random
import math
import time
from pygame import mixer

#intialise pygame
pygame.init()

choose_ship= False

#prints high score
f1 = open("score.txt", "r")
last_line = int(f1.readlines()[-1])
f1.close()
highscore=last_line

gameover = "no"

#choose ship screen text
select_num_font=pygame.font.Font("KuchenHollow.ttf", 40)
select_num=select_num_font.render("SELECT THE SHIP YOU WANT TO USE :", True, (255, 255, 255))


#creates screen
screen=pygame.display.set_mode((800, 600))

#background
background=pygame.image.load("spacen.jpg")

#title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


#player
playerX=370
playerY=480
playerX_change=0

#player choice of ships
playerImg1 = pygame.image.load("spaceship1.png")
playerImg2 = pygame.image.load("spaceship2.png")
playerImg3 = pygame.image.load("spaceship3.png")
playerImg4 = pygame.image.load("spaceship4.png")
playerImg5 = pygame.image.load("spaceship5.png")


#load explosion sound
explosion=mixer.Sound("explosion.wav")
hit=mixer.Sound("hit.wav")

#start font
startfont = pygame.font.Font("04B_30__.TTF",  47)


#new highscore font
newscore_font= pygame.font.Font("04B_30__.TTF", 30)

#high score font
hiscorefont = pygame.font.Font("04B_30__.TTF",  25)

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("purple alien.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(100, 200))
    enemyX_change.append(2)
    enemyY_change.append(30)

#ready - bullet not vissible
#fire - bullet is moving
#bullet
bulletImg = pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=8
bullet_state="ready"

#square cusror coordinates
sqr_change=0
sqrX=195
sqrY=245

#title
title_font = pygame.font.Font("8-Bit Madness.ttf", 45)

#difficulty
diffont = pygame.font.Font("8-Bit Madness.ttf", 25)
difficulty_level= ("normal")


#score
score_value=0
font = pygame.font.Font("8-Bit Madness.ttf", 35)
textX = 10
textY=10

#gameover screen
game_over_font = pygame.font.Font("8-Bit Madness.ttf", 64)


def hiscoren():
    newscore=newscore_font.render("NEW HIGH SCORE!", True, (255, 0, 0))
    screen.blit(newscore, (223, 450))

def hiscore():
    if highscore < score_value:
        file = open("score.txt", "a+")
        file.write("\n" + str(score_value))
        file.close()


def show_hi_score(x, y,):
    hi_score= hiscorefont.render("The current high score is: " + (str(highscore)), True, (255, 255, 255))
    screen.blit(hi_score, (x, y))

def show_start_screen(x, y):
    start= startfont.render(("PRESS"), True, (50, 135, 255))
    screen.blit(start, (x, y))

def show_difficulty(x, y):
    difficulty= diffont.render("difficulty: " + (difficulty_level), True, (255, 255, 255))
    screen.blit(difficulty, (x, y))

def show_game_over():
    game_over= game_over_font.render("GAME OVER", True, (255,255,0))
    screen.blit(game_over, (275, 250))

def show_title(x, y):
    title= title_font.render("space invaders", True, (0, 255, 255))
    screen.blit(title, (x, y))


def show_score(x, y):
    score= font.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance <27:
        return True
    else:
        return False


running = False

#starting screen loop
start= True
while start:
    screen.fill((15, 55, 115))
    show_start_screen(295, 220)
    show_hi_score(108, 15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            start = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                start= False
                choose_ship= True
        
    psbtn=pygame.image.load("psx.png")
    screen.blit(psbtn, (315, 300))
    pygame.display.update()





#CHOOSE SHIP SCREEN  ==========
while choose_ship:
    screen.fill((0, 0, 0))

    square=pygame.image.load("sqr.png")
    screen.blit(square, (sqrX, sqrY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            choose_ship = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sqr_change=+100
                sqrX+=sqr_change

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sqr_change=-100
                sqrX+=sqr_change

        if sqrX==195:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playership = pygame.image.load("spaceship1.png")
                    choose_ship= False
                    running= True

        if sqrX==295:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playership = pygame.image.load("spaceship2.png")
                    choose_ship= False
                    running= True

        if sqrX==395:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playership = pygame.image.load("spaceship3.png")
                    choose_ship= False
                    running= True
                    
        if sqrX==495:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playership = pygame.image.load("spaceship4.png")
                    choose_ship= False
                    running= True

        if sqrX==595:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playership = pygame.image.load("spaceship5.png")
                    choose_ship= False
                    running= True

    if sqrX<195:
        sqrX=195
    if sqrX>595:
        sqrX=595
        
    screen.blit(playerImg1, (200, 250))

    screen.blit(playerImg2, (300, 250))

    screen.blit(playerImg3, (400, 250))

    screen.blit(playerImg4, (500, 250))

    screen.blit(playerImg5, (600, 250))

    screen.blit(select_num, (205,10))


    



    pygame.display.update()





#game loop
running = True

while running:
    #RGB value
    screen.fill((0, 0, 0))

    #background
    screen.blit(background, (0, 0))

    #writes difficulty on screen
    show_difficulty(315, 5)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            running = False

        #if key is pressed check wether is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change=-2
            if event.key == pygame.K_RIGHT:
                playerX_change=+2

            if event.key == pygame.K_SPACE:
                if bullet_state=="ready":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)   
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0

    playerX +=playerX_change

    #player boundraies
    if playerX <=0:
        playerX=0
    elif playerX >736:
        playerX=736

    #enemy movement
    for i in range(num_of_enemies):

        #game over
        if enemyY[i] >440 and enemyY[i] <2000:
            for j in range(num_of_enemies):
                enemyY[j] = 2500
            bullet_state="ready"
            explosion.play()
            playerX=20000
            playerY=20000
            hiscore()
            show_game_over()
            gameover = "yes"
                
            
            break
        
        if enemyY[i] >=2000 and enemyY[i] <=3000:
            show_game_over()
            enemyY[i] = 3500
            bullet_state="ready"
           

        if enemyY[i] >= 3500 and enemyY[i]<4000:
            show_game_over()
            bullet_state="ready"
            enemyY[i] = 4500

        if enemyY[i]>4000:
            show_game_over()
            bullet_state="ready"
        

        enemyX[i] += enemyX_change[i]
        #enemy boundraies

        #enemy speed
        if enemyX[i] <= 0 and score_value <= 10:
            enemyX_change[i] = 0.7#Enemy speed 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736 and score_value <= 10:
            enemyX_change[i] = -0.7
            enemyY[i] += enemyY_change[i]

        #becomes faster
        elif enemyX[i] <= 0 and score_value > 10 and score_value <=20:
            enemyX_change[i] = 0.8#Enemy speed 2
            enemyY[i] += enemyY_change[i]
            difficulty_level= ("hard")
            
        elif enemyX[i] >= 736 and score_value > 10 and score_value <= 20:
            enemyX_change[i] = -0.8
            enemyY[i] += enemyY_change[i]
            difficulty_level= ("hard")

        #becomes even faster
        elif enemyX[i] <= 0 and score_value > 20:
            enemyX_change[i] = 1.0#Enemy speed 3
            enemyY[i] += enemyY_change[i]
            difficulty_level= ("expert")
            
        elif enemyX[i] >= 736 and score_value > 20:
            enemyX_change[i] = -1.0
            enemyY[i] += enemyY_change[i]
            difficulty_level= ("expert")



            

        #collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if  collision:
            hit.play()
            bulletY = 480
            bullet_state="ready"
            score_value+=1
            

            #normal difficulty
            if score_value <=20:
                enemyX[i]=random.randint(0, 735)
                enemyY[i]=random.randint(100, 200)
            #enemies spawn lower
            elif score_value >20:
                enemyX[i]=random.randint(0, 735)
                enemyY[i]=random.randint(150, 270)


        enemy(enemyX[i], enemyY[i], i)



    #bullet movement
    if bulletY <=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state=="fire":
        fire_bullet(bulletX, bulletY)
        bulletY -=bulletY_change

    if gameover == "yes":
        if score_value>highscore:
            hiscoren()



    show_title(270, 30)
    screen.blit(playership, (playerX, playerY))
    show_score(textX, textY)
    pygame.display.update()




