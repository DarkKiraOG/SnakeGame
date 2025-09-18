from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color(["white", "seagreen2", "seagreen1"][STARTING_POSITIONS.index(pos)])
            segment.goto(pos)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.segments[0].forward(20)

    def right(self):
        if self.segments[0].heading() == 180:
            return
        self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() == 0:
            return
        self.segments[0].setheading(180)

    def up(self):
        if self.segments[0].heading() == 270:
            return
        self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() == 90:
            return
        self.segments[0].setheading(270)

    def grow(self):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        self.segments.append(segment)

    def body_hit(self):

        return False
