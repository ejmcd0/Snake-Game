from turtle import Turtle, Screen

STARTING_POS = [(0,0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        #self.tail = self.snake_body[segment]


    def create_snake(self):
        for new_snake in STARTING_POS:
            self.plus_one(new_snake)

            # snake = Turtle(shape="square")
            # snake.color("white")
            # snake.penup()
            # snake.goto(x=X_COORDINATES[new_snake], y=0)
            # self.snake_body.append(snake)

    def plus_one(self, new_snake):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(new_snake)
        self.snake_body.append(snake)

    def extend_snake(self):
        self.plus_one(self.snake_body[-1].position())
    def move(self):
        for segment in range(len(self.snake_body)-1, 0, -1): #(start, stop, step)
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for piece in self.snake_body:
            piece.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]




    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




