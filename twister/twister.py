#!/usr/bin/python

execfile("523.py")
import random, time, pyttsx
tts = pyttsx.init()
tts.say('Starting Twister')
tts.runAndWait()
colors = [[red, green, blue, yellow], ['red', 'green', 'blue', 'yellow']]
def namestr(obj, namespace):
	return [name for name in namespace if namespace[name] is obj]
pick = lambda items: random.choice(items)
while not time.sleep(6):
	color=pick((0, 1, 2, 3))
	side=pick(("left", "right"))
	appendage=pick(("foot", "hand"))
	main(True,colors[0][color]) 
	line = "Place " + side + " " + appendage + " on " +colors[1][color]
	print line
	tts.say(line)
	tts.runAndWait()
