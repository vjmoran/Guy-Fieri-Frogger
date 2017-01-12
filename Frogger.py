from visual import *

grutorMode = False

def main():
    """ this is the main function, including
        all of the data objects and the "event loop"
        which is the while True: loop that will
        be the universe's "time stream"
    """
    bounds = makeBoundaries()
    b0, b1, b2, b3 = bounds

    Guy = makeGuy()
    Guy.vel = vector(0,0,0)

    cars = makeCars()
    for c in cars[:3]:
        c.vel = vector(0.8,0,0)
    for c in cars[3:7]:
        c.vel = vector(-1.3,0,0)
    for c in cars[7:12]:
        c.vel = vector(0.6,0,0)
    for c in cars[12:15]:
        c.vel = vector(-1.8,0,0)

    logs = makeLogs()
    for l in logs[:4]:
        l.vel = vector(1.5,0,0)
    for l in logs[4:8]:
        l.vel = vector(-1,0,0)
    for l in logs[8:10]:
        l.vel = vector(1.8,0,0)

    road = makeRoad()

    sideWalk = makeSidewalk()

    water = makeWater()

    platform = makePlatform()

    bun = makeBun()

    patty = makePatty()

    tomato = makeTomato()

    onion = makeOnion()

    RATE = 8

    if grutorMode == False:
        lives = 10
        livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)

    win = 0 # variable represents number of ingredients Guy has gotten

    # this is the main loop of the program! it's "time" or the "event loop"
    while True:
        rate(RATE)

        Guy.pos = Guy.pos + Guy.vel
        
        #loop position updates
        for c in cars:
            c.pos = c.pos + c.vel

            if c.pos.x < b0.pos.x:  # b0 has the smallest x value
                c.pos.x = b2.pos.x  # make sure we stay in bounds

            if c.pos.x > b2.pos.x:  # b2 has the largest x value
                c.pos.x = b0.pos.x  # make sure we stay in bounds

            if Guy.pos.y == c.pos.y and Guy.pos.x > c.pos.x - 5 and Guy.pos.x < c.pos.x + 5:
                if grutorMode == False:
                    lives -= 1
                    livesText.visible = False
                    del livesText
                    livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)
                Guy.pos = (0,-50,0)
        
        for l in logs:
            l.pos = l.pos + l.vel

            if l.pos.x < b0.pos.x and l.vel.x < 0:
                l.pos.x = b2.pos.x - 10

            if l.pos.x > b2.pos.x - l.axis.x and l.vel.x > 0:
                l.pos.x = b0.pos.x

            if Guy.pos.y < 5:
                Guy.vel = vector(0,0,0)

            if Guy.pos.y == l.pos.y:
                Guy.vel = l.vel
            
            if Guy.pos.x < (b0.pos.x + (l.axis.x / 2)) and Guy.vel.x < 0:
                if grutorMode == False:
                    lives -= 1
                    livesText.visible = False
                    del livesText
                    livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)
                Guy.pos = (0,-50,0)
                Guy.vel = vector(0,0,0)

            if Guy.pos.x > (b2.pos.x - (l.axis.x / 2)) and Guy.vel.x > 0:
                if grutorMode == False:
                    lives -= 1
                    livesText.visible = False
                    del livesText
                    livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)
                Guy.pos = (0,-50,0)
                Guy.vel = vector(0,0,0)

        if Guy.pos.y == 40:
        
            if Guy.pos.x > bun.pos.x - 5 and Guy.pos.x < bun.pos.x + 5 and bun.visible == True:
                bun.pos = (-10,47,-2)
            
            elif Guy.pos.x > patty.pos.x - 5 and Guy.pos.x < patty.pos.x + 5 and patty.visible == True:
                patty.pos = (-2,47,-2)

            elif Guy.pos.x > tomato.pos.x - 5 and Guy.pos.x < tomato.pos.x + 5 and tomato.visible == True:
                tomato.pos = (6,47,-2)

            elif Guy.pos.x > onion.pos.x - 5 and Guy.pos.x < onion.pos.x + 5 and onion.visible == True:
                onion.pos = (14,47,-2)

            elif grutorMode == False:
                lives -= 1
                livesText.visible = False
                del livesText
                livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)

            Guy.vel = vector(0,0,0)
            Guy.pos = (0,-50,0)

        if grutorMode == False:
            if lives == 0:
                print("Game Over!")
                break
        
        if bun.pos.y == 47 and patty.pos.y == 47 and tomato.pos.y == 47 and onion.pos.y == 47:
            print("CONGRATS GUY! You made a burger!")
            bun.pos = (0,10,20)
            for obj in bun.objects:
                obj.radius *= 5
                if obj.radius < 10:
                    obj.pos.x *= 5
                    obj.pos.y *= 5
                    obj.pos.z += 7.5
            patty.pos = (0,8.2,22)
            patty.radius *= 5.2
            tomato.pos = (0,8,20)
            for obj in tomato.objects:
                obj.radius *= 5
                if obj.radius == 10:
                    obj.thickness *= 5
            onion.pos = (0,7,18)
            for obj in onion.objects:
                obj.radius *= 5
                obj.thickness *= 5
            break

        if Guy.pos.y == 30:
            if win == 1:
                bun.visible = True
            if win == 2:
                patty.visible = True
            if win == 3:
                tomato.visible = True
            if win == 4:
                onion.visible = True

        if scene.kb.keys:   # any keypress to be handled?
            s = scene.kb.getkey()

            if s == 'up' and Guy.pos.y < 50: 
                Guy.pos.y += 10

                if Guy.pos.y > 0 and Guy.pos.y < 40:
                    onALog = False
                    for l in logs:
                        if Guy.pos.y == l.pos.y and Guy.pos.x > l.pos.x and Guy.pos.x < l.pos.x + l.axis.x:
                            onALog = True
                    if onALog == False: 
                        Guy.pos = (0,-50,0)
                        Guy.vel = vector(0,0,0)
                        if grutorMode == False:
                            lives -= 1
                            livesText.visible = False
                            del livesText
                            livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)
                
                if Guy.pos.y == 30:
                    win += 1

            if s == 'down' and Guy.pos.y > -50: 
                Guy.pos.y -= 10

                if Guy.pos.y > 0 and Guy.pos.y < 40:
                    onALog = False
                    for l in logs:
                        if Guy.pos.y == l.pos.y and Guy.pos.x > l.pos.x and Guy.pos.x < l.pos.x + l.axis.x:
                            onALog = True
                    if onALog == False: 
                        Guy.pos = (0,-50,0)
                        Guy.vel = vector(0,0,0)
                        if grutorMode == False:
                            lives -= 1
                            livesText.visible = False
                            del livesText
                            livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)

            if s == 'right' and Guy.pos.x < 50: 
                Guy.pos.x += 7

                if Guy.pos.y > 0 and Guy.pos.y < 40:
                    onALog = False
                    for l in logs:
                        if Guy.pos.y == l.pos.y and Guy.pos.x > l.pos.x and Guy.pos.x < l.pos.x + l.axis.x:
                            onALog = True
                    if onALog == False: 
                        Guy.pos = (0,-50,0)
                        Guy.vel = vector(0,0,0)
                        if grutorMode == False:
                            lives -= 1
                            livesText.visible = False
                            del livesText
                            livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)

            if s == 'left' and Guy.pos.x > -50: 
                Guy.pos.x -= 7

                if Guy.pos.y > 0 and Guy.pos.y < 40:
                    onALog = False
                    for l in logs:
                        if Guy.pos.y == l.pos.y and Guy.pos.x > l.pos.x and Guy.pos.x < l.pos.x + l.axis.x:
                            onALog = True
                    if onALog == False: 
                        Guy.pos = (0,-50,0)
                        Guy.vel = vector(0,0,0)
                        if grutorMode == False:
                            lives -= 1
                            livesText.visible = False
                            del livesText
                            livesText = text(pos = (-49,45,0), text = 'Lives: ' + str(lives), height = 3)

