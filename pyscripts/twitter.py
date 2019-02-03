from twitterscraper import query_tweets
from pyscripts import sentiment

def find(keyword):
    SENTIMENTS = []
    #print the retrieved tweets to the screen:
    for tweet in query_tweets(keyword, 10):
        SENTIMENTS.append(sentiment.sentiment(tweet.text))
    return int(1000*sum(SENTIMENTS)/len(SENTIMENTS))
