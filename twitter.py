#!/usr/bin/python

execfile("523.py")

import twitter

my_consumer_key = 'None'
my_consumer_secret = 'None'
my_access_token = 'None'
my_access_token_secret = 'None'

commandHandle = 'None'

api = twitter.Api(consumer_key=my_consumer_key, consumer_secret=my_consumer_secret, access_token_key=my_access_token, access_token_secret=my_access_token_secret)

## This example just takes the most recent post from a specified twitter user, and sets the color of your room to that
statuses = api.GetUserTimeline(commandHandle)
humanRGB(entry,statuses[0].text)
