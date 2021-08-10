import pygame
import random

# colors
background = (40,44,52)
red = (224,108,117)
green = (152,192,123)
yellow = (229,192,123)
blue = (97,175,239)
purple = (198,120,221)

fps = 10

# most flags are either 1:2 or 2:3 ratio
smWidth, smHeight = 180, 120    # total of 300
laWidth, laHeight = 200, 100    # must be same total (300)

#width = 0
#height = 0

# pygame related
winWidth, winHeight = 900, 500
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("pygame test")

#vSplits = random.randrange(1, 4)    # randrange is exclusive
#hSplits = random.randrange(1, 4)

colorArray = [red, green, yellow, blue, purple]

# creates arrays for the dimensions of each split dynamically
vSplitArray = []
hSplitArray = []


def generateRatio():
    j = random.randint(1, 2)
    print(j)

    if (j == 1):
        width, height = smWidth, smHeight   # 2:3 ratio
        print(width, height)
    else:
        width, height = laWidth, laHeight   # 1:2 ratio
        print(width, height)


def generateSplitArrays(width, height, hSplits, vSplits):
    for i in range(vSplits):
        vSplitArray.append(30+height/vSplits*i)
        print(vSplitArray)

        for i in range(hSplits):
            hSplitArray.append(30+width/hSplits*i)


def randomise():
    global vSplits
    global hSplits
    random.shuffle(colorArray)

    vSplits = random.randrange(1, 4)    # randrange is exclusive
    hSplits = random.randrange(1, 4)

    j = random.randint(1, 2)
    print(j)

    global width
    global height

    if (j == 1):
        width, height = smWidth, smHeight   # 2:3 ratio
        print(width, height)
    else:
        width, height = laWidth, laHeight   # 1:2 ratio
        print(width, height)

    for i in range(vSplits):
        vSplitArray.append(30+height/vSplits*i)
        print(vSplitArray)

        for i in range(hSplits):
            hSplitArray.append(30+width/hSplits*i)

    #generateRatio()
    #generateSplitArrays(width, height, hSplits, vSplits)

randomise()


def drawWindow():
    win.fill(background)

    for i in range(vSplits):
        pygame.draw.rect(win, colorArray[i], pygame.Rect(30, vSplitArray[i], width, height/vSplits))

    for i in range(hSplits):
        pygame.draw.rect(win, colorArray[i], pygame.Rect(hSplitArray[i], 30, width/hSplits, height))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(fps)     # caps fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        drawWindow()

        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_SPACE]:
            print("space")
            randomise()

    pygame.quit()


main()
