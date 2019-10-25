# -*- coding: utf-8 -*-

__author__ = 'Kevin Martin Lankut'
__email__ = 'kela@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = 2 ** 31 - 1

    def rand(self):
        self.seed = self.a * self.seed % self.m
        return self.seed


class ListRand:
    def __init__(self, liste):
        self.liste = liste
        self.liste_len = len(liste)
        self.index = -1
        # Kommentar til megselv:
        # Bruker index = -1 fordi første elementet i en liste er 0

    def rand(self):
        self.index += 1
        if self.index >= self.liste_len:
            raise RuntimeError()
        return self.liste[self.index]


if __name__ == "__main__":
    lcg = LCGRand(666)
    print(lcg.rand())
    numbers = [4, 20, 69]
    lr = ListRand(numbers)
    for _ in range(len(numbers)):
        print(lr.rand())
