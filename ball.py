from turtle import Turtle
from random import randint
class Ball(Turtle):
     def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white" )
        self.penup()
        self.x=10
        self.y=10


     def ball_moves(self):
         new_X= self.xcor()+self.x
         new_y= self.ycor()+self.y
         self.goto(new_X,new_y)

     def wall_bounce(self):
         self.y *= -1
         
     def paddle_bounce(self):
         self.x *= -1


     def reset_ball(self):
         self.goto(0,0)    

     

         
