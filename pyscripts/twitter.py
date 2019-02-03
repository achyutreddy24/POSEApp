from twitterscraper import query_tweets
from pyscripts import sentiment

def find(keyword):
    extremes = {"min": "", "max": ""}
    SENTIMENTS = []
    low = 1
    high = -1
    #print the retrieved tweets to the screen:
    for tweet in query_tweets(keyword, 10):
        sent = sentiment.sentiment(tweet.text)
        if sent < low:
            low = sent
            extremes["min"] = tweet.text
        elif sent > high:
            high = sent
            extremes["max"] = tweet.text
        SENTIMENTS.append(sent)
    return int(1000*sum(SENTIMENTS)/len(SENTIMENTS)), extremes
