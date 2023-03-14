import turtle
from turtle import *
import math as g
import random
from random import *
import colorsys
from time import perf_counter as clock
from turtle import Shape, Turtle, mainloop, Vec2D as Vec
from turtle import TurtleScreen, RawTurtle, TK
import math

def HexaColor():
    tuxedo = turtle.Turtle()
    tuxedo.speed(0)
    colors = ["red", "blue", "yellow", "green", "orange"]
    for i in range(100):
        tuxedo.color(colors[i%5])
        tuxedo.pensize(5)
        tuxedo.forward(i)
        tuxedo.left(60)
    turtle.done()
    
#----------------------------------------------------------------------------------------------------------------------------------------------    

def Flower():
    b = turtle.Turtle()
    b.speed(100)
    b.color("red", "yellow")
    b.begin_fill()
    for i in range(100):  #for loop for the number of iterations of lines
        b.forward(100)
        b.left(167)   #each iteration with 167 degrees
    b.end_fill()  #color fill
    b.hideturtle()
    turtle.done()
    
#----------------------------------------------------------------------------------------------------------------------------------------------    
    
def Heart():
    heart = turtle.Turtle()
    b = turtle.Screen()
    b.bgcolor("black")
    turtle.title("BHARATH_GUNTREDDI")
    heart.color("red")
    heart.up()
    heart.goto(0, -100)
    heart.down()
    heart.begin_fill()
    heart.fillcolor("red")
    heart.left(140)
    heart.forward(300)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90,200)
    heart.forward(300)
    heart.goto(0,-100)
    heart.end_fill()
    turtle.done()

"""
/*-Turtle position-*/

-- The turtle position is specified with the 2d co-ordination system

-- Default direction of the turtle is East

-- b = turtle.Turtle()

-- Change direction of the turtle by -

				[ b.setheading(degree) ] # any direction can be mention

-- Moving the turtle forward by -
				[ b.forward(any_pixel_value) ]   #argument can be int or float

-- Moving the turtle forward by -
				[ b.backward(any_pixel_value) ]   #argument can be int or float

-- Turning the turtle by -
				[ b.left(degree) ]  #turn the turtle to the assigned angle

-- [ b.hideturtle() ]  #hides the turtle
		- If you want to hide the turtle at last you try this at the end of your code
		- If you want to hide th turtle from the very begining you can place this at begining

-- [ b.speed(0-10) ]  #values form 0 to 10 o is the fastest and comes the 10

-- b.begin_fill()
-- b.fillcolor("cool_name")   #fills the area with the specified color
-- b.end_fill()

-- OR can be 

-- b.color("turtle_color", "area_color")  

-- b.pensize(value)   #thickness of lines

-- b.home()  #goto home i.e center of the window

"""

#----------------------------------------------------------------------------------------------------------------------------------------------    

def HexaShapes():
    shape = turtle.Turtle()
    color =["blue", "green", "red", "pink", "yellow", "purple"]
    def color_shape(a):
        for i in range(200):
            shape.circle(50, steps=a)
            shape.forward(i)
            shape.color()
            shape.left(45)
    color_shape(6)
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    
 
def FillSquare():
    b = turtle.Turtle()  #adds an arrow
    b.begin_fill()
    b.color("blue", "red") #fills line withn blue and square with red
    b.forward(200)
    b.left(90)
    b.forward(200)
    b.left(90)
    b.forward(200)
    b.left(90)
    b.forward(200)
    b.end_fill()
    turtle.done() #end of the turtle

#----------------------------------------------------------------------------------------------------------------------------------------------    

