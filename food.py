from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        #inherits everything from the superclass Turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        #instead of being a 20x20 square, it will now be a 10x10 circle
        self.color("lawngreen")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
