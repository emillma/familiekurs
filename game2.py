#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:36:21 2019

@author: emil
"""


pinne_1 = []
pinne_2 = []
pinne_3 = []
n = 40
for i in range(n,0,-1):
    pinne_1.append(i)


def show_game():
    n = len(pinne_1)+ len(pinne_2)+ len(pinne_3)
    pinne_1_padda = pinne_1 + (n-len(pinne_1)) * [0]
    pinne_2_padda = pinne_2 + (n-len(pinne_2)) * [0]
    pinne_3_padda = pinne_3 + (n-len(pinne_3)) * [0]
    table = ''
    for level in range(n-1,-1,-1):
        table += f'|' +' '*4
        for pinne in [pinne_1_padda, pinne_2_padda, pinne_3_padda]:
            disk = pinne[level]
            if disk != 0:
                table += ' '*4 + f'{disk:2d}' + ' '*4 + '|'
            else:
                table += ' '*4 + f'  ' + ' '*4 + '|'
        table += '\n'
    # table += ('_'*(n+1) + '|' + '_'*(n))*3
    print(table)


def move(p1, p2):
    if len(p1) == 0 or (len(p2) > 0 and p2[-1] < p1[-1]):
        raise Exception('Invalid move')
    else:
        p2.append(p1.pop())


def solve(n, fra, til, via, pause = 1, parent_count = 0):
    count = parent_count
    if n == 1:
        move(fra, til)
        if (parent_count+1) % pause == 0:
            show_game()
            input(f'Du har flyttet {parent_count + 1} brikker. Trykk enter for å fortsette.\n')
        return 1
    else:
        count += solve(n-1, fra, via, til, pause, count)
        count += solve(1,fra, til, via, pause, count)
        count += solve(n-1, via, til, fra, pause, count)
    return count - parent_count

def solve2(n, fra, til, via, pause = 1, parent_count = 0, top = True):
    if top:
        pause = n
    count = parent_count
    if n == 1:
        move(fra, til)

        count += 1
    else:
        count += solve2(n-1, fra, via, til, pause-1, count, False)
        count += solve2(1  , fra, til, via, -1, count, False)
        count += solve2(n-1, via, til, fra, -1, count, False)
    if n == pause:
        show_game()
        input(f'{n} Du har flyttet {count} brikker. Trykk enter for å fortsette.\n')
    return count - parent_count

show_game()
solve2(len(pinne_1), pinne_1, pinne_2, pinne_3)

