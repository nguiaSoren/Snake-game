#
# snake.py
# Snake game
#
#  Created by OBOUNOU LEKOGO NGUIA Benaja Soren on 21/05/21.
#  Copyright © 2021 OBOUNOU LEKOGO NGUIA Benaja Soren. All rights reserved.
#

from turtle import Turtle

# We write it in upper case because it is a constant
MOVE_DISTANCE = 20
# 90 degrees corresponds to the north(up)
UP = 90
# 270 degrees corresponds to the south(down) 
DOWN = 270
# 180 degrees corresponds to the east(left) 
LEFT = 180
# 0 degree corresponds to the west(right) 
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        # We create a list for the segment
        self.segments = []
        self.initial_positionX = 0
        # When we initialize the snake, we also create it
        self.create_snake()
        # Since the first segment is the one leading, create attribute head for this
        self.head = self.segments[0]

    def create_snake(self):
        # Use a for loop to create 3 differents segments following each other
        for _ in range(3):
            # We create a turtle object whose shape is square
            segment = Turtle(shape="square")
            # We set the color of this turtlee object to white
            segment.color(255, 255, 255)
            # We use the penup() function such that the segment doesn't draw anything
            segment.penup()
            # We make the turtle object go to the "initial_positionX" variable
            segment.goto(x=self.initial_positionX,y=0)
            # Update the "initial_positionX" by doing the difference by 20, since every turtle default size
            # is 20. This way, the positionX will always be behind the previous turtle
            self.initial_positionX -= 20
            self.segments.append(segment)


    def move(self):
        # In order that the three segments (all segment) move in the same direction, no matter the direction
        # up,down,left,right, we need to move the actual segment at the position of the precedent one
        # Except the first one(leading one) that we will move(forward,up,etc) according to the user 
        # ...... SEGMENT 5 ---- SEGMENT 4 ---- SEGMENT 3 ----- SEGMENT 2 ---- SEGMENT 1 ---- SEGMENT 0
        # We use a for loop to go in descending order through each number(index)
        # if a segments list has 3 elements , segments = [segment,segment,segment], then
        # range(start = 2, end = 0, step = 1), as usual the end is excluded
        for seg_num in range(len(self.segments)-1,0,-1):
            # store actual segment's precedent segment's coordinates in variable 
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            # Move the segment corresponding to the segment number at the position
            # of the segment that precedes it
            self.segments[seg_num].goto(new_x,new_y)
        # When done with the for loop , simply move the first segment in the current direction
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # In the official snake game we can't move in opposite direction, so we use an if statement
        if self.head.heading() != DOWN:
            # Set the orientation of the turtle to 90 degrees which corresponds to the north(up) 
            self.head.setheading(UP)
        # Since the snake will always be moving in our main code,
        # we don't need to call the move() method 


    def down(self):
        # In the official snake game we can't move in opposite direction, so we use an if statement
        if self.head.heading() != UP:
            # Set the orientation of the turtle to DOWN 
            self.head.setheading(DOWN)
    
    def right(self):
        # In the official snake game we can't move in opposite direction, so we use an if statement
        if self.head.heading() != LEFT:
            # Set the orientation of the turtle to RIGHT
            self.head.setheading(RIGHT)
    
    def left(self):
        # In the official snake game we can't move in opposite direction, so we use an if statement
        if self.head.heading() != RIGHT:
            # Set the orientation of the turtle to LEFT
            self.head.setheading(LEFT)
        
    def eat(self):
        # We create a new_segment that we will add to the snake if he ate
        new_segment = Turtle(shape="square")
        # We set the color of this turtlee object to white
        new_segment.color(255, 255, 255)
        # We use the penup() function such that the new_segment doesn't draw anything
        new_segment.penup()
        # Set the same position as the last segment(anyway, it will be updated later)
        new_segment.setposition(self.segments[-1].pos())
        # Add new segment to our list
        self.segments.append(new_segment)


    def touched_segment(self):
        """
        check if snake_head touched one of the segments
        """
        for segment in self.segments[1:]:
            # Do a for loop to check for every segment except the head
            if self.head.distance(segment.pos()) < 10:
                # If the distance is less than 10, it means that it touched, we stop the game
                return True


           


  



            

        
        
        
        
        
 
 
