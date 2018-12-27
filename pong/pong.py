import turtle
import winsound

win = turtle.Screen()
win.title("Pong by _dy")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

#Score
score_a = 0
score_b = 0
#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)           #speed of the animation of the paddle moving across
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(0,280)
paddle_a.shapesize(stretch_wid= 1, stretch_len = 5)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)           #speed of the animation of the paddle moving across
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(0,-280)
paddle_b.shapesize(stretch_wid= 1, stretch_len = 5)

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.goto(0,0)
ball.penup()
ball.speed(0)
ball.dx = 0.25
ball.dy = 0.25
 
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,0)
pen.write("Blue : 0  Red :0",align="center", font= ("courier",24,"normal"))


#Functions for moving paddles
def paddle_a_right():
    x = paddle_a.xcor()
    x +=20
    paddle_a.setx(x)

def paddle_a_left():
    x = paddle_a.xcor()
    x -=20
    paddle_a.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x +=20
    paddle_b.setx(x)

def paddle_b_left():
    x = paddle_b.xcor()
    x -=20
    paddle_b.setx(x)

#Keyboard binding
win.listen()
win.onkeypress(paddle_a_right,"Right")
win.onkeypress(paddle_a_left,"Left")
win.onkeypress(paddle_b_left,"a")
win.onkeypress(paddle_b_right,"d")


#Main game loop

while True:
    win.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        winsound.PlaySound("wall.wav",winsound.SND_ASYNC)
    
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        winsound.PlaySound("wall.wav",winsound.SND_ASYNC)

    if ball.ycor() > 290:
        ball.goto(0,0)
        ball.dy *= -1
        score_b +=1
        pen.clear()
        pen.write("Blue : {}  Red :{}".format(score_a,score_b),align="center", font= ("courier",24,"normal"))
        winsound.PlaySound("miss.wav",winsound.SND_ASYNC)
            
    if ball.ycor() < -290:
        ball.goto(0,0)
        ball.dy *= -1
        score_a +=1
        pen.clear()
        pen.write("Blue : {}  Red :{}".format(score_a,score_b),align="center", font= ("courier",24,"normal"))
        winsound.PlaySound("miss.wav",winsound.SND_ASYNC)

    #collision with paddles
    if ball.ycor() > 260 and (ball.xcor()< paddle_a.xcor()+ 40 and ball.xcor() > paddle_a.xcor() - 40):
        ball.dy *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor() < -260 and (ball.xcor()< paddle_b.xcor()+ 40 and ball.xcor() > paddle_b.xcor() - 40):
        ball.dy *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)