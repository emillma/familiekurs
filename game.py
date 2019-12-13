#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:43:38 2019

@author: emil
"""
import numpy as np

pinne_1 = []
pinne_2 = []
pinne_3 = []
n = 25
alle = [pinne_1, pinne_2, pinne_3]
for i in range(n,0,-1):
    r = np.random.randint(0,3)
    alle[r].append(i)


def print_alle_pinner(alle_pinner):
    table = ''
    max_height = max([len(liste)-1 for liste in alle_pinner])
    for level in range(max_height,-1,-1):
        for pinne in alle_pinner:
            if level >= len(pinne):
                disk = 0
            else:
                disk = pinne[level]
            table += ' '*(n-disk+1) + '-'*disk + '|' + '-'*disk + ' '*(n-disk)
        table += '\n'
    table += ('_'*(n+1) + '|' + '_'*(n))*3
    print(table)



def foo(pinne_1, pinne_2, pinne_3):
    max_på_en_pinne = max(len(pinne_1), len(pinne_2), len(pinne_3))
    pinne_1 = pinne_1 + (n-len(pinne_1)) * [0]
    pinne_2 = pinne_2 + (n-len(pinne_2)) * [0]
    pinne_3 = pinne_3 + (n-len(pinne_3)) * [0]
    table = ''
    for level in range(max_på_en_pinne-1,-1,-1):
        for pinne in [pinne_1, pinne_2, pinne_3]:
            disk = pinne[level]
            table += ' '*(n-disk+1) + '-'*disk + '|' + '-'*disk + ' '*(n-disk)
        table += '\n'
    table += ('_'*(n+1) + '|' + '_'*(n))*3
    print(table)


def foo2(pinne_1, pinne_2, pinne_3):
    max_på_en_pinne = len(pinne_1)+ len(pinne_2)+ len(pinne_3)
    pinne_1 = pinne_1 + (n-len(pinne_1)) * [0]
    pinne_2 = pinne_2 + (n-len(pinne_2)) * [0]
    pinne_3 = pinne_3 + (n-len(pinne_3)) * [0]
    table = ''
    for level in range(max_på_en_pinne-1,-1,-1):
        for pinne in [pinne_1, pinne_2, pinne_3]:
            disk = pinne[level]
            if disk != 0:
                table += f'{disk:2d}' + ' '*4
            else:
                table += ' '*6
        table += '\n'
    # table += ('_'*(n+1) + '|' + '_'*(n))*3
    print('\x1b[2J')
    print(table)


for i in range(10):
    foo(pinne_1, pinne_2, pinne_3)
    print(i)
    input('press enter')