def makeBoundaries():
    """creates the walls for game boundaries"""
    b0 = box(pos=(-50,0,0), axis=(0,1,0), 
             length=101, width=0.1, height = 1, color=color.white)
    b1 = box(pos=(0,-50,0), axis=(1,0,0), 
             length=101, width=0.1, height = 1, color=color.white)
    b2 = box(pos=(50,0,0), axis=(0,1,0),
             length=101, width=0.1, height = 1, color=color.white)
    b3 = box(pos=(0,50,0), axis=(1,0,0), 
             length=101, width=0.1, height = 1, color=color.white)
    boundList = [b0,b1,b2,b3]
    return boundList

def makeGuy():
    """creates Guy Fieri, the moving object"""
    Guy = frame(pos=(0,-50,0))
    sphere(frame=Guy, radius=3, color=(1.0,0.8,0.6))
    ellipsoid(frame=Guy, pos=(-1.0,0.8,3.0), length=2.0, height=1.0, width=0.8, color=color.black)
    ellipsoid(frame=Guy, pos=(1.0,0.8,3.0), length=2.0, height=1.0, width=0.8, color=color.black)
    curve(frame=Guy, pos=[(-1.1,-1.0,2.6),(-0.5,-1.4,3.0),(0.5,-1.4,3.0),(1.1,-1.0,2.6)], radius=0.3, color = color.black)
    pyramid(frame=Guy, pos=(0,-2.2,2.3), axis=(0,-1.5,0), size=(1.5,1.5,0.5))
    pyramid(frame=Guy, pos=(0,2.2,1.0), axis=(0,1.5,0), size=(1.8,1.8,1.5))
    pyramid(frame=Guy, pos=(-1.0,2.0,1.0), axis=(-0.5,1.5,0), size=(1.5,1.8,1.4))
    pyramid(frame=Guy, pos=(1.0,2.0,1.0), axis=(0.5,1.5,0), size=(1.5,1.8,1.4))
    pyramid(frame=Guy, pos=(-2.0,1.7,1.0), axis=(-1.0,1.5,0), size=(0.8,1.8,1.2))
    pyramid(frame=Guy, pos=(2.0,1.7,1.0), axis=(1.0,1.5,0), size=(0.8,1.8,1.2))
    return Guy

