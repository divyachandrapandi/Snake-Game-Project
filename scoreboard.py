from turtle import Turtle

X = 0
Y = 270
ALIGNMENT = 'center'
FONT = ("Verdana", 15, "normal")


# TODO - 10  creating scoreboard inherited from turtle class

class Scoreboard(Turtle):
    def __init__(self, score=0):
        super().__init__()
        # TODO - 11 score variable as attribute of scoreboard class
        self.score = 0
        with open("highscore.txt") as file:
            highscore = file.read()
            self.highscore = int(highscore)
        self.color("white")
        self.penup()
        self.setpos(X, Y)
        self.write(f"score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    # TODO -18 To update scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    # TODO - 13 create gameover using write
#     def gameover(self):
#         self.goto (0,0)
#         self.write("GAME OVER", align='center', font=("Verdana", 15, "normal"))

    # TODO - 20 to reset the score to zero and to update high score
    def reset(self):

        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode = "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # TODO - 19 function to increase the score
    def increase_score(self):
        """https://docs.python.org/3/library/turtle.html#turtle.write"""
        self.score += 1
        self.update_scoreboard()