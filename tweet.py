#!/usr/bin/python

execfile("523.py")

import twitter

#Do not be dumb and leave your secrets here when you commit 
my_consumer_key = 'None'
my_consumer_secret = 'None'
my_access_token = 'None'
my_access_token_secret = 'None'

commandHandle = 'None'

api = twitter.Api(consumer_key=my_consumer_key,
                  consumer_secret=my_consumer_secret,
                  access_token_key=my_access_token,
                  access_token_secret=my_access_token_secret)

## This example just takes the most recent post from a specified twitter user, and sets the color of your room to that
while True:
    status = api.GetSearch(commandHandle)
    stripped = status[0].text.replace(commandHandle+" ","")
    print stripped
    humanRGB(table,stripped)
    time.sleep(5)
