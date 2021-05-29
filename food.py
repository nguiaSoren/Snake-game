#
# food.py
# Snake game
#
#  Created by OBOUNOU LEKOGO NGUIA Benaja Soren on 21/05/21.
#  Copyright © 2021 OBOUNOU LEKOGO NGUIA Benaja Soren. All rights reserved.
#




from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        # We set the color of this turtle object to red
        self.color(255, 0, 0)
        # We use the penup() function such that the turtle object doesn't draw
        self.penup()
        # We stretch the size, it it was 0.5 at the place of 0.65, it would be half
        self.shapesize(stretch_len=0.65,stretch_wid=0.65)
        self.set_food()


    def set_food(self):
        """
        Change food coordinates
        """
        # We create random coordinates in our orthonormal graph using the randint() function
        random_x, random_y = randint(-370,370), randint(-370,370) 
        # We set the position if our meal using the randomnly generated coordinates
        self.setpos(random_x,random_y)
    
