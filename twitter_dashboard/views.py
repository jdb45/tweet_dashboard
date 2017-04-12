from django.shortcuts import render, redirect, reverse, get_object_or_404
from TwitterSearch import *
import tweepy
import time
import folium
from geopy.geocoders import Nominatim

# enter keys here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet_locations = []

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
    # opening and closing the file to clear it for a second search
    open('twitter_dashboard/static/text/system.txt', 'w').close()
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

def open_map_locations(request):

    geolocator = Nominatim(scheme='http')
    location = []
    world_map = folium.Map(location=[40, -120], zoom_start=3, tiles='Stamen Terrain')

    for i in tweet_locations:
        if i != '':
            location = geolocator.geocode(i)
            if location == None:
                pass
            else:
                marker = folium.Marker([location.latitude, location.longitude], popup=i)
                marker.add_to(world_map)

    world_map.save('twitter_dashboard/templates/twitter_dashboard/tweet_map.html')

    return render(request, 'twitter_dashboard/tweet_map.html')

def live_tweets(request):

    system_output = open('twitter_dashboard/static/text/system.txt', 'r+')
    try:
        if request.method == 'POST':
            post_request = request.POST
            user_search = str(post_request['search']) # getting the user search
            count = 1
            tso.set_keywords([user_search])  # setting the keyword to search for
            '''stream_listener = StreamListener()
            stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
            stream.filter(track=[user_search])''' # TODO figure out how to process tweets fast enough to use tweepy
            text_list = []
            top_fifty_tweets = 50
            for tweet in ts.search_tweets_iterable(tso):
                count += 1
                # getting the first fifty tweets
                text_list.append(tweet['text'])
                if tweet['user']['location'] != '':
                    tweet_locations.append(tweet['user']['location'])
                if count == top_fifty_tweets:
                    break
            # writing the list to a text file to display
            for line in text_list:
                system_output.write('<p>' + line + '</p>' + '\n')
                system_output.flush()
                # waiting 5 seconds so it looks like it is updating in real time
                time.sleep(5)

    except TwitterSearchException as e:  # catch any errors
        print(e)

    return redirect('tweet_list')
