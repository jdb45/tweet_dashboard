from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url


def tweet_list(request):

    return render(request, 'twitter_dashboard/tweet.html')
