import pygame

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
pos_perso = (100,700)
lvl = 0
drop = (500,-100)
star = pygame.image.load("star.png")
star = pygame.transform.scale(star,(100,100))


vel = 10
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


def dessiner_map():
    global background,x
    fenetre.fill((0,0,0))
    for i in range(10):
        fenetre.blit(sol,(i*150,750))
    fenetre.blit(background,(0,0))
    fenetre.blit(perso,(pos_perso))
    #pygame.draw.rect(fenetre,(244,233,59),hitbox_perso,5)

def dessiner_niv1():
    dessiner_map()
    fenetre.blit(anvil,(drop))
    fenetre.blit(star,(1300,500))
    pygame.display.flip()

clock = pygame.time.Clock()

while lvl == 0:
    clock.tick(100)
    if pos_perso[0] > 350:
        if drop[1]<900:
            drop = (drop[0],drop[1]+20)
    drop_rect = (drop[0],drop[1],90,90)
    hitbox_perso = (pos_perso[0]+7,pos_perso[1],33,50)
    if perso == perso_crouch:
        hitbox_perso = (pos_perso[0]+7,pos_perso[1]+25,33,25)
    if drop[0]+20 < hitbox_perso[0]+33 < drop[0] + 100 and drop[1] < hitbox_perso[1] < drop[1] + 90:
        lvl = 1
    if 1320 < hitbox_perso[0]+33 < 1400 and 500 < hitbox_perso[1] < 580:
        lvl = 1
    dessiner_niv1()
    Clavier()