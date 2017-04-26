from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tweet_list, name='tweet_list'),
    url(r'^live_tweets$', views.live_tweets, name='live_tweets'),
    url(r'^map_location$', views.open_map_locations, name='map_location'),
    url(r'^save_information$', views.save_information, name='save_information'),
    ]
