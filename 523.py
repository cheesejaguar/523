#!/usr/bin/pythonc

#Import Python Hue API
from phue import Bridge
import time

#Setup the bridge
b = Bridge('192.168.2.144')

#create lights object
lights = b.get_light_objects('name')

#create light object for each light
entry = lights['Entry']
lamp = lights['Lamp']
book = lights['Bookcase']
bed = lights['Bed']
table = lights['Dining table']

#Setup transition times
entry.transitiontime = 8
lamp.transitiontime = 8
book.transitiontime = 8
bed.transitiontime = 8
table.transitiontime = 8

#Define some basic rainbow colors
red = [0.675, 0.322]
yellow = [0.542, 0.42]
green = [0.288, 0.279]
blue = [0.167, 0.04]
pink = [0.421, 0.181]

# Function to convert RGB to xy values
# From Hue API: If an xy value outside of the green triangle is chosen, it will produce the closest color it can make
def rgb2xy(R, G, B):
    # Convert RGB to XYZ
    X = 0.649926 * R + 0.103455 * G + 0.197109 * B
    Y = 0.234327 * R + 0.743075 * G + 0.022598 * B
    Z = 0.000000 * R + 0.053077 * G + 1.035763 * B
    # Get color point
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    # create vector
    xy_vec = [x,y]
    return xy_vec

def trans(finish, duration, bulb):
    oldstatus = bulb.transitiontime
    bulb.transitiontime = 0
    start = bulb.xy
    tempxy = start
    rise = finish[1] - start[1]
    run = finish[0] - start[0]
    slope = rise / run
    for j in range(0,duration):
        tempxy[0] += (run/duration)
        tempxy[1] +=  (rise/duration)
        bulb.xy = tempxy
        time.sleep(0.1)
    bulb.transitiontime = oldstatus

    

#Group hack for main room
def  main(on,color,bright):
    for bulb in ['Entry', 'Dining table']:
        lights[bulb].on = on
        lights[bulb].xy = color
        lights[bulb].bri = bright

#Cycles power state of specified bulb
# must be passed a phue light object
def toggle(bulb):
    if bulb.on == True:
        bulb.on = False
    else:
        bulb.on = True

'''
for light in ['Lamp', 'Bookcase', 'Bed']:
    lights[light].on = True
    lights[light].brightness = 254
'''