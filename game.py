import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 240, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycle")

FPS = 480
FPSgedaan = 0
timernieuwemove = 0

font = pygame.font.SysFont('comicsans', 40)

waarvoorwerp = 1
level = 2
with open(os.path.join("level.txt")) as level:
    level = int(str(level.read()))

appel = pygame.image.load(os.path.join("Assets", "Appel.png"))
flesje = pygame.image.load(os.path.join("Assets", "Flesje.png"))
krant = pygame.image.load(os.path.join("Assets", "Krant.png"))
appel = pygame.transform.scale(appel, (80, 80))
flesje = pygame.transform.scale(flesje, (80, 80))
krant = pygame.transform.scale(krant, (80, 80))
eend = pygame.image.load(os.path.join("Assets", "Eend.png"))
eend = pygame.transform.scale(eend, (80, 80))
plastic_container = pygame.image.load(os.path.join("Assets", "Plastic.png"))
plastic_container = pygame.transform.scale(plastic_container, (80, 160))
papier_container = pygame.image.load(os.path.join("Assets", "Papier.png"))
papier_container = pygame.transform.scale(papier_container, (80, 160))
overig_container = pygame.image.load(os.path.join("Assets", "Overig.png"))
overig_container = pygame.transform.scale(overig_container, (80, 160))
luchtframe1 = pygame.image.load(os.path.join("Assets", "Lucht1.png"))
luchtframe1 = pygame.transform.scale(luchtframe1, (240, 480))
luchtframe2 = pygame.image.load(os.path.join("Assets", "Lucht2.png"))
luchtframe2 = pygame.transform.scale(luchtframe2, (240, 480))
luchtframe3 = pygame.image.load(os.path.join("Assets", "Lucht3.png"))
luchtframe3 = pygame.transform.scale(luchtframe3, (240, 480))
luchtframe4 = pygame.image.load(os.path.join("Assets", "Lucht4.png"))
luchtframe4 = pygame.transform.scale(luchtframe4, (240, 480))
luchtframe5 = pygame.image.load(os.path.join("Assets", "Lucht5.png"))
luchtframe5 = pygame.transform.scale(luchtframe5, (240, 480))
luchtframe6 = pygame.image.load(os.path.join("Assets", "Lucht6.png"))
luchtframe6 = pygame.transform.scale(luchtframe6, (240, 480))
luchtframe7 = pygame.image.load(os.path.join("Assets", "Lucht7.png"))
luchtframe7 = pygame.transform.scale(luchtframe7, (240, 480))
luchtframe8 = pygame.image.load(os.path.join("Assets", "Lucht8.png"))
luchtframe8 = pygame.transform.scale(luchtframe8, (240, 480))
luchtframe9 = pygame.image.load(os.path.join("Assets", "Lucht9.png"))
luchtframe9 = pygame.transform.scale(luchtframe9, (240, 480))
luchtframe10 = pygame.image.load(os.path.join("Assets", "Lucht10.png"))
luchtframe10 = pygame.transform.scale(luchtframe10, (240, 480))
luchtframe11 = pygame.image.load(os.path.join("Assets", "Lucht11.png"))
luchtframe11 = pygame.transform.scale(luchtframe11, (240, 480))
luchtframe12 = pygame.image.load(os.path.join("Assets", "Lucht12.png"))
luchtframe12 = pygame.transform.scale(luchtframe12, (240, 480))
luchtframe13 = pygame.image.load(os.path.join("Assets", "Lucht13.png"))
luchtframe13 = pygame.transform.scale(luchtframe13, (240, 480))
luchtframe14 = pygame.image.load(os.path.join("Assets", "Lucht14.png"))
luchtframe14 = pygame.transform.scale(luchtframe14, (240, 480))
luchtframe15 = pygame.image.load(os.path.join("Assets", "Lucht15.png"))
luchtframe15 = pygame.transform.scale(luchtframe15, (240, 480))
luchtframe16 = pygame.image.load(os.path.join("Assets", "Lucht16.png"))
luchtframe16 = pygame.transform.scale(luchtframe16, (240, 480))


