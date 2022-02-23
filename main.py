import turtle
import time
from snake import Snake
from food import Food
import score
# general declarations -------------------------------------------------------------------------------------------------

screen = turtle.Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
game_is_on = True
snake = Snake()
food = Food()
food.new_dot()
score = score.Score()
edge = turtle.Turtle()

# screen edges ---------------------------------------------------------------------------------------------------------

edge = turtle.Turtle()
edge.color("white")
edge.penup()
edge.goto(-300,300)
edge.pendown()
edge.hideturtle()
edge.goto(300,300)
edge.goto(300,-300)
edge.goto(-300,-300)
edge.goto(-300,300)
# program code ---------------------------------------------------------------------------------------------------------

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    score.display_high_score()
    score.high_score_check()
    
    if snake.snake_run_cheack() == False:
        for pos in range(len(snake.segments)):
            snake.segments[pos].setposition(2000,2000)
        
        score.score = 0
        score.score_display()
        snake = Snake()
        
        

    if snake.segments[0].distance(food) < 15: # score system and new dot creating snake segment add
        score.score_count()
        score.display_high_score()
        score.score_display()
        food.new_dot()
        snake.snake_segment_add()
    
    
screen.exitonclick()
