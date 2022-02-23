import turtle
import random

screen = turtle.Screen()
init_color_list = ("red","green","blue")
color_list = ("yellow","brown","DeepPink1","DarkOrange","cyan","BlueViolet","coral2","aquamarine","azure","DeepSkyBlue")

class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.init_position = ((0, 0), (-20, 0), (-40, 0))
        self.i = 0
        self.segments = []
        self.snake_creating()
        self.move()
        
        

    def snake_creating(self): # initial snake creation
        for seg in self.init_position:
            self.new_segment = turtle.Turtle("square")
            self.new_segment.speed("fastest")
            self.new_segment.penup()
            self.new_segment.color(init_color_list[self.i])
            self.new_segment.goto(seg)
            self.segments.append(self.new_segment)
            self.i += 1

    def move(self): # movment of snake
        def turn_left():
            self.segments[0].left(90)

        def turn_right():
            self.segments[0].right(90)

        screen.listen()
        screen.onkey(fun=turn_right, key="Right")
        screen.onkey(fun=turn_left, key="Left")


        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.segments[0].forward(20)

    def snake_segment_add(self): # adding a new segment to snake call from main
        self.new_segment = turtle.Turtle("square")        
        self.new_segment.penup()
        self.new_segment.color(random.choice(color_list))
        self.segments.append(self.new_segment)

    def snake_position(self): # returns snake position x and y seperated
        self.current_x = self.segments[0].xcor()
        self.current_y = self.segments[0].ycor()
        return self.current_x, self.current_y

    def snake_run_cheack(self): # checks hiting it self and hitting in borders returns True or False
        if self.segments[0].xcor() > 280 or self.segments[0].xcor() < -280:
            return False
        if self.segments[0].ycor() > 280 or self.segments[0].ycor() < -280:
            return False
        for i in range(len(self.segments)- 1 ):
            i += 1
            self.head = self.segments[0].position()
            if  self.segments[i].distance(self.head) < 10:
                
                return False 
            
        