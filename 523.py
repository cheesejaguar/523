#!/usr/bin/python

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
green = [0.408, 0.517]
blue = [0.167, 0.04]
pink = [0.421, 0.181]
white = [.35,.35]

#RGB Array if needed
class rgbClass:
    def __init__(self):
        self.data = {'red' : 0, 'green' : 0, 'blue' : 0}


# Function to convert RGB to xy values
# From Hue API: If an xy value outside of the green triangle is chosen, it will produce the closest color it can make
def rgb2xy(rgb):
    # Convert RGB to XYZ
    X = 0.649926 * rgb['red'] + 0.103455 * rgb['green'] + 0.197109 * rgb['blue']
    Y = 0.234327 * rgb['red'] + 0.743075 * rgb['green'] + 0.022598 * rgb['blue']
    Z = 0.000000 * rgb['red'] + 0.053077 * rgb['green'] + 1.035763 * rgb['blue']
    # Get color point
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    # create vector
    xy_vec = [x,y]
    return xy_vec


#This function translates english into numbers
#Inspired by https://github.com/interstateone/siriproxy-hue/
def humanRGB(bulb, english):

    url = "/api/colors?keywords=" + english + "&numResults=1&format=json"
    url.replace(' ','%20')
    connection = httplib.HTTPConnection('www.colourlovers.com')
    connection.request('GET', url)
    response = connection.getresponse()
    connection.close()
    result_str = response.read()
    parsed = json.loads(result_str)
    data_rgb = parsed[0]['rgb']
    data_hsv = parsed[0]['hsv']
    bulb.xy = rgb2xy(data_rgb)
    bulb.saturation = data_hsv['saturation']


#This function transitions the light from the current color to a specified color
#Updated this function to receive duration in units of 10ms rather than 100ms
#Should be a smoother transition
def trans(finish, duration, bulb):
    oldstatus = bulb.transitiontime
    bulb.transitiontime = 0
    start = bulb.xy
    tempxy = start
    rise = finish[1] - start[1]
    run = finish[0] - start[0]
    for j in range(0,duration):
        tempxy[0] += (run/duration)
        tempxy[1] +=  (rise/duration)
        bulb.xy = tempxy
        time.sleep(0.01)
    bulb.transitiontime = oldstatus

    

#Basic Group Change Function 
def  main(on,xy=white,brightness=200,tt=8):
    command = {'on' : on,'xy' : xy,'bri' : brightness, 'transitiontime' : tt }
    b.set_group(3,command)
    

def ct_trans(bulb,temp,start=-1,steps=10,steptime=0.1):
    ''' Colortemp transition function
    '''
    if start == -1:
        start = bulb.colortemp
    path = temp - start
    step = divmod(math.fabs(path),steps)
    for j in range(0,(steps+1)):
        if j == steps:
            start += math.copysign(step[1],path)
        else:
            start += math.copysign(step[0],path)
        print start
        command = {"ct": int(start)}
        b.set_light(bulb.light_id, command)
        time.sleep(steptime)
    

#Proposed replacement for Color Temp Transition
def ct_trans_aaron(bulb, temp, tt=100):
    current_ct = bulb.colortemp_k
    bulb.colortemp_k = current_ct
    path = temp - current_ct
    print path
    step = path / tt
    for j in range(1,tt):
        current_ct += step
        #"clean" markup, but may not work if not already in ct mode
        bulb.colortemp_k = current_ct
        #sleep 10ms
        time.sleep(0.01)
    
#Cycles power state of specified bulb
# must be passed a phue light object
def toggle(bulb):
    if bulb.on == True:
        bulb.on = False
    else:
        bulb.on = True
