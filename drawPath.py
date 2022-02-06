import sys, pygame

def doAnimate(path, roomtoxy):
    pygame.init()
    width, height = 1275, 2100
    sc = .4
    width = width * sc
    height = height * sc
    size  = width, height
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    background = pygame.image.load("gates_ctr_6-unsh.png")
    background = pygame.transform.scale(background, (width, height))
    robot = pygame.image.load("walle.jpg")
    robot = pygame.transform.scale(robot, (15, 15))
    robotrect = robot.get_rect()
    currX, currY = roomtoxy[path[0]]
    ite = 0
    ctr = 0
    mod = 30
    while 1:
        ite += 1
        if (ite % mod == 0):
            ctr += 1
            if (ctr < len(path)):
                currX, currY = roomtoxy[path[ctr]]
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        for room in roomtoxy:
            (x, y) = roomtoxy[room]
            (x, y) = (x * sc, y * sc)
            r = 2
            pygame.draw.circle(screen, "red", (x, y), r)
        
        robotrect.left = currX * sc
        robotrect.top = currY * sc

        screen.blit(robot, robotrect)
        pygame.display.flip()