def TurtlePenS():
    b = turtle.Turtle()  #adds an arrow
    b.shape("turtle")   #changes the shape of the point
    # b.colormode(255)  #to set color code to rgb
    '''
    b.forward(100)  #moves the arrow forward
    b.left(45)   #rotates 45 degrees
    b.forward(100)   #and agian moves forward
    b.right(90)   #moves right 90 degrees
    b.forward(100) #moves forward
    '''
    b.color("blue", "red", )
    b.begin_fill()
    for i in range(4):
        b.forward(50)
        b.left(90)
    b.penup()  #jumps to the next line doesnt draw a line
    b.forward(100)
    b.pendown()
    for i in range(4):
        b.forward(50)
        b.left(90)
    b.penup()
    b.forward(100)
    b.pendown()
    for i in range(4):
        b.forward(50)
        b.left(90)
    b.end_fill()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Title(title):
    unicorn = turtle.Turtle()
    unicorn.speed(10)
    b = turtle.Screen()
    b.bgcolor("black")
    b.title(title)
    unicorn.color("red")
    # unicorn.color()
    # unicorn.getcolor().bgcolor()
    unicorn.up()
    unicorn.goto(-200, 200)
    unicorn.down()
    # unicorn.forward(300)
    # unicorn.left(250)
    # unicorn.forward(300)
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Circle1():
    b = turtle.Turtle()
    b.getscreen().bgcolor("black")
    # b.title("BHARATH_GUNTREDDI")
    b.speed(0)
    def circle(x, y, color, radius):
        b.up()
        b.goto(x, y)
        b.down()
        b.begin_fill()
        b.fillcolor(color)
        b.circle(radius)
        b.end_fill()
        b.up()
        b.home()
        b.down()
    circle(0, -50, "blue", 50)
    circle(400, 200, "green", 60)
    circle(400, -200, "pink", -50)
    circle(-400, -200, "red", -50)
    circle(-400, 200, "yellow", 50)

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Circle2():
    b = turtle.Turtle ()
    b.speed(0)
    b.up()
    b.goto(-300, -300)
    color1 = ["red", "blue", "yellow", "green"]
    for i in range(4):
        b.down()
        b.begin_fill()
        b.circle(50)
        b.color(color1[i])
        b.end_fill()
        b.up()
        b.forward(100)
        b.down()
    b.up()
    b.forward(-50)
    b.setheading(90)
    b.forward(100)
    for i in range(4):
        b.up()
        b.forward(100)
        b.down()
        b.down()
        b.begin_fill()
        b.circle(50)
        b.color(color1[i])
        b.end_fill()
    b.up()
    b.forward(150)
    b.left(135)
    b.forward(170)
    for i in range(4):
        b.up()
        b.forward(100)
        b.down()
        b.down()
        b.begin_fill()
        b.circle(50)
        b.color(color1[i])
        b.end_fill()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Circle3():
    b = turtle.Turtle()
    b.speed(10)
    b.color("red", "yellow")
    for i in range(2000):
        b.forward(g.sqrt(i))
        b.left(i%180)
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Bone():
    b = turtle.Turtle()
    b.speed(10000)
    b.color("blue")
    b.begin_fill()
    for i in range(200):
        b.forward(10)
        b.left(g.sin(i/10)*25)
        b.left(20)
    b.end_fill()
    turtle.done()
    
#----------------------------------------------------------------------------------------------------------------------------------------------    

