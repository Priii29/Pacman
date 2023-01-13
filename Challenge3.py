from turtle import*
showturtle()
from math import floor
letters="a b c d e f".split()


def toHex(r, g, b):
# This function will convert the three R,G,B values given into a HEX code string 
    r1=floor(r/16)
    if r1>9:
        r1=letters[r1-10]

    r2=r%16
    if r2>9:
        r2=letters[r2-10]       

    g1=floor(g/16)
    if g1>9:
        g1=letters[g1-10]

    g2=g%16
    if g2>9:
        g2=letters[g2-10]     

    b1=floor(b/16)
    if b1>9:
        b1=letters[b1-10]

    b2=b%16
    if b2>9:
        b2=letters[b2-10]        

    r1=str(r1)
    r2=str(r2)
    g1=str(g1)
    g2=str(g2)
    b1=str(b1)
    b2=str(b2)         
    hex='#'+r1+r2+g1+g2+b1+b2

    return hex

def IsColorInPath(R, G, B, stepsAhead, obj):
    # This functions will determine if the color of the canvas in the turtle's
    # path is the same color as the color given in R,G,B
    # the 'stepsAhead' are the number of pixels ahead of the turtle to sample

    # convert the turtle coordinates top canvas coordinates
    y = obj.ycor() *-1
    x = obj.xcor()

    radius = int(stepsAhead/2)   
    canvas = getcanvas() # get access to tkinter.Canvas

    # determine coordinate ahead of turtle based on heading
    if obj.heading() == 0:     # find IDs of all objects in rectangle
        x1 = x+stepsAhead
        y1 = y+radius
        x2 = x+stepsAhead
        y2 = y-radius 
    elif obj.heading() == 180:
        x1 = x-stepsAhead
        y1 = y+radius
        x2 = x-stepsAhead
        y2 = y-radius 
    elif obj.heading() == 90:
        x1 = x+radius
        y1 = y-stepsAhead
        x2 = x-radius
        y2 = y-stepsAhead 
    elif obj.heading() == 270:
        x1 = x+radius
        y1 = y+stepsAhead
        x2 = x-radius
        y2 = y+stepsAhead 



    colorInPath = '0'
    ids = canvas.find_overlapping(x1, y1, x2, y2) # find IDs of all objects in rectangle
    
    if ids:     # if found objects
#        print(ids)
        index = ids[-1]        # get ID of last object (top most)
        colorInPath = canvas.itemcget(index, "fill") # get color in hex code


    colorToCheck = toHex(R, G, B) # get Hex values for the color passed through the function


    # compare R,G,B colors given to the color ahead 
    if colorInPath == colorToCheck:
        return True
    else:
        return False



def CreateMaze():
    speed(10)

    dot()

    colormode(255)
    bgcolor(0,0,0)

    pencolor(0,0,255)
    pensize(7)

       

    seth(90)
    pu()
    goto(0,380)
    pd()

        
    fillcolor(0,0,0)

    begin_fill()
    bk(50)
    rt(90)
    fd(250)
    rt(90)
    fd(250)
    lt(90)
    fd(50)
    rt(90)
    fd(50)
    rt(90)
    fd(50)
    lt(90)
    fd(280)
    rt(90)
    fd(550)
    rt(90)
    fd(580)
    rt(90)
    fd(250)
    lt(90)
    fd(50)
    rt(90)
    fd(50)
    end_fill()


    fillcolor(0,0,0)
    pu()
    rt(90)
    fd(100)
    pd()
    begin_fill()
    fd(200)
    lt(90)
    fd(200)
    lt(90)
    fd(200)
    lt(90)
    fd(200)
    end_fill()

    fillcolor(0,0,0)
    pu()
    fd(50)
    pd()
    begin_fill()
    fd(200)
    lt(90)
    fd(480)
    lt(90)
    fd(450)
    lt(90)
    fd(230)
    lt(90)
    fd(250)
    rt(90)
    fd(250)
    end_fill()

    pencolor(222, 47, 140)
    pu()
    goto(200,80)
    pd()
    rt(90)
    fd(45)




    pu()


def insertpellets():
    goto(0,0)
    seth(90)
    pu()

    colormode(255)

    pensize(50)
    pencolor(255,0,0)
    pelletDist = 20
    pelletSize = 5


    pu()
    pencolor(255,0,0)

    goto(-274,-222)
    for j in range(21):
        dot(pelletSize)
        fd(int(500/pelletDist))
    rt(90)
    for j in range(20): 
        dot(pelletSize)
        fd(int(500/pelletDist))
    rt(90)
    for j in range(21): 
        dot(pelletSize)
        fd(int(500/pelletDist))
    rt(90)
    for j in range(21): 
        dot(pelletSize)
        fd(int(500/pelletDist))
    rt(90)

    pu()
    goto(-24,52)

    for j in range(13):
        dot(pelletSize)
        fd(int(500/pelletDist))

    pu()
    goto(-24,52)
    rt(90)
    for i in range(13):
        dot(pelletSize)
        fd(int(500/pelletDist))

    pu()

#insert super pellets
    
def insertsuperpellets():
    pensize(50)  
    pelletSize = 25
    pelletDist = 523

    pu()
    pencolor(186, 3, 252)

    goto(-274,-222)
    dot(pelletSize)
    goto(-274,301)
    dot(pelletSize)
    goto(225,301)
    dot(pelletSize)
    goto(225,-222)
    dot(pelletSize)

    goto(0,55)
    hideturtle()
