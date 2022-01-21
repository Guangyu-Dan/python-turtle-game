from turtle import Screen, Turtle
from my_turtle import My_turtle
from level_board import Levelboard
import time
import numpy as np
import random
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Trutle crossing")
screen.tracer(0)
my_turtle = My_turtle()
my_turtle.reset_position()
my_turtle.reset_orientation()

levelboard = Levelboard()
game_is_on = True
reset = True
level = 0
speed = list(range(10,30,2))

generate_block_prob =  np.linspace(0.1,0.2,10)

while game_is_on:
    if reset:
        blocks = []
        my_turtle.reset_position()
        screen.listen()
        screen.onkey(my_turtle.move, "Up")
        levelboard.update_scoreboard()
        reset = False
    screen.update()
    time.sleep(0.05)
    if random.uniform(0, 1) < generate_block_prob[level]:
        new_block = Turtle()
        new_block.color("white")
        new_block.shape("square")
        new_block.shapesize(stretch_wid=1, stretch_len=3)
        new_block.penup()
        new_block.goto((400, random.randint(-10,13) * 20))
        new_block.left(180)
        blocks.append(new_block)
    for block in blocks:
        block.forward(speed[level])
        if block.distance(my_turtle) < 20:
            game_is_on = False
    if blocks and blocks[0].xcor() < -500: blocks = blocks[1:]
    if my_turtle.ycor()>=280:
        for block in blocks: block.hideturtle()
        reset = True
        level += 1
        levelboard.level = level
        if level == len(speed):
            game_is_on = False


if not game_is_on:
    game_over = Turtle()
    game_over.color("red")
    game_over.penup()
    game_over.hideturtle()
    game_over.goto(0,0)
    game_over.write('game over', align="center", font=("Courier", 80, "normal"))



screen.exitonclick()