#!/usr/bin/env python
# coding: utf-8


from itertools import permutations
from numpy.random import shuffle
from random import choice
import copy
from common import *


class NumeronAgent(object):
    """
    Numeron Player(AI)
    """

    def __init__(self, number=None):
        self.candidate = [''.join(i) for i in permutations(CHARS, DIGITS)]
        if number is None:
            number = choice(self.candidate)

        if type(number) in [str, int]:
            number = list(str(number))

        self.number = number
        self.turn = 1
        assert len(number) == DIGITS
        self.all_candidate = copy.deepcopy(self.candidate)

    def reply_coincidence(self, opponent_call_number):
        """
        相手の宣言した数字に対し、eatとbiteの数を返す

        Parameters
        ----------
        opponent_call_number : list(str) 相手の宣言した数字

        Returns
        -------
        Judge eatとbiteの数

        """
        return coincidence(self.number, opponent_call_number)

    def decide_call_number(self, max_num=1000):
        """
        次の宣言する数字を決める

        Parameters
        ----------
        max_num : int 探索数

        Returns
        -------
        call_number : list(str) 最もエントロピーが高くなる数字

        """
        if self.turn > 1:
            '''
            State情報を使ってもっと上手くやりたい
            '''
            shuffle(self.candidate)

            if len(self.candidate) <= max_num:
                array = self.candidate + self.all_candidate[:max_num - len(self.candidate)]
            else:
                shuffle(self.all_candidate)
                array = self.all_candidate[:max_num]

            entropy_list = map(lambda x: entropy(x, self.candidate[:max_num]), array)
            call_number = array[np.argmax(entropy_list)]

        else:
            call_number = choice(self.candidate)
        print('call number: {}'.format(call_number))
        return call_number

    def update_candidate(self, judge, call_number):
        """
        候補を更新

        Parameters
        ----------
        judge : Judge 今回のeatとbite
        call_number : list(str) 今回の宣言した数字

        """
        self.candidate = filter(lambda x: coincidence(
            x, call_number) == judge, self.candidate)

    def action(self, opponent):
        """
        1ターンの一連のアクションを行う

        Parameters
        ----------
        opponent : NumeronAgent

        """
        call_number = self.decide_call_number()
        j = opponent.reply_coincidence(call_number)
        print(j)
        if j.eat == DIGITS:
            print('WIN!!!')
            exit()
        self.update_candidate(j, call_number)
        print('candidate: {}'.format(len(self.candidate)))
        self.turn += 1


class NumeronHumanAgent(NumeronAgent):
    """
    Numeron Player(人間)
    """

    def __init__(self):
        number = self.input_number('please set your number (digits = {}): '.format(DIGITS))
        assert len(number) == DIGITS
        NumeronAgent.__init__(self, number)

    def input_number(self, message):
        while True:
            number = list(raw_input(message))
            if is_valid_number(number, DIGITS, CHARS):
                return number
            else:
                print('invalid number')

    def decide_call_number(self, max_num=1000):
        number = self.input_number('call number: ')
        assert len(number) == DIGITS
        return number