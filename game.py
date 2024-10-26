import pygame
import random

pygame.init()
pygame.display.set_caption("Jump Game")
screen = pygame.display.set_mode((800, 600))     
background = pygame.image.load('bg.png')
bg =pygame.transform.scale(background,(800,600))

FPS = 60
clock=pygame.time.Clock()

playerImg = pygame.image.load('char.png')
player=pygame.transform.scale(playerImg,(150,130))
player_rect = player.get_rect()
player_rect.topleft = (50,300)

blockimg1 = pygame.image.load('block/tile_0068.png')
block1=pygame.transform.scale(blockimg1,(150,75))
block1_rect = block1.get_rect()
block1_rect.bottomleft = (800,430)

blockimg2 = pygame.image.load('block/tile_0126.png')
block2=pygame.transform.scale(blockimg2,(100,150))
block2_rect = block2.get_rect()
block2_rect.bottomleft = (800,430)


blockimg3 = pygame.image.load('block/tile_0127.png')
block3=pygame.transform.scale(blockimg3,(105,135))
block3_rect = block3.get_rect()
block3_rect.bottomleft = (800,430)


blockimg4 = pygame.image.load('block/tile_0128.png')
block4=pygame.transform.scale(blockimg4,(100,100))
block4_rect = block4.get_rect()
block4_rect.bottomleft = (800,430)

blockrect = [block1_rect,block2_rect,block3_rect,block4_rect]
blockimg =[block1,block2,block3,block4]

jump = "ready"
score_value = 0
speed_block = 8

font = pygame.font.Font("Font/Coiny.ttf",30)

score_txt = font.render("Score : "+str(score_value),True,000)
score_rect = score_txt.get_rect()
score_rect.topleft=(10,10)

over_txt = font.render("Game Over",True,000)
over_rect = over_txt.get_rect()
over_rect.center=(800/2,600/2)

Restart_txt = font.render("Press R to restart",True,000)
Restart_rect = over_txt.get_rect()
Restart_rect.centerx=(800/2-50)
Restart_rect.bottom=(590)

obstacleimg = 0
obstaclerect = 0

running=True

def jumping():
    global jump
    if jump == "up1" and player_rect.top >= 100:
        player_rect.y -= 7
    elif jump == "up1" and player_rect.top <= 100 :
        jump = "down"
    elif jump == "down":
        if player_rect.top < 300:
            player_rect.y += 10
        if player_rect.top >= 300:
            jump = "ready"
            player_rect.topleft = (50,300)
    elif jump == "up2" :
        for i in range(30):
            player_rect.y -= 7
            blockmove()
            screen.blit(bg, (0, 0))
            screen.blit(score_txt,score_rect) 
            screen.blit(obstacleimg,obstaclerect)
            screen.blit(player,player_rect)
            pygame.display.update()
            clock.tick(FPS)
        jump ="down"

def random_block():
    global obstacleimg,obstaclerect
    num_block = random.randint(0,3)
    obstacleimg = blockimg[num_block]
    obstaclerect = blockrect[num_block]
            
def blockmove():
    global score_value,speed_block,score_txt
    if obstaclerect.left <= 800:
        obstaclerect.left -= speed_block
    if obstaclerect.right <= 0:
        random_block()
        score_value += 1
        score_txt= font.render("Score : "+str(score_value),True,000)
        obstaclerect.bottomleft = (800,430)
        if score_value%10 == 0 :
            speed_block +=1
        
def run():
    global running,jump,score_value,speed_block,score_txt,Restart_txt
    while running:
        screen.blit(bg, (0, 0))
        screen.blit(score_txt,score_rect)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump == "ready":
                    jump = "up1"
                elif event.key == pygame.K_SPACE and jump == "up1":
                    jump = "up2"

        jumping()
        blockmove()
        if player_rect.colliderect(obstaclerect):
            score_value = 0
            while running:
                screen.blit(score_txt,score_rect)
                screen.blit(over_txt,over_rect)
                screen.blit(Restart_txt,Restart_rect)
                pygame.display.update()
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running=False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r :
                            player_rect.topleft = (50,300)
                            obstaclerect.bottomleft = (800,430)
                            score_value = 0
                            speed_block = 8
                            score_txt = font.render("Score : "+str(score_value),True,000)
                            screen.blit(score_txt,score_rect)  
                            run()
                            
        screen.blit(score_txt,score_rect)            
        screen.blit(obstacleimg,obstaclerect)
        screen.blit(player,player_rect)
        pygame.display.update()
        clock.tick(FPS)
        
random_block()        
run()
pygame.quit()