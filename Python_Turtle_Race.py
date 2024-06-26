import turtle
import random

die = [1,2,3,4,5,6]

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

s = turtle.getscreen()

for i in range(20):
    if player_one.pos() >= (300,100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300,-100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(die_outcome * 20)
        player_two_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.fd(die_outcome * 20)
turtle.mainloop()