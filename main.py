#
# main.py
# Snake game
#
#  Created by OBOUNOU LEKOGO NGUIA Benaja Soren on 21/05/21.
#  Copyright © 2021 OBOUNOU LEKOGO NGUIA Benaja Soren. All rights reserved.
#



# We import  the square root function from the math module because we need it to calculate
# The distance between the snake head and the food
from food import Food
from turtle import Screen
import time
# import the Snake class from the snake module
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
# We set the screen  color mode to 255 such that we could use the rgb color
screen.colormode(255)
screen.setup(width=800,height=800)
# We set the screen background color to black
screen.bgcolor(0, 0, 0)
screen.title("Snake game")
# We set the screen tracer to 0 with the tracer() function
# This way the screen won't show the turtle animation
# in our case for example, the screen won't show how the segments move piece by piece
screen.tracer(0)

# Create a snake object
snake = Snake()

# Create a food object
food = Food()

# Create a scoreboard object
scoreboard = Scoreboard()

# Set focus on TurtleScreen (in order to collect key-events)
screen.listen()

# Use onkey() function to move the snake up if user touches the "Up" key
screen.onkey(snake.up,"Up")
# Use onkey() function  to move the snake down if user touches the "Down" key
screen.onkey(snake.down,"Down")
# Use onkey() function to move the snake left if user touches the "Left" key
screen.onkey(snake.left,"Left")
# Use onkey() function to move the snake right if usertouches the "Right" key
screen.onkey(snake.right,"Right")
screen.update()
# Create boolean variable that will determine if the game is still on
game_is_on = True




while game_is_on:
    # We use the update() method to refresh the screen and to immediately see our segments moved
    # without the animation they made to move themselves (piece by piece)
    screen.update()
    # Delay the execution of the next iteration ,such that the segments can be seen moving
    # We delay the next iteration's execution by (will wait for) 0.09 second
    time.sleep(0.09)
    # Make the snake object move
    snake.move()
    # Check if boundary has been touched
    if snake.head.xcor() == 380 or snake.head.xcor() == -380 or snake.head.ycor() == 380 or snake.head.ycor() == -380:
        # If snake head touched one of the screen limit
        # We display the game over message
        scoreboard.game_over()
        # We stop the game
        game_is_on = False  
    # Check if snake touched segment(body)
    elif snake.touched_segment() is True:
        # If snake touched body, user lost
        # We display the game over message
        scoreboard.game_over()
        # Set "game_is_on" boolean variable to False to stop the loop
        game_is_on = False
    # Check if snake ate food by checking that the distance between them is inferior to 20
    elif snake.head.distance(food) <= 15:
        # We activate the eat() function from the snake class
        snake.eat()
        # We change the position of the food
        food.set_food()
        scoreboard.update_score()
        # We set the value of snake_eaten boolean to True
        #snake_eaten = True
        print("JUST ATE")



    




     

screen.exitonclick()

