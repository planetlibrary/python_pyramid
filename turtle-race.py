import turtle as t
from random import randint

class TurtleRace:
    def __init__(self):
        self.setup_track()
        self.setup_players()

    def setup_track(self):
        t.bgcolor("white")
        t.speed(0)
        t.penup()
        t.goto(-140, 140)
        for step in range(15):
            self.write(step)
            t.right(90)
            for num in range(8):
                t.penup()
                t.forward(10)
                t.pendown()
                t.forward(10)
            t.penup()
            t.backward(160)
            t.left(90)
            t.forward(20)

    def setup_players(self):
        self.players = []
        player_data = [
            ("red", 100, 36),
            ("blue", 70, 5),
            ("green", 40, 6),
            ("orange", 10, -12)
        ]
        for color, start_y, angle in player_data:
            player = self.setup_player(color, start_y, angle)
            self.players.append(player)

    def setup_player(self, player_color, start_y, angle):
        player = t.Turtle()
        player.color(player_color)
        player.shape("turtle")
        player.penup()
        player.goto(-160, start_y)
        player.pendown()
        for turn in range(10):
            player.right(angle)
        return player

    def run_race(self):
        for turn in range(100):
            for player in self.players:
                player.forward(randint(1, 5))

    def write(self, step):
        t.penup()
        t.forward(10)
        t.write(step, align='center')
        t.backward(10)

if __name__ == "__main__":
    race = TurtleRace()
    race.run_race()
    t.done()
