from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("plum")
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.score = 0
        self.high_score = self.show_high_score()
        self.update_score()
        self.show_high_score()


    def update_high_score(self):
        with open("data.txt", mode="r") as new_high_score:
            contents = new_high_score.read()
            if self.high_score > int(contents):
                with open("data.txt", mode="w") as highest_score:
                    highest_score.write(f"{self.high_score}")

    def show_high_score(self):
        with open("data.txt") as show_score:
            high_score = show_score.read()
            return int(high_score)


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Futura', 26, 'normal'))



    # def game_over(self): #taking this out to update game and show high score
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER", align="center", font=('Futura', 40, 'bold'))

    def add_point(self):
        self.score += 1
        self.update_score()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.update_score()
            self.update_high_score()





