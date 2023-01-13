from turtle import *
from time import sleep
from Challenge3 import *
from math import floor
letters="a b c d e f".split()

title("PacMan")
setup(width=500,height=500)
colormode(255)
bgcolor(0,0,0)


tracer(0)
CreateMaze()
insertpellets()
insertsuperpellets()

PM = Turtle()
PM.hideturtle()
#PM.shape(https//i.gifer.com/origin/f2/f2726893541a7446b988ba7743c5296c_w200.gif, shape=None)
PM.shape("circle")
PM.shapesize(1.8)
PM.color(255,255,0)
PM.pencolor(0,0,0)
PM.pensize(15)
PM.speed(7)
PM.pu()
PM.goto(0,55)
PM.seth(90)
PM.showturtle()

ghost = Turtle()
ghost.hideturtle()
ghost.shape("triangle")
ghost.shapesize(1.8)
ghost.pu()
ghost.color(0,255,0)
ghost.goto(227,-200)
ghost.seth(90)
ghost.showturtle()
ghost.speed(5)

ghost2 = Turtle()
ghost2.hideturtle()
ghost2.shape("triangle")
ghost2.shapesize(1.8)
ghost2.pu()
ghost2.color(0,200,200)
ghost2.goto(-274,-233)
ghost2.seth(90)
ghost2.showturtle()
ghost2.speed(1)


scoreboard=Turtle()
scoreboard.hideturtle()
scoreboard.speed(0)
scoreboard.color(255,255,255)
scoreboard.pu()
scoreboard.goto(170,340)
scoreboard.write("Score: 0 Lives: 3", align="center", font=("Comfortaa", 24, "normal"))

life=Turtle()
life.hideturtle()
#variables
score = 0
lives = 3

#functions
def updateScore():
    scoreboard.clear()
    scoreboard.write("Score: "+str(score)+ " Lives: " + str(lives), align="center", font=("Courier", 24, "normal"))
    
def startOver():

    global score
    global lives
    
    sleep(1)
    PM.pu()
    PM.goto(0,55)
    PM.pd()
    lives-=1
    updateScore()
    if lives <= 0 :
        life.pencolor(255,0,0)
        life.write("GAME OVER - starting again in 5 secs", align="center", font=("Geostar",40,"normal"))
        life.clear()
        sleep(1)
        score = 0
        lives = 3
        sleep(5)
        Reset()

def Reset():
    CreateMaze()
    insertpellets()
    insertsuperpellets()

def KeyUp():
    PM.seth(90)

def KeyLeft():
    PM.seth(180)

def KeyRight():
    PM.seth(0)

def KeyDown():
    PM.seth(270)

onkeypress(KeyUp,"Up")
onkeypress(KeyLeft,"Left")
onkeypress(KeyRight,"Right")
onkeypress(KeyDown,"Down")


listen()


PM.pd()
#Pacman eating pellets 
def CheckPort():
    if PM.ycor() > 70 and PM.ycor() < 95: 
        if PM.xcor()>190 and PM.xcor()<255:
            PM.seth(0)
            PM.pu()
            PM.hideturtle()
            PM.goto(0,55)
            PM.showturtle()
            PM.pd()


        
while True:
    CheckPort()
    if IsColorInPath(255,0,0,21,PM) or IsColorInPath(0,0,0,21,PM)or IsColorInPath(186, 3, 252,21,PM) or IsColorInPath(222, 47, 140,21,PM) :
       if IsColorInPath(255,0,0,21,PM):
           score+=1
           
       if IsColorInPath(0,255,0,27,PM) or IsColorInPath(0,200,200,27,PM):
           startOver()
      
       PM.fd(5)
       
#Ghost movements

    
    if IsColorInPath(0,0,0,25,ghost) or IsColorInPath(255,0,0,25,ghost)or IsColorInPath(186, 3, 252,25,ghost):
        ghost.fd(1)
    else: 
        ghost.rt(90)
    
    if IsColorInPath(0,0,0,25,ghost2) or IsColorInPath(255,0,0,25,ghost2)or IsColorInPath(186, 3, 252,25,ghost2):
        ghost2.fd(0.5)
    else: 
        ghost2.lt(90)


       
    updateScore()
    update()
    sleep(0.005)
