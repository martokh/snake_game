from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.speed("fastest")
        self.stem = Turtle()
        self.stem.hideturtle()
        self.stem.penup()
        self.stem.shape("square")
        self.stem.shapesize(stretch_len=0.2, stretch_wid=0.5)
        self.stem.color("green")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-190, 190)
        self.goto(random_x, random_y)
        # Move the stem just above the apple
        self.stem.goto(random_x, random_y + 13)
        self.stem.showturtle()