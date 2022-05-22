from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# TODO - 1 Set up screen, bgcolor
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
# TODO - 2 Set tracer method to turn off the animation and explicitly call update method for the screen to refresh
#  and code to work
"""https://stackoverflow.com/questions/62613041/what-does-turtle-tracer-do 
   the tracer method have delay at 15 rate. 0 is for off, 1 is for on. Just 
   like CRT TV, gif Image it passes the bunch images to create a video"""
screen.tracer(0, 15)

snake = Snake()
# TODO - 8 Calling food object
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
"""screen.update() called here gives an output of snake segments but not the rest of the code
    Inside while and for loop below, make snake segments to move block wise
    Inside while loop outside for loop, make snake segment in a piece"""
"""time.sleep() will delay the speed of the result"""
# screen.update()

# TODO - 5 while loop for calling move method on snake object
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # TODO - 9 to detect the collision of food with snake
    #  "https://docs.python.org/3/library/turtle.html#turtle.distance"
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()
    # TODO - 16 Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.gameover()
        # TODO - 22 reset calling from scoreboard and snake
        scoreboard.reset()
        snake.reset_snake()
    # TODO - 17 Detecting collision with body
    for segment in snake.segments[1:]:  # snake head colliding with itself at first position so [1:]
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.gameover()
            scoreboard.reset()
            snake.reset_snake()

    # print(scoreboard.score)
screen.exitonclick()
