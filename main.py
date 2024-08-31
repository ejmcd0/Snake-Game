# from turtle import Turtle, Screen
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# x_coordinates = [0, -20, -40]
# snake_body = []
# screen.listen()
# game_on = True
# screen.tracer(0)
#
# def turn_left():
#     snake_body[0].left(90)
#
# def turn_right():
#     snake_body[0].right(90)
#
#
# for new_snake in range(3):
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(x= x_coordinates[new_snake], y= 0)
#     snake_body.append(snake)
# timer = True
#
#
# while game_on:
#     screen.update() #updates the screen after each segment is looped through
#     time.sleep(0.1) #slows down time by 0.1 seconds
#     screen.onkey(key="Left", fun=turn_left)
#     screen.onkey(key="Right", fun=turn_right)
#
#     if snake_body[0].xcor() > 260 or snake_body[0].xcor() < -260:
#         game_on = False
#         timer = False
#     elif snake_body[0].ycor() > 260 or snake_body[0].ycor() < -260:
#         game_on = False
#         timer = False
#     for segment in range(len(snake_body)-1, 0, -1): #(start, stop, step)
#         new_x = snake_body[segment - 1].xcor()
#         new_y = snake_body[segment - 1].ycor()
#         snake_body[segment].goto(new_x, new_y)
#     snake_body[0].forward(20)
#
#
#
#
############# turning everything above into snake Class
#
#
#
#
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_point()
        snake.extend_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    for segment in snake.snake_body[1:]:
    #slices snake_body and loops through the list starting at position 1 instead of position 0
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    snake.move()
screen.exitonclick()