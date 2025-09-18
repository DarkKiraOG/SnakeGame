from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        data = open("Data.txt", mode = "r")
        contents = data.read()
        self.highscore = int(contents)

        self.color("white")
        self.penup()

        self.hideturtle()
        self.update_scorecard()
        data.close()
    def update_scorecard(self ):
        self.goto(0, 270)
        self.write(f"Score : {self.score}",align = ALIGNMENT, font = FONT )
        self.goto(0, 240)
        self.write(f"High Score : {self.highscore}", align=ALIGNMENT, font=FONT)


    def gameover(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorecard()