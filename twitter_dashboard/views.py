from django.shortcuts import render, redirect, reverse, get_object_or_404
from TwitterSearch import *
import tweepy
import time
# enter keys here
consumer_key = 'ovs0wuKgyaWl3U3heJGQTrSpe'
consumer_secret = 'RMUEm84gYwgxHBQFCtoqbE4LdfAIjN4XjgOPqXMPgaq3Kr09SB'
access_token = '836064650559111169-X3k0Jgw1JjPf83se7Ug1LAy6bFsPP8o'
access_token_secret = 'mup8qi1aQfwNVmQW5Uv88xSwfafPXZrFaflwJeFo0Nnkk'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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
    top_five_tweets = 5
    # getting the top five tweets
    for trend in trends:
        names.append(trend)
        count += 1
        if count == top_five_tweets:
            break
    return render(request, 'twitter_dashboard/tweet.html', {'names' : names})

def live_tweets(request):
    # opening and closing the file to clear it for a second search
    open('twitter_dashboard/static/text/system.txt', 'w').close()
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
            for tweet in ts.search_tweets_iterable(tso):
                count += 1
                # getting the first fifty texts
                text_list.append(tweet['text'])
                if count == 50:
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
