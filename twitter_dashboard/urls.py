from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tweet_list, name='tweet_list'),
    url(r'^live_tweets$', views.live_tweets, name='live_tweets'),
    ]
