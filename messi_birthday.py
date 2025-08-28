import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Messi Birthday Dribble for Priyanshu Chote")
screen.bgcolor("green")
screen.setup(width=800, height=600)

# Messi
messi = turtle.Turtle()
messi.shape("circle")
messi.color("blue")
messi.penup()
messi.goto(-350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(-360, -10)

# Players
def create_defender(x, y):
    d = turtle.Turtle()
    d.shape("square")
    d.color("red")
    d.shapesize(stretch_wid=2, stretch_len=1)
    d.penup()
    d.goto(x, y)
    return d

defenders = [
    create_defender(-150, 30),
    create_defender(0, -30),
    create_defender(150, 20)
]

# Goalpost
goal = turtle.Turtle()
goal.color("yellow")
goal.pensize(5)
goal.penup()
goal.goto(300, -100)
goal.pendown()
goal.goto(300, 100)

# Message
message = turtle.Turtle()
message.hideturtle()
message.color("white")
message.penup()

# Messi dribble and goal animation
steps = [(-300, 0), (-200, 10), (-150, 30), (-100, 0), (0, -30), (50, 10), (100, 0), (150, 20), (200, 10), (280, 0)]
for x, y in steps:
    messi.goto(x, y)
    ball.goto(x - 10, y - 10)
    time.sleep(0.3)

# Goal celebration
for _ in range(3):
    messi.color("yellow")
    ball.color("blue")
    time.sleep(0.2)
    messi.color("blue")
    ball.color("white")
    time.sleep(0.2)

# Show birthday message
message.goto(0, 200)
message.write("Happy Birthday Priyanshu Chote!!", align="center", font=("Arial", 24, "bold"))

# Keep the window open
turtle.done()
