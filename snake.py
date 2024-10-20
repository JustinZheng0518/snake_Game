from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segment[-1].position())

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.setposition(position)
        snake_segment.color("white")
        self.segment.append(snake_segment)
        snake_segment.penup()

    def reset(self):
        for seg in self.segment:
            seg.goto(1000000, 1000000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)