def makeCars():
    """creates several car objects from spheres"""
    car0 = sphere(radius=2, pos=(30,-40,0), color=(0.4,0.8,0.7))
    car1 = sphere(radius=2, pos=(-3,-40,0), color=(0.4,0.8,0.7))
    car2 = sphere(radius=2, pos=(-36,-40,0), color=(0.4,0.8,0.7))
    car3 = sphere(radius=2, pos=(48,-30,0), color=(1.0,0.5,0.6))
    car4 = sphere(radius=2, pos=(23,-30,0), color=(1.0,0.5,0.6))
    car5 = sphere(radius=2, pos=(-2,-30,0), color=(1.0,0.5,0.6))
    car6 = sphere(radius=2, pos=(-27,-30,0), color=(1.0,0.5,0.6))
    car7 = sphere(radius=2, pos=(45,-20,0), color=(0.5,0.5,0.8))
    car8 = sphere(radius=2, pos=(25,-20,0), color=(0.5,0.5,0.8))
    car9 = sphere(radius=2, pos=(5,-20,0), color=(0.5,0.5,0.8))
    car10 = sphere(radius=2, pos=(-15,-20,0), color=(0.5,0.5,0.8))
    car11 = sphere(radius=2, pos=(-35,-20,0), color=(0.5,0.5,0.8))
    car12 = sphere(radius=2, pos=(40,-10,0), color=(0.6,0.9,0.5))
    car13 = sphere(radius=2, pos=(7,-10,0), color=(0.6,0.9,0.5))
    car14 = sphere(radius=2, pos=(-26,-10,0), color=(0.6,0.9,0.5))
    carList = [car0, car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, car13, car14]
    return carList

def makeLogs():
    """creates several log objects from cylinders"""
    log0 = cylinder(pos=(-40,10,-2), axis=(10,0,0), radius=2, color=(0.5,0.3,0))
    log1 = cylinder(pos=(-16,10,-2), axis=(10,0,0), radius=2, color=(0.5,0.3,0))
    log2 = cylinder(pos=(8,10,-2), axis=(10,0,0), radius=2, color=(0.5,0.3,0))
    log3 = cylinder(pos=(30,10,-2), axis=(10,0,0), radius=2, color=(0.5,0.3,0))
    log4 = cylinder(pos=(-40,20,-2), axis=(10,0,0), radius=2, color=(0.6,0.4,0.2))
    log5 = cylinder(pos=(-16,20,-2), axis=(10,0,0), radius=2, color=(0.6,0.4,0.2))
    log6 = cylinder(pos=(8,20,-2), axis=(10,0,0), radius=2, color=(0.6,0.4,0.2))
    log7 = cylinder(pos=(30,20,-2), axis=(10,0,0), radius=2, color=(0.6,0.4,0.2))
    log8 = cylinder(pos=(-22,30,-2), axis=(20,0,0), radius=2, color=(0.4,0.2,0))
    log9 = cylinder(pos=(18,30,-2), axis=(20,0,0), radius=2, color=(0.4,0.2,0))
    logList = [log0, log1, log2, log3, log4, log5, log6, log7, log8, log9]
    return logList

