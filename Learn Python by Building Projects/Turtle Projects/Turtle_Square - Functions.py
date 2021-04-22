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

def forward():
    my_turtle.forward(100)

#Actions
for sqr in range(6):
    square(200,90)
    forward()



#square(200,90)
#forward()
#square(200,90)
#forward()
#square(200,90)
#forward()