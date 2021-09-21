import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class x_score:
    def __init__(self, num):
        self.num = num

    def change_score(self, add_score):
        while True:
            self.add_score = self.num + 0

            return self.add_score


class Player(x_score):
    def move(self):
        choice = random.choice(moves)
        if 'rock' or 'paper' or 'scissors' in choice:

            return choice

    def learn(self, my_move, their_move):
        pass


class Player1(Player):
    def option(self):
        choice = input("choose rock, paper or scissors ")
        if 'rock' or 'paper' or 'scissors' in choice:

            return choice


class Game(x_score):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        new_score = x_score(0)

        new2_score = x_score(0)

        y = new2_score.change_score(0)

        x = new_score.change_score(0)

        while True:
            P1 = Player1(0)
            gues = P1.option()
            print(gues)
            P2 = Player(0)
            gues1 = P2.move()
            print(gues1)

            if (gues == 'rock' and gues1 == 'scissors' or gues == 'paper' and
               gues1 == 'rock' or gues == 'scissors' and gues1 == 'paper'):
                x += 1
                print('you won, you gained 1 point')
                time.sleep(2)
                print('the score is know..')
                time.sleep(1)
                print('Player 1:' + str(x))
                time.sleep(1)
                print('Player 2:', str(y))
                time.sleep(2)

            elif gues == gues1:
                print('its a draw!..')
                time.sleep(2)

            else:
                y += 1
                print('Player 2 gains 1 point')
                time.sleep(2)
                print('the score is know..')
                time.sleep(1)
                print('Player 1:', str(x))
                time.sleep(1)
                print('Player 2:', str(y))
                time.sleep(2)
            if x == 3:
                print("you win, thank you for playing..")
                break
            elif y == 3:
                print('you loose, thank you for playing..')
                break

        self.p1.learn(P1, P2)
        self.p2.learn(P2, P1)

    def play_game(self):
        print("Game start!")
        time.sleep(1)
        for round in range(1):
            print(f"Round {round}:")
            time.sleep(1)
            self.play_round()
            time.sleep(1)
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player1(0), Player(0))
    game.play_game()
