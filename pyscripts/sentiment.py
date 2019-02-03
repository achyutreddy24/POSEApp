from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
def sentiment(media):
    vs  = analyzer.polarity_scores(media)
    return vs['compound']
        
