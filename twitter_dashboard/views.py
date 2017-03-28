from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Tweet
import tweepy

def tweet_list(request):
    # enter keys here
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    # OAuth processing
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    trends_place = api.trends_place(2458410) # The WOEID for the USA. Change for another country
    data = trends_place[0]
    # getting the trends from the results
    trends = data['trends']
    count = 0
    names = []
    ten_tweets = 10
    # getting the top ten tweets
    for trend in trends:
        names.append(trend)
        count += 1
        if count == ten_tweets:
            break

    return render(request, 'twitter_dashboard/tweet.html', {'names' : names})
