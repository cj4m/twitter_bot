import tweepy
import random


auth = tweepy.OAuthHandler('poggers', 'poggers')
auth.set_access_token('poggers', 'poggers')

api = tweepy.API(auth)
################
#This is it lol#
################

with open('twitter_bot/library1.txt') as f:
    lines = f.readlines()

status = random.choice(lines)

api.update_status(status)