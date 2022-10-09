import pygame as pyg 
import random
import time 

from os import path 
from pygame import mixer

img_dir = path.join(path.dirname(__file__) , 'icon')
snd_dir = path.join(path.dirname(__file__) , 'sound')

def ballon(x , y):
    ballon_path = pyg.image.load(img_dir+"\Ballon_2.png")
    screen.blit(ballon_path , (x,y))

def cannon(x , y):
    cannon_path = pyg.image.load(img_dir+"\cannon_part_3.png")
    screen.blit(cannon_path , (x-10,y-10))

def bullet(x , y):
    bullet_path = pyg.image.load(img_dir+"\Bullet_2.png")
    global bullet_state
    bullet_state = "Fire"
    screen.blit( bullet_path, (x,y))

def isCollision(x1,x2,y1,y2):

    ''' 
                    2D
    AB = root( (x1-y1)^2 + (x2-y2)^2 ) 
    x1 = ballon_pos_x , x2 = ballon_pos_y 
    y1 = cannon_pos_x , y2 = cannon_pos_y 

    '''
    # print(f"Value of collision : {((x2-x1)**2 + (y2-y1)**2 )**0.5}")
    return True if ( ( (x1-y1)**2 + (x2-y2)**2 )**0.5 ) < 30 else False 

def show_score(x,y , xm , ym):
    global score_show , miss_score_show
    font = pyg.font.Font('freesansbold.ttf' , 16)
    score = font.render("Score : " + str(score_show) , True , (255 , 255 , 255))
    score_miss = font.render("Miss : " + str(miss_score_show) , True , (255 , 255 , 255))
    screen.blit( score, (x,y))
    screen.blit( score_miss, (xm,ym))

def show_time ():
    named_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y , %H:%M:%S" , named_tuple)
    font = pyg.font.Font('freesansbold.ttf' , 16)
    time_sh = font.render(str(time_str),True , (255,255,255))
    screen.blit(time_sh , (235 , 10))

def game_over():
    font = pyg.font.Font('freesansbold.ttf' , 43)
    go = font.render("GAME OVER" , True , (255,255,255))
    screen.blit(go , (70 , 140))

if __name__ == "__main__":
    # Intialize the pygame (pyg)
    pyg.init()

    # Create the screen
    screen = pyg.display.set_mode( (400,300) ) # w*h 

    # Title and Icon 
    pyg.display.set_caption("Balloon shooting challenge")
    icon_path = pyg.image.load(img_dir+'\cannon_icon_start.png')
    pyg.display.set_icon(icon_path)

    # Background 
    background = pyg.image.load(img_dir+'\RB.png')

    # Background Sound 
    mixer.music.load(snd_dir+"\Super Mario Bros.wav")
    mixer.music.play(-1)

    # Position Cannon 
    cannon_pos_x , cannon_pos_y = 315 ,  134

    # Position Ballon 
    ballon_pos_x , ballon_pos_y = random.randint(0,60) ,  random.randint(-16 , 254)
    ballon_pos_change_rd = 0.2

    # Bullet
    bullet_pos_x , bullet_pos_y = 315 , 0 
    bullet_pos_x_change, bullet_pos_y_change = 2  , 0 # Bullet should faster than ballon 10 times.
    bullet_state = "Ready"

    # Position of score and miss score 
    score_show = 0
    textX,texty = 10,10

    miss_score_show = 0 
    miss_x , miss_y = 100 , 10 

    # Game is working in progress 
    progress = True

    # END GAME
    
    while progress:
        screen.fill( (70 , 70 , 70) ) # black 
        # Load BG image
        screen.blit(background , (0,0))

        for w_in_p in pyg.event.get():
            progress = False if w_in_p.type == pyg.QUIT else True
            # The player can move the cannon up and down using arrow keys.
            arrow_in = pyg.key.get_pressed()
            if arrow_in[pyg.K_UP] : 
                # print("U")
                cannon_pos_y-=8 
            if arrow_in[pyg.K_DOWN] : 
                # print("D")
                cannon_pos_y+=8
            if arrow_in[pyg.K_SPACE]:
                # This condition is fix a collab between space bar and arrow.
                if bullet_state == "Ready": 
                    # print("Shooted!")
                    bullet_sound = mixer.Sound(snd_dir+"\Cannon Sound Effect.wav")
                    bullet_sound.play()
                    bullet_pos_y = cannon_pos_y
                    bullet(bullet_pos_x , bullet_pos_y )
            
        ''' Boundaries of cannon and ballon'''
        cannon_pos_y = -16 if cannon_pos_y <= -16 else cannon_pos_y
        cannon_pos_y = 254 if cannon_pos_y >= 254 else cannon_pos_y

        ballon_pos_y += ballon_pos_change_rd
        ballon_pos_change_rd = 0.2 if ballon_pos_y <= -16 else ballon_pos_change_rd
        ballon_pos_change_rd = -0.2 if ballon_pos_y >= 254 else ballon_pos_change_rd
        

        # Bullet Movement
        if bullet_pos_x <= 0 :
            bullet_pos_x = 315
            bullet_state = "Ready"
            miss_score_show+=1 
            miss_sound = mixer.Sound(snd_dir+"\Missed Sound.wav")
            miss_sound.play()

        if bullet_state == "Fire":
            # print("Bullet Move!")
            bullet(bullet_pos_x , bullet_pos_y )
            bullet_pos_x -= bullet_pos_x_change

        # Collision 
        collison = isCollision(ballon_pos_x , ballon_pos_y , bullet_pos_x , bullet_pos_y)
        # print(f"Condition :{collison}")
        
        if collison :
            bullet_pos_x = 315
            bullet_state = "Ready"
            score_show +=1 
            explosion_sound = mixer.Sound(snd_dir+"\Balloon Pop Sound Effect.wav")
            explosion_sound.play()
            # print(f"Score : {score_show}" ) 
            ballon_pos_x , ballon_pos_y = random.randint(0,60) ,  random.randint(-16 , 254)

        cannon(cannon_pos_x , cannon_pos_y)
        ballon(ballon_pos_x , ballon_pos_y)
        show_score(textX , texty , miss_x , miss_y)
        show_time()
        
        pyg.display.update()
