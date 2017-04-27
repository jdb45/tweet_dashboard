# tweet_dashboard

This is a dashboard for seeing information about tweets on twitter.

## Some of the features:
# *Displays top trending tweets
<img width="1275" alt="screen shot 2017-04-26 at 8 51 36 pm" src="https://cloud.githubusercontent.com/assets/22032532/25465383/846e8c64-2ac7-11e7-8db3-865a493a18c3.png">

# *Displays live tweets for a searched topic
<img width="1280" alt="screen shot 2017-04-26 at 9 07 41 pm" src="https://cloud.githubusercontent.com/assets/22032532/25465498/39cf780c-2ac8-11e7-9c91-5caceaca5c06.png">

# *Saves tweets and other information to a database


# *Displaying a map of where the locations of the tweets are coming from
<img width="1280" alt="screen shot 2017-04-26 at 7 41 28 pm" src="https://cloud.githubusercontent.com/assets/22032532/25465782/fe7c87b6-2ac9-11e7-9105-27ff056dbd60.png">

NOTE: The live tweets will sometimes not work correctly unless you clear your browsing history, cookies, and cache before starting the app.

It is recommended to use Google Chrome and to disable network the cache. 

This is done be doing these steps:

`click the settings icon on top right corner| More Tools | Developer Tools | Network | Disable cache`


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

Create a Twitter account (using your personal account is not recommended).
[Get API keys from Twitter](https://apps.twitter.com/). The following keys must
be stored as system environment variables:
* TWITTER_CONSUMER_KEY
* TWITTER_CONSUMER_SECRET
* TWITTER_ACCESS_TOKEN
* TWITTER_ACCESS_TOKEN_SECRET
