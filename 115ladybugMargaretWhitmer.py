#   a115_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()

# configure legs
legs = 6
leg_length = 70
turtle_direction = 360 / legs
ladybug.pensize(5)

# draw legs
loop_variable = 0
while (loop_variable < legs):
  ladybug.goto(0,-30)
  ladybug.setheading(turtle_direction*loop_variable)
  ladybug.forward(leg_length)
  loop_variable+=1

# create ladybug head and body
ladybug.up()
ladybug.goto(0,0)
ladybug.down()
ladybug.pensize(40)
ladybug.circle(5)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)


# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)

# # draw two sets of dots
while (num_dots < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots+=1

# position next dots
  xpos = xpos + 5
  xpos = ypos + 25
  num_dot = num_dots + 1





ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()