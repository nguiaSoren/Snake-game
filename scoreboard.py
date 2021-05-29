from turtle import Turtle

FONT = ("Arial", 24, "normal")
#
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Set initials score to 0
        self.score = 0
        # Set colot to white
        self.color("white")
        # Hide the turtle, we wonly want to see the text
        self.hideturtle()
        # Do not draaw when the turtle will move
        self.penup()
        # Move the turtle to the top
        self.goto(0,370)
        # Write initial score
        self.write(arg = f"Score: {self.score}", align="center", font=FONT)
        
    
    def update_score(self):
        "Update current score"
        # Clear the screen (erase the writings and drawings)
        self.clear()
        # Update the score attribute
        self.score += 1
        # Write the new text with the new score
        self.write(arg = f"Score: {self.score}", align="center", font=FONT)
    
    def game_over(self):
        "Show game over message"
        # Show game over message at the center of the screen
        self.goto(0,0)
        self.write(arg = "Game Over", align="center", font=FONT)