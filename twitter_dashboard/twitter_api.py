import os
import tweepy

consumer_key=os.environ['TWITTER_CONSUMER_KEY']
consumer_secret=os.environ['TWITTER_CONSUMER_SECRET']
access_token=os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
