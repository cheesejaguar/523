#!/usr/bin/python

execfile("523.py")

import twitter
import re

#Do not be dumb and leave your secrets here when you commit 
my_consumer_key = 'None'
my_consumer_secret = 'None'
my_access_token = 'None'
my_access_token_secret = 'None'

commandHandle = 'None' #Format: '@UserName' No spaces
old = 'None'

entry.on = True
table.on = True

api = twitter.Api(consumer_key=my_consumer_key,
                  consumer_secret=my_consumer_secret,
                  access_token_key=my_access_token,
                  access_token_secret=my_access_token_secret)

## This example just takes the most recent post from a specified twitter user, and sets the color of your room to that
while True:
    status = api.GetSearch(commandHandle)
    commandHandle += ' '
    commandHandle = re.compile(commandHandle, re.IGNORECASE)
    stripped = commandHandle.sub("", status[0].text)
    if old != stripped:
        print stripped
        humanRGB(table,stripped)
        humanRGB(entry,stripped)
        old = stripped
    time.sleep(5)
