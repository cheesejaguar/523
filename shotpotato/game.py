#!/usr/bin/python

execfile("../523.py")

''' This game should stat playing a random song from a list, and slowly fade a color from blue to red
    The song should stop when the bulb turns red?
'''

import sys, random, re

random.seed()
song = sys.argv[1]
loser = []

while True:
    i = 0
    print 'Starting round!'
    timer = random.randint(10,30)
    trans(red, timer, table)
    time.sleep(timer)
    print 'Game over, please enter loser!'
    loser.append(raw_input())
    loser[i] = loser[i].upper()
    print 'Player:',loser[i],' has lost',loser.count(loser[i]),' times!'
    i += 1
    table.xy = blue
