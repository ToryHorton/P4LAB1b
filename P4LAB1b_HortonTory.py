import turtle
win = turtle.Screen()
t = turtle.Turtle()
t.pencolor("pink")
t.pensize(3)

# for the letter T

t.forward(100)
t.right(90)
t.forward(170)
t.left(180)
t.forward(170)
t.right(90)
t.forward(100)
t.penup()
t.forward(10)
t.pendown()

# for the letter H

t.right(90)
t.forward(170)
t.right(180)
t.forward(85)
t.right(90)
t.forward(90)
t.right(90)
t.forward(85)
t.right(180)
t.forward(170)

win.mainloop()
