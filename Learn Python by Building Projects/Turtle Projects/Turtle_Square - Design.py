import turtle

#Create Turtle
my_turtle = turtle.Turtle()

#Objective: Create a circle with the squares created in turtle

#Create Turtle
my_turtle = turtle.Turtle()
#Speed Up Turtle
my_turtle.speed(0)

#Function
def square(length):
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)
    my_turtle.left(90)
    my_turtle.forward(length)
    my_turtle.left(90)

a = 10
#Loop
for circle in range(200):
    square(a)
    a = a + 2
    my_turtle.left(8)