def stroke():
    b = turtle.Turtle()
    b.speed(10)
    b.color("blue")
    for i in range(1000):
        b.forward(10)
        b.left(i%20)
        b.penup()
        b.forward(10)
        b.right(45)
        b.left(i%45)
        b.pendown()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def AmongUs():
    us = turtle.Turtle()
    b = turtle.Screen()
    b.bgcolor("black")
    #us.speed(0)
    def character():
        us.pensize(10)
        us.color("red")
        us.begin_fill()
        us.fillcolor("red")
        # us.speed(0)
        us.up()
        us.goto(0, -100)
        us.down()
        us.left(90)
        us.forward(300)
        us.right(180)
        us.circle(100, -180)
        us.right(180)
        us.forward(300)
        us.right(180)
        us.circle(25, -180)
        us.right(180)
        us.forward(150)
        # us.right(180)
        us.circle(50, -180)
        us.forward(150)
        us.right(180)
        us.circle(25, -180)
        us.end_fill()
    def goggle():
        us.pensize(10)
        us.color("blue")
        us.up()
        us.goto(200, 200)
        us.down()
        # us.speed(0)
        us.begin_fill()
        us.fillcolor("blue")
        us.right(90)
        us.circle(25, -180)
        us.right(180)
        us.forward(120)
        us.right(180)
        us.circle(25, -180)
        us.right(180)
        us.forward(120)
        us.end_fill()
    def bag():
        us.pensize(10)
        us.up()
        us.home()
        us.down()
        # us.speed(0)
        us.color("red")
        us.begin_fill()
        us.fillcolor("red")
        us.left(90)
        us.forward(50)
        us.left(360)
        us.circle(25, -180)
        us.right(180)
        us.forward(100)
        us.right(180)
        us.circle(25, -180)
        us.right(180)
        us.forward(100)
        us.end_fill()
    character()
    goggle()
    bag()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Car():
    car = turtle.Turtle()
    # code for drawing rectangular upper body
    car.color('black')
    car.fillcolor('red')
    car.penup()
    car.goto(0,0)
    car.pendown()
    car.begin_fill()
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.end_fill()
    # code for drawing window and roof
    car.penup()
    car.goto(100, 50)
    car.pendown()
    car.setheading(45)
    car.forward(70)
    car.setheading(0)
    car.forward(100)
    car.setheading(-45)
    car.forward(70)
    car.setheading(90)
    car.penup()
    car.goto(200, 50)
    car.pendown()
    car.forward(49.50)
    # code for drawing two tyres
    car.penup()
    car.goto(100, -10)
    car.pendown()
    car.color('black')
    car.fillcolor('black')
    car.begin_fill()
    car.circle(20)
    car.end_fill()
    car.penup()
    car.goto(300, -10)
    car.pendown()
    car.color('black')
    car.fillcolor('black')
    car.begin_fill()
    car.circle(20)
    car.end_fill()
    car.hideturtle()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def IndiaFlag():
    flag = turtle.Turtle()
    b = turtle.Screen()
    b.bgcolor("red")
    def stick():
        flag.pensize(3)
        flag.goto(0, -500)
        flag.goto(0, 300)
    stick()
    def flag_color(color):
        for i in range(2):
            flag.color(color)
            flag.begin_fill()
            flag.fillcolor(color)
            flag.forward(400)
            flag.right(90)
            flag.forward(80)
            flag.right(90)
            flag.end_fill()
    flag_color("orange")
    flag.goto(0, 220)
    flag_color("white")		
    flag.goto(0, 140)
    flag_color("green")
    flag.forward(200)
    flag.color("blue")
    flag.circle(40)
    flag.left(90)
    flag.forward(40)
    def chakra():
        for i in range(24):
            flag.forward(40)
            flag.backward(40)
            flag.left(15)
    flag.hideturtle()
    chakra()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Infinity():
    inf = turtle.Turtle()
    b = turtle.Screen()
    b.bgcolor("black")
    inf.color("skyblue")
    inf.right(45)
    inf.speed(0)
    for i in range(155):
        inf.circle(30)
        if 7 < i < 65:
            inf.left(5)
        if 85 < i <138:
            inf.right(5)
        if i < 85:
            inf.forward(10)
        else:
            inf.forward(5)
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def IronMan():
    canvas1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
            (-40, -20), (0, -20)],
            [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
            (40, 120), (0, 120)]
        ]
    canvas2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
            (-80, -230), (-64, -210), (0, -210)],
            [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
            (100, -46), (50, -40), (40, -30), (0, -30)]
        ]
    canvas3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
            (0, -250)],
            [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
            (0, -220)]
        ]
    turtle.hideturtle()
    turtle.bgcolor('red')  # Dark Red
    turtle.setup(500, 600)
    turtle.title("I AM IRONMAN")
    canvas1Goto = (0, 120)
    canvas2Goto = (0, -30)
    canvas3Goto = (0, -220)
    turtle.speed(2)
    def logo(a, b):
        turtle.penup()
        turtle.goto(b)
        turtle.pendown()
        turtle.color('yellow')  # Light Yellow
        turtle.begin_fill()
        for i in range(len(a[0])):
            x, y = a[0][i]
            turtle.goto(x, y)
        for i in range(len(a[1])):
            x, y = a[1][i]
            turtle.goto(x, y)
        turtle.end_fill()
    logo(canvas1, canvas1Goto)
    logo(canvas2, canvas2Goto)
    logo(canvas3, canvas3Goto)
    turtle.hideturtle()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def SquareLamo():
    sqd = turtle.Turtle()
    sqd.speed(0)
    b = turtle.Screen()
    b.bgcolor("black")
    sqd.hideturtle()
    def pot():
        for i in range(500):
            turtle.colormode(255)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            sqd.color(r, g, b)
            sqd.forward(i)
            sqd.right(100)
    pot()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def SquareMixSpiral():
    sq = turtle.Turtle()
    b = turtle.Screen()
    b.bgcolor("black")
    sq.speed(0)
    sq.pensize(2)
    sq.left(45)
    def sq1():
        for i in range(300):
            turtle.colormode(255)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            sq.pencolor(r, g, b)
            sq.forward(i )
            sq.right(90)
    sq1()
    sq.left(90)
    def sq2():
        for i in range(100):
            turtle.colormode(255)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            sq.pencolor(r, g, b)
            sq.forward(i )
            sq.right(90)
    sq2()
    sq.forward(100)
    sq.right(90)
    sq.forward(100)
    sq.right(90)
    sq.forward(50)
    sq.left(90)
    sq.forward(250)
    sq2()
    sq.right(90)
    sq.forward(100)
    sq.left(90)
    sq.forward(50)
    sq.right(90)
    sq.forward(250)
    sq2()
    sq.right(90)
    sq.forward(100)
    sq.left(90)
    sq.forward(50)
    sq.right(90)
    sq.forward(250)
    sq2()
    sq.hideturtle()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def SquareSpiral():
    ddd = turtle.Turtle()
    b = turtle.Screen()
    b.bgcolor('black') 
    ddd.speed(0) 
    turtle.title("rgb spiral design")
    ddd.hideturtle()
    def spiral():
        x = 1 
        while x < 400: 
            r = random.randint(0,255) 
            g = random.randint(0,255)  
            b = random.randint(0,255) 
            turtle.colormode(255)  
            ddd.pencolor(r,g,b) 
            ddd.forward(x) 
            ddd.right(90.991) 
            x = x+1 
    spiral()        
    turtle.done() 

