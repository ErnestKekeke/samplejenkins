from vpython import *

spaceLen  = 20
spaceBre = 8
spaceDepth = 10
WoodThick = 0.5
ballRadius = 0.4

rateSpeed = 30

mylight = distant_light(direction=vec(-1, 1, 1), color=color.white * 0.7)


leftWall = box(pos=vec(-spaceLen/2 - WoodThick/2, 0, 0), size = vec(WoodThick,spaceBre + WoodThick, spaceDepth), texture = textures.wood)
leftWall = box(pos=vec(spaceLen/2 + WoodThick/2, 0, 0), size = vec(WoodThick,spaceBre+WoodThick, spaceDepth),texture = textures.wood )
ceilling = box(pos=vec(0, spaceBre/2, 0), size = vec(spaceLen, WoodThick, spaceDepth))
groundFloor = box(pos=vec(0, -spaceBre/2, 0), size = vec(spaceLen, WoodThick, spaceDepth))
backWall = box(pos=vec(0, 0, -spaceDepth/2 - WoodThick/2), size = vec(spaceLen+2*WoodThick, spaceBre+WoodThick, WoodThick), texture = textures.earth)
ball  = sphere(pos = vec(0,0,0), radius = ballRadius, color = color.red, emissive = False, make_trail=True)

xPos = 0
yPos = 0
zPos = 0
deltaX = 0.1
deltaY = 0.75
deltaZ = 0.64
n = 0

while True:
    xPos+= deltaX
    yPos+=deltaY
    zPos+= deltaZ
    
    rate(rateSpeed)
    ball.pos = vec(xPos, yPos, zPos)
    if(xPos>=spaceLen/2-ballRadius or xPos<=-spaceLen/2+ballRadius):
        deltaX*= -1

    if(yPos>=spaceBre/2 - ballRadius - WoodThick or yPos<=-spaceBre/2 + ballRadius + WoodThick):
        deltaY*= -1
    
    if(zPos>=spaceDepth/2 - ballRadius - WoodThick/2 or zPos<= - spaceDepth/2 + ballRadius + WoodThick/2):
        deltaZ*= -1
