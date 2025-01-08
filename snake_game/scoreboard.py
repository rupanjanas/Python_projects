from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()


    #def game_over(self):
      #  self.goto(0,0)
      #  self.write("Game over",align="center",font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score+=1

        self.update_scoreboard()