def draw_ding(fpsding, voorwerp, waar, aan, leveltje):
    # geanimeerde achtergrond
    if fpsding == 30 or fpsding < 30:
        WIN.blit(luchtframe1, (0, 0))
    elif fpsding > 30 and fpsding < 60:
        WIN.blit(luchtframe2, (0, 0))
    elif fpsding > 60 and fpsding < 90:
        WIN.blit(luchtframe3, (0, 0))
    elif fpsding > 90 and fpsding < 120:
        WIN.blit(luchtframe4, (0, 0))
    elif fpsding > 120 and fpsding < 150:
        WIN.blit(luchtframe5, (0, 0))
    elif fpsding > 150 and fpsding < 180:
        WIN.blit(luchtframe6, (0, 0))
    elif fpsding > 180 and fpsding < 210:
        WIN.blit(luchtframe7, (0, 0))
    elif fpsding > 210 and fpsding < 240:
        WIN.blit(luchtframe8, (0, 0))
    elif fpsding > 240 and fpsding < 270:
        WIN.blit(luchtframe9, (0, 0))
    elif fpsding > 270 and fpsding < 300:
        WIN.blit(luchtframe10, (0, 0))
    elif fpsding > 300 and fpsding < 330:
        WIN.blit(luchtframe11, (0, 0))
    elif fpsding > 330 and fpsding < 360:
        WIN.blit(luchtframe12, (0, 0))
    elif fpsding > 360 and fpsding < 390:
        WIN.blit(luchtframe13, (0, 0))
    elif fpsding > 390 and fpsding < 420:
        WIN.blit(luchtframe14, (0, 0))
    elif fpsding > 420 and fpsding < 450:
        WIN.blit(luchtframe15, (0, 0))
    elif fpsding > 450 and fpsding < 480:
        WIN.blit(luchtframe16, (0, 0))
    WIN.blit(plastic_container, (0, 320))
    WIN.blit(overig_container, (80, 320))
    WIN.blit(papier_container, (160, 320))
    check_prullenbak(waar, voorwerp)
    with open(os.path.join("level.txt")) as level:
        level = int(str(level.read()))
        if waar == 0:
            voorwerp.x = 0
        elif waar == 1:
            voorwerp.x = 80
        elif waar == 2:
            voorwerp.x = 160
        if level % 2 == 0:
            WIN.blit(appel, (voorwerp.x, voorwerp.y))
        elif level % 3 == 0:
            WIN.blit(krant, (voorwerp.x, voorwerp.y))
        elif not level % 2 == 0:
            if not level % 3 == 0:
                WIN.blit(flesje, (voorwerp.x, voorwerp.y))
        WIN.blit(eend, (80, 80))
        leveltekst = font.render("Level: " + str(level), 1, (0, 0, 0,))
        WIN.blit(leveltekst, (0, 0))
        pygame.display.update()


def check_prullenbak(waar, voorwerp):
    with open(os.path.join("level.txt")) as level:
        level = int(str(level.read()))
        if waar == 1 and voorwerp.y == 320 and level % 2 == 0:
            level = level + 1
            os.system("echo " + str(level) + " > level.txt")
            voorwerp.y = 80
            voorwerp.x = 80
        elif waar == 2 and voorwerp.y > 320 and level % 3 == 0:
            level = level + 1
            os.system("echo " + str(level) + " > level.txt")
            voorwerp.y = 80
            voorwerp.x = 80
        elif waar == 0 and voorwerp.y > 320:
            if not level % 2 == 0 and not level % 3 == 0:
                level = level + 1
                os.system("echo " + str(level) + " > level.txt")
                voorwerp.y = 80
                voorwerp.x = 80
        elif not waar == 1 and voorwerp.y == 320 and level % 2 == 0:
            level = level - 1
            os.system("echo " + str(level) + " > level.txt")
            voorwerp.y = 80
            voorwerp.x = 80
        elif not waar == 2 and voorwerp.y > 320 and level % 3 == 0:
            level = level - 1
            os.system("echo " + str(level) + " > level.txt")
            voorwerp.y = 80
            voorwerp.x = 80
        elif not waar == 0 and voorwerp.y > 320:
            if not level % 2 == 0 and not level % 3 == 0:
                level = level - 1
                os.system("echo " + str(level) + " > level.txt")
                voorwerp.y = 80
                voorwerp.x = 80


def main(fpsding, waarvoorwerp, timertje, leveltje):
    voorwerp = pygame.Rect(80, 0, 80, 80)

    klokje = pygame.time.Clock()
    aan = True
    while aan:
        if fpsding == 480:
            fpsding = 0
        klokje.tick(FPS)
        fpsding = fpsding + 1
        timertje = timertje + 1
        for ding in pygame.event.get():
            if ding.type == pygame.QUIT:
                aan = False

        dingeningedruktinjereed = pygame.key.get_pressed()
        # Links
        if dingeningedruktinjereed[pygame.K_a] or dingeningedruktinjereed[pygame.K_LEFT]:
            if not waarvoorwerp == 0 and timertje > 29:
                waarvoorwerp = waarvoorwerp - 1
                timertje = 0
        # Rechts
        elif dingeningedruktinjereed[pygame.K_d] or dingeningedruktinjereed[pygame.K_RIGHT]:
            if not waarvoorwerp == 2 and timertje > 29:
                waarvoorwerp = waarvoorwerp + 1
                timertje = 0
        with open(os.path.join("level.txt")) as level:
            level = int(str(level.read()))
            snelheid = int(level / 25 + 1)
            voorwerp.y = voorwerp.y + snelheid
        draw_ding(fpsding, voorwerp, waarvoorwerp, aan, leveltje)
    pygame.quit()


def ui():
    aan = True
    while aan:
        for ding in pygame.event.get():
            if ding.type == pygame.QUIT:
                aan = False
        klokje = pygame.time.Clock()
        klokje.tick(FPS)
        WIN.blit(luchtframe1, (0, 0))
        spatietekst = font.render("Press space to start", 1, (0, 0, 0,))
        WIN.blit(spatietekst, (0, 320))
        pygame.display.update()
        dingeningedruktinjereed = pygame.key.get_pressed()
        if dingeningedruktinjereed[pygame.K_SPACE]:
            main(FPSgedaan, waarvoorwerp, timernieuwemove, level)


ui()
