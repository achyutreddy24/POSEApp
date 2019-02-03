from psaw import PushshiftAPI

from pyscripts import sentiment

api = PushshiftAPI()

def find(keyword):
    SENTIMENTS = []
    gen = api.search_comments(q=keyword, limit=500)
    for c in gen:
        SENTIMENTS.append(sentiment.sentiment(c.body))
    return int(1000*sum(SENTIMENTS)/len(SENTIMENTS))
