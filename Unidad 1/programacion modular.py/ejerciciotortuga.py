import turtle

def pintalinea(color,largo,x,y): 
    turtle.goto(x,y)
    for i in range(4):           #cuadrado
        turtle.color(color)
        turtle.forward(largo)
        turtle.right(90)

pintalinea("green", 150,0,0)
pintalinea("blue", 150,200,200)
pintalinea("yellow", 150,-200,-200)

turtle.hideturtle()
turtle.done()

#estrella
#puntas= input("Dame un número del 3 al 7: ")

