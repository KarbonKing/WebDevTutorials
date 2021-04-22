import turtle

#Create Turtle
my_turtle = turtle.Turtle()

#Functions
def square(length, angle):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)

def turn():
    my_turtle.left(10)

#Loop
for sqr in range(50):
    square(200,90)
    turn()




#square(200,90)
#forward()
#square(200,90)
#forward()
#square(200,90)
#forward()