import pygame
import tilemap as tl
#0 = Süden
#1 = Norden
#2 = Westen
#3 = Osten

draw = False
class Color:
    def __init__(self):
        self.red = (225,0,0)
        self.green = (0,225,0)
        self.blue = (0,0,225)
        self.white = (225,225,225)
        self.black = (0,0,0)
        self.values = [self.red,self.green,self.blue,self.white,self.black]
    def getvalue(self, index):
        return self.values[index]
offset = [0,0]  
class Player:
    def __init__(self, src):
        self.health = (225,0,0)
        self.img = [
            pygame.image.load("player_one.png"),
            pygame.image.load("player_left.png"),
            pygame.image.load("player_down.png"),
            pygame.image.load("player_up.png")
            ]
        self.x = src.get_width() / 2
        self.y = src.get_height() / 2
        self.speed = 0.35
        self.index = 0
        self.velocity = (1,1)
        self.values = [self.health]
        self.size = 128
        self.key = 0
        self.locked = "up"
    def draw(self):
        self.img[self.index] = pygame.transform.scale(self.img[self.index],(self.size,self.size))
        src.blit(self.img[self.index],(self.x,self.y))
    def collision(self):
        prect = pygame.Rect(self.x,self.y,self.size,self.size)
        for tarray in tl.tilearray:
            if tarray.colliderect(prect):
                if self.key == 0:
                    self.y -= 1
                    self.locked = "south"
                if self.key == 1:
                    self.y += 1
                    self.locked = "north"
                if self.key == 2:
                    self.x += 1
                    self.locked = "east"
                if self.key == 3:
                    self.x -= 1
                    self.locked = "west"
        imgrect = self.img[self.index].get_rect()
    def drawx(self,value):
        prect = pygame.Rect(self.x,self.y,self.size,self.size)
        for tarray in tl.tilearray:
            if tarray.colliderect(prect):
                tarray.left = value
    def drawy(self,value):
        prect = pygame.Rect(self.x,self.y,self.size,self.size)
        for tarray in tl.tilearray:
            if tarray.colliderect(prect):
                tarray.top = value
                
#Arrays
pygame.init()
running = True
#Set The Display
pygame.display.set_caption("Classes System")
icon = pygame.image.load("classes.png")
pygame.display.set_icon(icon)
src = pygame.display.set_mode((666,666),pygame.RESIZABLE)
#Add the array

#Classes Refference
color = Color()
player1 = Player(src=src)
#Font
bfont = pygame.font.SysFont("bahnschrift",16,True)
text_one = bfont.render("Hello World", True, color.red )
while running:
    tl.addarray(offset=offset)
    keys=pygame.key.get_pressed()
    player1.collision()
    if keys[pygame.K_m]:
        print("Shoot")
    elif keys[pygame.K_a]:
        player1.index = 1
        # player1.x -= player1.speed
        if player1.locked != "south":
            offset[0] -= player1.speed * 2
            player1.drawx(-player1.speed)
            player1.key = 2
            draw = True
    elif keys[pygame.K_d]:
        offset[0] += player1.speed * 2 
        player1.index = 0
        # player1.x += player1.speed
        if player1.key != 3:
            player1.drawx(+player1.speed)
        player1.key = 3
        draw = True
    elif keys[pygame.K_s]:
        offset[1] += player1.speed * 2
        player1.index = 2
        # player1.y += player1.speed
        if player1.key != 0:
            player1.drawy(+player1.speed)
        player1.key = 0
        draw = True
    elif keys[pygame.K_w]:
        offset[1] -= player1.speed * 2
        player1.index = 3
        # player1.y -= player1.speed
        if player1.key != 1:
            player1.drawy(-player1.speed)
        player1.key = 1
        draw = True
    pygame.display.flip()
    src.fill(color.getvalue(0))
    if draw:
        pass
    tl.draw(window=src,offset=offset)
    tl.debug(src,offset)
    player1.draw()
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if color.getvalue(0) != color.red:
                    color.values[0] = color.red
                else:
                    color.values[0] = color.white
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    draw = False

quit()
