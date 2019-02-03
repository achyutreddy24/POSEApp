import praw # simple interface to the reddit API, also handles rate limiting of requests
import time
import OAuth2Util

from pyscripts import sentiment

#  Import Settings from Config.py
try:
    import Config
    USERAGENT = Config.USERAGENT
    MAXPOSTS = Config.MAXPOSTS
    REPLYMESSAGE = Config.REPLYMESSAGE
    
    print("Loaded Config")
except ImportError:
    print("Error Importing Config.py")
    
WAIT = 5
SENTIMENTSr = []

r = praw.Reddit(USERAGENT)
#r.login(USERNAME, PASSWORD)
o = OAuth2Util.OAuth2Util(r)

def scan(keyword):
    subreddit = r.get_subreddit("all")
    stream = praw.helpers.comment_stream(r, subreddit, limit=100)
    for comment in stream:
        cbody = comment.body
        if keyword not in cbody.lower():
            continue
        else:
            SENTIMENTSr.append(sentiment.sentiment(comment))
        
def find(keyword):
    SENTIMENTSr = []
    for _ in range(1,50):
        scan(keyword)
        time.sleep(WAIT)
    return sum(SENTIMENTSr)/len(SENTIMENTSr)

