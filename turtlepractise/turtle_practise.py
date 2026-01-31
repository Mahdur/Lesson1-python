import turtle

screen = turtle.Screen()
screen.bgcolor("lime")
screen.setup(1000, 1000)

polygon = turtle.Turtle()

num_sides = 4
side_length1 = 20
side_length2 = 80
angle = 360 / num_sides

for i in range(num_sides):
    polygon.forward(side_length1)
    polygon.right(angle)
    polygon.forward(side_length2)
    polygon.right(angle)
    
    
    

turtle.done()