#----------------------------------------------------------------------------------------------------------------------------------------------    

def StarPix():
    star = turtle.Turtle()
    b = turtle.Screen()  #created screen object 
    b.title("BHARATH_GUNTREDDI") 
    # star.shape("turtle") 
    star.getscreen().bgcolor("black")  #screen object created and background color changed 
    star.speed(10)
    star.color("red")
    star.penup()
    star.goto((-100, 100))
    star.pendown()
    def draw(star, size):
        if size <= 10:
            return 
        else:
            star.begin_fill()
            for i in range(5):
                star.forward(size)
                draw(star, size/3)
                star.left(216)
            star.end_fill()
    draw(star,300)
    star.hideturtle()
    turtle.done()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def TurtleRace():
    race = turtle.Turtle()
    '''
    # start_race = False
    # race.shape("turtle")
    # b = turtle.Screen()
    # bet = b.textinput(title = "Bet On A Turtle", prompt = "Enter the Turtle color and the bet amount :")
    # colors = ["red", "green", "blue", "yellow", "orange", "pink"]
    # position = [-70, -40, -10, 20, 50, 80]
    # turtles =[]

    # for i in range(0, 6):
    # 	race.color(colors[i])
    # 	# race.penup()
    # 	race.goto(-230, position[i])
    # 	# race.pendown()
    # 	turtles.append(turtles)

    # if bet:
    # 	start_race = True 

    # while start_race:
    # 	for race in turtles:
    # 		if race.xcor() > 230:
    # 			start_race = False
    # 			win_color = race.pencolor()
    # 			if win_color == bet:
    # 				print(" &d is the winner, you won the bet " % (win_color))
    # 			else:
    # 				print("&d is the winner , you lost the bet " % (win_color))

    # 		distance = random.randint(0, 10)
    # 		race.forward(distance)
    '''
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-140, 140)
    # racing track
    for i in range(15):
        turtle.write(i, align ='center')
        turtle.right(90)
        for j in range(8):
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
            turtle.forward(10)
        turtle.penup()
        turtle.backward(160)
        turtle.left(90)
        turtle.forward(20)
    # first player details
    player_1 = turtle.Turtle()
    player_1.color('red')
    player_1.shape('turtle')
    # first player proceeds to racing track
    player_1.penup()
    player_1.goto(-160, 100)
    player_1.pendown()
    # 360 degree turn
    for turn in range(10):
        player_1.right(36)
    # second player details
    player_2 = turtle.Turtle()
    player_2.color('blue')
    player_2.shape('turtle')
    # second player enters in the racing track
    player_2.penup()
    player_2.goto(-160, 70)
    player_2.pendown()
    # 360 degree turn
    for turn in range(72):
        player_2.left(5)
    # third player details
    player_3 = turtle.Turtle()
    player_3.shape('turtle')
    player_3.color('green')
    # third player enters in the racing track
    player_3.penup()
    player_3.goto(-160, 40)
    player_3.pendown()
    # 360 degree turn
    for turn in range(60):
        player_3.right(6)
    # fourth player details
    player_4 = turtle.Turtle()
    player_4.shape('turtle')
    player_4.color('orange')
    # fourth player enters in the racing track
    player_4.penup()
    player_4.goto(-160, 10)
    player_4.pendown()
    # turn to 360 degrees
    for turn in range(30):
        player_4.left(12)
    # turtles speed
    for turn in range(100):
        player_1.forward(random.randint(1, 5))
        player_2.forward(random.randint(1, 5))
        player_3.forward(random.randint(1, 5))
        player_4.forward(random.randint(1, 5))
    turtle.done()
