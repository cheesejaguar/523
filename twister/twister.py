#!/usr/bin/python

execfile("523.py")
import random, time, pyttsx
tts = pyttsx.init()
tts.say('Starting Twister')
tts.runAndWait()
def namestr(obj, namespace):
	return [name for name in namespace if namespace[name] is obj]
pick = lambda items: random.choice(items)
while not time.sleep(6):
	color=pick((red, green, blue, yellow))
	side=pick(("left", "right"))
	appendage=pick(("foot", "hand"))
	main(True,color) 
	line = "Place " + side + " " + appendage + " on " + namestr(color,globals())[0]
	print line
	tts.say(line)
	tts.runAndWait()