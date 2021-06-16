import turtle

# Game window Design
wind = turtle.Screen()
wind.title('My First Game Code')
wind.bgcolor('blue')
wind.setup(width=800, height=600)
wind.tracer(0) # window not automatically updated

# madrab1 design
madrab1 = turtle.Turtle() #initialize turtle object (shape)
madrab1.speed(0) # سرعة رسم الشكل على الشاشة وليس سرعة حركة الشكل
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.shape('square')
madrab1.color('white')
madrab1.penup()
madrab1.goto(-350, 0)

# madrab2 Design
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.shape('square')
madrab2.color('white')
madrab2.penup()
madrab2.goto(350, 0)

# ball Design
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.40
ball.dy = 0.40

# Score showing
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color('yellow')
score.hideturtle()
score.penup()
score.goto(0, 260)
score.write('Hadeer: 0 Joud: 0', align='center', font=('courier', 18, 'normal'))

# Functions
# up and down movements for madrab1
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)
# keyboard bindings for move-uo
wind.listen()
wind.onkeypress(madrab1_up, 'w')

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)
# keyboard bindings for move-down
wind.listen()
wind.onkeypress(madrab1_down, 's')

# up and down movements for madrab2
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
# keyboard bindings for move-uo
wind.listen()
wind.onkeypress(madrab2_up, 'Up')

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)
# keyboard bindings for move-down
wind.listen()
wind.onkeypress(madrab2_down, 'Down')



# The Game main Function
while True:
    wind.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

   # Window border check
    # Top and Bottom borders on Y coordinate (axis)
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    # Right and left borders on X coordinate
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        # Scoring if out from the right
        score1 += 1
        score.clear()
        score.write('Hadeer: {} Joud: {}'.format(score1, score2), align='center', font=('courier', 18, 'normal'))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        # Scoring if out from the left
        score2 += 1
        score.clear()
        score.write('Hadeer: {} Joud: {}'.format(score1, score2), align='center', font=('courier', 18, 'normal'))

    # التصادم مع المضارب (صد الكرة باستخدام المضارب)
    if (ball.xcor() > 340 and ball.xcor() > 350 and ball.ycor() < madrab2.ycor() +40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350 and ball.ycor() < madrab1.ycor() +40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1