# TurtleRace()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def WindowsLogo():
    turtle.speed(1)
    turtle.bgcolor('black')
    turtle.penup()
    turtle.goto(-50,60)
    turtle.pendown()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.goto (100,100)
    turtle.goto (100,-100)
    #Draw windows
    turtle.goto(-50,-60)
    turtle.goto(-50,60)
    turtle.end_fill()
    turtle.color('black')
    turtle.goto(15,100)
    #cut 2 equal parts
    turtle.color('black')
    turtle.width(10)
    turtle.goto (15,-100)
    turtle.penup()
    turtle.goto(100,0)
    turtle.pendown()
    turtle.goto(-100,0)
    turtle.done()
# WindowsLogo()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def CircleSpiral():
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.color('blue')
    turtle.hideturtle()
    n = 1
    p = True
    while True:
        turtle.circle(n)
        if p:
            n = n - 1
        else:
            n = n + 1
        if n == 0 or n == 60:
            p = not p
        turtle.left(1)
        turtle.forward(3)
    turtle.done()
# ColorSpiral()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def ColorSpiral():
    t = turtle.Turtle()
    s = turtle.Screen().bgcolor('black')
    t.speed(0)
    n = 70
    h = 0
    for i in range (360):
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h+= 1/n
        t.color(c)
        t.left(1)
        t.fd(1)
        for j in range (2):
            t.left(2)
            t.circle(100)
