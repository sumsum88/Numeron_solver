#!/usr/bin/env python
# coding: utf-8

from agent import NumeronAgent, NumeronHumanAgent


class Game(object):
    """
    Numeron対戦用クラス
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def main(self):
        nof_turns = 1
        while True:
            print('---------- Turn {} ----------'.format(nof_turns))
            print('---- pleyer1\'s turn ----')
            player1.action(player2)
            print('---- pleyer2\'s turn ----')
            player2.action(player1)
            nof_turns += 1


if __name__ == '__main__':
    player1 = NumeronHumanAgent()
    player2 = NumeronAgent()

    game = Game(player1, player2)
    game.main()
