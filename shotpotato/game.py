#!/usr/bin/python

execfile("../523.py")

''' This game should stat playing a random song from a list, and slowly fade a color from blue to red
    The song should stop when the bulb turns red?
'''

import sys, random, re

random.seed()
song = sys.argv[1] #This will eventually enable us to play a song during the fading of the color
loser = []
i = 0
scoretable = []
table.xy = blue

while True:
    
    print 'Starting round!'
    timer = random.randint(10,30)
    trans(red, timer*100, table)
    table.alert = 'lselect'
    time.sleep(5)
    table.alert = 'none'
    print 'Game over, please enter loser!'
    loser.append(raw_input())
    loser[i] = loser[i].upper()
    print 'Player:',loser[i],' has lost',loser.count(loser[i]),' times!'
    if loser.count(loser[i]) = 1:
        scoretable.append(loser[i])
    #Scoretable print here
    i += 1
    table.xy = blue