# ColorSpiral()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def GoogleLogo():
    gg = turtle.Turtle()
    turtle.bgcolor("black")
    gg.color("#4285F4","#4285F4")
    gg.pensize(5)
    gg.speed(2)
    def google():
        gg.forward(120)
        gg.right(90)
        gg.circle(-150,50)
        gg.color("green")
        gg.circle(-150,100)
        gg.color("yellow")
        gg.circle(-150,60)
        gg.color("red","red")
        gg.begin_fill()
        gg.circle(-150,100)
        gg.right(90)
        gg.forward(50)
        gg.right(90)
        gg.circle(100,100)
        gg.right(90)
        gg.forward(50)
        gg.end_fill()
        gg.begin_fill()
        gg.color("yellow","yellow")
        gg.right(180)
        gg.forward(50)
        gg.right(90)
        gg.circle(100,60)
        gg.right(90)
        gg.forward(50)
        gg.right(90)
        gg.circle(-150,60)
        gg.end_fill()
        gg.right(90)
        gg.forward(50)
        gg.right(90)
        gg.circle(100,60)
        gg.color("green","green")
        gg.begin_fill()
        gg.circle(100,100)
        gg.right(90)
        gg.forward(50)
        gg.right(90)
        gg.circle(-150,100)
        gg.right(90)
        gg.forward(50)
        gg.end_fill()
        gg.right(90)
        gg.circle(100,100)
        gg.color("blue","blue")
        gg.begin_fill()
        gg.circle(100,25)
        gg.left(115)
        gg.forward(65)
        gg.right(90)
        gg.forward(42)
        gg.right(90)
        gg.forward(124)
        gg.right(90)
        gg.circle(-150,50)
        gg.right(90)
        gg.forward(50)
        gg.end_fill()
        
    google()
    turtle.done()

# GoogleLogo()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Cube():
    cube = turtle.Turtle()
    cube.forward(50)
    cube.right(90)
    cube.forward(50)
    cube.right(90)
    cube.forward(50)
    cube.right(90)
    cube.forward(50)
    cube.right(90)
    turtle.done()
# Cube()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Star():
    star = turtle.Turtle()
    for i in range(50):
        star.forward(50)
        star.right(144)
    turtle.done()
# Star()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def SpiralStar():
    spiral = turtle.Turtle()
    for i in range(20):
        spiral.forward(i * 10)
        spiral.right(144)
    turtle.done()
# SpiralStar()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def LineColor():
    painter = turtle.Turtle()
    painter.pencolor("blue")
    turtle.speed(0)
    for i in range(50):
        painter.forward(50)
        painter.left(123) # Let's go counterclockwise this time 
    painter.pencolor("red")
    for i in range(50):
        painter.forward(100)
        painter.left(123)
    turtle.done()
# LineColor()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def Dots():
    seurat = turtle.Turtle()
    dot_distance = 25
    width = 5
    height = 7
    seurat.penup()
    for y in range(height):
        for i in range(width):
            seurat.dot()
            seurat.forward(dot_distance)
        seurat.backward(dot_distance * width)
        seurat.right(90)
        seurat.forward(dot_distance)
        seurat.left(90)
    turtle.done()
# Dots()

#----------------------------------------------------------------------------------------------------------------------------------------------    

def NinjaSpiral():
    ninja = turtle.Turtle()
    ninja.speed(10)
    for i in range(180):
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        ninja.right(2)
    turtle.done()
# NinjaSpiral()

#----------------------------------------------------------------------------------------------------------------------------------------------    

N = 80
def f(x):
    return 3.9*x*(1-x)
def g(x):
    return 3.9*(x-x**2)
def h(x):
    return 3.9*x-3.9*x*x
def jumpto(x, y):
    penup(); goto(x,y)
def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)
def coosys():
    line(-1, 0, N+1, 0)
    line(0, -0.1, 0, 1.1)
