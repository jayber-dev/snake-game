import turtle
import snake

class Score():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.high_score_pen = turtle.Turtle()
        self.high_score_pen.color("white")
        self.high_score_pen.penup()
        self.high_score_pen.hideturtle()
        self.score = 0
        self.high_score = 0
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(x = -100, y = 280)
        self.pen.write(f"score is : ", font=18)
        
    
    def score_count(self):
        self.score +=1
        
    def score_display(self):
        self.pen.clear()
        self.pen.goto(x = -100, y = 280)
        self.pen.write(f"score is : {self.score}", font=18)

    def high_score_check(self):
                
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("high_score.txt", mode="w")
            file.write(str(self.high_score))
            file.close()
            
       

    def display_high_score(self):
        file = open("high_score.txt", mode="r")
        self.saved_high_score =  file.read()
        file.close()
        self.high_score_pen.clear()
        self.high_score_pen.setposition(50,280)
        self.high_score_pen.write(f"high score : {self.saved_high_score}", font=18)
        self.high_score = int(self.saved_high_score)
    
        

    