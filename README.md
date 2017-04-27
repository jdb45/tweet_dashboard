# tweet_dashboard

This is a dashboard for seeing information about tweets on twitter
This program is to be used for FUN use only.
This program is NOT to be used for any monetary gain of any sort.
I am not affiliated with Twitter in anyway. All names and logos are copyright to Twitter.
Some of the features:

*Displays live tweets for a searched topic

*Displays top trending tweets


*Coming soon

Saving tweets and other information to a database

Displaying a map of where the locations of the tweets are coming from

Displaying charts of other useful information about where the tweets are coming from

NOTE: The live tweets will sometimes not work correctly unless you clear your browsing history, cookies, and cache.

### To install

1. Create and activate a virtual environment. Use Python3 as the interpreter.

2. pip install -r requirements.txt

3. cd twitter_dashboard/twitter

4. python manage.py makemigrations

5. python manage.py migrate

6. python manage.py runserver

Site at

127.0.0.1:8000

### Create superuser

from twitter_dashboard/twitter

python manage.py createsuperuser

enter username and password

You will be able to use these to log into admin console at

127.0.0.1:8000/admin


### Twitter keys
For this program to work you need Twitter API keys.
Create a Twitter account (using your personal account is not recommended in case you make a mistake and request to many calls at once).
[Get API keys from Twitter](https://apps.twitter.com/). The following keys must
be stored as system environment variables:
* TWITTER_CONSUMER_KEY
* TWITTER_CONSUMER_SECRET
* TWITTER_ACCESS_TOKEN
* TWITTER_ACCESS_TOKEN_SECRET