def plot(fun, start, color):
    pencolor(color)
    x = start
    jumpto(0, x)
    pendown()
    dot(5)
    for i in range(N):
        x=fun(x)
        goto(i+1,x)
        dot(5)
def DotGraph():
    reset()
    setworldcoordinates(-1.0,-0.1, N+1, 1.1)
    speed(9)
    hideturtle()
    coosys()
    plot(f, 0.35, "blue")
    plot(g, 0.35, "green")
    plot(h, 0.35, "red")
    # Now zoom in:
    for s in range(100):
        setworldcoordinates(0.5*s,-0.1, N+1, 1.1)
    return "Done!"
# DotGraph()

#----------------------------------------------------------------------------------------------------------------------------------------
def Peace():
    speed(10)
    peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4"
            )
    reset()
    Screen()
    up()
    goto(-320,-195)
    width(70)
    for pcolor in peacecolors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)
    width(25)
    color("white")
    goto(0,-170)
    down()
    circle(170)
    left(90)
    forward(340)
    up()
    left(180)
    forward(170)
    right(45)
    down()
    forward(170)
    up()
    backward(170)
    left(90)
    down()
    forward(170)
    up()
    goto(0,300) # vanish if hideturtle() is not available ;-)
    return "Done!"
# Peace()

#----------------------------------------------------------------------------------------------------------------------------------------------    

G = 9

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()
class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a
## create compound yellow/blue turtleshape for planets
def SunEarth():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6,180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"orange")
    planetshape.addcomponent(m2,"blue")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)

    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")
    sun.color("yellow")
    sun.shapesize(1.8)
    sun.pu()
    earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)
    moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)
    gs.init()
    gs.start()
    return "Done!"
# SunEarth()

#----------------------------------------------------------------------------------------------------------------------------------------------    


class Block(Turtle):

    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(size * 1.5, 1.5, 2) # square-->rectangle
        self.fillcolor("black")
        self.st()

    def glow(self):
        self.fillcolor("red")

    def unglow(self):
        self.fillcolor("black")

    def __repr__(self):
        return "Block size: {0}".format(self.size)


class Shelf(list):

    def __init__(self, y):
        "create a shelf. y is y-position of first block"
        self.y = y
        self.x = -150

    def push(self, d):
        width, _, _ = d.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def _close_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

    def _open_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def pop(self, key):
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def insert(self, key, b):
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()

def isort(shelf):
    length = len(shelf)
    for i in range(1, length):
        hole = i
        while hole > 0 and shelf[i].size < shelf[hole - 1].size:
            hole = hole - 1
        shelf.insert(hole, shelf.pop(i))
    return

def ssort(shelf):
    length = len(shelf)
    for j in range(0, length - 1):
        imin = j
        for i in range(j + 1, length):
            if shelf[i].size < shelf[imin].size:
                imin = i
        if imin != j:
            shelf.insert(j, shelf.pop(imin))

def partition(shelf, left, right, pivot_index):
    pivot = shelf[pivot_index]
    shelf.insert(right, shelf.pop(pivot_index))
    store_index = left
    for i in range(left, right): # range is non-inclusive of ending value
        if shelf[i].size < pivot.size:
            shelf.insert(store_index, shelf.pop(i))
            store_index = store_index + 1
    shelf.insert(store_index, shelf.pop(right)) # move pivot to correct position
    return store_index

def qsort(shelf, left, right):
    if left < right:
        pivot_index = left
        pivot_new_index = partition(shelf, left, right, pivot_index)
        qsort(shelf, left, pivot_new_index - 1)
        qsort(shelf, pivot_new_index + 1, right)

def randomize():
    disable_keys()
    clear()
    target = list(range(10))
    random.shuffle(target)
    for i, t in enumerate(target):
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def show_text(text, line=0):
    line = 20 * line
    goto(0,-250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

def start_ssort():
    disable_keys()
    clear()
    show_text("Selection Sort")
    ssort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_isort():
    disable_keys()
    clear()
    show_text("Insertion Sort")
    isort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_qsort():
    disable_keys()
    clear()
    show_text("Quicksort")
    qsort(s, 0, len(s) - 1)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def init_shelf():
    global s
    s = Shelf(-200)
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))

