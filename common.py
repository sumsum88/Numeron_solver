#!/usr/bin/env python
# coding: utf-8


from collections import Counter
import numpy as np


CHARS = '1234567890'
DIGITS = 5


class Judge(object):

    eat = 0
    bite = 0

    def __repr__(self):
        return 'eat: {}, bite: {}'.format(self.eat, self.bite)

    def __eq__(self, other):
        return self.eat == other.eat and self.bite == other.bite

    def __ne__(self, other):
        return not (self.eat == other.eat and self.bite == other.bite)

    def __hash__(self):
        return self.eat * 1e4 + self.bite


class State(object):
    """
    呼ばれ方の等しい数字に分類する
    TODO
    """

    def __init__(self, chars=10, digits=5):
        self.put = np.zeros((chars, digits))

    def update(self, call_number):
        for i, n in enumerate(call_number):
            self.put[int(n)][i] += 1

    def get_group(self):
        putset = [sorted(x) for x in self.put]
        group = {}
        for i, s in enumerate(putset):
            if not str(s) in group.keys():
                group[str(s)] = [i]
            else:
                group[str(s)].append(i)

        return group

    def _generate(self, group):
        pass

    def generate(self):
        """
        やりたいこと
        AAAAABBBCCCDを使った5文字の文字列を全部列挙したい
        Returns
        -------
        """

        group = self.get_group()


def coincidence(n1, n2):
    """
    n1とn2の一致度を測る
    """
    j = Judge()
    for i, n in enumerate(n1):
        if n == n2[i]:
            j.eat += 1
        elif n in n2:
            j.bite += 1
    return j


def is_valid_number(number, digits, chars):
    if len(number) != digits:
        return False
    if len(number) != len(set(number)):
        return False
    for v in number:
        if not v in chars:
            return False
    else:
        return True


def entropy(num, num_list):
    """
    num_listが答えの候補である時にnumをcallすることで得られる情報量

    Parameters
    ----------
    num : list(str)
    num_list : list(list(str))

    Returns
    ----------
    entropy: list(int)

    """
    n = len(num_list)
    j_list = [coincidence(num_, num).__hash__() for num_ in num_list]
    counter = Counter(j_list)
    pr = [x * 1.0 / n for x in counter.values()]

    return sum(map(lambda p: p * -np.log2(p), pr))