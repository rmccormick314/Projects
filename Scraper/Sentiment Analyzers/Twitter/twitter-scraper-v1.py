from bs4 import BeautifulSoup
import tweepy
import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# <----- BEGIN VARIABLES ----->
secret_file = "twitter-keys.txt"

with open(secret_file) as f:
    lines = f.readlines()

twitter_keys = {
        'consumer_key':        lines[1].strip(),
        'consumer_secret':     lines[3].strip(),
        'bearer_token':        lines[5].strip(),
        'access_token_key':    lines[7].strip(),
        'access_token_secret': lines[9].strip(),
        'client_key':          lines[11].strip(),
        'client_token':        lines[13].strip()
    }

auth = tweepy.OAuthHandler(twitter_keys['consumer_key'],
                           twitter_keys['consumer_secret'])

auth.set_access_token(twitter_keys['access_token_key'],
                      twitter_keys['access_token_secret'])

api = tweepy.API(auth)

sid = SentimentIntensityAnalyzer()
# <------ END VARIABLES ------>
# <----- BEGIN FUNCTIONS ----->
def search_tweets_for_sentiment(searchterm, n):
    """Searches Twitter for given term."""
    sentiment = 0;

    # Searches for Tweets matching query.
    public_tweets = api.search_tweets(q=searchterm,
                                      count=n+1,
                                      lang='en',
                                      tweet_mode="extended")

    # For each tweet, get full text and analyze sentiment.
    for tweet_info in public_tweets:
        if 'retweeted_status' in dir(tweet_info):
            tweet=tweet_info.retweeted_status.full_text
        else:
            tweet=tweet_info.full_text

        sentiment += sid.polarity_scores(tweet)['compound']

    # Calculate average sentiment of all tweets and return.
    sentiment = str(sentiment / n)
    print("Average sentiment on Twitter for " + searchterm + " is: " + sentiment)
    return sentiment
# <------ END FUNCTIONS ------>