def makeRoad():
    """creates road below the cars"""
    road = frame(pos=(0,-27,0))
    box(frame=road, axis=(1,0,0), length=98, width=0.1, height = 45, color=(0.1,0.1,0.1))
    box(frame=road, pos=(0,2,0.1), axis=(1,0,0), length=100, width=0.1, height = 0.2, color=color.white)
    box(frame=road, pos=(0,12,0.1), axis=(1,0,0), length=100, width=0.1, height = 0.2, color=color.white)
    box(frame=road, pos=(0,-8,0.1), axis=(1,0,0), length=100, width=0.1, height = 0.2, color=color.white)
    box(frame=road, pos=(0,-18,0.1), axis=(1,0,0), length=100, width=0.1, height = 0.2, color=color.white)
    return road

def makeSidewalk():
    """creates a 'safe' object"""
    walk = box(pos=(0,0,0), axis=(1,0,0), length=99, width=0.1, height = 10, color=(0.7,0.7,0.7))
    return walk

def makeWater():
    """creates water background"""
    water = box(pos=(0,27,-5), axis=(1,0,0), length=105, width=0.1, height = 50, color=(0.3,0.5,1.0))
    return water

def makePlatform():
    """creates final platform that ingredients rest on"""
    platform = frame(pos=(0,47,-3))
    box(frame=platform, axis=(1,0,0), length=103, width=0.1, height = 8, color=(0.3,0.3,0.3))
    box(frame=platform, pos=(-30,-6,0), axis=(1,0,0), length=8, width=0.1, height = 10, color=(0.3,0.3,0.3))
    box(frame=platform, pos=(-10,-6,0), axis=(1,0,0), length=8, width=0.1, height = 10, color=(0.3,0.3,0.3))
    box(frame=platform, pos=(10,-6,0), axis=(1,0,0), length=8, width=0.1, height = 10, color=(0.3,0.3,0.3))
    box(frame=platform, pos=(30,-6,0), axis=(1,0,0), length=8, width=0.1, height = 10, color=(0.3,0.3,0.3))
    return box

def makeBun():
    """creates bun object that must be obtained to win"""
    bun = frame(pos=(-10,40,-2))
    sphere(frame=bun, radius=2.2, color=(0.8,0.6,0))
    sphere(frame=bun, pos=(0.2,-0.5,2.9), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(-0.7,-1.1,1.5), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(-0.2,0.3,2.9), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(1.4,-0.2,1.9), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(-1.5,-0.4,1.7), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(1.2,-1.3,1.4), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(0.3,-1.5,0.8), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(0.8,1,1.4), radius=0.2, color=color.white)
    sphere(frame=bun, pos=(-0.9,0.8,1.4), radius=0.2, color=color.white)
    bun.visible = False
    return bun

def makePatty():
    """creates burger patty object that must be obtained to win"""
    patty = cylinder(pos=(30,40,-2), axis=(0,0,1), radius=2, color=(0.3,0.2,0.1))
    patty.visible = False
    return patty

def makeTomato():
    """creates tomato object that must be obtained to win"""
    tomato = frame(pos=(10,40,-2))
    ring(frame=tomato, radius=2, thickness=0.3, axis=(0,0,1), color=(0.9,0.2,0.2))
    cylinder(frame=tomato, pos=(-2,0,0), axis=(4,0,0), radius=(0.3), color=(0.9,0.2,0.2))
    cylinder(frame=tomato, pos=(-1.2,-1.2,0), axis=(2.7,2.7,0), radius=(0.3), color=(0.9,0.2,0.2))
    cylinder(frame=tomato, pos=(-1.2,1.2,0), axis=(2.7,-2.7,0), radius=(0.3), color=(0.9,0.2,0.2))
    tomato.visible = False
    return tomato

def makeOnion():
    """creates tomato object that must be obtained to win"""
    onion = frame(pos=(-30,40,-2))
    ring(frame=onion, radius=2, thickness=0.3, axis=(0,0,1), color=(0.6,0,0.8))
    ring(frame=onion, radius=1.5, thickness=0.3, axis=(0,0,1), color=color.white)
    ring(frame=onion, radius=1, thickness=0.3, axis=(0,0,1), color=(0.6,0,0.8))
    ring(frame=onion, radius=0.5, thickness=0.3, axis=(0,0,1), color=color.white)
    onion.visible = False
    return onion

if __name__ == "__main__": 
    main() 
