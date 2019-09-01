#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from random import randint

# Write your program here
brick.sound.beep()

touchSensor = TouchSensor(Port.S1)

widthScreen = 178
heightScreen = 128

pipeWidth = 30
pipeHeight = 60
pipePosition_X = widthScreen + 10
pipePosition_Y = 0

pipePosition_X2 = widthScreen + 120
pipePosition_Y2 = 70

playerPosition_X = 30
playerPosition_Y = heightScreen / 2
playerWidth = 40
playerHeight = 40

velocityY = 1
maxVelocity = 8
playerVelocity = 1
flyToUp = False

isPressed = False
isReleased = False
isMoveBird = False


def loadImage():
    brick.display.image("FlappyBird.jpg", clear=False)
    brick.display.image("Pipe.jpg", (widthScreen + 40, 40), clear=False)
    brick.display.image("Pipe2.jpg", (widthScreen + 40, 40), clear=False)
    brick.display.image("bird.jpg", (int((178 / 2) - 20), 80), clear=False)
    wait(2000)
    brick.display.clear()


def setPressedAndReleasedFalse():
    global isPressed
    global isReleased
    isPressed = False
    isReleased = False


def pressedAndReleasedButton():
    global isPressed
    global isReleased
    global flyToUp
    global touchSensor
    global playerVelocity
    if(touchSensor.pressed()):
        isPressed = True

    if(isPressed == True and touchSensor.pressed() == False):
        isReleased = True

    if(isPressed == True and isReleased == True):
        setPressedAndReleasedFalse()
        brick.sound.beep()
        playerVelocity = 0
        flyToUp = True


def randomPipePositionY():
    global pipePosition_Y
    upOrDown = randint(0, 1)
    if(upOrDown == 0):
        return randint(-30, 0)
    elif(upOrDown == 1):
        return randint(68, 98)


def randomPipePositionY2():
    global pipePosition_Y2
    upOrDown = randint(0, 1)
    if(upOrDown == 0):
        return randint(-30, 0)
    elif(upOrDown == 1):
        return randint(68, 98)


def setPositionPipe():
    global pipePosition_X
    global pipePosition_Y
    global widthScreen
    pipePosition_X = widthScreen + 5
    pipePosition_Y = randomPipePositionY()


def setPositionPipe2():
    global pipePosition_X2
    global pipePosition_Y2
    global widthScreen
    pipePosition_X2 = widthScreen + 5
    pipePosition_Y2 = randomPipePositionY2()


def updatePositionPipes():
    global pipePosition_X
    global pipePosition_X2
    pipePosition_X -= 3
    pipePosition_X2 -= 3


loadImage()


while True:
    brick.display.image('bird.jpg', (int(playerPosition_X),
                                     int(playerPosition_Y)), clear=False)

    brick.display.image('Pipe.jpg', (int(pipePosition_X),
                                     int(pipePosition_Y)), clear=False)

    brick.display.image('Pipe.jpg', (int(pipePosition_X2),
                                     int(pipePosition_Y2)), clear=False)

    pressedAndReleasedButton()

    if(flyToUp == True):
        playerPosition_Y -= playerVelocity
        playerVelocity += 1
        if(playerVelocity >= maxVelocity):
            flyToUp = False
            playerVelocity = 0

    if(flyToUp == False):
        playerPosition_Y += playerVelocity
        playerVelocity += 1
        if(playerVelocity >= maxVelocity):
            playerVelocity = maxVelocity

    if(pipePosition_X <= 0):
        setPositionPipe()

    if(pipePosition_X2 <= 0):
        setPositionPipe2()

    updatePositionPipes()

    wait(60)
    brick.display.clear()
