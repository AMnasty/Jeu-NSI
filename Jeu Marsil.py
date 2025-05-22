import pygame
import time

pygame.init()

fenetre = pygame.display.set_mode((1500,900))
pygame.display.set_caption("2nd World's Hardest Game")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (1500,750))
sol = pygame.image.load("sol.jpg")
sol = pygame.transform.scale(sol, (150,150))
perso_crouch = pygame.image.load("perso_crouch.png")
perso_crouch = pygame.transform.scale(perso_crouch, (50,25))
perso_droit = pygame.image.load("perso_droit.png")
perso_droit = pygame.transform.scale(perso_droit, (50,50))
perso_gauche = pygame.image.load("perso_gauche.png")
perso_gauche = pygame.transform.scale(perso_gauche, (50,50))
perso = perso_droit
anvil = pygame.image.load("anvil (1).png")
anvil = pygame.transform.scale(anvil,(100,100))
bullet = pygame.image.load("bullet.png")
bullet = pygame.transform.scale(bullet,(100,46))
surf = pygame.Surface((100,23), pygame.SRCALPHA)

bullet_xy = (1500,700)
pos_perso = (100,700)
lvl = 1
drop = (500,-100)
drops = []
for i in range(7):
    drops.append((drop[0]-50*i,drop[1]-100*i))
star = pygame.image.load("star.png")
star = pygame.transform.scale(star,(100,100))
arial100 = pygame.font.SysFont("arial",100)
win_txt = arial100.render("Level Complete",True,pygame.Color(255,255,100))
lose_txt = arial100.render("Level Lost",True,pygame.Color(255,0,100))
a = 0
b = 0
vel = 10
limite = 0
jump = False


def Clavier():
    global pos_perso, perso, jump, vel
    touches = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            pygame.quit()
    if pos_perso[0] < 1460 and touches[pygame.K_RIGHT] == True or touches[pygame.K_d] == True:
        pos_perso = (pos_perso[0] + 5, pos_perso[1])
        perso = perso_droit
    if pos_perso[0] > -10 and touches[pygame.K_LEFT] == True or touches[pygame.K_q] == True:
        pos_perso = (pos_perso[0] - 5, pos_perso[1])
        perso = perso_gauche
    if jump == False and touches[pygame.K_UP] == True or touches[pygame.K_z] == True:
        jump = True
    if pos_perso[1] < 720 and touches[pygame.K_DOWN] == True or touches[pygame.K_s] == True: #and a == False:
        perso = perso_crouch
        #a = True
    if jump == True:
        pos_perso = (pos_perso[0], pos_perso[1] - vel)
        vel -= 0.2
        if vel < -10:
            jump = False
            vel = 10


def val_0():
    global pos_perso, lvl, drop, bullet_xy, a, b, vel
    pos_perso = (100,700)
    lvl = 0
    drop = (500,-100)
    bullet_xy = (1500,700)
    a = 0
    b = 0
    vel = 10
    jump = False
    
def val_1():
    global pos_perso, lvl, drop, bullet_xy, a, b, vel, limite
    pos_perso = (100,700)
    drops = []
    lvl = 1
    limite = 0
    drop = (500,-100)
    vel = 10
    for i in range(7):
        drops.append((drop[0]-50*i,drop[1]-100*i))
    jump = False
    
def dessiner_map():
    global background,x,bullet_rect
    bullet_rect = pygame.Rect(bullet_xy[0],bullet_xy[1]-207,100,230)
    fenetre.fill((0,0,0))
    for i in range(10):
        fenetre.blit(sol,(i*150,750))
    fenetre.blit(background,(0,0))
    fenetre.blit(perso,(pos_perso))

def position(num,max):
    global pos_perso,pos,limite
    pos = pos_perso[num]
    while limite != 1:
        if pos > max:
            limite = 1
            return True
        else:
            return False
    if limite == 1:
        return True

def dessiner_niv0():
    dessiner_map()
    fenetre.blit(anvil,(drop))
    fenetre.blit(star,(1300,500))
    surf.blit(bullet,(0, 0),(0, bullet_sprite, 100, 23))
    for i in range(10):
        fenetre.blit(surf,(bullet_xy[0],bullet_xy[1]-23*i))
    pygame.display.flip()

def dessiner_niv1():
    dessiner_map()
    for drop in drops:
        fenetre.blit(anvil,drop)
    pygame.display.flip()

def dessiner_niv_win():
    dessiner_map()
    fenetre.blit(win_txt,(400,350))
    pygame.display.flip()
    
def dessiner_niv_perdu():
    dessiner_map()
    fenetre.blit(lose_txt,(500,350))
    

clock = pygame.time.Clock()
while True:
    bullet_sprite = 0
    temps1 = time.time()
    print(drops)
    while lvl == 0:
        clock.tick(100)
        dessiner_niv0()
        Clavier()
        if pos_perso[0] > 350:
            a = 1
        if a == 1:
            if drop[1]<900:
                drop = (drop[0],drop[1]+20)
        if pos_perso[0] > 700:
            b = 1
        if b == 1:
            bullet_xy = (bullet_xy[0]-7,700)
        if int((temps1 - time.time())%2) == 1:
            bullet_sprite = 23
        if int((temps1 - time.time())%2) == 0:
            bullet_sprite = 0
        drop_rect = (drop[0],drop[1],90,90)
        hitbox_perso = pygame.Rect(pos_perso[0]+7,pos_perso[1],33,50)
        if perso == perso_crouch:
            hitbox_perso = pygame.Rect(pos_perso[0]+7,pos_perso[1]+25,33,25)
        if hitbox_perso.colliderect(bullet_rect) == True:
            niv = lvl
            lvl = -2
            temps = time.time()
        if drop[0]+20 < hitbox_perso[0]+33 < drop[0] + 100 and drop[1] < hitbox_perso[1] < drop[1] + 90:
            niv = lvl
            lvl = -2
            temps = time.time()
        if 1320 < hitbox_perso[0]+33 < 1400 and 500 < hitbox_perso[1] < 580:
            niv = lvl + 1
            lvl = -1
            temps = time.time()

    while lvl == -2:
        dessiner_niv_perdu()
        if niv == 0:
            fenetre.blit(anvil,(drop))
            fenetre.blit(star,(1300,500))
        if niv == 1:
            for drop in drops:
                fenetre.blit(anvil,drop)
        pygame.display.flip()
        if time.time() - temps > 5:
            lvl = niv
            if lvl == 0:
                val_0()
            if lvl == 1:
                val_1()
        
    while lvl == -1:
        dessiner_niv_win()
        if time.time() - temps > 5:
            lvl = niv
            val_1()

    while lvl == 1:
        clock.tick(100)
        Clavier()
        if position(0,350) == True:
            for i in range(len(drops)):
                drops[i] = (drops[i][0],drops[i][1]+20)
        pygame.Rect(pos_perso[0]+7,pos_perso[1],33,50)
        hitbox_perso = pygame.Rect(pos_perso[0]+7,pos_perso[1],33,50)
        for i,pos in enumerate(drops):
            drop_rect = pygame.Rect(pos[0],pos[1],70,70)
            if hitbox_perso.colliderect(drop_rect) == True :
                niv = lvl
                lvl = -2
                temps = time.time()
            
        dessiner_niv1()
        