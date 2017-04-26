from django.shortcuts import render, redirect, reverse, get_object_or_404
from TwitterSearch import *
from .forms import TweetForm
import time
import folium
from geopy.geocoders import Nominatim
import requests
import requests_cache
from .twitter_api import *


requests_cache.install_cache('twitter_cache', backend='sqlite', expire_after=180)


class TweetLists(object):
  def __init__(self):
    self.tweet_locations = []
    self.location = []
    self.text_list = []
    self.user_name = []
    self.date_tweeted = []

info_lists = TweetLists()

tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
tso.set_language('en')  # setting it to English only
tso.set_include_entities(False)  # not including entities

ts = TwitterSearch(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def tweet_list(request):

    trends_place = api.trends_place(2458410) # The WOEID for the USA. Change for another country
    data = trends_place[0]
    # getting the trends from the results
    trends = data['trends']
    count = 0
    names = []
    top_ten_tweets = 10
    # getting the top ten trending tweets
    for trend in trends:
        names.append(trend)
        count += 1
        if count == top_ten_tweets:
            break
    return render(request, 'twitter_dashboard/tweet.html', {'names' : names})

def save_information(request):
    print(len(info_lists.text_list))
    length = len(info_lists.text_list)
    if len(info_lists.user_name) == 0:
        pass
    else:
        count = 0
        while True:
            if request.method == 'POST':
                form = TweetForm(request.POST)
                if form.is_valid():
                    tweet_save = form.save(commit=False)
                    tweet_save.user_name = info_lists.user_name[count]
                    tweet_save.date_tweeted = info_lists.date_tweeted[count]
                    tweet_save.tweet = info_lists.text_list[count]
                    if count < len(info_lists.tweet_locations):
                        tweet_save.location = info_lists.tweet_locations[count]
                    tweet_save.save()
                    count += 1
                    if count == length:
                        break

    return redirect('tweet_list')

def open_map_locations(request):

    geolocator = Nominatim(scheme='http')
    world_map = folium.Map(location=[40, -120], zoom_start=3, tiles='Stamen Terrain')

    for i in info_lists.tweet_locations:
        if i != '':
            info_lists.location = geolocator.geocode(i)
            if info_lists.location == None:
                pass
            else:
                marker = folium.Marker([info_lists.location.latitude, info_lists.location.longitude], popup=i)
                marker.add_to(world_map)

    world_map.save('twitter_dashboard/templates/twitter_dashboard/tweet_map.html')

    return render(request, 'twitter_dashboard/tweet_map.html')

def live_tweets(request):
    # opening and closing the file to clear it for a second search
    open('twitter_dashboard/static/text/system.txt', 'w').close()
    system_output = open('twitter_dashboard/static/text/system.txt', 'r+')
    info_lists.location = []
    info_lists.text_list = []
    info_lists.tweet_locations = []
    info_lists.user_name = []
    info_lists.date_tweeted = []
    try:
        if request.method == 'POST':
            post_request = request.POST
            user_search = str(post_request['search']) # getting the user search
            count = 0
            tso.set_keywords([user_search])  # setting the keyword to search for
            '''stream_listener = StreamListener()
            stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
            stream.filter(track=[user_search])''' # TODO figure out how to process tweets fast enough to use tweepy
            top_fifty_tweets = 50
            for tweet in ts.search_tweets_iterable(tso):
                count += 1
                # getting the first fifty tweets
                info_lists.text_list.append(tweet['text'])
                info_lists.user_name.append(tweet['user']['screen_name'])
                info_lists.date_tweeted.append(tweet['created_at'])
                if tweet['user']['location'] != '':
                    info_lists.tweet_locations.append(tweet['user']['location'])
                if count == top_fifty_tweets:
                    break
            # writing the list to a text file to display
            for line in info_lists.text_list:
                system_output.write('<p>' + line + '</p>' + '\n')
                system_output.flush()
                # waiting 4 seconds so it looks like it is updating in real time
                time.sleep(4)

    except TwitterSearchException as e:  # catch any errors
        print(e)

    return redirect('tweet_list')