def disable_keys():
    onkey(None, "s")
    onkey(None, "i")
    onkey(None, "q")
    onkey(None, "r")

def enable_keys():
    onkey(start_isort, "i")
    onkey(start_ssort, "s")
    onkey(start_qsort, "q")
    onkey(randomize, "r")
    onkey(bye, "space")

def SortAlgorithm():
    getscreen().clearscreen()
    ht(); penup()
    init_shelf()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()
    listen()
    return "EVENTLOOP"
    done()
instructions1 = "press i for insertion sort, s for selection sort, q for quicksort"
instructions2 = "spacebar to quit, r to randomize"

# if __name__ == '__main__':
#     SortAlgorithm()
#     mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------

def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)
def YinYang():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"
# YinYang()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def Panda():
    pen = turtle.Turtle()
    def ring(col, rad):
        # Set the fill
        pen.fillcolor(col)
        #  filling the color
        pen.begin_fill()
        # circle
        pen.circle(rad)
        # Ending the filling of the color
        pen.end_fill()
    #  ears 
    #  first ear
    pen.up()
    pen.setpos(-35, 95)
    pen.down
    ring('black', 15)
    # second ear
    pen.up()
    pen.setpos(35, 95)
    pen.down()
    ring('black', 15)
    # face 
    pen.up()
    pen.setpos(0, 35)
    pen.down()
    ring('white', 40)
    # eyes black
    # first eye
    pen.up()
    pen.setpos(-18, 75)
    pen.down
    ring('black', 8)
    # second eye
    pen.up()
    pen.setpos(18, 75)
    pen.down()
    ring('black', 8)
    # eyes white 
    # first eye
    pen.up()
    pen.setpos(-18, 77)
    pen.down()
    ring('white', 4)
    # second eye
    pen.up()
    pen.setpos(18, 77)
    pen.down()
    ring('white', 4)
    #  nose 
    pen.up()
    pen.setpos(0, 55)
    pen.down
    ring('black', 5)
    # mouth
    pen.up()
    pen.setpos(0, 55)
    pen.down()
    pen.right(90)
    pen.circle(5, 180)
    pen.up()
    pen.setpos(0, 55)
    pen.down()
    pen.left(360)
    pen.circle(5, -180)
    pen.hideturtle()
# Panda()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def Graph():
    trtl=turtle.Turtle()
    trtl.speed(10)
    for i in range(0,400,20):
        trtl.pencolor('lightgrey')
        trtl.penup()
        trtl.setpos(-200+i,-200)
        if i==0:
            trtl.left(90)
        trtl.pendown()
        trtl.forward(400)
        trtl.backward(400)
    for i in range(0,400,20):
        trtl.pencolor('lightgrey')
        trtl.penup()
        trtl.setpos(-200,-200+i)
        if i==0:
            trtl.right(90)
        trtl.pendown()
        trtl.forward(400)
        trtl.backward(400) 
    trtl.penup()
    trtl.home()
    trtl.pendown()
    trtl.pencolor('black')
    trtl.backward(200)
    trtl.forward(400)
    trtl.backward(200)
    trtl.left(90)
    trtl.forward(200)
    trtl.backward(400)
    trtl.penup()
    trtl.setpos(5,5)
    trtl.pendown()
    trtl.write(0)
    trtl.penup()
    trtl.setpos(190,5)
    trtl.pendown()
    trtl.write("x")
    trtl.penup()
    trtl.setpos(5,190)
    trtl.pendown()
    trtl.write("y")
    trtl.penup()
    trtl.setpos(80,-180)
    trtl.pendown()
    trtl.write("Vivax Solutions")
    trtl.ht()
# Graph()