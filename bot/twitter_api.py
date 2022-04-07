from distutils.filelist import translate_pattern
import tweepy
from translate import translate_text
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



def print_tweets(topic, client,lang): 

    tweets = client.search_tweets(topic,count=1)
    response = ""
    
    for tweet in tweets: 
        print(tweet.text)
        response = "Here is a tweet that my help you search: " + tweet.text
    
    #UPDATE WITH TRANSLATION
    if lang != "en":
        response = translate_text(lang,response)

    return response

    
