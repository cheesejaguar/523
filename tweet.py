#!/usr/bin/python

execfile("523.py")

import twitter

#Do not be dumb and leave your secrets here when you commit 
my_consumer_key = 'wiAwJDA1xk0riS0TDu2lg'
my_consumer_secret = 'rmgDxHmwLrTFE2JSc50uOWYMexCTED6HL62Pw8THlk'
my_access_token = '14276619-QwuOw7srp2U0BYuprx7QVrAfcZZ1ewofWRksZvsQ7'
my_access_token_secret = 'moPlJVLBoLdCmSMYZRVYyzpUhtwrs0kht6E6RY414'

commandHandle = '@PentHome15'

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
