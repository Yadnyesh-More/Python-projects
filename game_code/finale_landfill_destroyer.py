import pygame
import random
import math

pygame.init()
width=650
height=700
invader_x=340 
invader_y=615
move_x=0
score=0



screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("space invader")
background=pygame.image.load("new_bg2.png")
machine=pygame.image.load("fighter.png")
bullet=pygame.image.load("bullet.png")
landfill=pygame.image.load("enemy.png")
landfill_x=random.randint(0,620)
landfill_y=random.randint(10,600)

def welcome():
    running=True
    while running:
        screen.fill((133,229,144)) 
        wel=font_gameover.render("WELCOME TO GAME",True,'black')    
        screen.blit(wel,(90,270))
        prs=font.render("press space bar to play ",True,'black')    
        screen.blit(prs,(190,340))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()

def gameover():
    if score>=5:
        no_of_landfill=0 
        check_bullet=False
        #screen.fill((133,229,144))
        gameover_txt=font_gameover.render(f'GAME OVER ',True,'black')
        screen.blit(gameover_txt,(180,300))
    #screen.fill((133,229,144))
    gameover_txt=font_gameover.render(f'GAME OVER ',True,'white','black')
    replay=font_replay.render("press ' r' for reply ",True,'white','black')
    screen.blit(gameover_txt,(160,270))
    screen.blit(replay,(220,380))
    


 


font=pygame.font.SysFont('Arial',32,'bold')

font_gameover=pygame.font.SysFont('Arial',64,'bold')

font_win=pygame.font.SysFont("Arial",90,'bold')

font_replay=pygame.font.SysFont("Market",32,'italic')


def gameloop():
    invader_x=340 
    invader_y=615
    move_x=0
    landfill_speed_x=5
    landfill_speed_y=20 
    bullet_x=355
    bullet_y=585
    score=0

    landfill=[]
    landfill_x=[]
    landfill_y=[]
    landfill_speed_x=[]
    landfill_speed_y=[]
    game_over=False
    you_won=False
    #with open("highscore.txt","r") as f:
    #    highscore = f.read() 

    no_of_landfill=5
    for i in range(no_of_landfill):
        landfill.append(pygame.image.load("enemy.png"))
        landfill_x.append(random.randint(0,620))
        landfill_y.append(random.randint(-10,120))
        landfill_speed_x.append(3.5)
        landfill_speed_y.append(20)
    check_bullet=False
    running=True

    start_ticks = pygame.time.get_ticks()  # Get the current time in milliseconds
    countdown_seconds = 120  # Set the countdown time in seconds

    
    while running:
        screen.blit(background,(0,0))
        if game_over is True:
            #with open('highscore.txt','w') as f:
            #    f.write(str(highscore))
            gameover()
            #screen.fill((133,229,144))
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    running=False    
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        welcome()
        
        elif you_won is True:
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    running=False    
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        gameloop()

                      


        else:

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    running=False    
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        move_x=10
                        
                    if event.key==pygame.K_a:
                        move_x=-10
                    
                    if event.key==pygame.K_SPACE:
                        if check_bullet is False:
                            check_bullet=True
                            bullet_x=invader_x+15
                        

                            
                if event.type==pygame.KEYUP:
                    move_x=0 
            
            invader_x+=move_x            
            if invader_x<=0:
                invader_x=0
            elif invader_x>=586:
                invader_x=586               
            
            for i in range(no_of_landfill):
            
                if landfill_y[i]>551:
                    for j in range(no_of_landfill):

                        landfill_y[j]=2000
                        break
                    #gameover()
                    game_over=True
                    check_bullet=False
                    landfill_speed_x[i]=0
                    landfill_speed_y[i]=0
                    
                    
                landfill_x[i]+=landfill_speed_x[i]
                if landfill_x[i]<=0:
                    landfill_speed_x[i]=6
                    landfill_y[i]+=landfill_speed_y[i]
                if landfill_x[i]>=626:
                    landfill_speed_x[i]=-6
                    landfill_y[i]+=landfill_speed_y[i]
                distance=math.sqrt(math.pow(bullet_x-landfill_x[i],2)+math.pow(bullet_y-landfill_y[i],2))
                if distance<30:
                    bullet_y=585
                    check_bullet=False
                    landfill_x[i]=random.randint(0,620)
                    landfill_y[i]=random.randint(10,120)
                    score+=1
                    #highscore+=1
                    #high=int(highscore)
                
                screen.blit(landfill[i],(landfill_x[i],landfill_y[i]))
                
            if bullet_y<=0:
                bullet_y=585
                check_bullet=False

            if check_bullet is True:
                screen.blit(bullet,(bullet_x,bullet_y))
                bullet_y-=11
            screen.blit(machine,(invader_x,invader_y))
            #score_txt()
            txt=font.render(f"Score :{score}",True,'white','black')
            screen.blit(txt,(10,10))
            #enemy_over()
            
             # Countdown timer
            elapsed_ticks = pygame.time.get_ticks() - start_ticks
            remaining_seconds = max(0, countdown_seconds - elapsed_ticks // 1000)  
            #timer_txt = font.render(f"Time: {remaining_seconds}", True, 'white', 'black')
            min=(remaining_seconds // 60)
            sec=(remaining_seconds % 60)
            timer_txt = font.render(f"Time: {remaining_seconds // 60:02}:{remaining_seconds % 60:02}", True, 'white', 'black')
            screen.blit(timer_txt, (260, 7))

        if remaining_seconds == 0:
            game_over = True    
            timer_txt = font.render(f"Time: {min}:{sec}", True, 'white', 'black')
            screen.blit(timer_txt, (260, 7))

             
        if score == 50 :
            screen.fill((133,229,144))
            won=font_win.render(" Y O U  W I N ",True,'white','black')
            screen.blit(won,(100,270))
            replay=font_replay.render("press ' r' for reply ",True,'white','black')
            screen.blit(replay,(220,380))
    
            no_of_landfill=0
            check_bullet=False
            you_won=True
            
                

                

        if score>=51:
            game_over=True
            no_of_landfill=0 
            check_bullet=False

        pygame.display.update()

welcome()       

