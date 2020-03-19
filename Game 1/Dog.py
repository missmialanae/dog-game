import turtle
import os

#Inspired by Space Invaders but not really 
#Made on Mac w/ Visual Studio

#Background
window = turtle.Screen()
window.bgcolor("white")

#can change to a picture using window.bgpic("name of pic here")

#Space for the Dog to thrive = border
border = turtle.Turtle()
border.speed(0)
border.color("black")

#this places the starting point of the pen at that location
border.penup()
border.setposition(-300, - 300)
border.pendown()
border.pensize(3)

#creates the actual square lines 
for i in range(4):
    border.forward(600)
    border.left(90)

#gets ride of the pen marker show you don't see it
border.hideturtle()

#Dog
dog = turtle.Turtle()
dog.color("green")
dog.shape("turtle")
dog.resizemode("auto")

#places the dog in a new spot on the game board 
dog.penup()

#this is animation speed but I am not entirely sure what it does
dog.speed(0)

#this places the dog at the end of the game board and allows 
dog.setposition(0,-250)

#Moving the Dog 

#this keeps the interval of the "number line"
dogspeed = 15

#dog moves left 
def moveLeft():
    #this takes the current location of the dog
    x = dog.xcor()

    #this takes the current value of x and subtracts dogs speed and assigns it to x
    x -= dogspeed
    
    #boundary checking
    if x < -280:
        x = - 280

    #set the dog to that x coordinate
    dog.setx(x)

#create the keybinding for left
turtle.listen()
turtle.onkey(moveLeft,"Left")

#dog moves right
def moveRight():
    #this is the current location of the dog 
    x = dog.xcor()

    #this takes the current value of x and subtracts it to the dog speed and assigns it to x 
    x += dogspeed
    #boundary checking
    if x > 280:
        x = 280

    #set the dog to that x coordinate
    dog.setx(x)

#create the keybinding for right
turtle.listen()
turtle.onkey(moveRight, "Right")

#note I would like the dog  to change directions when he turns a different direction when clicked 

#falling objects - I think I want them to be fish
#create a turtle objects kind of how you created the dog
#object movements 

#Delay 
delay = input("Press Enter to End Game")