import pygame
pygame.init()
screen=pygame.display.set_mode((600,800))
bg=pygame.image.load("C:\Aahana\Game Dev 2\lesson 5\sky.png")
rocket=pygame.image.load("C:\Aahana\Game Dev 2\lesson 5\Rocket.png")
bg=pygame.transform.scale(bg,(600,800))
rocketx=300
rockety=0
font=pygame.font.SysFont("brannboll script",70)
while True:
     
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                rockety=rockety-30
                
            if event.key==pygame.K_DOWN:
                rockety=rockety+30
            if event.key==pygame.K_LEFT:
                rocketx=rocketx-30
            if event.key==pygame.K_RIGHT:
                rocketx=rocketx+30  
    screen.blit(bg,(0,0))
    screen.blit(rocket,(rocketx,rockety))
    rockety=rockety+0.1
    pygame.display.update()
    if rockety>=800:
        text1=font.render("GAME OVER",True,"lime green")
        screen.blit(text1,(270,200))
        pygame.display.update()
    
