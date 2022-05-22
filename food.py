from turtle import Turtle
import random

# TODO - 6 create a food class inherited from Turtle class, TIP:"each time calling food object, init method initialised"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        """"https://docs.python.org/3/library/turtle.html#turtle.shapesize"""
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
# TODO - 7 Refresh method generates random x, y
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)