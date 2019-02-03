from psaw import PushshiftAPI

import sentiment

api = PushshiftAPI()

def find(keyword):
    extremes = {"min": "", "max": ""}
    low = 1
    high = -1
    SENTIMENTS = []
    gen = api.search_comments(q=keyword, limit=500)
    for c in gen:
        sent = sentiment.sentiment(c.body)
        if sent < low:
            low = sent
            extremes["min"] = c.body
        elif sent > high:
            high = sent
            extremes["max"] = c.body
        SENTIMENTS.append(sent)
    return int(1000*sum(SENTIMENTS)/len(SENTIMENTS)), extremes
