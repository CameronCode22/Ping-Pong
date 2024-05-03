import turtle

#setting up screen and game
screen = turtle.getscreen()
screen = turtle.Screen()
screen.title("DataFlair Pong game")
screen.setup(width=1000 , height=600)
paddle1 = turtle.Turtle()
paddle2 = turtle.Turtle()
ball = turtle.Turtle()
turtle.bgcolor("black")

#defining baton player 1
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(6,2)
paddle1.penup()
#paddle, go to the left
paddle1.goto(-400,0)

#defining baton player 1
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(6,2)
paddle2.penup()
#paddle, go to the left
paddle2.goto(400,0)

#ball
ball.shape("circle")
ball.color("white")
ball.penup()

#ball starts from the centre of screen each loop cycle
ball.goto(0, 0)

#setting dx and dy that decide the speed of the ball
ball.dx = 2
ball.dy = -2

#intializing the scores of both players
player1 = 0
player2 = 0

#displaying the score
score = turtle.Turtle()
score.speed(0)
score.penup()
#hiding the turtle to show text
score.hideturtle()
score.color("white")
#locating the scoreboard on top of screen
score.goto(0,260)

score.write("Player1 : 0 Player2: 0", align="center", font=("Courier", 20, "bold"))

#move paddle 1 up and down functions
def move_paddle1_up():
    y = paddle1.ycor()
    y += 15
    paddle1.sety(y)

def move_paddle1_down():
    y = paddle1.ycor()
    y -= 15
    paddle1.sety(y)

#move paddle 2 up and down functions
def move_paddle2_up():
    y = paddle2.ycor()
    y += 15
    paddle2.sety(y)

def move_paddle2_down():
    y = paddle2.ycor()
    y -= 15
    paddle2.sety(y)

#matching the keyboard buttons to function
screen.listen()
screen.onkeypress(move_paddle1_up, "Left")
screen.onkeypress(move_paddle1_down, "Right")
screen.onkeypress(move_paddle2_up, "Up")
screen.onkeypress(move_paddle2_down, "Down")

while True:
    #update the screen each loop
    screen.update()

    #moving the ball by updating the coordinates
    #works by using the velocity ball.dx/dy
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1 #bouncing the ball, multiplying by -1 to bounce
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        
    if ball.xcor() > 480 or ball.xcor() < -480:
        if ball.xcor() < -480:
            player2 += 1
        else:
            player1 += 1
        #reset ball position
        ball.goto(0,0)

        #reset ball velocity
        ball.dx = 2
        ball.dy = -2

        #reversing direction, will now head to the winner first
        ball.dx *= -1
        ball.dy *= -1

        #update the score board
        score.clear()
        score.write("Player1 : {} Player2 : {}".format(player1,player2), align ="center", font=("Courier", 20, "bold"))


        #checking if the left paddle hits the ball
    if (ball.xcor() < -380 and ball.xcor() > -400) and (paddle1.ycor()+ 50 > ball.ycor() > paddle1.ycor() -50):
        #if (ball.xcor() < -380 and ball.xcor() >-400):
        #increasing the score of the left player       
        #player1 += 1
        #score.clear()
        #score.write("Player A: {} PLayer B: {}".format(player1, player2), align= "center", font=("Courier", 20, "bold"))
        ball.setx(-360)

        #increase the speed of the ball, limit 7
        if (ball.dy>0 and ball.dy<5):
            #if dy is positive increase by
            ball.dy +=0.5
        elif (ball.dy<0 and ball.dy >-5):
            #if dy is negative increase by
            ball.dy -=0.5
        #Increasing speed of the ball X
        if(ball.dx > 0 and ball.dx <7):
            ball.dx+=1
        elif(ball.dx < 0 and ball.dx >-7):
            ball.dx-=1        
            
        #change direction of ball towards right player
        ball.dx *=-1

        #checking if the right player hit the ball

    if(ball.xcor() > 380 and ball.xcor() < 400 and paddle2.ycor()+50 > ball.ycor()>paddle2.ycor()-50):
        #player2 += 1
        #score.clear()
        #score.write("Player A: {} PLayer B: {}".format(player1, player2), align= "center", font=("Courier", 20, "bold"))
        ball.setx(360)

        #increasing speed of ball Y
        if(ball.dy > 0 and ball.dy<7):
            ball.dy+=1
        elif(ball.dy < 0 and ball.dy >-7):
            ball.dy-=1
        #Increasing speed of the ball X
        if(ball.dx > 0 and ball.dx <7):
            ball.dx+=1
        elif(ball.dx < 0 and ball.dx >-7):
            ball.dx-=1


        ball.dx *=-1
    print("ball x veloc", ball.dx)
    print("ball y veloc",ball.dy)

turtle.mainloop()