import tweepy
import twitter_keys


from tweepy import Cursor
from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Authenticate to Twitter
auth = OAuthHandler(twitter_keys.customer_key, twitter_keys.customer_secret)
auth.set_access_token(twitter_keys.access_token, twitter_keys.access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet.
api.update_status("Hello Tweepy")