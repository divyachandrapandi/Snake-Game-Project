from turtle import Turtle

# TODO - 3  To create snake class
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # TODO - 15 adding all segment added to create a snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # TODO -14 To separate functionality 'adding segment' and 'create_snake' as different functions
    def add_segment(self, position):
        """add_segment{3} using square turtle object in a row and appended to a list"""
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setpos(position)
        self.segments.append(snake)

    # TODO -21 reset snake to start position and send dead snake away from screen
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)  # Dragging out of the screen, the dead snake
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # TODO - 16 extending the segment and added to snake
    def extent(self):
        self.add_segment(self.segments[-1].position())

    # TODO - 4 define function for move forward
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            """range(start = len(segments) -1 ,end =  0 ,step = -1)
            len(segment) is 3 but range should be range(2,0,1) so sub one"""
            """movement of snake:
                        last segment to second segment
                        second segment to first segment
                        first segment to a new position moving forward"""
            # screen.update()
            new_x = self.segments[seg - 1].xcor()  # x coordinate of second segment
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)  # assigned to last segment
        self.head.forward(MOVE_DISTANCE)  # first segment moves forward with second, third in its previous position

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
