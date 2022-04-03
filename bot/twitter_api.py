import tweepy
from decouple import config

def twitter_client():
    # Retrieve Keys from Environment Variables 
    CONSUMER_KEY = config('CONSUMER_KEY')
    CONSUMER_SECRET = config('CONSUMER_SECRET')
    ACCESS_TOKEN = config('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)



def print_tweets(topic, client): 

    tweets = client.search_tweets("Where is atlantis ?",count=3)

    for tweet in tweets:
        print(tweet.text)