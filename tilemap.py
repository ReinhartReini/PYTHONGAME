import pygame

tilemap = [
    [0,0,0,0,1],
    [1,0,0,1,0],
    [0,0,0,0,0]
]
test = pygame.display.set_mode((2,2))
tilesize = 128
tilearray = []
def draw(window, offset):
    for row in range(len(tilemap)):
        for column in range(len(tilemap[row])):
            color = "gray"
            if tilemap[row][column] == 1:
                color = "green"
            else:
                color = "blue"
            rect = pygame.Rect(row*tilesize - offset[0],column*tilesize-offset[1],tilesize,tilesize)
            pygame.draw.rect(window,color,rect)
def addarray(offset):
    for row in range(len(tilemap)):
        for column in range(len(tilemap[row])):
            rect = pygame.Rect(row*tilesize - offset[0],column*tilesize- offset[1],tilesize,tilesize)
            if tilemap[row][column] == 1:
                tilearray.append(rect)
def debug(window,offset):
    for row in range(len(tilemap)):
        for column in range(len(tilemap[row])):
            rect = pygame.Rect(row*tilesize - offset[0],column*tilesize- offset[1],tilesize,tilesize)
            if tilemap[row][column] == 1:
                pygame.draw.rect(window,"orange",rect)
    