import praw
import nltk
import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# <----- BEGIN VARIABLES ----->
secret_file = "login_info.txt"

with open(secret_file) as f:
    lines = f.readlines()

reddit_keys = {
    'client_id':        lines[1].strip(),
    'client_secret':    lines[3].strip(),
    'user_agent':       "Web Scraper"
}

reddit = praw.Reddit(client_id      = reddit_keys['client_id'],
                     client_secret  = reddit_keys['client_secret'],
                     user_agent     = reddit_keys['user_agent'])

sid = SentimentIntensityAnalyzer()
# <------ END VARIABLES ------>
# <----- BEGIN FUNCTIONS ----->
def search_subreddit_for_sentiment(subreddit, searchterm):
    hot_posts = reddit.subreddit(subreddit).hot(limit=500)
    sentiment, n = 0, 0

    for post in hot_posts:
        if searchterm in str(post.title):
            #time = post.created
            #print(datetime.datetime.fromtimestamp(time))
            n += 1
            sentiment += sid.polarity_scores(post.selftext)['compound']

    if n != 0:
        sentiment = sentiment/n

    print("Average sentiment on /r/" + subreddit + " for " + searchterm + " is: " + str(sentiment))

    return float(sentiment)

def get_average_financial_sentiment(searchterm):
    sentiment = 0
    finance_subs = [
        "Stocks",
        "WallStreetBets",
        "Investing",
        "Finance",
        "Economics",
        "FinanceNews",
        "DueDilligence",
        "Traders",
        "EducatedInvesting"
    ]

    n = 0

    for subreddit in finance_subs:
        sub_sentiment = search_subreddit_for_sentiment(subreddit, searchterm)
        if sub_sentiment != 0:
            n += 1
            sentiment += sub_sentiment

    sentiment = sentiment/n

    print()
    print("Average sentiment on Reddit for " + searchterm + " is: " + str(sentiment))
    return sentiment

# <------ END FUNCTIONS ------>
get_average_financial_sentiment("Apple")
